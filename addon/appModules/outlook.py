# -*- coding: UTF-8 -*-
#appModules/outlook.py
#NVDA add-on: Outlook Extended
#Copyright (C) 2018 Cyrille Bougot, Ralf Kefferpuetz
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

#Known bugs (not resolved):
#1. Double-press NVDA+Shift+A to go to attachments may not always work when mail has 20 attachments or so (Outlook 2016),
#especially when e-mail has just been opened.

#Possible enhancements
#1. Use @script decorator for markAsRead and markAsUnread script gesturs, as well as for reportHeaderFieldN scripts. Did not manage to make it work.
#2. Deactivate following script when moving from message body to attachment or last header field in order to prevent NVDA from announcing document margin: shift+tab, bound to script tab on NVDAObjects.window.winword.WordDocument
#3. Rename fields wrongly named. E.g. value=None&name=textExpectedFromValue -> take label from previous window.
#4. Implement column navigation in address book: debug column navigation (scroll the list, access other children thant the ones visible...)
#5. Allow to get back to message body even when an attachment preview is displayed when calling NVDA+Shift+M


#TODO: (zzz)
#Check task assigned to others

from __future__ import unicode_literals

from comtypes import COMError
from scriptHandler import getLastScriptRepeatCount, script
import winUser
from logHandler import log
import api
import controlTypes
import ui
from NVDAObjects.IAccessible import IAccessible, List
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from NVDAObjects.behaviors import RowWithoutCellObjects, RowWithFakeNavigation
from NVDAObjects.UIA import UIA
from windowUtils import findDescendantWindow
import tones
import globalVars
from locationHelper import RectLTWH
import re
import threading

from nvdaBuiltin.appModules import outlook

import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]

# Translators: The key ont the right of the "0" key in the alpha-numeric part of the keyboard. Note: In the translated documentation (/website/addons/outlookExtended.xx.po in the screenReaderTranslations repo), do not forget to modify the commands section accordingly.
KEY_HEADER_FIELD11 = _("-")
# Translators: The key just ont the left of the backspace key. Note: In the translated documentation (/website/addons/outlookExtended.xx.po in the screenReaderTranslations repo), do not forget to modify the commands section accordingly.
KEY_HEADER_FIELD12 = _("=")

class HeaderFieldNotFoundeError(LookupError):
	pass
class NotInMessageWindowError(Exception):
	pass
	
class ElemWithReadStatus:

	scriptCategory = ADDON_SUMMARY
	
	@script(
		# Translators: Documentation for mark as read script.
		description = _("Mark a message as read")
		)
	def script_markAsRead(self, gesture):
		gesture.send()
		self.reportReadStatus()
		
	@script(
		# Translators: Documentation for mark as unread script.
		description = _("Mark a message as unread")
		)
	def script_markAsUnread(self, gesture):
		gesture.send()
		self.reportReadStatus()
	
	def reportReadStatus(self):
		focus = api.getFocusObject()
		if focus.appModule.nativeOm:
			try:
				selection=focus.appModule.nativeOm.activeExplorer().selection
			except COMError:
				return #No COM access
			nSel = selection.count
			if nSel > 1:
				# Translators: To what the mark as read/unread applies to
				itemType = _("Messages group: %s")
			elif nSel == 1:
				# Translators: To what the mark as read/unread applies to
				itemType = _("Messages: %s")
			else:
				# Translators: Error when mark as read/unread shortcut is called with no message selected
				ui.message(_("No message selected"))
				return
			selection=selection.item(1)
			try:
				unread=selection.unread
			except COMError:
				unread=False
			if unread:
				# Translators: To announce the message or group status: unread
				itemState = _("unread")
			else:
				# Translators: To announce the message or group status: read
				itemState = _("read")
			ui.message(itemType % itemState)
	
	__gestures={
		"kb:control+U":"markAsUnread",
		"kb:control+Q":"markAsRead",
		}	
		

class UIAGridRowWithReadStatus(outlook.UIAGridRow, ElemWithReadStatus):
	pass
	
class UIAWithReadStatus(UIA, ElemWithReadStatus):
	pass
	

class OutlookItemWindow(object):

	def __init__(self):
		self.rootDialog = self.getRootDialog()
		windowTypeList = ['Message', 'Message2', 'MeetingRequest', 'MeetingReply', 'TaskRequest', 'Report', 'RSS', 'Calendar', 'CalendarAttendeesList', 'CalendarAttendeesTrackingList', 'Task', 'Journal']
		self.windowType = [wt for wt in windowTypeList if getattr(self, 'is' + wt)()]
		log.debug('Window types: ' + str(self.windowType))
		#Log to investigate for new types of windows.
		#This log is disabled by default because it takes processing time and has thus side effect.
		#To activate it, open NVDA console and type:
		# import globalVars
		# globalVars.olexDebug = True
		globalVars.olexDebug = getattr(globalVars, 'olexDebug', False)
		if globalVars.olexDebug:
			log.debug(self.listHeaderFields())
		if len(self.windowType) != 1:
			raise NotInMessageWindowError()
		self.windowType = self.windowType[0]
		self.getHeaderFieldsFun = getattr(self, 'get' + self.windowType + 'HeaderFields')
	
	@staticmethod
	def getRootDialog():
		obj = api.getFocusObject()
		parent = obj.parent
		try:
			while obj.windowClassName != "#32770":
				obj = obj.parent
		except AttributeError:
			raise NotInMessageWindowError
		if obj.role == controlTypes.ROLE_WINDOW:
			#Sometimes going up hierarchy goes directly to window object without passing via dialog object -> go to first child
			obj = obj.firstChild
		return obj
	
	def isMessage(self):
		#These fields are always present even if not visible (according to reduced/developped headers state)
		lstCID= [
			4099, #'To'
			4100, #CC
			4103, #BCC 
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isMessage2(self):
		#Fields in office 365 update (32-bit) as reported by Ralf and user.
		lstCID= [
			4117, #To
			4126, #Cc
			4104 #Bcc
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isMeetingRequest(self):
		lstCID = [
			4514, 4098, #Required
			4515, 4099, #Optional
			4518, 4102, #Date/time
			4517, 4101, #Location
			]
		if self.hasHeaderFieldsInThisOrder(lstCID):
			return True
		#Test meeting request forwarding
		lstCID = [
			4098, #To
			4516, 4100, #Subject
			4517, 4101, #Location
			4518, 4102, #Date/time
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
	
	def isMeetingReply(self):
		lstCID= [
			4520, 4105, #Date/time
			4521, 4106, #Location
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isTaskRequest(self):
		lstCID = [
			4097, #Subject
			4110, #DueDate
			4104, #State
			4099, #Priority
			4112, #% completed
			4103, #Owner
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isReport(self):
		lstCID = [
			4512, 4096, #From
			4513, 4097, #Sent
			4514, 4098, #To
			4515, 4099, #Subject
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
	
	def isRSS(self):
		lstCID = [
			4527, 4106, #Feed
			4526, 4105, #Published on
			4528, 4107, #Author
			4529, 4108, #Subject
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isCalendar(self):
		lstCID = [
			4534, 4100, #'Subject'
			4530, #'Location'; Do not use combo-box (4102) since cid and/or position in hierarchy seems bugged.
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isCalendarAttendeesList(self):
		lstCID = [
			4866, 4098, #Start date
			4865, 4096, #Start date
			]
		#zzz del prima
		lstCID = [
			4542, #All attendees list
			4720, #All attendees status
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isCalendarAttendeesTrackingList(self):
		lstCID = [
			4542, #Attendees tracking list
			4870, #Attendees replies
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
	
	def isTask(self):
		lstCID = [
			4521, 4097, #Subject
			4514,4100, #StartDate
			4523, 4101, #EndDate
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def isJournal(self):
		lstCID = [
			4512, 4096, #Subject
			4513, #EntryType
			4515, 4098, #Company
			4099, #StartDate
			4100, #StartTime
			4101, #Duration
			]
		return self.hasHeaderFieldsInThisOrder(lstCID)
		
	def listHeaderFields(self):
		ls1 = [obj for obj in self.rootDialog.children]
		return [{
				'name': o.name,
				'value': o.value,
				'role': o.role,
				'states': o.states,
				'cid': o.windowControlID
				}
			for o in ls1]
	def hasHeaderFieldsInThisOrder(self, lstCID):
		ls1 = [obj.windowControlID for obj in self.rootDialog.children if obj.windowControlID in lstCID]
		return ls1 == lstCID
	
	def getMessageHeaderFields(self):
		hasFromEditing = len([o for o in self.rootDialog.children if o.windowControlID==4263 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasFromEditing:
			dic = {1: (4263, 'From')}
		else:
			dic = {1: (4097, 'From')}
		dic.update({
			2: (4098, 'Sent'),
			3: (4099, 'To'),
			4: (4100, 'Cc'),
			5: (4103, 'Bcc'),
			6: (4101, 'Subject'),
			7: (4346, 'SignedBy'),
			})
		#hasFromReduced = len([o for o in self.rootDialog.children if o.windowControlID==4292 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		hasFromReduced = len([o for o in self.rootDialog.children if o.windowControlID==4280 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasFromReduced:
			dic.update({
				1: (4292, 'From'),
				2: (4293, 'Sent'),
				3: (4295, 'ToCc'),
				4: (None, 'Cc'),
				5: (None, 'Bcc'),
				6: (4294, 'Subject')
				})
		return dic
		
	def getMessage2HeaderFields(self):
		#Fields in office 365 update (32-bit) as reported by Ralf and user.
		hasFromEditing = len([o for o in self.rootDialog.children if o.windowControlID==4263 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasFromEditing:
			dic = {1: (4263, 'From')}
		else:
			dic = {1: (4292, 'From')}
		dic.update({
			2: (4315, 'Sent'),
			3: (4117, 'To'),
			4: (4126, 'Cc'),
			5: (4104, 'Bcc'),
			6: (4294, 'Subject'),
			7: (4346, 'SignedBy') })
		hasFromReduced = len([o for o in self.rootDialog.children if o.windowControlID==4280 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasFromReduced:
			dic.update({
				1: (4292, 'From'),
				2: (4293, 'Sent'),
				3: (4295, 'ToCc'),
				4: (None, 'Cc'),
				5: (None, 'Bcc'),
				6: (4294, 'Subject')
				})
		return dic
			
	def getReportHeaderFields(self):
		dic = {
			1: (4096, 'From'),
			2: (4097, 'Sent'),
			3: (4098, 'To'),
			4: (None, 'Cc'),
			5: (None, 'BCC'),
			6: (4099, 'Subject'),
			}
		return dic
			
	def getRSSHeaderFields(self):
		dic = {
			1: (4107, 'Author'),
			2: (4105, 'Published'),
			3: (4106, 'Feed'),
			4: (None, 'Cc'),
			5: (None, 'BCC'),
			6: (4108, 'Subject')
			}
		return dic
		
	def getMeetingRequestHeaderFields(self):
		dic = {
			1: (4096, 'From'),
			2: (4097, 'Sent'),
			3: (4098, 'Required'),
			4: (4099, 'Optional'),
			5: (4100, 'Subject'),
			6:(4101, 'Location'),
			7:(4102, 'DateTime'),
			}
		hasFromReduced = len([o for o in self.rootDialog.children if o.windowControlID==4292 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasFromReduced:
			dic.update({
				1: (4292, 'From'),
				2: (4293, 'Sent'),
				3: (4295, 'ToCC'),
				4: (None, 'Optional'),
				5: (4294, 'Subject')
				})
		return dic
		
	def getMeetingReplyHeaderFields(self):
		dic = {
			1: (4097, 'From'),
			2: (4098, 'Sent'),
			3: (4107, 'To'),
			4: (4108, 'Cc'),
			5: (4099, 'Subject'),
			6: (4106, 'Location')
			}
		hasDateTime = len([o for o in self.rootDialog.children if o.windowControlID == 4105 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasDateTime:
			dic.update({7:(4105, 'DateTime')}) #Date/time or, for e-mails in edition, current time 
		else:
			dic.update({7: (4110, 'CurrentTime')})
		dic.update({
			8: (4109, 'ProposedNewTime'),
			9: (4100, 'Accepted'),
			10: (4101, 'Tentative'),
			11: (4102, 'Declined'),
			})
		return dic
			
	def getTaskRequestHeaderFields(self):
	#zzz Order of fields ?
		dic = {
			1: (4097, 'Subject'),
			2: (4110, 'DueDate'),
			3: (4104, 'State'),
			4: (4099, 'Priority'),
			5: (4112, '% completed'),
			6: (4103, 'Owner'),
			}
		return dic
	
	def getCalendarHeaderFields(self):
		hasOrganizer = len([o for o in self.rootDialog.children if o.windowControlID == 4523 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasOrganizer:
			dic = {1: (4523, 'Organizer')} #Exists invisible in appointment
		else:
			dic = {1: (4263, 'From')}
		dic.update({
			2: (4526, 'Sent'),
			3: (4106, 'To'),
			4: (4100, 'Subject'),
			5: (4102, 'Location')
			})
		#Test if item is a unique meeting by Checking if start date is visible
		isUniqueMeetingInstance = len([o for o in self.rootDialog.children if o.windowControlID == 4098 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if isUniqueMeetingInstance:
			dic.update({
				6: (4098, 'StartDate'),
				7: (4096, 'StartTime'),
				8: (4099, 'EndDate'),
				9: (4097, 'EndTime'),
				10: (4226, 'AllDay')
				})
		else: #Series
			dic.update({
				6: (4104, 'Periodicity'),
				7: (4226, 'AllDay')
				})
		return dic
	
	def getCalendarAttendeesListHeaderFields(self):
		dic = {
			1: (4542, 'AttendeesList'),
			2: (4720, 'AllAttendeesStatus'),
			}
		#Test if item is a unique meeting by Checking if start date is visible
		isUniqueMeetingInstance = len([o for o in self.rootDialog.children if o.windowControlID == 4098 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if isUniqueMeetingInstance:
			dic.update({
				3: (4098, 'StartDate'),
				4: (4096, 'StartTime'),
				5: (4099, 'EndDate'),
				6: (4097, 'EndTime'),
				})
		else:
			dic.update(
				{3: (4104, '')})
		return dic
		
	def getCalendarAttendeesTrackingListHeaderFields(self):
		dic = {1: (4542, 'AttendeesTrackingList')}
		return dic
		#zzz return self.getCalendarHeaderFields()
	
	def getTaskHeaderFields(self):
		dic = {
			1: (4263, 'From'),
			2: (4096, 'To'),
			3: (4097, 'Subject'),
			4: (4100, 'StartDate'),
			5: (4101, 'DueDate'),
			6: (4481, 'State'),
			7: (4480, 'Priority'),
			8: (4112, '% completed'),
			}
		hasReminder = len([o for o in self.rootDialog.children if o.windowControlID == 4226 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if hasReminder:
			dic.update({
				9: (4226, 'Reminder'),
				10: (4102, 'Date reminder'),
				11: (4108, 'Reminder time'),
				12: (4103, 'Owner'),
			})
		else: #task assignation editing
			dic.update({
				9: (4224, 'Keep my task list updated with copies of task'),
				10: (4225, 'Send me a status report when this task is complete'),
				})
		return dic
		
	def getJournalHeaderFields(self):
		dic = {
			1: (4096, 'Subject'),
			2: (4480, 'EntryType'),
			3: (4098, 'Company'),
			4: (4099, 'StartDate'),
			5: (4100, 'StartTime'),
			6: (4101, 'Duration'),
			}
		return dic
		
	def getHeaderFieldObject(self, nField):
		try:
			cid,name = self.getHeaderFieldsFun()[nField]
		except KeyError:
			raise HeaderFieldNotFoundeError()
		try:
			handle = findDescendantWindow(self.rootDialog.windowHandle, controlID=cid)
			if handle:
				obj = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
		except:
			raise HeaderFieldNotFoundeError()
		if controlTypes.STATE_INVISIBLE in obj.states:
			raise HeaderFieldNotFoundeError()
		return obj,name


class List(List):
	def getHeader(self):
		try:
			return self.header
		except AttributeError:
			#handle = findDescendantWindow(api.getForegroundObject().windowHandle, controlID=138, className='SysHeader32')
			handle = findDescendantWindow(self.parent.windowHandle, controlID=138, className='SysHeader32')
			self.header = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
			self.allowIAccessibleChildIDAndChildCountForPositionInfo = True
			return self.header
		
	def _get_columnCount(self):
		header = self.getHeader()
		return len(header.children)
		
	def _get_rowCount(self):
		#zzz Should be better defined since does not take scrolling use case
		return len(self.children)
	
	
class AddressBookEntry(RowWithoutCellObjects, RowWithFakeNavigation, outlook.AddressBookEntry):

	def _getColumnLocation(self, column):
		colHeader = self.parent.getHeader().getChild(column - 1)
		return RectLTWH(left=colHeader.location.left, top=self.location.top, width=colHeader.location.width, height=self.location.height)
		
	
	def _getColumnContent(self, column):
		"""Get the text content for a given column of this row.
		@param column: The index of the column, starting at 1.
		@type column: int
		@rtype: str
		"""
		colNames = [c.name for c in self.parent.getHeader().children]
		colPatterns = [name +r' (?P<C'+str(col+1)+r'>.*?)' for col,name in enumerate(colNames)]
		sep = ', '
		pattern = '^' + colPatterns[0] + ''.join(['(?:' + sep + cp + ')?' for cp in colPatterns[1:]]) + '$'
		m = re.match(pattern, self.name)
		if not m:
			log.warning('Parsing failed: self.name = '+str(self.name)+ ' ; colNames = ' + str(colNames))
			return
		return m.groupdict()['C'+str(column)]
		
	def _getColumnHeader(self, column):
		"""Get the header text for this column.
		@param column: The index of the column, starting at 1.
		@type column: int
		@rtype: str
		"""
		return self.parent.getHeader().getChild(column-1).name
	
	
	def _get_next(self):
		rows = self.parent.children
		index = rows.index(self)
		if index == len(rows) - 1:
			return None
		return rows[index+1]
		
	def _get_previous(self):
		rows = self.parent.children
		index = rows.index(self)
		if index == 0:
			return None
		return rows[index-1]
	
	def _moveToRow(self, row):
		#Supersedes _moveToRow in behaviors.py to disable row navigation because need to be debugged:
		#when pressing Ctrl+Alt+downarrow, the focus moves visually but NVDA takes updated focus only when you press control again.
		
		# Translators: When trying to move by column in address book (Alt+Ctrl+Up/DownArrow)
		ui.message(_('Column navigation not supported in the address book'))


class AppModule(outlook.AppModule):
	
	scriptCategory = ADDON_SUMMARY
	
	_headerFieldKeyMap = {str(i):i for i in range(1,10)}
	_headerFieldKeyMap.update({
		'0': 10,
		KEY_HEADER_FIELD11: 11,
		KEY_HEADER_FIELD12: 12})
		
	def __init__(self,*args,**kwargs):
		super(AppModule,self).__init__(*args,**kwargs)
		self.lastFocus = None
		
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
		if obj.role==controlTypes.ROLE_LISTITEM and obj.windowClassName=="OUTEXVLB":
			clsList.insert(0, AddressBookEntry)
			return
		if obj.role==controlTypes.ROLE_LIST and obj.windowClassName=="OUTEXVLB":
			clsList.insert(0, List)
			return
		if outlook.UIAGridRow in clsList:
			clsList.insert(0, UIAGridRowWithReadStatus)
		if UIA in clsList and obj.role == controlTypes.ROLE_GROUPING:
			clsList.insert(0,UIAWithReadStatus)
		
	def reportHeaderFieldN(self, nField, gesture):
		if api.getFocusObject().windowClassName in ['DayViewWnd', 'WeekViewWnd']:
		#Calendar view: Alt+digit is used command to set up number of days in the view
			gesture.send()
			return
		nRepeat = getLastScriptRepeatCount()
		if nRepeat == 0:
			try:
				self.olItemWindow = OutlookItemWindow()
			except NotInMessageWindowError:
				self.olItemWindow = None
		if self.olItemWindow is None:
			# Translators: When trying to use Alt+Number shortcut but not in message.
			ui.message(_("Not in a message window"))
			return
		try:
			obj, name = self.olItemWindow.getHeaderFieldObject(nField)
		except HeaderFieldNotFoundeError:
			self.errorBeep()
			return
		self.reportObject(obj, nRepeat)
		
	def reportObject(self, obj, nRepeat):
		if nRepeat == 0:
		# single press
			self.speakObject(obj)
			self.lastFocus= api.getFocusObject()
		elif nRepeat == 1:
		# double press, set focus in field
			handle = obj.windowHandle
			winUser.setForegroundWindow(handle)
		else:
		# trible press (or more), copy to clipboard and set focus to original focused object
			api.copyToClip(obj.value)
			# Translators: When user double press Alt+Number to copy a header's field to clipboard
			ui.message(_("Copied to clipboard"))
			api.setNavigatorObject(obj,isFocus=True)
			self.lastFocus.setFocus()
	
	def speakObject(self, obj):
		if obj.role == controlTypes.ROLE_CHECKBOX:
			name = obj.name
			# Translators: A checkbox state
			value = _('checked') if controlTypes.STATE_CHECKED in obj.states else _('unchecked')
		else:
			name,value = obj.name,obj.value
		# Translators: To report name and value of a heaeder's field
		ui.message(_("{name} {value}").format(name=name,value=value))
		
	def errorBeep(self):
		tones.beep(440, 80)
	
	@script(
		# Translators: Documentation for report info bar script.
		description=_("Reports the information bar in a message, calendar item or task window. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard."),	
		gestures = ["kb(desktop):NVDA+shift+I", "kb(laptop):NVDA+control+shift+I"]
		)
	def script_reportInfoBar(self, gesture):
		obj = self.getInfoBarObj()
		if obj is None:
			# Translators: When the info bar is not present
			ui.message(_("No information bar"))
			return
		self.reportObject(obj, getLastScriptRepeatCount())
		
	@script(
		# Translators: Documentation for move to message body script.
		description=_("Moves the focus to the message body"),
		gestures = ["kb(desktop):NVDA+shift+M", "kb(laptop):NVDA+control+shift+M"]
		)
	def script_focusToMessageBody(self, gesture):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=4159),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
			return
		obj.setFocus()
	
	@script(
		# Translators: Documentation for Attachments script.
		description=_("Reports the number and the names of attachments in a message window. If pressed twice, moves the focus to it."),
		gestures = ["kb(desktop):NVDA+shift+A", "kb(laptop):NVDA+control+shift+A"]
		)
	def script_attachments(self, gesture):
		obj = api.getFocusObject()
		appVersionMaj = int(obj.appModule.productVersion.split('.')[0])
		
		try:
			if appVersionMaj >= 16: #Outlook 2016+
				attachmentsList,handle,namesGen,windowName = self.getAttachmentInfos2016()
			else:
				attachmentsList,handle,namesGen,windowName = self.getAttachmentInfos2013()
		except LookupError:
			self.errorBeep()
			return
		self.nAttachments = len(attachmentsList)
		if getLastScriptRepeatCount() == 1 and self.nAttachments > 0:
		# double press, set focus in field
			self.focusInfo['firstObj'].setFocus()
			winUser.setForegroundWindow(self.focusInfo['handle'])
		else:
		# single press
			self.focusInfo = {'handle': handle}
			try:
				self.focusInfo['firstObj'] = attachmentsList[0]
			except IndexError:
				self.focusInfo['firstObj'] = None
			#Launch the attachments announcement code in a different thread since it can take time in the case of numerous attachments (above 17 on my machine).
			#In this case, getLastScriptRepeatCount() after double press will return 0 instead of 1.
			def announceAttachments():
				msg = (
					windowName + ": " + str(self.nAttachments) + '. ' +  #Attachments number
					', '.join(namesGen))
				ui.message(msg)
			threading.Thread(target=announceAttachments).start()
	
	def getAttachmentInfos2016(self):
		fg = api.getForegroundObject()
		cidAttachments=4306
		handle = findDescendantWindow(fg.windowHandle, className=None, controlID=cidAttachments)
		obj = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
		try:
			o = obj
			while o.role != controlTypes.ROLE_BUTTON:
				o = o.firstChild
			attachmentsList = [a for a in o.parent.children if a.role == controlTypes.ROLE_BUTTON]
		except AttributeError:
			attachmentsList = []
		namesGen = (child.firstChild.getChild(1).name for child in attachmentsList)
		return attachmentsList,handle,namesGen,obj.name
		
	def getAttachmentInfos2013(self):
		fg = api.getForegroundObject()
		cidAttachments=4623
		bFoundWindow = False
		bResult = False
		try:
			handle = findDescendantWindow(fg.windowHandle, className=None, controlID=cidAttachments)
			bFoundWindow = True
			obj = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
			if not (obj.location.width == 0 and obj.location.height == 0):
				attachmentsList = [c for c in obj.children[1:] if c.role == controlTypes.ROLE_LISTITEM]
				namesGen = (a.name for a in attachmentsList)
				bResult = True
		except LookupError:
			pass
		if not bResult:
			cidAttachments=4104
			try:
				handle = findDescendantWindow(fg.windowHandle, className=None, controlID=cidAttachments)
				obj = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
				if obj.firstChild is None:
					raise LookupError
				bFoundWindow = True
				def makeGenChildren(o): #Define a generator to get children since the .children roperty does not work
					o = o.firstChild
					while o is not None:
						if o.role == controlTypes.ROLE_BUTTON:
							yield o
						o = o.next
				attachmentsList = [o for o in makeGenChildren(obj)]
				namesGen = (a.name for a in attachmentsList)
				bResult = True
			except LookupError:
				pass
		if not bFoundWindow:
			raise LookupError
		if bResult:
			return attachmentsList,handle,namesGen,obj.name
		else:
			return [], handle,[],obj.name
		
	def getInfoBarControlId(self):
		majVer = int(self.productVersion.split('.')[0])
		if majVer <= 11:
			cid = 4105 #Outlook 2003
		else:
			cid = 4262 #Outlook 2016
		return cid
	
	def getInfoBarObj(self):
		try:
			cid = self.getInfoBarControlId()
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=cid),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			obj = None
		return obj
		
	
	__gestures = {"kb:alt+" + key : "reportHeaderField" + str(n) for (key,n) in _headerFieldKeyMap.items()}
	
	@staticmethod
	def _createScript_reportHeaderField(n):
		def  _genericScript_reportHeaderField(self, gesture):
			return self.reportHeaderFieldN(n, gesture)
		#Translators: Input help mode message for report a header's field command. in outlook message, calendar item or task window
		_genericScript_reportHeaderField.__doc__ = _("Reports the header field %s in a message, calendar item or task window. If pressed twice, moves the focus to this field if possible. If pressed three times, copies its content to the clipboard.") % str(n)
		return _genericScript_reportHeaderField
	
	@classmethod
	def createAllScript_reportHeaderField(cls):
		for n in range(1,len(cls._headerFieldKeyMap)+1):
			scriptName = 'script_reportHeaderField' + str(n)
			scriptFun = AppModule._createScript_reportHeaderField(n)
			setattr(cls, scriptName, scriptFun)
	
	
	
AppModule.createAllScript_reportHeaderField()

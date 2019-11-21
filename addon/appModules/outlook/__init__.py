# -*- coding: UTF-8 -*-
#appModules/outlook.py
#NVDA add-on: Outlook Extended
#Copyright (C) 2018-2021 Cyrille Bougot, Ralf Kefferpuetz
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

# Import all from original outlook appModule to keep it available if needed.
from nvdaBuiltin.appModules.outlook import *

# Import here explecitely used variables from original outlook appModule for clarity.
from nvdaBuiltin.appModules.outlook import UIAGridRow, AddressBookEntry, AppModule

from .itemWindow import OutlookItemWindow, NotInMessageWindowError, HeaderFieldNotFoundeError
from . import compa

from comtypes import COMError
from scriptHandler import getLastScriptRepeatCount, script
import winUser
from logHandler import log
import api
import controlTypes
controlTypes = compa.convertControlTypes(controlTypes)
import ui
from NVDAObjects.IAccessible import IAccessible, List
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from NVDAObjects.behaviors import RowWithoutCellObjects, RowWithFakeNavigation
from NVDAObjects.UIA import UIA
from windowUtils import findDescendantWindow
import tones
import globalVars
import core
import config

from locationHelper import RectLTWH
import sys
import re
import threading

import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]

# Translators: The key ont the right of the "0" key in the alpha-numeric part of the keyboard. Note: In the translated documentation (/website/addons/outlookExtended.xx.po in the screenReaderTranslations repo), do not forget to modify the commands section accordingly.
KEY_HEADER_FIELD11 = _("-")
# Translators: The key just ont the left of the backspace key. Note: In the translated documentation (/website/addons/outlookExtended.xx.po in the screenReaderTranslations repo), do not forget to modify the commands section accordingly.
KEY_HEADER_FIELD12 = _("=")

confspec = {
	'testCasePath': 'string(default="")',
}
config.conf.spec["outlookExtended"] = confspec

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
		

class UIAGridRowWithReadStatus(UIAGridRow, ElemWithReadStatus):
	pass
	
class UIAWithReadStatus(UIA, ElemWithReadStatus):
	pass
	

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
	
	
class AddressBookEntry(RowWithoutCellObjects, RowWithFakeNavigation, AddressBookEntry):

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


class UIAMailTipItemText(UIA):
	def event_NVDAObject_init(self):
		ui.message(self.name)

class UIAMailTipItemMessage(UIA):
	def event_NVDAObject_init(self):
		from tones import beep
		beep(440,500)
		
	def event_show(self):
		ui.message(self.name)
		#speech.speakObject(self, reason=controlTypes.REASON_FOCUS)

class UIARecipientButton(UIA):
	def _get_name(self):
		return self.firstChild.name
	def reportFocus(self):
		ui.message(self.name)
		
	def event_NVDAObject_init(self):
		from tones import beep
		beep(440, 440)

class AppModule(AppModule):
	
	scriptCategory = ADDON_SUMMARY
	
	_headerFieldKeyMap = {str(i):i for i in range(1,10)}
	_headerFieldKeyMap.update({
		'0': 10,
		KEY_HEADER_FIELD11: 11,
		KEY_HEADER_FIELD12: 12})
		
	def __init__(self,*args,**kwargs):
		super(AppModule,self).__init__(*args,**kwargs)
		self.lastFocus = None
		self.testCases = None
		self.tcNumber = 0
		self.initializeTestCases
		
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
		if obj.role==controlTypes.Role.LISTITEM and obj.windowClassName=="OUTEXVLB":
			clsList.insert(0, AddressBookEntry)
			return
		if obj.role==controlTypes.Role.LIST and obj.windowClassName=="OUTEXVLB":
			clsList.insert(0, List)
			return
		if UIAGridRow in clsList:
			clsList.insert(0, UIAGridRowWithReadStatus)
			return
		if UIA in clsList:
			if obj.role == controlTypes.Role.GROUPING and obj.parent.windowClassName == 'OutlookGrid':
				clsList.insert(0,UIAWithReadStatus)
			elif obj.role == controlTypes.Role.PANE and obj.parent.role == controlTypes.ROLE_GROUPING and obj.windowClassName == 'NetUIHWND':
				clsList.insert(0, UIAMailTipPane)
			#elif obj.role == controlTypes.Role.PANE and obj.parent.role == controlTypes.ROLE_GROUPING and obj.windowClassName == 'NetUIHWND':
			#	clsList.insert(0, UIAMailTipPane)
			elif obj.UIAElement.currentAutomationID == 'RecipientButton':
				clsList.insert(0, UIARecipientButton)
			#elif obj.UIAElement.currentAutomationID == 'MailTipItemText':
			#	clsList.insert(0, UIAMailTipItemText)
			#elif obj.UIAElement.currentAutomationID == 'MailTipItemMessage':
			#	clsList.insert(0, UIAMailTipItemMessage)
	
	def reportHeaderFieldN(self, nField, gesture):
		if api.getFocusObject().windowClassName in ['DayViewWnd', 'WeekViewWnd']:
		#Calendar view: Alt+digit is used command to set up number of days in the view
			gesture.send()
			return
		nRepeat = getLastScriptRepeatCount()
		if nRepeat == 0:
			# Check if globalVars.olexDebug exists and is True.
			# This debug mode allows to enable additional log to investigate for new types of windows.
			# This log is disabled by default because it takes processing time and has thus side effect.
			# To activate it, open NVDA console and type:
			# import globalVars
			# globalVars.olexDebug = True
			debug = getattr(globalVars, 'olexDebug', False)
			try:
				self.olItemWindow = OutlookItemWindow(self.getRootDialog(), debug=debug)
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
		elif nRepeat == 2:
		# triple press, copy to clipboard and set focus to original focused object
			api.copyToClip(obj.value)
<<<<<<< HEAD:addon/appModules/outlook/__init__.py
			# Translators: When user triple presses Alt+Number to copy a header's field to clipboard
			core.callLater(0, lambda: ui.message(_("Copied to clipboard")))
=======
			# Translators: When user triple press Alt+Number to copy a header's field to clipboard
			ui.message(_("Copied to clipboard"))
>>>>>>> 42f2db4 (ajout):addon/appModules/outlook.py
			api.setNavigatorObject(obj,isFocus=True)
			self.lastFocus.setFocus()
	
	def speakObject(self, obj):
		if obj.role == controlTypes.Role.CHECKBOX:
			name = obj.name
			# Translators: A checkbox state
			value = _('checked') if controlTypes.State.CHECKED in obj.states else _('unchecked')
		else:
			name,value = obj.name,obj.value
		# Translators: To report name and value of a heaeder's field
		ui.message(_("{name} {value}").format(name=name,value=value))
		
	def errorBeep(self):
		tones.beep(440, 80)
		
	@script(
		# Translators: Documentation for report info bar script.
		description=_("Reports the notification in a message. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard."),	
		gestures = ["kb(desktop):NVDA+shift+N", "kb(laptop):NVDA+control+shift+N"]
		)
	def script_reportNotification(self, gesture):
		obj = self.getNotificationObj()
		if obj is None:
			# Translators: When there is no notification
			ui.message(_("No notification"))
			return
		nRepeat = getLastScriptRepeatCount()
		if nRepeat == 0:
			namesList = []
			for o in obj.children:
				name = o.name
				if name:
					if namesList and re.match('^\w.*$', name, re.U):
						name = ' ' + name
					namesList.append(name)
			self.notificationText = ''.join(namesList)
			ui.message(self.notificationText)
			self.lastFocus = api.getFocusObject()
		elif nRepeat == 1:
			winUser.setForegroundWindow(obj.windowHandle)
		elif nRepeat == 2:
			api.copyToClip(self.notificationText)
			# Translators: When user triple press NVDA+shift+N to copy the notification text to clipboard
			ui.message(_("Copied to clipboard"))
			#api.setNavigatorObject(obj,isFocus=True)
			#self.lastFocus.setFocus()
			winUser.setForegroundWindow(self.lastFocus.windowHandle)
		
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
				core.callLater(0, ui.message, msg)
			threading.Thread(target=announceAttachments).start()
	
	def getAttachmentInfos2016(self):
		fg = api.getForegroundObject()
		cidAttachments=4306
		handle = findDescendantWindow(fg.windowHandle, className=None, controlID=cidAttachments)
		obj = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
		try:
			o = obj
			while o.role != controlTypes.Role.BUTTON:
				o = o.firstChild
			attachmentsList = [a for a in o.parent.children if a.role == controlTypes.Role.BUTTON]
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
				attachmentsList = [c for c in obj.children[1:] if c.role == controlTypes.Role.LISTITEM]
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
						if o.role == controlTypes.Role.BUTTON:
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
	
	def getRootDialog(self):
		obj = api.getFocusObject()
		parent = obj.parent
		try:
			while obj.windowClassName != "#32770":
				obj = obj.parent
		except AttributeError:
			raise NotInMessageWindowError
		# Check if config.conf['outlookExtended']['testCasePath'] is defined.
		# If defined, it allows setting up a debug test framework fore live tests on various message types.
		# The message types are defined in the file case.py that can be found in the Github repo of this add-on.
		# When a message type is selected, alt+digit return the header of the test case object
		# instead of the header of the real window.
		# To activate it, open NVDA console and type:
		# import config
		# config.conf['outlookExtended']['testCasePath'] = r'C:\pathToOutlookExtendedGITLocalRepo\tests\unit'
		if self.testCases and self.tcNumber != 0:
			tcName = list(self.testCases.keys())[self.tcNumber - 1]
			obj = self.FakeRootWindow(tcName)
			return obj
		if obj.role == controlTypes.Role.WINDOW:
			#Sometimes going up hierarchy goes directly to window object without passing via dialog object -> go to first child
			obj = obj.firstChild
		return obj
		
	def initializeTestCases(self):
		debugTcPath = config.conf['outlookExtended']['testCasePath']
		isTest = bool(debugTcPath)
		if isTest:
			if self.testCases is None:
				sys.path.append(debugTcPath)
				from cases import tcObjectPropertyDic 
				from fakeObjects import FakeRootWindow
				del sys.path[-1]
				self.testCases = tcObjectPropertyDic
				self.FakeRootWindow = FakeRootWindow
		else:
			ui.message(_('Test case path not defined.'))
		return isTest
	
	# Scripts to select next and previous test cases when test mode is active
	# These scripts are unassigned by default
	# To assign them, edit directly the gesture.ini file, e.g. by pasting the following lines:
	# [appModules.outlook.AppModule]
	# selectNextTestCase = kb:control+f6+nvda+shift
	# selectPreviousTestCase = kb:control+f5+nvda+shift
	def script_selectNextTestCase(self, gesture):
		return self.selectTestCase(offset=1)
	def script_selectPreviousTestCase(self, gesture):
		return self.selectTestCase(offset=-1)
		
	def selectTestCase(self, offset):
		if not self.initializeTestCases():
			return
		self.tcNumber = (self.tcNumber + offset) % (len(self.testCases) + 1)
		if self.tcNumber != 0:
			self.tcName = list(self.testCases.keys())[self.tcNumber - 1]
			ui.message(self.tcName)
		else:
			self.tcName = ''
			ui.message(_('Test mode offf'))

	def getNotificationObj(self):
		try:
			cid = 4265
			obj = getNVDAObjectFromEvent(
				findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=cid),
				winUser.OBJID_WINDOW, 0)
			getChildWithRole = lambda o,role: [oc for oc in obj.children if oc.role == role][0]
			obj = getChildWithRole(obj, controlTypes.ROLE_PANE)
			obj = getChildWithRole(obj, controlTypes.ROLE_PANE)
			obj = getChildWithRole(obj, controlTypes.ROLE_PANE)
			obj = getChildWithRole(obj, controlTypes.ROLE_GROUPING)
			obj = getChildWithRole(obj, controlTypes.ROLE_PANE)
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

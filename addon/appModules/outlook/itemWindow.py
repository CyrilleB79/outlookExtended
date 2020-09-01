# -*- coding: UTF-8 -*-
#appModules/outlook/itemWindow.py
#NVDA add-on: Outlook Extended
#Copyright (C) 2018-2020 Cyrille Bougot, Ralf Kefferpuetz
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

from logHandler import log
try:
	import controlTypes
except ModuleNotFoundError:
	# stub
	class CT: pass
	controlTypes = CT()
	controlTypes.STATE_INVISIBLE = 1024

try:
	import winUser
	from windowUtils import findDescendantWindow
	from NVDAObjects.IAccessible import getNVDAObjectFromEvent
except ModuleNotFoundError:
	pass

class NotInMessageWindowError(Exception):
	pass
class HeaderFieldNotFoundeError(LookupError):
	pass

class OutlookItemWindow(object):

	def __init__(self, rootDialog, debug=False):
		self.rootDialog = rootDialog
		windowTypeList = ['Message', 'Message2', 'MeetingRequest', 'MeetingRequest2', 'MeetingReply', 'TaskRequest', 'Report', 'RSS', 'Calendar', 'CalendarAttendeesList', 'CalendarAttendeesTrackingList', 'Task', 'Journal']
		self.windowType = [wt for wt in windowTypeList if getattr(self, 'is' + wt)()]
		log.debug('Window types: ' + str(self.windowType))
		#Log to investigate for new types of windows.
		#This log is disabled by default because it takes processing time and has thus side effect.
		if debug:
			log.debug(self.listHeaderFields())
		if len(self.windowType) != 1:
			raise NotInMessageWindowError()
		self.windowType = self.windowType[0]
		self.getHeaderFieldsFun = getattr(self, 'get' + self.windowType + 'HeaderFields')
	
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
	
	def isMeetingRequest2(self):
		# Fields in Office 365 64-bits for cancelled meeting request, as reported by DG on May 18th and 19th, 2020.
		lstCID = [
			4539, 4105, #Required
			4540, 4106, #Optional
			4534, 4102, #Date/time
			4538, 4101, #Location
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
		isWriting = len([o for o in self.rootDialog.children if o.windowControlID == 4256 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if isWriting:
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
		isWriting = len([o for o in self.rootDialog.children if o.windowControlID == 4256 and controlTypes.STATE_INVISIBLE not in o.states]) == 1
		if isWriting:
			dic = {1: (4263, 'From')}
		else:
			dic = {1: (4292, 'From')}
		dic.update({
			2: (4315, 'Sent'),
			3: (4117, 'To'),
			4: (4126, 'Cc'),
			5: (4104, 'Bcc'),
			6: (4101 if isWriting else 4294, 'Subject'),
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
		
	def getMeetingRequest2HeaderFields(self):
		dic = {
			1: (4292, 'From'),
			2: (4315, 'Sent'),
			3: (4105, 'Required'),
			4: (4106, 'Optional'),
			5: (4294, 'Subject'),
			6:(4101, 'Location'),
			7:(4102, 'DateTime'),
		}
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
		except LookupError:
			raise HeaderFieldNotFoundeError()
		except AttributeError:  # Exception raised when performing tests calling self.rootDialog.windowHandle on FakeRootDialog
			obj = [o for o in self.rootDialog.children if o.windowControlID == cid]
			if len(obj) != 1:
				infos = {
					'obj': obj,
					'cid': cid,
					'name': name,
				}
				log.debug(f'Header field not found. Infos: {infos}')
				raise HeaderFieldNotFoundeError()
			obj = obj[0]
		if controlTypes.STATE_INVISIBLE in obj.states:
			raise HeaderFieldNotFoundeError()
		return obj,name



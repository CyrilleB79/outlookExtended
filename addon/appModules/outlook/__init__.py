# -*- coding: UTF-8 -*-
# NVDA add-on: Outlook Extended
# Copyright (C) 2018-2023 Cyrille Bougot, Ralf Kefferpuetz
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

# Known bugs (not resolved):
# 1. Double-press NVDA+Shift+A to go to attachments may not always work when mail has 20 attachments or so
# (Outlook 2016), especially when e-mail has just been opened.

# Possible enhancements
# 1. Use @script decorator for markAsRead and markAsUnread script gesturs, as well as for reportHeaderFieldN
# scripts. Did not manage to make it work.
# 3. Rename fields wrongly named. E.g. value=None&name=textExpectedFromValue -> take label from previous
# window.
# 4. Implement column navigation in address book: debug column navigation (scroll the list, access other
# children thant the ones visible...)
# 5. Allow to get back to message body even when an attachment preview is displayed when calling NVDA+Shift+M


# TODO: (zzz)
# Check task assigned to others

# Import all from original outlook appModule to keep it available if needed for anyone using this module.
from nvdaBuiltin.appModules.outlook import *  # noqa: F401, F403

# Import here explecitely used variables from original outlook appModule for clarity.
from nvdaBuiltin.appModules.outlook import UIAGridRow, AddressBookEntry, AppModule

from .itemWindow import OutlookItemWindow, NotInMessageWindowError, HeaderFieldNotFoundeError
from .compa import CTWRAPPER as controlTypes

from scriptHandler import getLastScriptRepeatCount, script
import winUser
from logHandler import log
import api
import ui
try:
	from speech import speech
except ImportError:
	# Import for older version of NVDA such as 2019.3.1
	import speech
from NVDAObjects import NVDAObject
from NVDAObjects.window import Window
from NVDAObjects.IAccessible import List, getNVDAObjectFromEvent
from NVDAObjects.behaviors import RowWithoutCellObjects, RowWithFakeNavigation
from NVDAObjects.UIA import UIA
from windowUtils import findDescendantWindow
import tones
import globalVars
import core
import config
import nvwave

import sys
import os
from comtypes import COMError
from locationHelper import RectLTWH
import re
import threading
from time import sleep

import addonHandler

# Save NVDA translation before overriding it
nvdaTranslation = _

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

# Translators: The key ont the right of the "0" key in the alpha-numeric part of the keyboard.
# Note: In the translated documentation (/website/addons/outlookExtended.xx.po in the
# screenReaderTranslations repo), do not forget to modify the commands section accordingly.
KEY_HEADER_FIELD11 = _("-")
# Translators: The key just ont the left of the backspace key.
# Note: In the translated documentation (/website/addons/outlookExtended.xx.po in the
# screenReaderTranslations repo), do not forget to modify the commands section accordingly.
KEY_HEADER_FIELD12 = _("=")

confspec = {
	'testCasePath': 'string(default="")',
}
config.conf.spec["outlookExtended"] = confspec


class ElemWithReadStatus:

	scriptCategory = ADDON_SUMMARY

	@script(
		# Translators: Documentation for mark as read script.
		description=_("Mark a message as read")
	)
	def script_markAsRead(self, gesture):
		gesture.send()
		self.reportReadStatus()

	@script(
		# Translators: Documentation for mark as unread script.
		description=_("Mark a message as unread")
	)
	def script_markAsUnread(self, gesture):
		gesture.send()
		self.reportReadStatus()

	def reportReadStatus(self):
		focus = api.getFocusObject()
		if focus.appModule.nativeOm:
			try:
				selection = focus.appModule.nativeOm.activeExplorer().selection
			except COMError:
				return  # No COM access
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
			selection = selection.item(1)
			try:
				unread = selection.unread
			except COMError:
				unread = False
			if unread:
				# Translators: To announce the message or group status: unread
				itemState = _("unread")
			else:
				# Translators: To announce the message or group status: read
				itemState = _("read")
			ui.message(itemType % itemState)

	__gestures = {
		"kb:control+U": "markAsUnread",
		"kb:control+Q": "markAsRead",
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
			# handle = findDescendantWindow(api.getForegroundObject().windowHandle, controlID=138,
			# className='SysHeader32')
			handle = findDescendantWindow(self.parent.windowHandle, controlID=138, className='SysHeader32')
			self.header = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
			self.allowIAccessibleChildIDAndChildCountForPositionInfo = True
			return self.header

	def _get_columnCount(self):
		header = self.getHeader()
		return len(header.children)

	def _get_rowCount(self):
		# zzz Should be better defined since does not take scrolling use case
		return len(self.children)


class AddressBookEntry(RowWithoutCellObjects, RowWithFakeNavigation, AddressBookEntry):

	def _getColumnLocation(self, column):
		colHeader = self.parent.getHeader().getChild(column - 1)
		return RectLTWH(
			left=colHeader.location.left,
			top=self.location.top,
			width=colHeader.location.width,
			height=self.location.height,
		)

	def _getColumnContent(self, column):
		"""Get the text content for a given column of this row.
		@param column: The index of the column, starting at 1.
		@type column: int
		@rtype: str
		"""
		colNames = [c.name for c in self.parent.getHeader().children]
		colPatterns = [fr"{name} (?P<C{col+1}>.*?)" for col, name in enumerate(colNames)]
		sep = ', '
		pattern = f"^{colPatterns[0]}{''.join(['(?:' + sep + cp + ')?' for cp in colPatterns[1:]])}$"
		m = re.match(pattern, self.name)
		if not m:
			log.warning(f"Parsing failed: self.name = {self.name}; colNames = {colNames}")
			return
		return m.groupdict()[f"C{column}"]

	def _getColumnHeader(self, column):
		"""Get the header text for this column.
		@param column: The index of the column, starting at 1.
		@type column: int
		@rtype: str
		"""
		return self.parent.getHeader().getChild(column - 1).name

	def _get_next(self):
		rows = self.parent.children
		index = rows.index(self)
		if index == len(rows) - 1:
			return None
		return rows[index + 1]

	def _get_previous(self):
		rows = self.parent.children
		index = rows.index(self)
		if index == 0:
			return None
		return rows[index - 1]

	def _moveToRow(self, row):
		# Supersedes _moveToRow in behaviors.py to disable row navigation because need to be debugged:
		# when pressing Ctrl+Alt+downarrow, the focus moves visually but NVDA takes updated focus only when you
		# press control again.

		# Translators: When trying to move by column in address book (Alt+Ctrl+Up/DownArrow)
		ui.message(_('Column navigation not supported in the address book'))


class FakeRootDialog(Window):

	role = controlTypes.Role.DIALOG
	# Translators: The name of a fake NVDA object used for tests.
	name = _("Fake root")
	treeInterceptor = None

	def __init__(self, object=None):
		self.parent = api.getFocusObject()
		self.obj = object
		self.childObjList = object.children
		super().__init__(windowHandle=self.parent.windowHandle)

	def _get_childCount(self):
		return len(self.childObjList)

	def _makeFakeObject(self, index):
		if index < 0 or index >= self.childCount:
			return None
		return _FakeObject(parent=self, index=index, obj=self.childObjList[index])

	def _get_firstChild(self):
		return self._makeFakeObject(0)

	def _get_children(self):
		return [self._makeFakeObject(index) for index in range(0, self.childCount)]

	def _getChild(self, index):
		return self._makeFakeObject(index)


class _FakeObject(NVDAObject):

	def __init__(self, parent, index, obj):
		super().__init__()
		self.parent = parent
		self.index = index
		for k in dir(obj):
			if not k.startswith('_'):
				setattr(self, k, getattr(obj, k))
		self.role = controlTypes.Role(self.role)
		self.states = {controlTypes.State(s) for s in self.states}
		self.processID = parent.processID
		try:
			# HACK: Some NVDA code depends on window properties, even for non-Window objects.
			self.windowHandle = parent.windowHandle
			self.windowClassName = parent.windowClassName
		except AttributeError:
			pass

	def _get_next(self):
		return self.parent._makeFakeObject(self.index + 1)

	def _get_previous(self):
		return self.parent._makeFakeObject(self.index - 1)

	firstChild = None


class UIANotificationZoneButton(UIA):

	@script(
		gestures=['kb:upArrow', 'kb:downArrow'],
	)
	def script_cancelGesture(self, gesture):
		# A script to cancel the upArrow or downArrow in the notification zone,
		# since these gesture may move the focus out of the notification zone.
		pass

	@script(
		gesture='kb:leftArrow',
	)
	def script_previousButton(self, gesture):
		self.sendGestureIfOtherButton(gesture, 'backward')

	@script(
		gesture='kb:rightArrow',
	)
	def script_nextButton(self, gesture):
		self.sendGestureIfOtherButton(gesture, 'forward')

	def sendGestureIfOtherButton(self, gesture, direction):
		obj = self.walkObj(
			oStart=self,
			direction=direction,
			stopCondition=lambda o: o.role == controlTypes.Role.BUTTON and o.isFocusable,
			isRootObj=lambda o: o.role == controlTypes.Role.GROUPING,
		)
		if obj is None:
			return
		gesture.send()

	def walkObj(self, oStart, direction, stopCondition, isRootObj, ignoreChildren=False):
		"""A function to walk the object hierarchy until a condition is met.
		The function returns the first object meeting the condition or None if no object is found.

		@param oStart: the start object
		@type obj: NVDAObject
		@param direction ('backward' or 'forward'): a direction to walk the object hierarchy.
			backward: look for a matching object considering last child, then previous sibling, then parent.
			forward: look for a matching object considering first child, then next sibling, then parent.
		@type direction: str
		@param stopCondition: a function to evaluate if hierarchy walking should stop on this object.
		@type stopCondition: function
		@param isRootObj: a function to evaluate if an object is the root object of the considered object
			hierarchy.
		@type isRootObj: function
		@param ignoreChildren: do not consider first/last child when searching for next matching object.
		@type ignoreChildren: bool
		@rtype: NVDAObject | None
		"""

		if isRootObj(oStart):
			# If root object is reach, no object satisfying the condition has been found.
			return None
		if direction == 'forward':
			propList = ['firstChild', 'next', 'parent']
		elif direction == 'backward':
			propList = ['lastChild', 'previous', 'parent']
		if ignoreChildren:
			del propList[0]
		for prop in propList:
			o = getattr(oStart, prop)
			if o:
				isParent = prop == 'parent'
				if stopCondition(o) and not isParent:
					return o
				else:
					return self.walkObj(o, direction, stopCondition, isRootObj, ignoreChildren=isParent)
		raise RuntimeError('Unexpected object tree structure')


class UIARecipientButton(UIANotificationZoneButton):

	def _get_name(self):
		try:
			return self.firstChild.name
		except AttributeError:
			return super().name

	def reportFocus(self):
		ui.message(self.name)


class UIAMoreInfoButton(UIANotificationZoneButton):

	def _get_name(self):
		# Translators: The name for a button in the notification bar to display more or less information.
		return _('More or less information')

	def reportFocus(self):
		ui.message(self.name)


class NotificationChecker(threading.Thread):
	def __init__(self, appModule, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.outlookAppModule = appModule
		self._stop = threading.Event()

	def stop(self):
		self._stop.set()
		self.outlookAppModule = None

	def stopped(self):
		return self._stop.isSet()

	def run(self):
		oldInfoSet = set()
		oldFgHwnd = 0
		while not self.stopped():
			try:
				try:
					notif = self.outlookAppModule.getNotificationObj()
				except AttributeError:  # In case self.outlookAppModule is set to None.
					log.debugWarning('No link to Outlook appModule.')
				else:
					fg = api.getForegroundObject()
					fgHwnd = fg.windowHandle if fg else 0
					if notif:
						infoSet = {
							# Old version: beeps whenever the notification bar content changes (names added or deleted)
							o.name for o in notif.children if (
								(o.role == controlTypes.Role.BUTTON and o.UIAElement.currentAutomationID == 'RecipientButton')
								or (
									o.role == controlTypes.Role.STATICTEXT
									and o.UIAElement.currentAutomationID == 'MailTipItemPreText'
								)
							)
						}
					else:
						infoSet = set()
					if fgHwnd == oldFgHwnd and infoSet != oldInfoSet:
						focus = api.getFocusObject()
						if focus.windowClassName == 'RichEdit20WPT':
							nvwave.playWaveFile(os.path.join(addonHandler.getCodeAddon().path, "waves", "notify.wav"))
					oldInfoSet = infoSet
					oldFgHwnd = fgHwnd
			except Exception as e:
				# If an error occurs, log it but do not stop the thread.
				log.error(e, exc_info=True)
			sleep(0.5)


class NotificationPaneElement:
	def __init__(self, name, location):
		self.name = name
		self.location = location

	def __repr__(self):
		return '{name} - \nL={left}, T={top}, W= {width}, H={height}\n'.format(
			name=self.name,
			left=self.location.left,
			top=self.location.top,
			width=self.location.width,
			height=self.location.height,
		)


class NotificationPaneRow:
	def __init__(self, obj):
		self.elements = [obj]
		self._bottom = None

	@property
	def bottom(self):
		if self._bottom is None:
			self._bottom = self.elements[0].location.bottom
		return self._bottom

	def add(self, elem):
		if self.bottom != elem.location.bottom:
			log.error('{} != {}'.format(self.bottom, elem.bottom))
		self.elements.append(elem)

	@property
	def text(self):
		textList = []
		for elem in self.elements:
			name = elem.name
			if textList and re.match(r'^\w.*$', name, re.U):
				name = ' ' + name
			textList.append(name)
		return ''.join(textList)


class NotificationPane:
	def __init__(self, pane):
		self.rows = []
		for obj in pane.children:
			name = obj.name
			if name:
				elem = NotificationPaneElement(obj.name, obj.location)
				if not self.rows or self.rows[-1].bottom <= obj.location.top:
					row = NotificationPaneRow(elem)
					self.rows.append(row)
				else:
					self.rows[-1].add(elem)

	@property
	def text(self):
		return '\n'.join(r.text for r in self.rows)


class AppModule(AppModule):

	scriptCategory = ADDON_SUMMARY

	_headerFieldKeyMap = {str(i): i for i in range(1, 10)}
	_headerFieldKeyMap.update({
		'0': 10,
		KEY_HEADER_FIELD11: 11,
		KEY_HEADER_FIELD12: 12})

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lastFocus = None
		self.testCases = None
		self.tcNumber = 0
		self.notificationChecker = NotificationChecker(appModule=self)
		self.notificationChecker.start()

	def terminate(self, *args, **kwargs):
		self.notificationChecker.stop()
		self.notificationChecker = None  # To break ref cycle
		super().terminate(*args, **kwargs)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
		if obj.role == controlTypes.Role.LISTITEM and obj.windowClassName == "OUTEXVLB":
			clsList.insert(0, AddressBookEntry)
			return
		if obj.role == controlTypes.Role.LIST and obj.windowClassName == "OUTEXVLB":
			clsList.insert(0, List)
			return
		if UIAGridRow in clsList:
			clsList.insert(0, UIAGridRowWithReadStatus)
			return
		if UIA in clsList:
			if obj.role == controlTypes.Role.GROUPING and obj.parent.windowClassName == 'OutlookGrid':
				clsList.insert(0, UIAWithReadStatus)
			elif obj.UIAElement.currentAutomationID == 'RecipientButton':
				clsList.insert(0, UIARecipientButton)
			elif obj.UIAElement.currentAutomationID == 'MoreInfo':
				clsList.insert(0, UIAMoreInfoButton)

	def reportHeaderFieldN(self, nField, gesture):
		# Calendar view: Alt+digit is used command to set up number of days in the view
		if api.getFocusObject().windowClassName in ['DayViewWnd', 'WeekViewWnd']:
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
			# Get OutlookItem dialog
			try:
				rootDialog = self.getFakeRootDialog()
				if not rootDialog:
					rootDialog = self.getRootDialog()
				self.olItemWindow = OutlookItemWindow(rootDialog, debug=debug)
			except NotInMessageWindowError:
				self.olItemWindow = None
		if self.olItemWindow is None:
			# Translators: When trying to use Alt+Number shortcut but not in message.
			ui.message(_("Not in a message window"))
			return
		try:
			obj, name = self.olItemWindow.getHeaderFieldObject(nField)
		except HeaderFieldNotFoundeError as e:
			log.debug(f'Header not found: {e}')
			self.errorBeep()
			return
		self.reportObject(obj, nRepeat)

	def getFakeRootDialog(self):
		# Checks if config.conf['outlookExtended']['testCasePath'] is defined.
		# If defined, it allows setting up a debug test framework fore live tests on various message types.
		# The message types are defined in the file case.py that can be found in the Github repo of this add-on.
		# When a message type is selected, alt+digit return the header of the test case object
		# instead of the header of the real window.
		# To activate it, open NVDA console and type:
		# import config
		# config.conf['outlookExtended']['testCasePath'] = r'C:\pathToOutlookExtendedGITLocalRepo\tests\unit'
		if self.testCases and self.tcNumber != 0:
			tcName = list(self.testCases.keys())[self.tcNumber - 1]
			obj = FakeRootDialog(object=self.FakeRootWindow(tcName))
			return obj
		return None

	def reportObject(self, obj, nRepeat):
		# single press
		if nRepeat == 0:
			self.speakObject(obj)
			self.lastFocus = api.getFocusObject()
		# double press, set focus in field
		elif nRepeat == 1:
			handle = obj.windowHandle
			winUser.setForegroundWindow(handle)
		# triple press, copy to clipboard and set focus to original focused object
		elif nRepeat == 2:
			api.copyToClip(obj.value)
			# Translators: When user triple presses Alt+Number to copy a header's field to clipboard
			core.callLater(0, lambda: ui.message(_("Copied to clipboard")))
			api.setNavigatorObject(obj, isFocus=True)
			self.lastFocus.setFocus()

	def speakObject(self, obj):
		if obj.role == controlTypes.Role.CHECKBOX:
			name = obj.name
			value = (
				nvdaTranslation('checked') if controlTypes.State.CHECKED in obj.states
				else nvdaTranslation('not checked')
			)
		else:
			name, value = obj.name, obj.value
		# Translators: To report name and value of a heaeder's field
		ui.message(_("{name} {value}").format(name=name, value=value))

	def errorBeep(self):
		tones.beep(440, 80)

	@script(
		description=_(
			# Translators: Documentation for report notification script.
			"Reports the notification in a message. If pressed twice, moves the focus to it."
			" If pressed three times, copies its content to the clipboard."
		),
		gestures=["kb(desktop):NVDA+shift+N", "kb(laptop):NVDA+control+shift+N"]
	)
	def script_reportNotification(self, gesture):
		obj = self.getNotificationObj()
		if obj is None:
			# Translators: Message reported when calling the script to report notification bar.
			ui.message(_("No notification"))
			return
		nRepeat = getLastScriptRepeatCount()
		if nRepeat == 0:
			notif = NotificationPane(obj)
			self.notificationText = notif.text
			ui.message(self.notificationText)
			self.lastFocus = api.getFocusObject()
		elif nRepeat == 1:
			winUser.setForegroundWindow(obj.windowHandle)
		elif nRepeat == 2:
			api.copyToClip(self.notificationText)
			# Translators: When user triple press NVDA+shift+N to copy the notification text to clipboard
			ui.message(_("Copied to clipboard"))
			winUser.setForegroundWindow(self.lastFocus.windowHandle)

	@script(
		description=_(
			# Translators: Documentation for report info bar script.
			"Reports the information bar in a message, calendar item or task window."
			" If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard."
		),
		gestures=["kb(desktop):NVDA+shift+I", "kb(laptop):NVDA+control+shift+I"]
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
		gestures=["kb(desktop):NVDA+shift+M", "kb(laptop):NVDA+control+shift+M"]
	)
	def script_focusToMessageBody(self, gesture):
		try:
			obj = getNVDAObjectFromEvent(
				findDescendantWindow(
					api.getForegroundObject().windowHandle,
					visible=True,
					className=None,
					controlID=4159,
				),
				winUser.OBJID_CLIENT,
				0,
			)
		except LookupError:
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
			return
		obj.setFocus()

	@script(
		description=_(
			# Translators: Documentation for Attachments script.
			"Reports the number and the names of attachments in a message window."
			" If pressed twice, moves the focus to it.",
		),
		gestures=["kb(desktop):NVDA+shift+A", "kb(laptop):NVDA+control+shift+A"]
	)
	def script_attachments(self, gesture):
		obj = api.getFocusObject()
		appVersionMaj = int(obj.appModule.productVersion.split('.')[0])

		try:
			if appVersionMaj >= 16:  # Outlook 2016+
				attachmentsList, handle, namesGen, windowName = self.getAttachmentInfos2016()
			else:
				attachmentsList, handle, namesGen, windowName = self.getAttachmentInfos2013()
		except LookupError:
			self.errorBeep()
			return
		self.nAttachments = len(attachmentsList)
		# double press, set focus in field
		if getLastScriptRepeatCount() == 1 and self.nAttachments > 0:
			self.focusInfo['firstObj'].setFocus()
			winUser.setForegroundWindow(self.focusInfo['handle'])
		# single press
		else:
			self.focusInfo = {'handle': handle}
			try:
				self.focusInfo['firstObj'] = attachmentsList[0]
			except IndexError:
				self.focusInfo['firstObj'] = None

			# Launch the attachments announcement code in a different thread since it can take time in the case of
			# numerous attachments (above 17 on my machine).
			# In this case, getLastScriptRepeatCount() after double press will return 0 instead of 1.
			def announceAttachments():
				attachmentList = ', '.join(namesGen)
				msg = f"{windowName}: {self.nAttachments}. {attachmentList}"
				core.callLater(0, ui.message, msg)
			threading.Thread(target=announceAttachments).start()

	def getAttachmentInfos2016(self):
		fg = api.getForegroundObject()
		cidAttachments = 4306
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
		return attachmentsList, handle, namesGen, obj.name

	def getAttachmentInfos2013(self):
		fg = api.getForegroundObject()
		cidAttachments = 4623
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
			cidAttachments = 4104
			try:
				handle = findDescendantWindow(fg.windowHandle, className=None, controlID=cidAttachments)
				obj = getNVDAObjectFromEvent(handle, winUser.OBJID_CLIENT, 0)
				if obj.firstChild is None:
					raise LookupError
				bFoundWindow = True

				def makeGenChildren(o):
					"""Define a generator to get children since the .children property does not work
					"""

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
			return attachmentsList, handle, namesGen, obj.name
		else:
			return [], handle, [], obj.name

	def getInfoBarControlId(self):
		majVer = int(self.productVersion.split('.')[0])
		if majVer <= 11:
			cid = 4105  # Outlook 2003
		else:
			cid = 4262  # Outlook 2016
		return cid

	def getInfoBarObj(self):
		try:
			cid = self.getInfoBarControlId()
			obj = getNVDAObjectFromEvent(
				findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=cid),
				winUser.OBJID_CLIENT,
				0,
			)
		except LookupError:
			obj = None
		return obj

	def getRootDialog(self):
		obj = api.getFocusObject()
		try:
			while obj.windowClassName != "#32770":
				obj = obj.parent
		except AttributeError:
			raise NotInMessageWindowError
		if obj.role == controlTypes.Role.WINDOW:
			# Sometimes going up hierarchy goes directly to window object without passing via dialog object -> go to
			# first child
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
			# Translators: Reported when calling a test command
			ui.message(_('Test case path not defined.'))
		return isTest

	# Test scripts
	# 1. Scripts to select next and previous test cases when test mode is active
	# 2. Script to move the navigator object on the fake root dialog.
	# These scripts are unassigned by default
	# To assign them, edit directly the gesture.ini file, e.g. by pasting the following lines:
	# [appModules.outlook.AppModule]
	# selectNextTestCase = kb:control+f6+nvda+shift
	# selectPreviousTestCase = kb:control+f5+nvda+shift
	# move= kb:control+f8+nvda+shift
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
			# Translators: Reported when calling a test command
			ui.message(_('Test mode offf'))

	def script_navigatorObject_toFakeRootDialog(self, gesture):
		if not self.tcNumber:  # None or 0
			# Translators: Reported when calling a test command
			ui.message(_('Test mode is off.'))
			return
		obj = self.getFakeRootDialog()
		api.setNavigatorObject(obj)
		speech.speakObject(obj)

	def getNotificationObj(self):
		fgObj = api.getForegroundObject()
		if not fgObj or fgObj.appModule is not self:
			return None
		try:
			cid = 4265
			obj = getNVDAObjectFromEvent(
				findDescendantWindow(fgObj.windowHandle, visible=True, className=None, controlID=cid),
				winUser.OBJID_WINDOW, 0)

			def getChildWithRole(o, role):
				return [oc for oc in obj.children if oc.role == role][0]
			obj = getChildWithRole(obj, controlTypes.Role.PANE)
			obj = getChildWithRole(obj, controlTypes.Role.PANE)
			obj = getChildWithRole(obj, controlTypes.Role.PANE)
			obj = getChildWithRole(obj, controlTypes.Role.GROUPING)
			obj = getChildWithRole(obj, controlTypes.Role.PANE)
		except LookupError:
			return None
		return obj

	__gestures = {f"kb:alt+{key}": f"reportHeaderField{n}" for (key, n) in _headerFieldKeyMap.items()}

	@staticmethod
	def _createScript_reportHeaderField(n):
		def _genericScript_reportHeaderField(self, gesture):
			return self.reportHeaderFieldN(n, gesture)
		_genericScript_reportHeaderField.__doc__ = _(
			# Translators: Input help mode message for report a header's field command. in outlook message, calendar
			# item or task window
			"Reports the header field %s in a message, calendar item or task window. If pressed twice, moves"
			" the focus to this field if possible. If pressed three times, copies its content to the clipboard."
		) % str(n)
		return _genericScript_reportHeaderField

	@classmethod
	def createAllScript_reportHeaderField(cls):
		for n in range(1, len(cls._headerFieldKeyMap) + 1):
			scriptName = f"script_reportHeaderField{n}"
			scriptFun = AppModule._createScript_reportHeaderField(n)
			setattr(cls, scriptName, scriptFun)


AppModule.createAllScript_reportHeaderField()

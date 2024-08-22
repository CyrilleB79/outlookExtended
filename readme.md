# Outlook extended

* Authors: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Download [stable version][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes some native commands and adds extra commands and features.

## Commands

* Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Reports the header field 1 to 12 in a message, calendar item or task window. If pressed twice, moves the focus to this field if possible. If pressed three times, copies its content to the clipboard.
* NVDA+shift+I (desktop layout) / NVDA+control+shift+I (laptop layout): Reports the information bar in a message, calendar item or task window. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments; if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable message the attendees status on the time slot of the meeting.

* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout): Moves the focus to the message body.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout): Reports the notification in a message window. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: in the message list, marks the selected message or group of messages as read.
* Control+U: in the message list, marks the selected message or group of messages as unread.

## Additional improvements

* When the recipient you have entered in the To, Cc or Bcc fields sends automatic out of office replies or is not present anymore on the Exchange server, Outlook report it in the notification area of the message window. In this notification area, you also have buttons to remove the address of these recipients.
  This add-on will inform you with a ding when this notification area appears, disappears or is updated. You can then press NVDA+shif+N / NVDA+control+shift+N once to have it read and twice to jump to this area. Then move with the arrows on the recipient buttons and press a button to remove the corresponding recipient.
* In the address book's result list, you can use horizontal table navigation commands to read the content of each column.
  
## Notes

All the gestures can be modified in the NVDA command gestures dialog. You may want to modify them especially in the following situations:

* The default gestures to mark messages as read or unread are the ones for Outlook english version. If they differ from the ones of your Outlook local version, you will have to change them accordingly.
* The default gestures to read headers correspond to Alt combined with the keys of the first row of the alpha-numeric keyboard. You may need to re-map the gestures tor read header 11 and 12 if they do not match your local keyboard layout.

## Change log

### Version 3.0

* In a meeting window, in the all attendees tab, pressing NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout) now displays in a browseable message the attendees status on the time slot of the meeting.

### Version 2.4

* Compatibility with NVDA 2024.1.
* Relevant commands are now usable in on-demand speech mode.

### Version 2.3

* Note: From now on, translation updates will not appear anymore in the change log.

### Version 2.2

* Restored compatibiliity with NVDA 2019.3.1.
* Updated localizations.

### Version 2.1

* Removed the dev channel.
* Updated localizations.

### Version 2.0

* Improve the user experience with the notifications appearing when entering e-mail addresses which are not valid anymore or which send automatic out of office replies:
  a sound alerts when such notifications appear or are updated, a gesture allows to read it or to move to it, and navigation in this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Updated localizations.

### Version 1.9

* Compatibility with NVDA 2022.1.
* Dropped compatibility for versions of NVDA below 2019.3.
* The release is now performed thanks to a GitHub action instead of appVeyor.
* Fixed the announcement when the user triple-presses alt+number shortcuts.
* Fixed an issue preventing from reading calendar items headers of some versions of Outlook 365.
* Improvement of the test environment of the add-on: navigation in the fake root dialog.
* Updated localizations.

### Version 1.8

* Updated localizations.
* Ensure that all the variable from the original Outlook appModule are still available.

### Version 1.7

* Update compatibility for NVDA 2021.1.
* Updated localizations.

### Version 1.6

* Fixed various issues when reading messages headers in Outlook 365.
* Fixed an error in announce attachments script when a braille keyboard is used.
* Added a unit test framework.
* Updated localizations.

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA 2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are present.
* Added localizations.

### Version 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Added localizations.
* Releases performed now with appveyor.

### Version 1.2

* Fixed header reading when forwarding meeting.
* Added localizations.

### Version 1.1

* Added localizations.

### Version 1.0

* Initial release.

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

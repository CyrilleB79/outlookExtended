# Outlook extended

* Authors: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Download [stable version][1]
* Download [development version][2]

This addon improves the use of Microsoft Outlook by vocalizing some commands and adding extra commands.

## Commands

* Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Reports the header field 1 to 12 in a message, calendar item or task window. If pressed twice, moves the focus to this field if possible. If pressed three times, copies its content to the clipboard.
* NVDA+shift+I (desktop layout) / NVDA+control+shift+I (laptop layout): Reports the information bar in a message, calendar item or task window. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout): Reports the number and the names of attachments in a message window. If pressed twice, moves the focus to it.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout): Moves the focus to the message body.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout): Reports the notification in a message window. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard. The notification area messages contain buttons to remove the cited recipients; once the notification area is focused, use arrows to move between these buttons.
* Control+Alt+Left and Control+Alt+Right: in the address book search result list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of messages as read.
* Control+U: in the message list, marks the selected message or group of messages as unread.


## Notes

All the gestures can be modified in the NVDA command gestures dialog. You may want to modify them especially in the following situations:

* The default gestures to mark messages as read or unread are the ones for Outlook english version. If they differ from the ones of your Outlook local version, you will have to change them accordingly.
* The default gestures to read headers correspond to Alt combined with the keys of the first row of the alpha-numeric keyboard. You may need to re-map the gestures tor read header 11 and 12 if they do not match your local keyboard layout.

## Change log

### Version 1.9

* Prepared compatibility for NVDA 2022.1
* Dropped compatibility for versions of NVDA below 2019.3
* Fixed the announcement when the user triple-presses alt+number shortcuts.

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

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

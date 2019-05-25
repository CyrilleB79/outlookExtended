# Outlook extended

* Authors: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2018.3 to 2019.1
* Download [stable version][1]
* Download [development version][2]

This addon improves the use of Microsoft Outlook by vocalizing some commands and adding extra commands.

## Commands

* Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Reports the header field 1 to 12 in a message, calendar item or task window. If pressed twice, moves the focus to this field if possible. If pressed three times, copies its content to the clipboard.
* NVDA+shift+I (desktop layout) / NVDA+control+shift+I (laptop layout): Reports the information bar in a message, calendar item or task window. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout): Reports the number and the names of attachments in a message window. If pressed twice, moves the focus to it.
* NVDA+shift+M (desktop layout) / NVDA+shift+M (laptop layout): Moves the focus to the message body
* Control+Alt+Left and Control+Alt+Right: in the address book search result list, navigate between the fields of the currently selected line
* Control+Q: in the message list, mark the selected message or group of messages as read
* Control+U: in the message list, mark the selected message or group of messages as unread

## Notes

All the gestures can be modified in the NVDA command gestures dialog. You may want to modify them especially in the following situations:

* The default gestures to mark messages as read or unread are the ones for Outlook english version. If they differ from the ones of your Outlook local version, you will have to change them accordingly.
* The default gestures to read headers correspond to Alt combined with the keys of the first row of the alpha-numeric keyboard. You may need to re-map the gestures tor read header 11 and 12 if they do not match your local keyboard layout.

## Change log

### Version 1.2

* Fix header reading when forwarding meeting.
* Added localizations.

### Version 1.1

* Added localizations.

### Version 1.0

* Initial release.

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

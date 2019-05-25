# Erweiterte Outlook-Funktionen #

* Autoren: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2018.3 to 2019.1
* [stabile version herunterladen][1]
* Download [development version][2]

Diese Erweiterung verbessert die Verwendung von Microsoft Outlook mit NVDA,
indem es einige Tastenbefehle meldet und zusätzliche Befehle hinzufügt.

## Befehle

* Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Reports the header field 1 to 12 in a
  message, calendar item or task window. If pressed twice, moves the focus
  to this field if possible. If pressed three times, copies its content to
  the clipboard.
* NVDA+shift+I (desktop layout) / NVDA+control+shift+I (laptop layout):
  Reports the information bar in a message, calendar item or task window. If
  pressed twice, moves the focus to it. If pressed three times, copies its
  content to the clipboard.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  Reports the number and the names of attachments in a message window. If
  pressed twice, moves the focus to it.
* NVDA+shift+M (desktop layout) / NVDA+shift+M (laptop layout): Moves the
  focus to the message body
* STRG+Alt+Pfeil links und STRG+Alt+Pfeil rechts: navigiert zwischen den
  Spalten der aktuell ausgewählten Zeile in der Ergebnisliste der
  Adressbuchsuche
* STRG+Q: markiert die ausgewählte Nachricht oder Gruppe von Nachrichten als
  gelesen in der Nachrichtenliste
* STRG+U: markiert die ausgewählte Nachricht oder Gruppe von Nachrichten als
  ungelesen in der Nachrichtenliste

## Anmerkungen

Alle Tastenbefehle können im Dialogfeld "Eingaben" geändert
werden. Insbesondere in den folgenden Situationen könnte die Änderung der
Befehle sinnvoll sein:

* The default gestures to mark messages as read or unread are the ones for
  Outlook english version. If they differ from the ones of your Outlook
  local version, you will have to change them accordingly.
* Die Standardgesten für das Lesen der Kopfspalten entsprechen Alt in
  Kombination mit den Tasten der ersten Zeile der alphanumerischen
  Tastatur. Möglicherweise müssen Sie die Gesten für die gelesenen Header 11
  und 12 neu zuordnen, wenn sie nicht mit Ihrem lokalen Tastaturlayout
  übereinstimmen.

## Änderungsprotokoll

### Version 1.0

* Erste Veröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

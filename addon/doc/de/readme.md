# Erweiterte Outlook-Funktionen #

* Autoren: Cyrille Bougot, Ralf Kefferpuetz
* NVDA-Kompatibilität: 2018.3 bis 2019.3
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung verbessert die Verwendung von Microsoft Outlook mit NVDA,
indem es einige Tastenbefehle meldet und zusätzliche Befehle hinzufügt.

## Befehle

* Alt+1 bis Alt+9, Alt+0, Alt+-, alt+=: meldet die Kopfspalte 1 bis 12 in
  einer Nachricht, einem Kalenderelement oder einem
  Aufgabenfenster. Zweimaliges Drücken verschiebt den Systemfokus nach
  Möglichkeit auf das entsprechende Feld. Dreimaliges Drücken kopiert den
  Inhalt der Kopfspalte in die Zwischenablage.
* NVDA+Umschalt+I (Desktop-Schema) / NVDA+Strg+Umschalt+I (Laptop-Schema):
  meldet die Informationsleiste in einer Nachricht, einem Kalenderelement
  oder einem Aufgabenfenster. Zweimaliges Drücken verschiebt den Fokus auf
  das Informationsfeld. Dreimaliges Drücken kopiert den Inhalt des Feldes in
  die Zwischenablage.
* NVDA+Umschalt+A (Desktop-Schema)  / NVDA+Strg+Umschalt+A (Laptop-Schema):
  Meldet die Anzahl und die Namen der Anlagen in einem
  Nachrichtenfenster. Zweimaliges Drücken verschiebt den Fokus auf die Liste
  der Anlagen .
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

## Anmerkungen

Alle Tastenbefehle können im Dialogfeld "Eingaben" geändert
werden. Insbesondere in den folgenden Situationen könnte die Änderung der
Befehle sinnvoll sein:

* Die Standardgesten, um Nachrichten als gelesen oder ungelesen zu
  markieren, sind die für die englische Outlook-Version. Wenn sie von denen
  Ihrer lokalen Outlook-Version abweichen, müssen Sie sie entsprechend
  ändern.
* Die Standardgesten für das Lesen der Kopfspalten entsprechen Alt in
  Kombination mit den Tasten der ersten Zeile der alphanumerischen
  Tastatur. Möglicherweise müssen Sie die Gesten für die gelesenen Header 11
  und 12 neu zuordnen, wenn sie nicht mit Ihrem lokalen Tastaturlayout
  übereinstimmen.

## Änderungsprotokoll

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Lokalisierungen hinzugefügt.

### Version 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Lokalisierungen hinzugefügt.
* Releases performed now with appveyor.

### Version 1.2

* Fixed header reading when forwarding meeting.
* Lokalisierungen hinzugefügt.

### Version 1.1

* Lokalisierungen hinzugefügt.

### Version 1.0

* Erste Veröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

# Erweiterte Outlook-Funktionen #

* Autoren: Cyrille Bougot, Ralf Kefferpuetz
* NVDA-Kompatibilität: 2018.3 bis 2020.3
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
* NVDA+Umschalt+M (Desktop-Schema) / NVDA+Steuerung+Umschalt+M
  (Laptop-Schema): Verschiebt den Fokus auf den Nachrichtentext.
* STRG+Alt+Pfeil links und STRG+Alt+Pfeil rechts: navigiert zwischen den
  Spalten der aktuell ausgewählten Zeile in der Ergebnisliste der
  Adressbuchsuche.
* STRG+Q: markiert die ausgewählte Nachricht oder Gruppe von Nachrichten als
  gelesen in der Nachrichtenliste.
* STRG+U: markiert die ausgewählte Nachricht oder Gruppe von Nachrichten als
  ungelesen in der Nachrichtenliste.

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

### Version 1.6

* Mehrere Fehler behoben, die beim lesen von NachrichtenÜberschriften in
  Outlook 365 auftraten.
* Ein Fehler im Skript zum Ansagen von Anhängen bei verwendeter
  Braille-Tastatur wurde behoben.
* Ein Test-Framework wurde hinzugefügt.
* Lokalisierungen aktualisiert.

### Version 1.5

* Das Lesen der Informationsleiste funktioniert jetzt mit NVDA 2019.3.
* Die Tabellennavigation in den Adressbuchergebnissen funktioniert jetzt mit
  NVDA 2019.3.

### Version 1.4

* Das Skript zum Verschieben des Fokus auf Überschriften funktioniert
  wieder.
* Der Befehl, um zu Anlagen zu wechseln, funktioniert jetzt, wenn mehrere
  Anlagen vorhanden sind.
* Lokalisierungen hinzugefügt.

### Version 1.3

* Korrigiert das Vorlesen von Kopfzeilen in Nachrichten für neuere Office
  365-Versionen.
* Updates der Unterstützungen neuerer NVDA-Versionen (kompatibel mit Python
  2 und 3)
* Lokalisierungen hinzugefügt.
* Releases werden nun mit Appvayor bereitgestellt.

### Version 1.2

* Die Kopfzeilenanzeige beim Weiterleiten von Besprechungen wurde
  korrigiert.
* Lokalisierungen hinzugefügt.

### Version 1.1

* Lokalisierungen hinzugefügt.

### Version 1.0

* Erste Veröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

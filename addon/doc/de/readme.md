# Erweiterte Outlook-Funktionen #

* Autoren: Cyrille Bougot und Ralf Kefferpuetz
* NVDA-Kompatibilität: 2019.3 und neuer
* [Stabile Version herunterladen][1]

Diese NVDA-Erweiterung verbessert die Nutzung von Microsoft Outlook, indem
es einige systemeigene Befehle vokalisiert, zusätzliche Befehle hinzufügt
und zusätzliche Funktionen bietet.

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
* NVDA+Umschalt+N (Desktop-Layout) / NVDA+Strg+Umschalt+N (Laptop-Layout):
  Teilt die Benachrichtigung in einem Nachrichtenfenster mit. Bei
  zweimaligem Drücken wird der Fokus dorthin verschoben. Bei dreimaligem
  Drücken wird der Inhalt in die Zwischenablage kopiert.
* STRG+Q: markiert die ausgewählte Nachricht oder Gruppe von Nachrichten als
  gelesen in der Nachrichtenliste.
* STRG+U: markiert die ausgewählte Nachricht oder Gruppe von Nachrichten als
  ungelesen in der Nachrichtenliste.

## Zusätzliche Verbesserungen

* Wenn der Empfänger, den Sie in den Feldern An, Cc oder Bcc eingegeben
  haben, automatische Abwesenheitsantworten sendet oder nicht mehr auf dem
  Exchange-Server vorhanden ist, meldet Microsoft Outlook dies im
  Benachrichtigungsbereich. In diesem Benachrichtigungsbereich stehen Ihnen
  auch Schaltflächen zur Verfügung, um die Adressen dieser Empfänger zu
  entfernen.  Diese NVDA-Erweiterung informiert Sie mit einem Klingeln, wenn
  dieser Benachrichtigungsbereich erscheint, verschwindet oder aktualisiert
  wird. Sie können dann einmal NVDA+Umschalt+N oder NVDA+Strg+Umschalt+N
  drücken, um es vorzulesen und zweimal, um zu diesem Bereich zu
  springen. Bewegen Sie sich dann mit den Pfeiltasten auf den Empfängern und
  drücken Sie eine Taste, um den entsprechenden Empfänger zu entfernen.
* In der Ergebnisliste des Adressbuchs können Sie die horizontale
  Tabellennavigation verwenden, um den Inhalt der einzelnen Spalten
  vorzulesen.
  
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

### Version 2.1

* Der Dev-Kanal wurde entfernt.
* Lokalisierungen aktualisiert.

### Version 2.0

* Verbesserung der Benutzerfreundlichkeit durch Benachrichtigungen bei der
  Eingabe von E-Mail-Adressen, die nicht mehr gültig sind oder automatische
  Abwesenheitsantworten senden: ein Ton warnt, wenn solche
  Benachrichtigungen erscheinen oder aktualisiert werden, eine Geste
  ermöglicht es, sie zu lesen oder dorthin zu gelangen, und die Navigation
  in diesem Bereich wird durch Pfeile erleichtert.

### Version 1.10

* Kompatibel mit NVDA 2023.1.
* Lokalisierungen aktualisiert.

### Version 1.9

* Kompatibilität mit NVDA 2022.1.
* Die Unterstützung für NVDA-Versionen älter als 2019.3 wurde entfernt.
* Die Freigabe erfolgt nun über eine GitHub-Aktion anstelle von appVeyor.
* Die Mitteilung, sobald der Benutzer dreimal die Tastenkombination
  Alt+Ziffer drückt, wurde korrigiert.
* Es wurde ein Problem behoben, welches das Auslesen der Kopfzeilen von
  Kalenderelementen in einigen Versionen von Outlook 365 verhinderte.
* Verbesserung der Test-Umgebung der NVDA-Erweiterung: Navigation im
  Fake-Root-Dialogfeld.
* Lokalisierungen aktualisiert.

### Version 1.8

* Lokalisierungen aktualisiert.
* Es wird sichergestellt, dass alle Variablen aus dem ursprünglichen
  App-Modul für Outlook noch verfügbar sind.

### Version 1.7

* Kompatibilität aktualisiert für NVDA 2021.1.
* Lokalisierungen aktualisiert.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

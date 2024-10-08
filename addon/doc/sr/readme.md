# Poboljšanja za Outlook #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Preuzmite [stabilnu verziju][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

## Komande

* Od Alt+1 do Alt+9, Alt+0, Alt+-, Alt+=: Prijavljuje jedno od polja iz
  zaglavlja (od 1 do 12) u prozoru poruke, stavke u kalendaru ili
  zadatka. Ako se pritisne dva puta, premešta fokus na polje ukoliko je to
  moguće. Ako se pritisne tri puta, kopira sadržaj polja u privremenu
  memoriju.
* NVDA+Shift+I (desktop raspored) / NVDA+Control+Shift+I (laptop raspored):
  Prijavljuje traku sa informacijama u prozoru poruke, stavke u kalendaru
  ili zadatka. Ako se pritisne dva puta, premešta fokus na traku. Ako se
  pritisne tri puta, kopira njen sadržaj u privremenu memoriju.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA+Shift+M (desktop raspored) / NVDA+Control+Shift+M (laptop raspored):
  Premešta fokus na telo poruke.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: U listi poruka, označava trenutno odabrane poruke kao
  pročitane.
* Control+U: U listi poruka, označava trenutno odabrane poruke kao
  nepročitane.

## Additional improvements

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area of the message
  window. In this notification area, you also have buttons to remove the
  address of these recipients.  This add-on will inform you with a ding when
  this notification area appears, disappears or is updated. You can then
  press NVDA+shif+N / NVDA+control+shift+N once to have it read and twice to
  jump to this area. Then move with the arrows on the recipient buttons and
  press a button to remove the corresponding recipient.
* In the address book's result list, you can use horizontal table navigation
  commands to read the content of each column.
  
## Napomene

Sve prečice se mogu menjati u dijalogu za podešavanje ulaznih komandi. Možda
ćete želeti da ih promenite, pogotovo u sledećim situacijama:

* Podrazumevane prečice za označavanje poruka kao pročitanih ili
  nepročitanih su iz engleske verzije Outlook-a. Ako se razlikuju od onih u
  verziji na jeziku koji koristite, biće potrebno da ih podesite.
* Podrazumevane prečice za čitanje polja u zaglavlju odgovaraju tasteru Alt
  u kombinaciji sa jednim od tastera iz prvog, alfanumeričkog reda na
  tastaturi sa engleskim rasporedom. Možda će biti neophodno da promenite
  prečice za 11. i 12. polje ako koristite drugi raspored tastature.

## Lista promena

### Version 3.0

* In a meeting window, in the all attendees tab, pressing NVDA+shift+A
  (desktop layout) / NVDA+control+shift+A (laptop layout) now displays in a
  browseable message the attendees status on the time slot of the meeting.

### Version 2.4

* Compatibility with NVDA 2024.1.
* Relevant commands are now usable in on-demand speech mode.

### Version 2.3

* Note: From now on, translation updates will not appear anymore in the
  change log.

### Version 2.2

* Restored compatibiliity with NVDA 2019.3.1.
* Updated localizations.

### Version 2.1

* Removed the dev channel.
* Updated localizations.

### Version 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Updated localizations.

### Version 1.9

* Compatibility with NVDA 2022.1.
* Dropped compatibility for versions of NVDA below 2019.3.
* The release is now performed thanks to a GitHub action instead of
  appVeyor.
* Fixed the announcement when the user triple-presses alt+number shortcuts.
* Fixed an issue preventing from reading calendar items headers of some
  versions of Outlook 365.
* Improvement of the test environment of the add-on: navigation in the fake
  root dialog.
* Updated localizations.

### Version 1.8

* Updated localizations.
* Ensure that all the variable from the original Outlook appModule are still
  available.

### Version 1.7

* Update compatibility for NVDA 2021.1.
* Updated localizations.

### Version 1.6

* Fixed various issues when reading messages headers in Outlook 365.
* Fixed an error in announce attachments script when a braille keyboard is
  used.
* Added a unit test framework.
* Updated localizations.

### Verzija 1.5

* Čitanje trake sa informacijama sada radi sa NVDA 2019.3.
* Navigacija u rezultatima pretrage kontakata sada radi sa NVDA 2019.3.

### Verzija 1.4

* Skripta za premeštanje fokusa na polja u zaglavlju ponovo radi.
* Skripta za premeštanje fokusa na listu priloga sada radi i kada ima više
  priloga.
* Dodati prevodi.

### Verzija 1.3

* Ispravljeno čitanje zaglavlja poruka u novijoj verziji Outlook-a u okviru
  paketa Office 365.
* Ažuriranja kako bi novije NVDA verzije bile podržane (Python 2 i Python 3
  kompatibilnost).
* Dodati prevodi.
* Izdanja se sada izrađuju koristeći appveyor.

### Verzija 1.2

* Ispravljeno čitanje zaglavlja pri prosleđivanju sastanka.
* Dodati prevodi.

### Verzija 1.1

* Dodati prevodi.

### Verzija 1.0

* Prvo izdanje.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

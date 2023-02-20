# Poboljšanja za Outlook #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Preuzmite [stabilnu verziju][1]
* Preuzmite [verziju u razvoju][2]

Ovaj dodatak olakšava korišćenje programa Microsoft Outlook izgovaranjem
nekih postojećih i dodavanjem novih komandi.

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
* NVDA+Shift+A (desktop raspored) / NVDA+Control+Shift+A (laptop raspored):
  Prijavljuje broj i nazive priloga u prozoru poruke. Ako se pritisne dva
  puta, premešta fokus na priloge.
* NVDA+Shift+M (desktop raspored) / NVDA+Control+Shift+M (laptop raspored):
  Premešta fokus na telo poruke.
* Control+Alt+levo i Control+Alt+desno: U listi rezultata pretrage
  kontakata, kreće se po poljima trenutno odabranog rezultata.
* Control+Q: U listi poruka, označava trenutno odabrane poruke kao
  pročitane.
* Control+U: U listi poruka, označava trenutno odabrane poruke kao
  nepročitane.

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

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

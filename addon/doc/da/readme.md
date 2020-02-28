# Udvidelse til Outlook #

* Forfattere: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2018.3 to 2019.3
* Download [stabil version][1]
* Download [udviklingsversion][2]

Denne tilføjelse forbedrer brugen af Microsoft Outlook ved at udtale nogle
kommandoer og tilføje ekstra kommandoer.

## Kommandoer

* Alt+1 til Alt+9, Alt+0, Alt+-, alt+=: Rapporterer felterne fra 1 til 12 i
  overskrifterne i en besked, kalenderobjekt eller opgavevindue. Hvis denne
  kommando trykkes to gange, flyttes fokus til det pågældende felt hvis
  muligt. Hvis kommandoen trykkes to gange, kopieres indholdet til
  udklipsholderen.
* NVDA+shift+I (desktoplayout) NVDA+Shift+Ctrl+I (Laptoplayout): Rapporterer
  informationslinjen i en besked, kalenderobjekt eller opgavevindue. Hvis du
  trykker to gange, flyttes fokus til den. Hvis du trykker tre gange,
  kopierer du indholdet til udklipsholderen.
* NVDA+shift+A (Desktoplayout) NVDA+Shift+Ctrl+A (Laptoplayout): Rapporterer
  nummeret og navnene på vedhæftede filer i et meddelelsesvindue. Hvis du
  trykker to gange, flyttes fokus til det pågældende område.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

## Bemærkninger

Alle kommandoer kan ændres i dialogboksen for inputbevægelser. Du skal i
nogle tilfælde ændre dem særligt i følgende situationer:

* Standardkommandoerne til at markere meddelelser som læst eller ulæst er
  dem til Outlook i engelsk udgave. Hvis de adskiller sig fra dem i din
  Outlook-version på dit pågældende sprog, skal du ændre dem i
  overensstemmelse hermed.
* Standardkommandoerne til at læse overskrifter svarer til Alt kombineret
  med tasterne til den første række af det alfanumeriske tastatur. Du skal
  muligvis tildele andre kommandoer for at læse overskrift 11 og 12, hvis de
  ikke passer til dit lokale tastaturlayout.

## Ændringshistorik

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
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

* Første udgivelse

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

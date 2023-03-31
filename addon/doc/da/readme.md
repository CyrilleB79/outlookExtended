# Udvidelse til Outlook #

* Forfattere: Cyrille Bougot, Ralf Kefferpuetz
* NVDA-kompatibilitet: 2019.3 og derefter
* Download [stabil version][1]
* Download [udviklingsversion][2]

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

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
* NVDA+Shift+M (Desktoplayout) NVDA+Shift+M (Laptoplayout): flytter fokus
  til beskedområdet.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Ctrl+Q: Markerer den valgte besked eller gruppe af meddelelser som læst i
  meddelelseslisten.
* Ctrl+U: Markerer den valgte besked eller gruppe af meddelelser som ulæste
  i meddelelseslisten.

## Additional improvements

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area. In this notification
  area, you also have buttons to remove the address of these recipients.
  This add-on will inform you with a ding when this notification area
  appear, disappear or be updated. You can then press NVDA+shif+N /
  NVDA+control+shift+N once to have it read and twice to jump to this
  area. Then move with arrows on the recipient buttons and press a button to
  remove the corresponding recipient.
* In the address book's result list, you can use horizontal table navigation
  commands to read the content of each column.
  
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

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Opdaterede oversættelser.

### Version 1.9

* Kompatibilitet med NVDA 2022.1.
* Droppet kompatibilitet for versioner af NVDA under 2019.3.
* Udgivelsen udføres nu takket være en GitHub-handling i stedet for
  appVeyor.
* Rettede meddelelsen, når brugeren udfører et tredobbelte trykk på
  alt+nummer genveje.
* Rettede et problem, der forhindrede i at læse kalenderelementer i nogle
  versioner af Outlook 365.
* Forbedring af testmiljøet for tilføjelsen: navigation i den falske
  roddialog.
* Opdaterede oversættelser.

### Version 1.8

* Opdaterede oversættelser.
* Sørget for, at alle variabler fra det originale Outlook appModule stadig
  er tilgængelige.

### Version 1.7

* Opdateret kompatibilitetsstatus til NVDA 2021.1.
* Opdaterede oversættelser.

### Version 1.6

* Rettet forskellige problemer, når du læser beskedoverskrifter i Outlook
  365.
* Rettede en fejl i scriptet til annoncering af vedhæftelser, når et
  punkttastatur bruges.
* Tilføjet et unit test framework.
* Opdaterede oversættelser.

### Version 1.5

* Læsning af statuslinjen fungerer nu med NVDA 2019.3.
* Tabelnavigation i resultaterne af adressebogen fungerer nu med NVDA
  2019.3.

### Version 1.4

* Scriptet for at flytte fokus til overskrifter fungerer igen.
* Skriptet, der skal flytte til vedhæftede filer, fungerer nu, når flere
  vedhæftede filer er til stede.
* Tilføjede oversættelser.

### Version 1.3

* Rettede læsning af meddelelsesoverskrifter, der læser for nyere Office
  365-udgivelse.
* Opdateringer til understøttelse af nyere versioner af NVDA (kompatibel med
  Python 2 og 3)
* Tilføjede oversættelser.
* Udgivelser udføres nu med appveyor.

### Version 1.2

* Rettede læsning af overskrifter, når der videresendes møder.
* Tilføjede oversættelser.

### Version 1.1

* Tilføjede oversættelser.

### Version 1.0

* Første udgivelse.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

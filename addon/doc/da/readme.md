# Udvidelse til Outlook #

* Forfattere: Cyrille Bougot, Ralf Kefferpuetz
* NVDA-kompatibilitet: 2018.3 til 2019.1
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
* NVDA+Shift+M (Desktoplayout) NVDA+Shift+M (Laptoplayout): flytter fokus
  til beskedområdet.
* Ctrl+Alt+Venstre og Ctrl+Alt+Højre: I adressebogens søgeresultatliste vil
  kommandoen navigere mellem felterne for den aktuelt valgte linje.
* Ctrl+Q: Markerer den valgte besked eller gruppe af meddelelser som læst i
  meddelelseslisten.
* Ctrl+U: Markerer den valgte besked eller gruppe af meddelelser som ulæste
  i meddelelseslisten.

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

### Version 1.0

* Første udgivelse

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended

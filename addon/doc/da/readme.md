# Outlook extended (Udvidelse til Outlook) #

* Forfattere: Cyrille Bougot, Ralf Kefferpuetz
* NVDA-kompatibilitet: 2018.3 til 2019.1
* Download [stabil version][1]
* Download [udviklingsversion][2]

Denne tilføjelse forbedrer brugen af Microsoft Outlook ved at udtale nogle
kommandoer og tilføje ekstra kommandoer.

## Kommandoer

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

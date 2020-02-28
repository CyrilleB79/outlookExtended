# Prošireni Outlook (Outlook extended) #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* NVDA kompatibilnost: 2017.3 do 2019.3
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Ovaj dodatak poboljšava upotrebu Microsoft Outlooka. Izgovara neke naredbe i
dodaje dodatne naredbe.

## Naredbe

* Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Izvještava o poljima zaglavlja od 1
  to 12 u poruci, stavki kalendara ili prozoru zadatka. Ako se pritisne
  dvaput, fokusira to polje, ako je moguće. Ako se pritisne triput, kopira
  sadržaj u međuspremnik.
* NVDA+shift+I (desktop raspored) / NVDA+control+shift+I (laptop raspored):
  Izvještava o informacijskoj traci u poruci, stavki kalendara ili prozoru
  zadatka. Ako se pritisne dvaput, fokusira ga. Ako se pritisne triput,
  kopira sadržaj u međuspremnik.
* NVDA+shift+A (desktop raspored) / NVDA+control+shift+A (laptop raspored):
  Izvještava o broju privitaka i njihove nazive u prozoru poruke. Ako se
  pritisne dvaput, premješta fokus na njega.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

## Napomene

Sve se geste mogu izmijeniti u dijaloškom okviru NVDA gesta naredbi. Moguće
ih je promijeniti za sljedeće situacije:

* Zadane geste za označavanje poruka kao pročitanih ili nepročitanih su one,
  koje vrijede za englesku verziju Outlooka. Ako se razlikuju od lokalne
  verzije programa Outlook, potrebno ih je promijeniti u skladu s tim.
* Zadane geste za čitanje zaglavlja odgovaraju tipki Alt u kombinaciji s
  tipkama prvog reda alfa-numeričke tipkovnice. Možda će biti potrebno
  premapirati geste za čitanje zaglavlja 11 i 12, ako se ne podudaraju s
  rasporedom lokalne tipkovnice.

## Dnevnik promjena

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Dodane su lokalizacije.

### Verzija 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Dodane su lokalizacije.
* Releases performed now with appveyor.

### Verzija 1.2

* Fixed header reading when forwarding meeting.
* Dodane su lokalizacije.

### Verzija 1.1

* Dodane su lokalizacije.

### Verzija 1.0

* Prvo izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

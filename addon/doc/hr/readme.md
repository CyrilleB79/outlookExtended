# Prošireni Outlook (Outlook extended) #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* NVDA kompatibilnost: 2019.3 i novije verzije
* Preuzmi [stabilnu verziju][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

## Naredbe

* Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Izvještava o poljima zaglavlja od 1
  to 12 u poruci, stavki kalendara ili prozoru zadatka. Ako se pritisne
  dvaput, fokusira to polje, ako je moguće. Ako se pritisne triput, kopira
  sadržaj u međuspremnik.
* NVDA+šift+I (desktop raspored) / NVDA+kontrol+šift+I (laptop raspored):
  Izvještava o informacijskoj traci u poruci, stavki kalendara ili prozoru
  zadatka. Ako se pritisne dvaput, fokusira ga. Ako se pritisne triput,
  kopira sadržaj u međuspremnik.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA+šift+M (desktop raspored) / NVDA+kontrol+šift+M (laptop raspored):
  Premješta fokus u polje poruke.
* NVDA+šift+I (desktop raspored) / NVDA+kontrol+šift+N (laptop raspored):
  Izvještava obavijest u prozoru poruke. Ako se pritisne dvaput, pomiče
  fokus na njega. Ako se pritisne tri puta, kopira njegov sadržaj u
  međuspremnik.
* Kontrol+Q: u popisu poruka, označi odabranu poruku ili grupu poruka kao
  pročitane.
* Kontrol+U: u popisu poruka, označi odabranu poruku ili grupu poruka kao
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
* Prijevodi su aktualizirani.

### Verzija 2.1

* Uklonjen je kanal razvoja.
* Prijevodi su aktualizirani.

### Verzija 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Verzija 1.10

* Kompatibilnost s NVDA verzijom 2023.1.
* Prijevodi su aktualizirani.

### Verzija 1.9

* Kompatibilnost s NVDA 2022.1.
* Dodatak više nije kompatibilan s NVDA verzijama manje od 2019.3.
* Izdanje se sada izvodi zahvaljujući GitHub action umjesto appVeyora.
* Ispravljena je najava kada korisnik triput pritisne prečace alt+broj.
* Ispravljen je problem koji sprečava čitanje zaglavlja stavki kalendara
  nekih Outlooka 365 verzija.
* Poboljšanje testnog okruženja dodatka: navigacija u dijalogu lažnog
  korijena.
* Prijevodi su aktualizirani.

### Verzija 1.8

* Prijevodi su aktualizirani.
* Osigurava da su sve varijable iz izvornog Outlook appModule i dalje
  dostupne.

### Verzija 1.7

* Aktualizirana je kompatibilnost za NVDA 2021.1.
* Prijevodi su aktualizirani.

### Verzija 1.6

* Ispravljeni su razni problemi prilikom čitanja zaglavlja poruka u programu
  Outlook 365.
* Ispravljena je greška pri najavljivanju priloga kad se koristi brajeva
  tipkovnica.
* Dodan je okvir za testiranje jedinice.
* Prijevodi su aktualizirani.

### Verzija 1.5

* Čitanje informacijske trake sada radi s NVDA 2019.3.
* Kretanje po tablici u rezultatima adresara sada opet radi s NVDA 2019.3.

### Verzija 1.4

* Skripta za premještanje fokusa na zaglavlja sada opet radi.
* Skripta za premještanje na privitke sada opet radi, kad je prisutno više
  privitaka.
* Dodane su lokalizacije.

### Verzija 1.3

* Ispravljeno čitanje zaglavlja poruka za novija Office 365 izdanja.
* Nadogradnje za podršku novijih NVDA verzija (kompatibilne s Python 2 i 3).
* Dodane su lokalizacije.
* Izdanja se sada izrađuju pomoću „appveyor”.

### Verzija 1.2

* Ispravljeno čitanje zaglavlja poruka za prosljeđivanja sastanka.
* Dodane su lokalizacije.

### Verzija 1.1

* Dodane su lokalizacije.

### Verzija 1.0

* Prvo izdanje.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

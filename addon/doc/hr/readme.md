# Prošireni Outlook (Outlook extended) #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* NVDA kompatibilnost: 2018.3 i novije
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Ovaj dodatak poboljšava upotrebu Microsoft Outlooka. Izgovara neke naredbe i
dodaje dodatne naredbe.

## Naredbe

* Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Izvještava o poljima zaglavlja od 1
  to 12 u poruci, stavki kalendara ili prozoru zadatka. Ako se pritisne
  dvaput, fokusira to polje, ako je moguće. Ako se pritisne triput, kopira
  sadržaj u međuspremnik.
* NVDA+šift+I (desktop raspored) / NVDA+kontrol+šift+I (laptop raspored):
  Izvještava o informacijskoj traci u poruci, stavki kalendara ili prozoru
  zadatka. Ako se pritisne dvaput, fokusira ga. Ako se pritisne triput,
  kopira sadržaj u međuspremnik.
* NVDA+šift+A (desktop raspored) / NVDA+kontrol+šift+A (laptop raspored):
  Izvještava o broju privitaka i njihove nazive u prozoru poruke. Ako se
  pritisne dvaput, premješta fokus na njega.
* NVDA+šift+M (desktop raspored) / NVDA+kontrol+šift+M (laptop raspored):
  Premješta fokus u polje poruke.
* Kontrol+Alt+lijevo i kontrol+Alt+desno: u popisu pretrage adresara, kreći
  se između polja trenutačno odabranog retka.
* Kontrol+Q: u popisu poruka, označi odabranu poruku ili grupu poruka kao
  pročitane.
* Kontrol+U: u popisu poruka, označi odabranu poruku ili grupu poruka kao
  nepročitane.

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

### Verzija 1.7

* Aktualizirana kompatibilnost za NVDA 2021.1
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

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

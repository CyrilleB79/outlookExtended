# Outlook extended #

* Tekijät: Cyrille Bougot, Ralf Kefferpuetz
* Yhteensopivuus: NVDA 2018.3-2019.3
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa parantaa Microsoft Outlookin käyttöä puhumalla olemassa olevia
näppäinkomentoja sekä lisäämällä uusia.

## Näppäinkomennot

* Alt+1 - Alt+9, Alt+0, Alt+-, alt+=: Puhuu otsakekentät 1-12 viestissä,
  kalenterimerkinnässä tai tehtäväikkunassa. Kahdesti painettaessa kohdistus
  siirretään kyseiseen kenttään, mikäli mahdollista. Kolmesti painettaessa
  sen sisältö kopioidaan leikepöydälle.
* NVDA+Vaihto+I (pöytäkoneen näppäimistöasettelu) / NVDA+Ctrl+Vaihto+I
  (kannettavan näppäimistöasettelu): Puhuu viestin, kalenterimerkinnän tai
  tehtäväikkunan tietopalkin. Kahdesti painettaessa kohdistus siirretään
  siihen. Kolmesti painettaessa sen sisältö kopioidaan leikepöydälle.
* NVDA+Vaihto+A (pöytäkoneen näppäimistöasettelu) / NVDA+Ctrl+Vaihto+A
  (kannettavan näppäimistöasettelu): Lukee viesti-ikkunassa liitteiden
  lukumäärän ja nimet. Kahdesti painettaessa kohdistus siirretään
  liitetiedostojen luetteloon.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

## Huomautuksia

Kaikkia syötekomentoja on mahdollista muokata NVDA:n
Syötekomennot-valintaikkunassa. Se voi olla tarpeen erityisesti seuraavissa
tilanteissa:

* Viestit luetuiksi ja lukemattomiksi merkitsevät oletussyötekomennot ovat
  englanninkielistä Outlookia varten. Mikäli käyttämässäsi Outlookin
  kieliversiossa käytetään eri komentoja, sinun tulee muuttaa nämä komennot
  käytössä olevien komentojen mukaisiksi.
* Otsakkeiden lukemiseen tarkoitetuissa komennoissa käytetään Alt-näppäintä
  yhdessä numerorivin näppäinten kanssa. Otsakkeiden 11 ja 12 komennot on
  ehkä määriteltävä uudelleen, mikäli ne eivät täsmää näppäinasettelusi
  kanssa.

## Muutosloki

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Lokalisointeja lisätty.

### Versio 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Lokalisointeja lisätty.
* Releases performed now with appveyor.

### Versio 1.2

* Fixed header reading when forwarding meeting.
* Lokalisointeja lisätty.

### Versio 1.1

* Lokalisointeja lisätty.

### Versio 1.0

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

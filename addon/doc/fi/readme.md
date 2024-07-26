# Laajennettu Outlook #

* Tekijät: Cyrille Bougot, Ralf Kefferpuetz
* Yhteensopivuus: NVDA 2019.3 ja sitä uudemmat
* Lataa [vakaa versio][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

## Näppäinkomennot

* Alt+1 - Alt+9, Alt+0, Alt+-, alt+=: Puhuu otsakekentät 1-12 viestissä,
  kalenterimerkinnässä tai tehtäväikkunassa. Kahdesti painettaessa kohdistus
  siirretään kyseiseen kenttään, mikäli mahdollista. Kolmesti painettaessa
  sen sisältö kopioidaan leikepöydälle.
* NVDA+Vaihto+I (pöytäkoneen näppäimistöasettelu) / NVDA+Ctrl+Vaihto+I
  (kannettavan näppäimistöasettelu): Puhuu viestin, kalenterimerkinnän tai
  tehtäväikkunan tietopalkin. Kahdesti painettaessa kohdistus siirretään
  siihen. Kolmesti painettaessa sen sisältö kopioidaan leikepöydälle.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA+Vaihto+M (pöytäkoneen näppäimistöasettelu) / NVDA+Ctrl+M (kannettavan
  näppäimistöasettelu): Siirtää kohdistuksen viestirunkoon.
* NVDA+Vaihto+N (pöytäkoneen näppäimistöasettelu) / NVDA+Ctrl+Vaihto+N
  (kannettavan näppäimistöasettelu): Puhuu viesti-ikkunan
  ilmoituksen. Kahdesti painettaessa kohdistus siirretään siihen. Kolmesti
  painettaessa sen sisältö kopioidaan leikepöydälle.
* Ctrl+Q: Merkitsee valitun viestin/valitut viestit luetuiksi
  viestiluettelossa.
* Ctrl+U: Merkitsee valitun viestin/valitut viestit lukemattomiksi
  viestiluettelossa.

## Lisäparannukset

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area of the message
  window. In this notification area, you also have buttons to remove the
  address of these recipients.  This add-on will inform you with a ding when
  this notification area appears, disappears or is updated. You can then
  press NVDA+shif+N / NVDA+control+shift+N once to have it read and twice to
  jump to this area. Then move with the arrows on the recipient buttons and
  press a button to remove the corresponding recipient.
* Voit käyttää osoitekirjan tulosluettelossa vaakasuuntaisia
  taulukkonavigointikomentoja lukeaksesi kunkin sarakkeen sisällön.
  
## Huomautuksia

Kaikkia näppäinkomentoja on mahdollista muokata NVDA:n
Näppäinkomennot-valintaikkunassa. Se voi olla tarpeen erityisesti
seuraavissa tilanteissa:

* Viestit luetuiksi ja lukemattomiksi merkitsevät oletusarvoiset
  näppäinkomennot ovat englanninkielistä Outlookia varten. Mikäli
  käyttämässäsi Outlookin kieliversiossa käytetään eri komentoja, sinun
  tulee muuttaa nämä komennot käytössä olevien komentojen mukaisiksi.
* Otsakkeiden lukemiseen tarkoitetuissa komennoissa käytetään Alt-näppäintä
  yhdessä numerorivin näppäinten kanssa. Otsakkeiden 11 ja 12 komennot on
  ehkä määriteltävä uudelleen, mikäli ne eivät täsmää näppäinasettelusi
  kanssa.

## Muutosloki

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
* Lokalisointeja päivitetty.

### Versio 2.1

* Dev-kanava poistettu.
* Lokalisointeja päivitetty.

### Versio 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Versio 1.10

* Yhteensopivuus NVDA 2023.1:lle.
* Lokalisointeja päivitetty.

### Versio 1.9

* Yhteensopivuus NVDA 2022.1:lle.
* Poistettu yhteensopivuus NVDA:n versioilta, jotka ovat vanhempia kuin
  2019.3.
* Julkaisu suoritetaan nyt GitHub-toiminnolla appVeyorin sijasta.
* Korjattu ilmoitus, kun käyttäjä painaa kolmesti Alt+numero-pikanäppäimiä.
* Korjattu ongelma, joka esti kalenterimerkintöjen otsakkeiden lukemisen
  joissakin Outlook 365:n versioissa.
* Lisäosan testiympäristön parannus: valejuurivalintaikkunassa liikkuminen.
* Lokalisointeja päivitetty.

### Versio 1.8

* Lokalisointeja päivitetty.
* Varmistettu, että kaikki alkuperäisen Outlook-sovellusmoduulin muuttujat
  ovat edelleen käytettävissä.

### Versio 1.7

* Yhteensopivuus päivitetty NVDA 2021.1:lle.
* Lokalisointeja päivitetty.

### Versio 1.6

* Korjattu useita ongelmia luettaessa viestiotsakkeita Outlook 365:ssä.
* Korjattu virhe  puhu liite -skriptissä pistekirjoitusnäppäimistöä
  käytettäessä.
* Lisätty yksiköntestauskehys.
* Lokalisointeja päivitetty.

### Versio 1.5

* Tietopalkin lukeminen toimii nyt NVDA 2019.3:n kanssa.
* Taulukkonavigointi osoitekirjan hakutuloksissa toimii nyt NVDA 2019.3:n
  kanssa.

### Versio 1.4

* Kohdistuksen viestiotsakkeisiin siirtävä skripti toimii taas.
* Liitteisiin siirtävä skripti toimii nyt, kun liitteitä on enemmän.
* Lokalisointeja lisätty.

### Versio 1.3

* Korjattu viestiotsakkeiden lukeminen uudemmissa Office 365:n versioissa.
* Päivityksiä uudempien NVDA-versioiden tukemiseksi (Python 2- ja 3
  -yhteensopiva).
* Lokalisointeja lisätty.
* Julkaisut suoritetaan nyt appveyorilla.

### Versio 1.2

* Korjattu otsakkeen lukeminen kokousta välitettäessä.
* Lokalisointeja lisätty.

### Versio 1.1

* Lokalisointeja lisätty.

### Versio 1.0

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

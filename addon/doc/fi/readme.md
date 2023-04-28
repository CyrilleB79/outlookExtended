# Laajennettu Outlook #

* Tekijät: Cyrille Bougot, Ralf Kefferpuetz
* Yhteensopivuus: NVDA 2019.3 ja sitä uudemmat
* Lataa [vakaa versio][1]

Tämä lisäosa parantaa Microsoft Outlookin käyttöä puhumalla olemassa olevia
näppäinkomentoja sekä lisäämällä uusia komentoja ja ominaisuuksia.

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

* Kun To-, Cc- tai Bcc-kenttiin syöttämäsi vastaanottaja lähettää
  automaattisia poissaolovastauksia tai ei ole enää Exchange-palvelimella,
  Outlook ilmoittaa siitä ilmoitusalueella. Siinä on myös painikkeet, joilla
  nämä vastaanottajat voidaan poistaa. Tämä lisäosa ilmoittaa kilahduksella,
  kun ilmoitusalue tulee näkyviin, häviää näkyvistä tai päivittyy. Voit
  sitten painaa kerran NVDA+Vaihto+N/NVDA+Ctrl+Vaihto+N lukeaksesi sen tai
  kahdesti siirtyäksesi siihen. Liiku sitten nuolilla
  vastaanottajapainikkeissa ja paina haluamaasi painiketta poistaaksesi
  kyseisen vastaanottajan.
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

### Versio 2.1

* Dev-kanava poistettu.
* Lokalisointeja päivitetty.

### Versio 2.0

* Paranneltu näkyviin tulevien ilmoitusten käyttäjäkokemusta kirjoitettaessa
  sähköpostiosoitteita, jotka eivät ole enää käytössä tai lähettävät
  automaattisia poissaolovastauksia: ääni ilmoittaa, kun sellaisia
  ilmoituksia tulee näkyviin tai päivittyy, näppäinkomento mahdollistaa sen
  lukemisen tai siirtymisen siihen ja nuolinäppäimillä liikkuminen tällä
  alueella on helpompaa.

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

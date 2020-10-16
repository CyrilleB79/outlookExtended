# Outlook extended #

* Tekijät: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2018.3 to 2020.3
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
* NVDA+Vaihto+M (pöytäkoneen näppäimistöasettelu) / NVDA+Ctrl+M (kannettavan
  näppäimistöasettelu): Siirtää kohdistuksen viestirunkoon.
* Ctrl+Alt+Nuoli vasemmalle ja Ctrl+Alt+Nuoli oikealle: Liikkuu valittuna
  olevan rivin kenttien välillä osoitekirjan hakutulosluettelossa.
* Ctrl+Q: Merkitsee valitun viestin/valitut viestit luetuiksi
  viestiluettelossa.
* Ctrl+U: Merkitsee valitun viestin/valitut viestit lukemattomiksi
  viestiluettelossa.

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

### Version 1.6

* Fixed various issues when reading messages headers in Outlook 365.
* Fixed an error in announce attachments script when a braille keyboard is
  used.
* Added a unit test framework.
* Updated localizations.

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

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

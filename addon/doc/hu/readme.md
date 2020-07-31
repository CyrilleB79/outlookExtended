# Outlook kiegészítő #

* Készítők: Cyrille Bougot, Ralf Kefferpuetz
* Kompatibilis NVDA kiadások: 2018.3 és 2019.3 között minden kiadás
* [stabil verzió][1] letöltése
* [fejlesztői verzió][2] letöltése

Ez a kiegészítő megkönnyíti a Microsoft Outlook használatát.

## Billentyűparancsok:

* Alt+számok 0-tól 9-ig  az alfanumerikus billentyűzet első sorából, Alt+-,
  Alt+=: Az első 12 fejléc bejelentése az üzenetek a naptár és a feladatok
  ablakában. Kétszeri lenyomásra a fókuszt a kérdéses mezőre helyezi,
  amennyiben az lehetséges. Háromszori lenyomásra a mező tartalmát a
  vágólapra helyezi.
* NVDA+shift+I (asztali kiosztás) / NVDA+ctrl+shift+I (laptop kiosztás):
  információs sáv bejelentése üzenet, naptár és feladatok
  ablakában. Kétszeri lenyomásra a fókuszt az információs sávra helyezi,
  Háromszori lenyomásra a vágólapra másolja az információs sáv tartalmát.
* NVDA+shift+A (asztali) / NVDA+control+shift+A (laptop): Bejelenti a
  mellékletek számát és nevét az üzenetablakban. Kétszeri lenyomásra a
  mellékletekre helyezi a fókuszt.
* NVDA+shift+M (asztali) / NVDA+ctrl+shift+M (laptop): Az üzenettörzsre
  helyezi a fókuszt.
* Ctrl+Alt+balnyíl és Ctrl+Alt+jobbnyíl: Navigál a kijelölt sor különböző
  elemei között a címjegyzék keresési találati listáján.
* Ctrl+Q: Olvasottnak jelöli a kijelölt üzeneteket az üzenetlistában.
* Ctrl+U: Olvasatlannak jelöli a kijelölt üzeneteket az üzenetlistában.

## Megjegyzések

Minden billentyűparancs megváltoztatható az NVDA beviteli parancsok
ablakában.

* Az üzenetek olvasott és olvasatlan megjelölése az Outlook angol
  verziójának parancsait használja.
* A fejlécek bejelentésének alapértelmezett parancsai az alt billentyűből és
  az alfanumerikus billentyűzet első sorának karaktereiből állnak. Az
  alapértelmezett parancsok az angol billentyűzetkiosztáson alapulnak, így
  előfordulhat, hogy magyar kiosztás esetén meg kell változtatni néhány
  parancsot, hogy kövesse a logikát.

## Változások

### 1.5-ös verzió

* Az NVDA 2019.3 verziójával már működik az információs sáv olvasása
* Az NVDA 2019.3 verzióval már lehetséges táblázatnavigációs parancsokat
  használni a Címjegyzékben.

### 1.4-es verzió

* A fejlécekre ugrás szkript ismét működik
* A mellékletekre ugrás szkript akkor is működik, ha több melléklet is
  tartozik az üzenethez.
* Fordításokat adtak hozzá

### 1.3-as verzió

* Javították az üzenetfejlécek olvasását az újabb Microsoft 365 kiadásokban
* Frissítés az NVDA újabb kiadásaival való használathoz, Python 2 és Python
  3 kompatibilitás
* Fordításokat adtak hozzá
* A bővítmény kiadásai mostantól az AppVeyor segítségével készülnek

### 1.2-es verzió

* Javították a fejlécek olvasását a találkozók továbbküldésénél
* Fordításokat adtak hozzá

### 1.1-es verzió

* Fordításokat adtak hozzá

### 1.0-s verzió

* Első kiadás

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

# Outlook kiegészítő #

* Készítők: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* [stabil verzió][1] letöltése
* [fejlesztői verzió][2] letöltése

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

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
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Ctrl+Q: Olvasottnak jelöli a kijelölt üzeneteket az üzenetlistában.
* Ctrl+U: Olvasatlannak jelöli a kijelölt üzeneteket az üzenetlistában.

## Additional improvements

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area. In this notification
  area, you also have buttons to remove the address of these recipients.
  This add-on will inform you with a ding when this notification area
  appear, disappear or be updated. You can then press NVDA+shif+N /
  NVDA+control+shift+N once to have it read and twice to jump to this
  area. Then move with arrows on the recipient buttons and press a button to
  remove the corresponding recipient.
* In the address book's result list, you can use horizontal table navigation
  commands to read the content of each column.
  
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

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Updated localizations.

### Version 1.9

* Compatibility with NVDA 2022.1.
* Dropped compatibility for versions of NVDA below 2019.3.
* The release is now performed thanks to a GitHub action instead of
  appVeyor.
* Fixed the announcement when the user triple-presses alt+number shortcuts.
* Fixed an issue preventing from reading calendar items headers of some
  versions of Outlook 365.
* Improvement of the test environment of the add-on: navigation in the fake
  root dialog.
* Updated localizations.

### Version 1.8

* Updated localizations.
* Ensure that all the variable from the original Outlook appModule are still
  available.

### Version 1.7

* Update compatibility for NVDA 2021.1.
* Updated localizations.

### Version 1.6

* Fixed various issues when reading messages headers in Outlook 365.
* Fixed an error in announce attachments script when a braille keyboard is
  used.
* Added a unit test framework.
* Updated localizations.

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

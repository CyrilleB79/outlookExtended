# Rozšírená podpora pre Microsoft Outlook #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]

Zlepšuje prístupnosť Microsoft Outlooku pridaním klávesových skratiek a
oznamovaním rôznych informácií.

## Klávesové skratky

* Alt+1 do Alt+9, Alt+0, Alt+-, Alt+=: Oznamuje hlavičky pre správy,
  udalosti v kalendári alebo zozname úloh. Stlačené dvakrát rýchlo za sebou
  presunie na hlavičku fokus, ak je to možné.
* NVDA+shift+I (rozloženie desktop) / NVDA+ctrl+shift+I (rozloženie laptop):
  Oznámi informačný panel v správe, udalosti v kalendári alebo v
  úlohe. Stlačené dvakrát rýchlo za sebou presunie na informačný panel
  fokus. Stlačené trikrát rýchlo za sebou skopíruje informáciu do schránky.
* NVDA+shift+A (rozloženie desktop) / NVDA+ctrl+shift+A (rozloženie laptop):
  Oznámi počet a názvy príloh v okne správy. Stlačené dvakrát rýchlo za
  sebou presunie fokus na prílohy.
* NVDA+shift+M (desktop) a NVDA+ctrl+shift+M (laptop): Presunie fokus do
  tela správy
* Ctrl+alt+ľavá a pravá šípka: V zozname kontaktov presúva medzi poliami
  vybratého kontaktu.
* Ctrl+q: Označí správu alebo vybraté správy v zozname správ ako prečítané.
* Ctrl+u: Označí správu alebo vybraté správy v zozname správ ako
  neprečítané.

## Poznámky

Všetky skratky je možné upraviť v dialógu NVDA Klávesové skratky. Skratky
budete chcieť zmeniť v nasledujúcich situáciách:

* Skratky na označenie správ ako prečítaných a neprečítaných sú predvolene
  pre anglickú verziu Outlooku. Vo vašej verzii Outlooku môžu byť tieto
  skratky iné a preto je vhodné ih upraviť aj v doplnku.
* Skratky na čítanie hlavičiek sú vytvorené tak, aby ste mohli použiť kláves
  alt s prvým radom kláves na klávesnici. Toto ale môže byť potrebné
  upraviť, ak používate inú ako anglickú klávesnicu.

## Zoznam zmien

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

### Verzia 1.5

* Čítanie informarčného panela funguje s NVDA 2019.3.
* Čítanie tabuľky výsledkov v adresári funguje s NVDA 2019.3.

### Verzia 1.4

* Opravená funkcia prechodu na hlavičky.
* Funkcia na prechodk prílohám funguje aj vtedy, ak je v správe viacero
  príloh.
* Pridané preklady.

### Verzia 1.3

* Opravené čítanie hlavičiek správ pre nové verzie Office 365.
* Upravené pre nové verzie NVDA (kompatibilné s Python 2 a 3).
* Pridané preklady.
* Vydania sú teraz odosielané cez appveyor.

### Verzia 1.2

* Opravené čítanie hlavičiek pri preposielaní stretnutia.
* Pridané preklady.

### Verzia 1.1

* Pridané preklady.

### Verzia 1.0

* Prvé vydanie.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

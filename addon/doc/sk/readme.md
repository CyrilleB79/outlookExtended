# Rozšírená podpora pre Microsoft Outlook #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* Funguje s NVDA 2018.3 do 2019.3
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
* NVDA+shift+M: Presunie fokus do tela správy
* Ctrl+alt+ľavá a pravá šípka: V zozname kontaktov presúva medzi poliami
  vybratého kontaktu
* Ctrl+q: Označí správu alebo vybraté správy v zozname správ ako prečítané
* Ctrl+u: Označí správu alebo vybraté správy v zozname správ ako neprečítané

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

### Verzia 1.3

* Opravené čítanie hlavičiek správ pre Office 365.
* Pridaná podpora pre Python 3 tak, aby doplnok fungoval s novou verziou
  NVDA.
* Pridané preklady.
* Vydania sú teraz odosielané cez appveyor

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

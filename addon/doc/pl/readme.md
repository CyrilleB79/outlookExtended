# Outlook extended #

* Autorzy: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Pobierz [Wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

## Skróty klawiszowe

* Alt+1 do Alt+9, Alt+0, Alt+-, Alt+=: odczytuje pola nagłówków od 1 do 12 w
  wiadomości, elemencie kalendarza, oraz oknie zadań. Jeśli te skrąty
  zostaną naciśnięte dwukrotnie, fokus zostanie przeniesiony na to pole, o
  ile to możliwe. Jeżeli te skróty naciśnięte są trzykrotnie, zawartość
  wymówiona zostanie skopiowana do schowka.
* NVDA+shift+I (układ klawiatury dla komputerów stacjonarnych) /
  NVDA+control+shift+I (układ klawiatury dla komputerów przenośnych):
  Odczytuje pasek informacji w oknie wiadomości, elemencie kalendarza lub
  oknie zadań. Jeśli ten skrót został naciśnięty dwukrotnie, fokus zostanie
  przeniesiony na jeden z wyżej wymienionych elementów. Jeżeli skrót jest
  naciśnięty trzykrotnie, odczytany komunikat zostanie skopiowany do
  schowka.
* NVDA+shift+A (układ dla komputerów stacjonarnych) / NVDA+control+shift+A
  (ukłąd dla komputerów przenosnych): Odczytuje nazwy i liczbę załączników w
  oknie wiadomości. Jeżeli skrót jest naciśnięty dwukrotnie, fokus zostanie
  skierowany na tę informację.
* NVDA+shift+M (układ dla komputerów stacjonarnych) / NVDA+control+shift+M
  (układ dla komputerów przenośnych): Przemieszcza fokus do tekstu
  wiadomości.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: na liście wiadomości zaznacz zaznaczoną wiadomość lub grupę
  wiadomości jako przeczytane.
* Control+U: na liście wiadomości zaznacz zaznaczoną wiadomość lub grupę
  wiadomości jako nieprzeczytaną.

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
  
## Uwagi

Wszystkie gesty można modyfikować w oknie dialogowym gestów poleceń
NVDA. Możesz je zmodyfikować, szczególnie w następujących sytuacjach:

* Domyślne gesty oznaczające wiadomości jako przeczytane lub nieprzeczytane
  to gesty dla programu Outlook w wersji angielskiej. Jeśli różnią się one
  od wersji lokalnej programu Outlook, musisz je odpowiednio zmienić.
* Domyślne gesty odczytu nagłówków odpowiadają Alt w połączeniu z pierwszego
  wiersza klawiatury alfanumerycznej. Może być konieczne ponowne mapowanie
  gestów tor odczytanych nagłówków 11 i 12, jeśli nie pasują one do
  lokalnego układu klawiatury.

## Lista zmian

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Zaktualizowane lokalizacje.

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
* Zaktualizowane lokalizacje.

### Version 1.8

* Zaktualizowane lokalizacje.
* Ensure that all the variable from the original Outlook appModule are still
  available.

### Wersja 1.7

* Zgodność aktualizacji dla NVDA 2021.1.
* Zaktualizowane lokalizacje.

### Wersja 1.6

* Naprawiono różne problemy podczas czytania nagłówków wiadomości w
  programie Outlook 365.
* Naprawiono błąd w skrypcie ogłaszania załączników podczas używania
  klawiatury brajlowskiej.
* Dodano strukturę testów jednostkowych.
* Zaktualizowane lokalizacje.

### Wersja 1.5

* Czytanie paska informacji działa teraz z NVDA 2019.3.
* Nawigacja po tabeli w wynikach książki adresowej działa teraz z NVDA
  2019.3.

### Wersja 1.4

* Skrypt przenoszący fokus do nagłówków działa ponownie.
* Skrypt do przejścia do załączników działa teraz, gdy jest więcej
  załączników.
* Dodano tłumaczenia.

### Wersja 1.3

* Naprawiono odczyt nagłówków wiadomości dla nowszej wersji usługi Office
  365.
* Aktualizacja wsparcia dla nowych wersji  NVDA (Python 2 i 3 zgodny)
* Dodano tłumaczenia.
* Wersje release są kompilowane z appwejorem.

### Wersja 1.2

* Poprawiono odczyt nagłówka podczas przekazywania spotkania.
* Dodano tłumaczenia.

### Wersja 1.1

* Dodano tłumaczenia.

### Wersja 1.0

* Wersja pierwotna.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

# Outlook extended #

* Autorzy: Cyrille Bougot, Ralf Kefferpuetz
* Zgodność z NVDA: 2018.3 i nowsze
* Pobierz [Wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]

Ten dodatek ułatwia używanie programu Microsoft outlook, odczytując
naciśnięcia niektórych skrótów klawiszowych. Dodatek też dodaje dodatkowe
skróty klawiszowe.

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
* Kombinacja Control+Alt+Left i Control+Alt+Right: na liście wyników
  wyszukiwania w książce adresowej nawiguje między polami aktualnie
  zaznaczonego wiersza.
* Control+Q: na liście wiadomości zaznacz zaznaczoną wiadomość lub grupę
  wiadomości jako przeczytane.
* Control+U: na liście wiadomości zaznacz zaznaczoną wiadomość lub grupę
  wiadomości jako nieprzeczytaną.

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

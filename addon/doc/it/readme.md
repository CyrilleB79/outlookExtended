# Outlook extended #

* Autori: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilità NVDA : dalla versione 2018.3 alla 2020.3
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]

Questo add-on migliora l'utilizzo di Microsoft Outlook, vocalizzando alcuni
comandi ed aggiungendone altri.

## Comandi

* Da alt+1 a Alt+9, Alt+0, Alt+-, Alt+=: legge i campi da 1 a 12 in un
  messaggio, elemento di calendario o finestra attività. Se premuto due
  volte, sposta il focus su questo campo, se possibile. Se premuto tre
  volte, ne copia il contenuto negli appunti.
* NVDA+shift+I (layout desktop) / NVDA+control+shift+I (layout laptop):
  legge la barra informazioni in un messaggio, elemento di calendario o
  finestra attività. Se premuto due volte, sposta il focus su di essa. Se
  premuto tre volte, ne copia il contenuto negli appunti.
* NVDA+shift+A (layout desktop) / NVDA+control+shift+A (layout laptop):
  legge il numero e i nomi degli allegati in una finestra di messaggio. Se
  premuto due volte, sposta il focus su di essi.
* NVDA+shift+M (layout desktop) / NVDA+control+shift+M (layout laptop):
  sposta il focus sul corpo di un messaggio.
* Control+Alt+Freccia sinistra/destra: nell'elenco dei risultati di ricerca
  della rubrica, naviga tra i campi della riga selezionata.
* Control+Q: nell'elenco dei messaggi, marca il messaggio o gruppo di
  messaggi selezionato come letto.
* Control+U: nell'elenco dei messaggi, marca il messaggio o gruppo di
  messaggi selezionato come non letto.

## Note

Tutti i comandi possono essere modificati nella finestra Gesti e Tasti di
Immissione di NVDA. Può essere utile modificarli specialmente nelle seguenti
situazioni:

* I tasti di default per marcare i messaggi come letti o non letti sono
  quelli della versione inglese di Outlook. Se questi differeiscono da
  quelli della versione di Outlook in uso nel tuo paese, li dovrai
  modificare di conseguenza.
* I tasti di default per leggere le intestazioni corrispondono ad Alt
  premuto assieme ai tasti della prima riga della tastiera alfanumerica
  americana. Potresti aver bisogno di rimappare i tasti per leggere le
  intestazioni 11 e 12 se sono collocati in posizioni diverse nel tuo layout
  tastiera.

## Elenco delle modifiche

### Novità nella versione 1.6

* Risolti diversi problemi con la lettura delle intestazioni dei messaggi in
  Outlook 365.
* Risolto un problema nello script di lettura degli allegati che si
  verificava quando è utilizzata una tastiera Braille.
* Aggiunto un framework per testare le unità.
* Traduzioni aggiornate.

### Novità nella versione 1.5

* Ora la lettura della barra informazioni funziona con NVDA 2019.3.
* Ora la navigazione nella tabella dei risultati di ricerca della rubrica
  funziona con NVDA 2019.3.

### Novità nella versione 1.4

* Lo script per spostare il focus sulle intestazioni funziona nuovamente.
* Lo script per spostarsi sugli allegati ora funziona quando è presente più
  di un allegato.
* Aggiunte traduzioni.

### Novità nella versione 1.3

* Sistemata la lettura delle intestazioni dei messaggi per le nuove versioni
  di Office 365.
* Aggiornamenti per supportare le nuove versioni di NVDA (compatibile con
  Python 2 e 3).
* Aggiunte traduzioni.
* Le versioni sono ora rilasciate con appveyor.

### Novità nella versione 1.2

* Risolto un problema con la lettura delle intestazioni quando si inoltra
  una convocazione di riunione.
* Aggiunte traduzioni.

### Novità nella versione 1.1

* Aggiunte traduzioni.

### Novità nella versione 1.0

* Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

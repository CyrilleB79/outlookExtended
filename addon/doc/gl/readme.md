# Outlook extended #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidade con NVDA: da 2018.3 á 2019.3
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Este complemento mellora o uso de Microsoft Outlook falando certas ordes e
engadindo atallos adicionais.

## Ordes de teclado

* Alt+1 a Alt+9, Alt+0, alt+_, alt+=: Anuncia o campo de cabeceira 1 a 12
  nunha xanela de mensaxe, elemento de calendario ou tarefa. Se se preme
  dúas veces, move o foco a este campo se é posible. Se se preme tres veces,
  copia os seus contidos ao portapapeis.
* NVDA+shift+I (distribución de escritorio) / NVDA+control+shift+I
  (distribución portátil): Anuncia a barra de información nunha xanela de
  mensaxe, elemento de calendario ou tarefa. Se se preme dúas veces, move o
  foco cara ela. Se se preme tres veces, copia os seus contidos ao
  portapapeis.
* NVDA+shift+A (distribución de escritorio) / NVDA+control+shift+A
  (distribución portátil): Anuncia o número e os nomes dos adxuntos nunha
  xanela de mensaxe. Se se preme dúas veces, move o foco cara eles.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

## Notas

Todos os xestos pódense modificar dende o diálogo Xestos de entrada de
NVDA. Poderías querer modificalos especialmente nas seguintes situacións:

* Os xestos por defecto para marcar mensaxes como lidas ou non lidas son os
  da versión en inglés de Outlook. Se difiren daqueles da túa versión local
  de Outlook, necesitarás cambialos en consecuencia.
* Os xestos por defecto para ler as cabeceiras corresponden a Alt combinado
  coas teclas da primeira fila do teclado alfanumérico. Poderías necesitar
  reasignar os xestos para ler as cabeceiras 11 e 12 se non coinciden coa
  túa distribución de teclado local.

## Rexistro de trocos

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Traducións engadidas.

### Versión 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Traducións engadidas.
* Releases performed now with appveyor.

### Versión 1.2

* Fixed header reading when forwarding meeting.
* Traducións engadidas.

### Versión 1.1

* Traducións engadidas.

### Versión 1.0

* Publicación inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

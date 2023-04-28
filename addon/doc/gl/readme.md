# Outlook extended #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidade con NVDA: 2019.3 en diante
* Descargar [versión estable][1]

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

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
* NVDA+shift+M (distribución de escritorio) / NVDA+control+shift+M
  (distribución portátil): Move o foco ó corpo da mensaxe.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: na lista de mensaxes, marca como lida a mensaxe ou o grupo de
  mensaxes seleccionado.
* Control+U: na lista de mensaxes, marca como non lida a mensaxe ou o grupo
  de mensaxes seleccionado.

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

### Version 2.1

* Removed the dev channel.
* Traducións actualizadas.

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Traducións actualizadas.

### Versión 1.9

* Compatibilidade con NVDA 2022.1.
* Eliminada a compatibilidade con versións de NVDA por baixo da 2019.3.
* A publicación agora faise grazas a unha acción de GitHub no canto de
  appVeyor.
* Arranxado o anuncio de cando o usuario preme tres veces o atallo
  alt+número.
* Arranxado un problema que impedía ler os encabezados de elementos de
  calendario nalgunhas versións de Outlook 365.
* Mellora do entorno de probas do complemento: navegación no diálogo de raíz
  falsa.
* Traducións actualizadas.

### Versión 1.8

* Traducións actualizadas.
* Asegurarse de que todas as variables do módulo de aplicación orixinal de
  Outlook seguen estando dispoñibles.

### Versión 1.7

* Actualizar compatibilidade para NVDA 2021.1.
* Traducións actualizadas.

### Versión 1.6

* Arranxados varios problemas ao ler encabezados de mensaxes en Outlook 365.
* Arranxado un erro no script de anunciar adxuntos cando se usa un teclado
  braille.
* Engadido un marco de probas unitarias (unit test framework).
* Traducións actualizadas.

### Versión 1.5

* A lectura da barra de información xa funciona con NVDA 2019.3.
* A navegación por táboa nos resultados da libreta de enderezos xa funciona
  con NVDA 2019.3.

### Versión 1.4

* O script para mover o foco ás cabeceiras volve a funcionar.
* O script para moverse aos adxuntos xa funciona cando están presentes máis
  adxuntos.
* Traducións engadidas.

### Versión 1.3

* Arranxada a lectura de encabezados de mensaxes para versións máis novas de
  Office 365.
* Actualizacións para soportar versións máis novas do NVDA (compatible con
  Python 2 e 3).
* Traducións engadidas.
* As liberacións realízanse agora con Appveyor.

### Versión 1.2

* Arranxada a lectura de encabezamentos ao reenviar reunións.
* Traducións engadidas.

### Versión 1.1

* Traducións engadidas.

### Versión 1.0

* Publicación inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

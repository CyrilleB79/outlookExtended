# Outlook extended #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidad con NVDA: de 2018.3 a 2019.3
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento mejora el uso de Microsoft Outlook verbalizando algunas
órdenes y añadiendo órdenes extra.

## Órdenes

* De alt+1 a alt+9, alt+0, alt+_ y alt+=: verbaliza los campos de cabecera
  del 1 al 12 en un mensaje, elemento del calendario o ventana de tarea. Si
  se pulsa dos veces, mueve el foco a ese campo si es posible. Si se pulsa
  tres veces, copia sus contenidos al portapapeles.
* NVDA+shift+I (distribución de escritorio) / NVDA+control+shift+I
  (distribución portátil): verbaliza la barra de información en un mensaje,
  elemento del calendario o ventana de tarea. Si se pulsa dos veces, mueve
  el foco hasta allí. Si se pulsa tres veces, copia su contenido al
  portapapeles.
* NVDA+shift+A (distribución de escritorio) / NVDA+control+shift+A
  (distribución portátil): indica el número y los nombres de los adjuntos en
  una ventana de mensaje. Si se pulsa dos veces, mueve el foco hasta allí.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

## Notas

Todos los gestos pueden cambiarse en el diálogo Gestos de entrada de
NVDA. Puedes querer modificarlos en las siguientes situaciones:

* Los gestos por defecto para marcar como leído o como no leído son los que
  vienen en la versión en inglés de Microsoft Outlook. Si son diferentes de
  los que vienen en tu versión local, deberás cambiarlos según corresponda.
* Los gestos por defecto para leer cabeceras se corresponden con la tecla
  Alt combinada con la fila superior del teclado alfanumérico. Puede ser
  necesario reasignar los gestos para leer las cabeceras 11 y 12 si no
  encajan con tu distribución de teclado.

## Registro de cambios

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Traducciones añadidas

### Versión 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Traducciones añadidas
* Releases performed now with appveyor.

### Versión 1.2

* Fixed header reading when forwarding meeting.
* Traducciones añadidas

### Versión 1.1

* Traducciones añadidas

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

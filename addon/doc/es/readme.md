# Outlook extended #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidad con NVDA: de 2019.3 en adelante
* Descargar [versión estable][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

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
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA+shift+M (distribución de escritorio) / NVDA+control+shift+M
  (distribución portátil): mueve el foco al cuerpo del mensaje.
* NVDA+shift+N (distribución de escritorio) / NVDA+control+shift+N
  (distribución portátil): muestra la notificación en una ventana de
  mensaje. Si se pulsa dos veces, mueve el foco hacia ella. Si se pulsa tres
  veces, copia su contenido al portapapeles.
* Ctrl+q: en la lista de mensajes, marca el mensaje o grupo de mensajes
  seleccionado como leído.
* Ctrl+u: en la lista de mensajes, marca el mensaje o grupo de mensajes
  seleccionado como no leído.

## Mejoras adicionales

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area of the message
  window. In this notification area, you also have buttons to remove the
  address of these recipients.  This add-on will inform you with a ding when
  this notification area appears, disappears or is updated. You can then
  press NVDA+shif+N / NVDA+control+shift+N once to have it read and twice to
  jump to this area. Then move with the arrows on the recipient buttons and
  press a button to remove the corresponding recipient.
* En la lista de resultados de la libreta de direcciones, se pueden usar
  órdenes de navegación horizontal por tablas para leer el contenido de cada
  columna.
  
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

### Version 3.0

* In a meeting window, in the all attendees tab, pressing NVDA+shift+A
  (desktop layout) / NVDA+control+shift+A (laptop layout) now displays in a
  browseable message the attendees status on the time slot of the meeting.

### Version 2.4

* Compatibility with NVDA 2024.1.
* Relevant commands are now usable in on-demand speech mode.

### Version 2.3

* Note: From now on, translation updates will not appear anymore in the
  change log.

### Version 2.2

* Restored compatibiliity with NVDA 2019.3.1.
* Traducciones actualizadas.

### Versión 2.1

* Se ha eliminado el canal de desarrollo.
* Traducciones actualizadas.

### Versión 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Versión 1.10

* Compatibilidad con NVDA 2023.1.
* Traducciones actualizadas.

### Versión 1.9

* Compatibilidad con NVDA 2022.1.
* Eliminada la compatibilidad con versiones de NVDA anteriores a la 2019.3.
* La versión se construye con una acción de GitHub en lugar de AppVeyor.
* Corregido el anuncio cuando el usuario pulsa los atajos alt+números tres
  veces.
* Corregido un problema que impedía leer las cabeceras de algunos elementos
  del calendario en algunas versiones de Outlook 365.
* Mejora del entorno de pruebas del complemento: navegación en el diálogo de
  raíz falsa.
* Traducciones actualizadas.

### Versión 1.8

* Traducciones actualizadas.
* Se garantiza que todas las variables del módulo original de Outlook se
  encuentran todavía disponibles.

### Versión 1.7

* Se ha actualizado la compatibilidad para NVDA 2021.1.
* Traducciones actualizadas.

### Versión 1.6

* Corregidos diversos problemas al leer las cabeceras de los mensajes en
  Outlook 365.
* Corregido un error en el script para anunciar adjuntos cuando se usa un
  teclado Braille.
* Añadido un marco de trabajo de pruebas unitarias.
* Traducciones actualizadas.

### Versión 1.5

* Ahora funciona la lectura de la barra de información con NVDA 2019.3.
* La navegación por tablas en los resultados de la libreta de direcciones ya
  funciona en NVDA 2019.3.

### Versión 1.4

* Vuelve a funcionar el script para desplazar el foco a las cabeceras.
* Vuelve a funcionar el script que permite desplazarse a los adjuntos cuando
  hay varios archivos presentes.
* Traducciones añadidas.

### Versión 1.3

* Arreglada la lectura de encabezados de mensajes en compilaciones más
  nuevas de Office 365.
* Actualizaciones para soportar versiones más nuevas de NVDA (compatible con
  Python 2 y 3).
* Traducciones añadidas.
* Las liberaciones se realizan ahora con Appveyor.

### Versión 1.2

* Arreglada la lectura de encabezados al reenviar reuniones.
* Traducciones añadidas.

### Versión 1.1

* Traducciones añadidas.

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

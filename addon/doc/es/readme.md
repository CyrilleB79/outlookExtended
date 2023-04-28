# Outlook extended #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidad con NVDA: de 2019.3 en adelante
* Descargar [versión estable][1]

Este complemento mejora el uso de Microsoft Outlook verbalizando algunas
órdenes y añadiendo órdenes y funciones extra.

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

* Cuando el destinatario introducido en los campos Para, CC o CCO envía
  respuestas automáticas por desconexión o ya no está presente en el
  servidor Exchange, Outlook lo anuncia en el área de notificaciones. En
  esta zona de notificaciones, también hay botones para eliminar la
  dirección de estos destinatarios. Este complemento informará con un pitido
  cuando aparezca el área de notificaciones, desaparezca o se actualice. En
  ese momento, se puede pulsar una vez NVDA+shift+N o NVDA+control+shift+N
  para leerla o dos veces para saltar a ella. Después, se puede usar el
  desplazamiento con las flechas para moverse por los botones del
  destinatario y pulsar uno para eliminar al destinatario correspondiente.
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

### Versión 2.1

* Se ha eliminado el canal de desarrollo.
* Traducciones actualizadas.

### Versión 2.0

* Se mejora la experiencia de usuario con las notificaciones que aparecen al
  introducir direcciones de correo electrónico que ya no son válidas o que
  envían respuestas automáticas de desconexión de la oficina: se reproduce
  un sonido cuando dichas notificaciones aparecen o se actualizan, un gesto
  permite leerlas o desplazarse hasta ellas, y se facilita la navegación por
  la zona con las flechas.

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

# Outlook extended #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidad con NVDA: de 2018.3 a 2020.3
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
* NVDA+shift+M (distribución de escritorio) / NVDA+control+shift+M
  (distribución portátil): mueve el foco al cuerpo del mensaje.
* Ctrl+alt+flechas izquierda y derecha: en la lista de resultados de
  búsqueda de la libreta de direcciones, navega entre los campos de la línea
  seleccionada actualmente.
* Ctrl+q: en la lista de mensajes, marca el mensaje o grupo de mensajes
  seleccionado como leído.
* Ctrl+u: en la lista de mensajes, marca el mensaje o grupo de mensajes
  seleccionado como no leído.

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

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

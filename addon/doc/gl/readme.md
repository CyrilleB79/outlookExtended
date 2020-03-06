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
* NVDA+shift+M (distribución de escritorio) / NVDA+control+shift+M
  (distribución portátil): Move o foco ó corpo da mensaxe.
* Control+Alt+Esquerda e Control+Alt+Dereita: na lista de resultados de
  busca na libreta de enderezos, navega entre os campos da liña actualmente
  seleccionada.
* Control+Q: na lista de mensaxes, marca como lida a mensaxe ou o grupo de
  mensaxes seleccionado.
* Control+U: na lista de mensaxes, marca como non lida a mensaxe ou o grupo
  de mensaxes seleccionado.

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

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

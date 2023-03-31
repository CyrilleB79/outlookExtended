# Outlook mais acessível #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Baixar [Versão estável][1]
* Baixar [Versão de desenvolvimento][2]

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

## Comandos:

* Alt+1 até Alt+9, Alt+0, Alt+_, alt+=: Lêem os campos de cabeçalho de 1 a
  12 numa mensagem, item de calendário ou janela de tarefas. Se pressionados
  duas vezes, movem o foco para este campo, se possível. Se pressionados
  três vezes, copiam o seu conteúdo para a área de transferência.
* NVDA+shift+I (Computador de secretária) / NVDA+control+shift+I (computador
  portátil): lê a barra de informações numa mensagem, item de calendário ou
  janela de tarefas. Se pressionado duas vezes, move o foco para ela. Se
  pressionado três vezes, copia o seu conteúdo para a área de transferência.
* NVDA+shift+A (computador de secretária) / NVDA+control+shift+A (computador
  portátil): Lê o número e os nomes dos anexos, numa janela de mensagem. Se
  pressionado duas vezes, move o foco os anexos.
* NVDA+shift+M (teclado do desktop) / NVDA+control+shift+M (teclado do
  laptop): Muda o foco para o corpo da mensagem.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: na lista de mensagens, marca a mensagem ou grupo de mensagens
  seleccionadas como lidas.
* Control+U: na lista de mensagens, marca a mensagem ou grupo de mensagens
  seleccionadas como não lidas.

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
  
## Notas:

Todos os comandos podem ser modificados no diálogo de definir comandos do
NVDA. Pode querer alterá-los especialmente nas seguintes situações:

* Os comandos padrão para marcar mensagens como lidas ou não lidas são os da
  versão em inglês do Outlook. Se forem diferentes das versões locais do
  programa, deverá alterá-las em conformidade.
* Os comandos padrão para ler cabeçalhos correspondem à tecla Alt combinada
  com as teclas da primeira linha do teclado alfanumérico. Talvez seja
  necessário mapear novamente os comandos dos cabeçalhos de leitura 11 e 12,
  se eles não corresponderem ao esquema do teclado local.

## Modificações:

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Traduções actualizadas.

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
* Traduções actualizadas.

### Version 1.8

* Traduções actualizadas.
* Ensure that all the variable from the original Outlook appModule are still
  available.

### Versão 1.7

* Compatibilidade de actualização para NVDA 2021.1.
* Traduções actualizadas.

### Versão 1.6

* Corrigidos vários problemas ao ler cabeçalhos de mensagens no Outlook 365.
* Corrigido um erro no script de anúncios de anexos quando é utilizado um
  teclado braille.
* Adicionada uma estrutura de teste unitário.
* Traduções actualizadas.

### Versão 1.5

* A leitura da barra de informação está agora a funcionar com o NVDA 2019.3.
* A navegação na tabela dos resultados do livro de endereços está agora a
  trabalhar com o NVDA 2019.3.

### Versão 1.4

* O script para mover o foco para os cabeçalhos está a funcionar novamente.
* O script para mover para anexos está agora a funcionar quando mais anexos
  estão presentes.
* Adicionadas traduções.

### Versão 1.3

* resolvido o problema da Leitura de cabeçalhos de mensagens para o novo
  lançamento do Office 365.
* Actualizações para suportar versões mais recentes do NVDA (compatibilidade
  com Python 2 e 3).
* Adicionadas traduções.
* Lançamentos realizados agora com o appveyor.

### Versão 1.2

* Resolvido o problema da Leitura de cabeçalho ao encaminhar a reunião.
* Adicionadas traduções.

### Versão 1.1

* Adicionadas traduções.

### Versão 1.0

* Versão inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

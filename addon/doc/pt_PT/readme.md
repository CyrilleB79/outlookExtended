# Outlook mais acessível #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2018.3 to 2019.3
* Baixar [Versão estável][1]
* Baixar [Versão de desenvolvimento][2]

Este extra melhora o uso do Microsoft Outlook, verbalizando determinados
comandos e adicionando alguns novos.

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
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

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

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Added localizations.

### Version 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Added localizations.
* Releases performed now with appveyor.

### Version 1.2

* Fixed header reading when forwarding meeting.
* Added localizations.

### Version 1.1

* Added localizations.

### Versão 1.0

* Versão inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

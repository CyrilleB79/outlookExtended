# Outlook estendido (Outlook extended) #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidade com NVDA: 2018.3 e além
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Este complemento melhora o uso do Microsoft Outlook vocalizando alguns
comandos e adicionando comandos extras.

## Comandos

* Alt+1 até Alt+9, Alt+0, Alt+-, Alt+=: Informa o campo de cabeçalho 1 a 12
  em uma mensagem, item de calendário ou janela de tarefa. Se pressionado
  duas vezes, move o foco para este campo, se possível. Se pressionado três
  vezes, copia seu conteúdo para a área de transferência.
* NVDA+shift+I (leiaute de computador de mesa) / NVDA+control+shift+I
  (leiaute de computador portátil): Relata a barra de informações em uma
  mensagem, item de calendário ou janela de tarefa. Se pressionado duas
  vezes, move o foco para tal. Se pressionado três vezes, copia seu conteúdo
  para a área de transferência.
* NVDA+shift+A (leiaute de computador de mesa) / NVDA+control+shift+A
  (leiaute de computador portátil): Informa o número e os nomes dos anexos
  em uma janela de mensagem. Se pressionado duas vezes, move o foco para
  ele.
* NVDA+shift+M (leiaute de computador de mesa) / NVDA+control+shift+M
  (leiaute de computador portátil): Move o foco para o corpo da mensagem.
* Control+Alt+Esquerda e Control+Alt+Direita: na lista de resultados da
  pesquisa do catálogo de endereços, navega entre os campos da linha
  selecionada no momento.
* Control+Q: na lista de mensagens, marca a mensagem ou o grupo de mensagens
  selecionadas como lida.
* Control+U: na lista de mensagens, marca a mensagem ou o grupo de mensagens
  selecionadas como não lida.

## Notas

Todos os comandos (gestos) podem ser modificados no diálogo definir comandos
do NVDA. Pode querer alterá-los especialmente nas seguintes situações:

* Os comandos padrão para marcar mensagens como lidas ou não lidas são os da
  versão em inglês do Outlook. Se forem diferentes das versões locais do
  programa, deverá alterá-las em conformidade.
* Os comandos (gestos) padrão para ler os cabeçalhos correspondem a Alt
  combinado com as teclas da primeira linha do teclado alfanumérico. Pode
  ser necessário mapear novamente os comandos para ler os cabeçalhos 11 e
  12, se não corresponderem ao leiaute do teclado local.

## Registro de alterações (Change log)

### Versão 1.7

* Atualizada a compatibilidade para NVDA 2021.1.
* Localizações (traduções) atualizadas.

### Versão 1.6

* Vários problemas corrigidos ao ler cabeçalhos de mensagens no Outlook 365.
* Corrigido um erro no script de anúncio de anexos quando um teclado braille
  é usado.
* Adicionada uma estrutura (framework) de teste de unidade.
* Localizações (traduções) atualizadas.

### Versão 1.5

* A leitura da barra de informações agora está funcionando com o NVDA
  2019.3.
* A navegação da tabela nos resultados do catálogo de endereços agora está
  funcionando com o NVDA 2019.3.

### Versão 1.4

* O script para mover o foco para os cabeçalhos está funcionando novamente.
* O script para mover para anexos agora está funcionando quando há mais
  anexos presentes.
* Localizações (traduções) adicionadas.

### Versão 1.3

* Corrigida a leitura de cabeçalhos de mensagens para uma versão mais
  recente do Office 365.
* Atualização para oferecer suporte a versões mais recentes do NVDA
  (compatível com Python 2 e 3).
* Localizações (traduções) adicionadas.
* Versões realizadas agora com appveyor.

### Versão 1.2

* Corrigida a leitura do cabeçalho ao encaminhar a reunião.
* Localizações (traduções) adicionadas.

### Versão 1.1

* Localizações (traduções) adicionadas.

### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

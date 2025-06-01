# Outlook estendido (Outlook extended) #

* Autores: Cyrille Bougot, Ralf Kefferpuetz
* Compatibilidade com NVDA: 2019.3 e posteriorCompatibilidade com NVDA:
  2018.3 e além
* Baixe a [versão estável][1]

Esse complemento aprimora o uso do Microsoft Outlook com o NVDA: ele
vocaliza alguns comandos nativos e adiciona comandos e recursos extras.

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
* NVDA+shift+A (layout de desktop) / NVDA+control+shift+A (layout de
  laptop):
  
    * Em uma janela de mensagem: informa o número e os nomes dos anexos; se
      pressionado duas vezes, move o foco para ele. NVDA+shift+A (leiaute de
      computador de mesa) / NVDA+control+shift+A (leiaute de computador
      portátil): Informa o número e os nomes dos anexos em uma janela de
      mensagem. Se pressionado duas vezes, move o foco para ele.
    * Em uma janela de reunião, na guia Todos os participantes: exiba em uma
      mensagem navegável o status dos participantes no intervalo de tempo da
      reunião.

* NVDA+shift+M (leiaute de computador de mesa) / NVDA+control+shift+M
  (leiaute de computador portátil): Move o foco para o corpo da mensagem.
* NVDA+shift+N (layout de desktop) / NVDA+control+shift+N (layout de
  laptop): Relata a notificação em uma janela de mensagem. Se pressionado
  duas vezes, move o foco para ela. Se pressionado três vezes, copia seu
  conteúdo para a área de transferência.NVDA+shift+I (leiaute de computador
  de mesa) / NVDA+control+shift+I (leiaute de computador portátil): Relata a
  barra de informações em uma mensagem, item de calendário ou janela de
  tarefa. Se pressionado duas vezes, move o foco para tal. Se pressionado
  três vezes, copia seu conteúdo para a área de transferência.
* Control+Q: na lista de mensagens, marca a mensagem ou o grupo de mensagens
  selecionadas como lida.
* Control+U: na lista de mensagens, marca a mensagem ou o grupo de mensagens
  selecionadas como não lida.

## Melhorias adicionais

* Quando o destinatário que você inseriu nos campos Para, Cc ou Bcc envia
  respostas automáticas fora do office ou não está mais presente no servidor
  do Exchange, o Outlook informa isso na área de notificação da janela da
  mensagem. Nessa área de notificação, você também tem botões para remover o
  endereço desses destinatários.  Esse complemento o informará com um ding
  quando a área de notificação aparecer, desaparecer ou for atualizada. Você
  pode então pressionar NVDA+shif+N / NVDA+control+shift+N uma vez para ler
  e duas vezes para pular para essa área. Em seguida, mova-se com as setas
  nos botões de destinatário e pressione um botão para remover o
  destinatário correspondente.
* Na lista de resultados do catálogo de endereços, você pode usar os
  comandos de navegação da tabela horizontal para ler o conteúdo de cada
  coluna.
  
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

## Registro de alterações

### Versão 3.0

* Em uma janela de reunião, na guia Todos os participantes, pressionar
  NVDA+shift+A (layout de desktop) / NVDA+control+shift+A (layout de laptop)
  agora exibe em uma mensagem navegável o status dos participantes no
  intervalo de tempo da reunião.

### Versão 2.4

* Compatibilidade com o NVDA 2024.1.Atualizada a compatibilidade para NVDA
  2021.1.
* Os comandos relevantes agora podem ser usados no modo de fala sob demanda.

### Versão 2.3

* Nota: De agora em diante, as atualizações de tradução não aparecerão mais
  no registro de alterações.

### Versão 2.2

* Compatibilidade restaurada com o NVDA 2019.3.1.Atualizada a
  compatibilidade para NVDA 2021.1.
* Localizações atualizadas.

### Versão 2.1

* Removido o canal de desenvolvimento.
* Localizações atualizadas.

### Versão 2.0

* Aprimore a experiência do usuário com as notificações que aparecem ao
  inserir endereços de e-mail que não são mais válidos ou que enviam
  respostas automáticas fora do office: um som alerta quando essas
  notificações aparecem ou são atualizadas, um gesto permite ler ou ir para
  elas e a navegação nessa área com setas fica mais fácil.

### Versão 1.10

* Compatibilidade com o NVDA 2023.1.Atualizada a compatibilidade para NVDA
  2021.1.
* Localizações atualizadas.

### Versão 1.9

* Compatibilidade com o NVDA 2022.1.Atualizada a compatibilidade para NVDA
  2021.1.
* Compatibilidade eliminada para versões do NVDA abaixo de 2019.3.Atualizada
  a compatibilidade para NVDA 2021.1.
* O lançamento agora é realizado graças a uma ação do GitHub em vez do
  appVeyor.
* Corrigido o anúncio quando o usuário pressiona três vezes os atalhos
  alt+número.
* Corrigido um problema que impedia a leitura de cabeçalhos de itens de
  calendário de algumas versões do Outlook 365.
* Aprimoramento do ambiente de teste do complemento: navegação na caixa de
  diálogo de raiz falsa.
* Localizações atualizadas.

### Versão 1.8

* Localizações atualizadas.
* Certifique-se de que todas as variáveis do appModule original do Outlook
  ainda estejam disponíveis.

### Versão 1.7

* Atualizada a compatibilidade para NVDA 2021.1.
* Localizações atualizadas.

### Versão 1.6

* Vários problemas corrigidos ao ler cabeçalhos de mensagens no Outlook 365.
* Corrigido um erro no script de anúncio de anexos quando um teclado braille
  é usado.
* Adicionada uma estrutura (framework) de teste de unidade.
* Localizações atualizadas.

### Versão 1.5

* A leitura da barra de informações agora está funcionando com o NVDA
  2019.3.
* A navegação da tabela nos resultados do catálogo de endereços agora está
  funcionando com o NVDA 2019.3.

### Versão 1.4

* O script para mover o foco para os cabeçalhos está funcionando novamente.
* O script para mover para anexos agora está funcionando quando há mais
  anexos presentes.
* Adicionadas localizações.

### Versão 1.3

* Corrigida a leitura de cabeçalhos de mensagens para uma versão mais
  recente do Office 365.
* Atualização para oferecer suporte a versões mais recentes do NVDA
  (compatível com Python 2 e 3).
* Adicionadas localizações.
* Versões realizadas agora com appveyor.

### Versão 1.2

* Corrigida a leitura do cabeçalho ao encaminhar a reunião.
* Adicionadas localizações.

### Versão 1.1

* Adicionadas localizações.

### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

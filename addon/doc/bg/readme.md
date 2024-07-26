# Разширена функционалност за Outlook (Outlook extended) #

* Автори: Cyrille Bougot, Ralf Kefferpuetz
* Съвместимост с NVDA: от 2019.3 и по-нови
* Изтегляне на [стабилна версия][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

## Команди

* От Alt+1 до Alt+9, Alt+0, Alt+-, Alt+=: Съобщава полето на заглавката за
  колоните от 1 до 12 в съобщение, елемент от календара или в прозореца на
  задачите. При двукратно натискане, ако е възможно, премества фокуса в това
  поле. Трикратното натискане копира съдържанието му в клипборда.
* NVDA+Shift+I (настолна подредба) / NVDA+Control+Shift+I (лаптоп подредба):
  Съобщава информационната лента в съобщение, елемент от календара или в
  прозореца на задачите. Двукратното натискане премества фокуса в
  нея. Трикратното натискане копира съдържанието й в клипборда.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA+Shift+M (настолна подредба) / NVDA+Control+Shift+M (лаптоп подредба):
  Премества фокуса в полето със съдържанието на съобщението.
* NVDA+Shift+N (настолна подредба) / NVDA+Control+Shift+N (лаптоп подредба):
  Докладва известието в прозорец със съобщение. При двукратно натискане,
  премества фокуса върху него. При трикратно натискане, копира съдържанието
  му в клипборда.
* Control+Q: В списъка със съобщения отбелязва избраното съобщение или група
  от съобщения като прочетени.
* Control+U: В списъка със съобщения отбелязва избраното съобщение или група
  от съобщения като непрочетени.

## Допълнителни подобрения

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area of the message
  window. In this notification area, you also have buttons to remove the
  address of these recipients.  This add-on will inform you with a ding when
  this notification area appears, disappears or is updated. You can then
  press NVDA+shif+N / NVDA+control+shift+N once to have it read and twice to
  jump to this area. Then move with the arrows on the recipient buttons and
  press a button to remove the corresponding recipient.
* В списъка с резултати на адресната книга можете да използвате команди за
  хоризонтална навигация в таблица, за да прочетете съдържанието на всяка
  колона.
  
## Бележки

Всички жестове/команди могат да се променят в диалоговия прозорец на NVDA
"Жестове на въвеждане". Може да пожелаете да промените някои от тях, особено
в следните ситуации:

* Жестовете по подразбиране за отбелязване на съобщения като прочетени или
  непрочетени са тези за версията на Outlook на английски. Ако те се
  различават от тези на Outlook на вашия език, ще трябва да ги промените в
  съответствие.
* Жестовете по подразбиране за четене на заглавките съответстват на Alt,
  комбиниран с клавишите на първия ред на буквено-цифровата клавиатура. Може
  да се наложи да промените жестовете за прочитане на заглавките за колони
  11 и 12, ако символно те не съвпадат с използваната от вас клавиатурна
  подредба.

## Списък с промените

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
* Обновени преводи.

### Версия 2.1

* Премахнат е тестовият канал.
* Обновени преводи.

### Версия 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Версия 1.10

* Съвместимост с NVDA 2023.1.
* Обновени преводи.

### Версия 1.9

* Съвместимост с NVDA 2022.1.
* Премахната е съвместимостта с версии на NVDA по-стари от 2019.3.
* Публикуването вече се извършва посредством действие на GitHub вместо
  appVeyor.
* Поправено е съобщението при натискане на клавишните команди с Alt и
  цифрите.
* Поправен е проблем, предотвратяващ четенето на заглавки на елементи от
  календара на някои версии на Outlook 365.
* Подобряване на тестовата среда на добавката: навигация в диалоговия
  прозорец "fake root".
* Обновени преводи.

### Версия 1.8

* Обновени преводи.
* Проверка, че всички променливи от оригиналния модул за приложението
  Outlook са все още налични.

### Версия 1.7

* Обновяване с цел съвместимост с NVDA 2021.1.
* Обновени преводи.

### Версия 1.6

* Отстранени разни проблеми при четене на заглавките на съобщенията в
  Outlook 365.
* Поправена е грешка в скрипта за съобщаване на прикачените файлове при
  използване на брайлова клавиатура.
* Добавена е работна среда за тестване на елементи.
* Обновени преводи.

### Версия 1.5

* Четенето на информационната лента вече работи с NVDA 2019.3.
* Навигацията по таблиците в резултатите от адресната книга вече работи с
  NVDA 2019.3.

### Версия 1.4

* Скриптът за преместване на фокуса в заглавките работи отново.
* Скриптът за придвижване към прикачените файлове вече работи, когато има
  повече прикачени файлове.
* Добавени са нови преводи.

### Версия 1.3

* Поправено е четенето на заглавките на съобщенията за по-новите издания на
  Office 365.
* Обновления с цел поддръжка на по-нови версии на NVDA (съвместимост с
  Python 2 и 3).
* Добавени са нови преводи.
* Изданията вече се изпълняват посредством appveyor.

### Версия 1.2

* Поправено е четенето на заглавката при препращане на срещи.
* Добавени са нови преводи.

### Версия 1.1

* Добавени са нови преводи.

### Версия 1.0

* Първо издание.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

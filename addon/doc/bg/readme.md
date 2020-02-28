# Разширена функционалност за Outlook (Outlook extended) #

* Автори: Cyrille Bougot, Ralf Kefferpuetz
* Съвместимост с NVDA: от 2018.3 до 2019.3
* Изтегляне на [стабилна версия][1]
* Изтегляне на [тестова версия][2]

Тази добавка подобрява използването на Microsoft Outlook чрез озвучаване на
някои команди и добавяне на допълнителни команди.

## Команди

* От Alt+1 до Alt+9, Alt+0, Alt+-, Alt+=: Съобщава полето на заглавката за
  колоните от 1 до 12 в съобщение, елемент от календара или в прозореца на
  задачите. При двукратно натискане, ако е възможно, премества фокуса в това
  поле. Трикратното натискане копира съдържанието му в клипборда.
* NVDA+Shift+I (настолна подредба) / NVDA+Control+Shift+I (лаптоп подредба):
  Съобщава информационната лента в съобщение, елемент от календара или в
  прозореца на задачите. Двукратното натискане премества фокуса в
  нея. Трикратното натискане копира съдържанието й в клипборда.
* NVDA+Shift+A (настолна подредба) / NVDA+Control+Shift+A (лаптоп подредба):
  Съобщава броя и имената на прикачените файлове в прозореца за
  съобщения. Двукратното натискане премества фокуса в полето с прикачените
  файлове.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

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

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Добавени са нови преводи.

### Версия 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Добавени са нови преводи.
* Releases performed now with appveyor.

### Версия 1.2

* Fixed header reading when forwarding meeting.
* Добавени са нови преводи.

### Версия 1.1

* Добавени са нови преводи.

### Версия 1.0

* Първо издание.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

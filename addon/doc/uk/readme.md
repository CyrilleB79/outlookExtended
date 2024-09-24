# Outlook extended (Розширення для Outlook) #

* Автори: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Завантажити [стабільну версію][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

## Команди

* Alt+1  до Alt+9, Alt+0, Alt+-, Alt+=: відображає поля заголовка від 1 до
  12 в повідомленні, події календаря чи у вікні завдань. Натиснувши двічі,
  переміщує фокус в це поле, якщо це можливо. Натиснувши тричі, копіює його
  вміст до буфера обміну.
* NVDA+shift+I (розкладка клавіатури desktop) / NVDA+control+shift+I
  (розкладка laptop): відображає панель інформації в повідомленні, події
  календаря чи у вікні завдань. Подвійне натискання  переміщує фокус на
  нього. Потрійне натискання копіює його вміст до буфера обміну.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA+shift+M (розкладка клавіатури desktop) / NVDA+control+shift+M
  (розкладка laptop): переміщує фокус на текст повідомлення.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: у списку повідомлень позначає вибране повідомлення або групу
  повідомлень як прочитані.
* Control+U: у списку повідомлень позначає вибране повідомлення або групу
  повідомлень як непрочитані.

## Additional improvements

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area of the message
  window. In this notification area, you also have buttons to remove the
  address of these recipients.  This add-on will inform you with a ding when
  this notification area appears, disappears or is updated. You can then
  press NVDA+shif+N / NVDA+control+shift+N once to have it read and twice to
  jump to this area. Then move with the arrows on the recipient buttons and
  press a button to remove the corresponding recipient.
* In the address book's result list, you can use horizontal table navigation
  commands to read the content of each column.
  
## Примітки

Всі жести можна змінити у діалозі «Жести вводу» NVDA. Бажання їх змінити
виникає особливо в таких ситуаціях:

* Початкові жести для позначення повідомлень як прочитаних чи непрочитаних —
  це жести для англійської версії Outlook. Якщо вони відрізняються від вашої
  локальної версії Outlook, вам доведеться відповідним чином їх змінити.
* Початкові жести для читання заголовків відповідають Alt у поєднанні з
  клавішами першого рядка буквенно-цифрової клавіатури. Можливо вам буде
  потрібно змінити відображення жестів для читання заголовків 11 і 12, якщо
  вони не відповідають вашій локальній розкладці клавіатури.

## Журнал змін

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
* Оновлено локалізації.

### Version 2.1

* Removed the dev channel.
* Оновлено локалізації.

### Version 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Оновлено локалізації.

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
* Оновлено локалізації.

### Version 1.8

* Оновлено локалізації.
* Ensure that all the variable from the original Outlook appModule are still
  available.

### Версія 1.7

* Оновлено сумісність для версії NVDA 2021.1.
* Оновлено локалізації.

### Версія 1.6

* Виправлено різноманітні проблеми при читанні заголовків повідомлень в
  Outlook 365.
* Виправлено помилку у сценарії  оголошення вкладень при використанні
  брайлівської клавіатури.
* Додано розділ модульного тестування.
* Оновлено локалізації.

### Версія 1.5

* Читання інформаційної панелі тепер працює з NVDA 2019.3.
* Навігація в таблиці у результатах адресної книги тепер працює з NVDA
  2019.3.

### Версія 1.4

* Сценарій для переміщення фокуса по заголовках знову працює.
* Сценарій для переміщення по вкладеннях знову працює при наявності більшої
  кількості вкладень.
* Додано локалізації.

### Версія 1.3

* Виправлено читання заголовків повідомлень для новішої версії Office 365.
* Оновлено для підтримки новіших версій NVDA (сумісних з Python 2 і 3).
* Додано локалізації.
* Версії зараз розробляються за допомогою appveyor.

### Версія 1.2

* Виправлено читання заголовка під час пересилання зустрічі.
* Додано локалізації.

### Версія 1.1

* Додано локалізації.

### Версія 1.0

* Перша версія.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

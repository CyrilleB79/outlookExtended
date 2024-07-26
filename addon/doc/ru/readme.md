# Расширенный Outlook #

* Авторы: Cyrille Bougot, Ralf Kefferpuetz
* Совместимость с NVDA: 2019.3 и выше
* Загрузить [стабильную версию][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

## Команды

* Alt+1 до Alt+9, Alt+0, Alt+-, Alt+=: Объявляет поля заголовка с 1 по 12 в
  сообщении, элементе календаря или окне задачи. При двойном нажатии фокус
  перемещается на это поле, если это возможно. При тройном нажатии
  копируется его содержимое в буфер обмена.
* NVDA+shift+I (настольная) / NVDA+control+shift+I (ноутбук): Озвучивает
  информационную панель в сообщении, событии календаря или окне задачи. Если
  нажать дважды, переводит в него фокус. Если нажать трижды, копирует его
  содержимое в буфер обмена.
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA+shift+M (настольная) / NVDA+control+shift+M (ноутбук): Перемещает
  фокус в тело сообщения.
* NVDA+shift+N (настольная) / NVDA+control+shift+N (ноутбук): Объявляет
  уведомление в окне сообщений. При двойном нажатии перемещает на него
  фокус. При тройном нажатии копирует его содержимое в буфер обмена.
* Control+Q: в списке сообщений помечает выбранное сообщение или группу
  сообщений как прочитанные.
* Control+U: в списке сообщений помечает выбранное сообщение или группу
  сообщений как непрочитанные.

## Дополнительные улучшения

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area of the message
  window. In this notification area, you also have buttons to remove the
  address of these recipients.  This add-on will inform you with a ding when
  this notification area appears, disappears or is updated. You can then
  press NVDA+shif+N / NVDA+control+shift+N once to have it read and twice to
  jump to this area. Then move with the arrows on the recipient buttons and
  press a button to remove the corresponding recipient.
* В списке результатов адресной книги вы можете использовать команды
  горизонтальной навигации по таблице, чтобы прочитать содержимое каждого
  столбца.
  
## Примечания

Все жесты можно изменить в диалоге командных жестов NVDA. Вы можете захотеть
изменить их, в частности, в следующих ситуациях:

* Жесты, используемые по умолчанию для пометки сообщений как прочитанных или
  непрочитанных, используются в английской версии Outlook. Если они
  отличаются от жестов в вашей локальной версии Outlook, вам придется
  изменить их соответствующим образом.
* Жесты, используемые по умолчанию для чтения заголовков, соответствуют
  клавише Alt в сочетании с клавишами первого ряда буквенно-цифровой
  клавиатуры. Возможно, вам потребуется перенастроить жесты для чтения
  заголовков 11 и 12, если они не соответствуют вашей местной раскладке
  клавиатуры.

## Журнал изменений

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
* Обновлены локализации.

### Версия 2.1

* Удален канал разработчика.
* Обновлены локализации.

### Версия 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Версия 1.10

* Совместимость с NVDA 2023.1.
* Обновлены локализации.

### Версия 1.9

* Совместимость с NVDA 2022.1.
* Заброшена совместимость для версий NVDA ниже 2019.3.
* Выпуск теперь выполняется благодаря действию на GitHub вместо AppVeyor.
* Исправлено объявление, когда пользователь трижды нажимал сочетания клавиш
  alt+цифра.
* Исправлена ошибка, из-за которой не удавалось прочитать заголовки
  элементов календаря в некоторых версиях Outlook 365.
* Улучшение тестовой среды дополнения: навигация в поддельном корневом
  диалоге.
* Обновлены локализации.

### Версия 1.8

* Обновлены локализации.
* Проверено, что все переменные из исходного модуля приложения Outlook
  по-прежнему доступны.

### Версия 1.7

* Обновление совместимости для NVDA 2021.1.
* Обновлены локализации.

### Версия 1.6

* Исправлены различные проблемы при чтении заголовков сообщений в Outlook
  365.
* Исправлена ошибка в скрипте объявления вложений при использовании
  брайлевской клавиатуры.
* Добавлен фреймворк модульного тестирования.
* Обновлены локализации.

### Версия 1.5

* Чтение информационной панели теперь работает с NVDA 2019.3.
* Навигация по таблицам в результатах поиска адресной книги теперь работает
  с NVDA 2019.3.

### Версия 1.4

* Скрипт для перемещения фокуса на заголовки снова работает.
* Скрипт для перехода к вложениям теперь работает при наличии большего
  количества вложений.
* Добавлены локализации.

### Версия 1.3

* Исправлено чтение заголовков сообщений для более новой версии Office 365.
* Обновления для поддержки более новых версий NVDA (совместимых с Python 2 и
  3).
* Добавлены локализации.
* Выпуски теперь выполняются с помощью appveyor.

### Версия 1.2

* Исправлено чтение заголовка при переадресации собрания.
* Добавлены локализации.

### Версия 1.1

* Добавлены локализации.

### Версия 1.0

* Первоначальный выпуск.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

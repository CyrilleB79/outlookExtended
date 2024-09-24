# Outlook 扩展 #

* 作者: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* 下载 [稳定版][1]

This addon improves the use of Microsoft Outlook with NVDA: it vocalizes
some native commands and adds extra commands and features.

## 命令

* Alt+1 到 Alt+9, Alt+0, Alt+-, Alt+=:
  在消息，日历项或任务窗口中朗读标题1到12。按两次，将焦点移动到此字段。按三次，则将其内容复制到剪贴板。
* NVDA+shift+I (台式机方按) / NVDA+control+shift+I (笔记本方按):
  案一次，朗读消息，日历项目或任务窗口中的信息栏。按两次，则将焦点移动到上述项目。按三次，则将其内容复制到剪贴板。
* NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout):
  
    * In a message window: reports the number and the names of attachments;
      if pressed twice, moves the focus to it.
    * In a meeting window, in the all attendees tab: display in a browseable
      message the attendees status on the time slot of the meeting.

* NVDA + shift + M（台机布局）/ NVDA + control + shift + M（笔电布局）：将焦点移到邮件正文。
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: 在消息列表中，将所选消息或消息组标记为已读。
* Control + U：在消息列表中，将选定的消息或一组消息标记为未读。

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
  
## 注意

可以在NVDA命令手势对话框中修改所有手势。您可能希望修改它们，尤其是在以下情况下：

* 将邮件标记为已读或未读的默认手势是Outlook英文版的手势。如果它们与Outlook本地版本不同，则必须相应地更改它们。
* 读取标题的默认手势对应于Alt与字母数字键盘第一行的键组合。如果它们与本地键盘布局不匹配，您可能需要重新映射读取标题11和12的手势。

## 更新日志

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
* 新增本地化。

### Version 2.1

* Removed the dev channel.
* 新增本地化。

### Version 2.0

* Improve the user experience with the notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* 新增本地化。

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
* 新增本地化。

### Version 1.8

* 新增本地化。
* Ensure that all the variable from the original Outlook appModule are still
  available.

### 版本1.7

* 更新兼容 NVDA 2021.1。
* 新增本地化。

### 版本1.6

* 修复了在 Outlook 365 中读取邮件头时的各种问题。
* 修复了使用盲文键盘时公告附件脚本中的错误。
* 添加了单元测试框架。
* 新增本地化。

### 版本1.5

* 现在可使用NVDA 2019.3。阅读信息栏。
* 通讯簿结果中的表浏览现在可用于NVDA 2019.3。

### 版本1.4

* 将焦点移到标题的脚本再次起作用。
* 当存在更多附件时，移至附件的脚本现在可以使用。
* 新增本地化。

### 版本1.3

* 修复了较新的Office 365版本的邮件标题读取。
* 更新以支持（兼容Python 2和3）。
* 新增本地化。
* 现在使用appveyor进行发布。

### 版本1.2

* 修复了转发会议时读取标题的问题。
* 新增本地化。

### 版本1.1

* 新增本地化。

### 版本1.0

* 发布初始版。

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

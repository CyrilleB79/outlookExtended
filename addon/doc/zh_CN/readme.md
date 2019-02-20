# Outlook 扩展 #

* 作者: Cyrille Bougot, Ralf Kefferpuetz
* NVDA兼容版本: 2018.3至2019.1
* 下载 [稳定版][1]
* 下载 [开发板][2]

此插件主要通过发出一些命令并添加额外的命令来改进Microsoft Outlook的使用体验。

## 命令

* Alt+1 和 Alt+9, Alt+0, Alt+_, alt+=:
  分别在消息，日历项或任务窗口中朗读标题字段1到12。如果按两次，请尽可能将焦点移动到此字段。如果按三次，则将其内容复制到剪贴板。
* NVDA+shift+I: 朗读消息，日历项目或任务窗口中的信息栏。如果按两次，则将焦点移动到上数项目。如果按三次，则将其内容复制到剪贴板。
* NVDA+shift+A: 在消息窗口中朗读附件的编号和名称。如果按两次，则将焦点移动到附件。
* NVDA+shift+M: 将焦点移动到邮件正文
* Control+Alt+左光标 和 Control+Alt+右光标: 分别在地址簿搜索结果列表，和当前所选的编辑框之间进行浏览
* Control+Q: 在消息列表中，将所选消息或消息组标记为已读
* Control+U: 在邮件列表中，将所选邮件或邮件组标记为未读

## 注意

可以在NVDA命令手势对话框中修改所有手势。您可能希望修改它们，尤其是在以下情况下：

* 将邮件标记为已读或未读的默认手势是Outlook英文版的手势。如果它们与Outlook本地版本不同，则必须相应地更改它们。
* 读取标题的默认手势对应于Alt与字母数字键盘第一行的键组合。如果它们与本地键盘布局不匹配，您可能需要重新映射读取标题11和12的手势。

## 更新日志

### 版本1.0

* 发布初始版。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended

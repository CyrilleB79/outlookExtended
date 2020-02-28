# Outlook extended #

* Tác giả: Cyrille Bougot, Ralf Kefferpuetz
* NVDA tương thích: 2018.3 đến 2019.3
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]

Add-on này cải thiện việc sử dụng Microsoft Outlook bằng cách đọc lên và
thêm vào một số phím lệnh.

## Các phím lệnh

* Alt+1 đến Alt+9, Alt+0, Alt+-, Alt+=: đọc các trường tiêu đề từ 1 đến 12
  của thư, thành phần lịch hay cửa sổ tác vụ. Nếu bấm hai lần, chuyển con
  trỏ đến trường đó khi có thể. Nếu bấm ba lần, chép nội dung của nó vào bộ
  nhớ tạm.
* NVDA+shift+I (kiểu bàn phím desktop) / NVDA+control+shift+I (kiểu bàn phím
  laptop): đọc thanh thông tin của thư, thành phần lịch hay cửa sổ tác
  vụ. Nếu bấm hai lần, chuyển con trỏ đến nó. Nếu bấm ba lần, chép nội dung
  của nó vào bộ nhớ tạm.
* NVDA+shift+A (kiểu bàn phím desktop) / NVDA+control+shift+A (kiểu bàn phím
  laptop): đọc số lượng và tên của các tệp đính kèm trong thư. Bấm hai lần,
  chuyển con trỏ đến nó.
* NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout):
  Moves the focus to the message body.
* Control+Alt+Left and Control+Alt+Right: in the address book search result
  list, navigates between the fields of the currently selected line.
* Control+Q: in the message list, marks the selected message or group of
  messages as read.
* Control+U: in the message list, marks the selected message or group of
  messages as unread.

## Các lưu ý

Có thể thiết lập lại các thao tác trong hộp thoại quản lý thao tác của
NVDA. Có thể bạn muốn thay đổi nó trong các tình huống sau:

* Các phím tắt mặc định để đánh dấu đọc / chưa đọc là dành cho phiên bản
  tiếng Anh của Outlook. Nếu nó khác với phiên bản Outlook ở ngôn ngữ của
  bạn, cần phải thay đổi chúng.
* Phím tắt mặc định để đọc các tiêu đề tương ứng là phím Alt kết hợp với các
  phím ở dòng đầu tiên của hàng phím số. Có thể bạn cần phải gán lại các
  thao tác để đọc  tiêu đề thứ 11 và 12 nếu nó không khớp với bàn phím của
  bạn.

## Bản ghi các thay đổi

### Version 1.5

* Reading the information bar is now working with NVDA 2019.3.
* Table navigation in the address book results is now working with NVDA
  2019.3.

### Version 1.4

* The script to move focus to headers is working again.
* The script to move to attachments is now working when more attachments are
  present.
* Đã thêm các bản dịch.

### Phiên bản 1.3

* Fixed message headers reading for newer Office 365 release.
* Updates to support newer versions of NVDA (Python 2 and 3 compatible).
* Đã thêm các bản dịch.
* Releases performed now with appveyor.

### Phiên bản 1.2

* Fixed header reading when forwarding meeting.
* Đã thêm các bản dịch.

### Phiên bản 1.1

* Đã thêm các bản dịch.

### Phiên bản 1.0

* Bản phát hành đầu tiên.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

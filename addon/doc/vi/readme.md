# Outlook extended #

* Tác giả: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

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
* NVDA+shift+M (kiểu bàn phím desktop) / NVDA+shift+M (kiểu bàn phím laptop
  ): chuyển con trỏ đến nội dung thư.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Control+Q: trong danh sách thư, đánh dấu đã đọc cho các thư hay nhóm thư
  đã chọn.
* Control+U: trong danh sách thư, đánh dấu chưa đọc cho các thư hay nhóm thư
  đã chọn.

## Additional improvements

* When the recipient you have entered in the To, Cc or Bcc fields sends
  automatic out of office replies or is not present anymore on the Exchange
  server, Outlook report it in the notification area. In this notification
  area, you also have buttons to remove the address of these recipients.
  This add-on will inform you with a ding when this notification area
  appear, disappear or be updated. You can then press NVDA+shif+N /
  NVDA+control+shift+N once to have it read and twice to jump to this
  area. Then move with arrows on the recipient buttons and press a button to
  remove the corresponding recipient.
* In the address book's result list, you can use horizontal table navigation
  commands to read the content of each column.
  
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

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Đã thêm các bản phiên dịch.

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
* Đã thêm các bản phiên dịch.

### Version 1.8

* Đã thêm các bản phiên dịch.
* Ensure that all the variable from the original Outlook appModule are still
  available.

### Phiên bản 1.7

* Cập nhật tương thích cho NVDA 2021.1
* Đã thêm các bản phiên dịch.

### Phiên bản 1.6

* Sửa nhiều lỗi khi đọc các tiêu đề của thư trong Outlook 365.
* Sửa một lỗi trong kịch bản thông báo tập tin đính kèm khi dùng bàn phím
  chữ nổi.
* Thêm một bộ kiểm tra.
* Đã thêm các bản phiên dịch.

### Phiên bản 1.5

* Việc đọc thanh thông tin giờ đã hoạt động với NVDA 2019.3.
* Việc điều hướng trong bảng ơ 3ket61 quả trong sổ địa chỉ giờ đây đã hoạt
  động với NVDA 2019.3.

### Phiên bản 1.4

* Kịch bản chuyển con trỏ đến tiêu đề giờ đây đã hoạt động trở lại.
* Kịch bản chuyển con trỏ đến tập tin đính kèm giờ đây đã hoạt động khi có
  nhiều tập tin đính kèm.
* Đã thêm các bản dịch.

### Phiên bản 1.3

* Sửa lỗi đọc các tiêu đề thư cho các bản phát hành mới hơn của Office 365.
* Cập nhật hỗ trợ các phiên bản NVDA mới hơn (tương thích với Python 2 và
  3).
* Đã thêm các bản dịch.
* Các bản phát hành giờ đã vận hành được với appveyor.

### Phiên bản 1.2

* Sửa lỗi đọc tiêu đề khi chuyển tiếp thông tin cuộc họp.
* Đã thêm các bản dịch.

### Phiên bản 1.1

* Đã thêm các bản dịch.

### Phiên bản 1.0

* Bản phát hành đầu tiên.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

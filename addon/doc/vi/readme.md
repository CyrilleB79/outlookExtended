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
* NVDA+shift+M (kiểu bàn phím desktop) / NVDA+shift+M (kiểu bàn phím laptop
  ): chuyển con trỏ đến nội dung thư
* Control+Alt+mũi tên trái và Control+Alt+mũi tên phải: trong danh sách kết
  quả tìm kiếm của sổ địa chỉ, duyệt giữa các trường của dòng đang được chọn
* Control+Q: trong danh sách thư, đánh dấu đã đọc cho các thư hay nhóm thư
  đã chọn
* Control+U: trong danh sách thư, đánh dấu chưa đọc cho các thư hay nhóm thư
  đã chọn

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

### Phiên bản 1.3

* Sửa lỗi đọc các tiêu đề thư cho các bản phát hành mới hơn của Office 365.
* Cập nhật hỗ trợ các phiên bản NVDA mới hơn (tương thích với Python 2 và 3)
* Đã thêm các bản dịch.
* Các bản phát hành giờ đã vận hành được với appveyor

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

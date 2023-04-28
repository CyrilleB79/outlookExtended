# geliştirilmiş Outlook desteği #

* Yazarlar: Cyrille Bougot, Ralf Kefferpuetz
* NVDA compatibility: 2019.3 and beyond
* [kararlı sürüm][1]ü indir

This addon improves the use of Microsoft Outlook by vocalizing some native
commands, adding extra commands and adds extra features.

## Komutlar

* Alt+1-9, Alt+0, Alt+-, Alt+=: 1-12 sayılı iletinin, takvim öğesinin veya
  görev penceresinin başlık alanını söyler. İki kez basıldığında, mümkün
  olduğunda odağı  başlık alanına taşır. Üç kez basıldığında başlık alanının
  içeriğini panoya kopyalar.
* NVDA+shift+I (masaüstü düzeni) / NVDA+control+shift+I (dizüstü düzeni):
  iletinin, takvim öğesinin veya görev penceresinin bilgi çubuğunu okur. İki
  kez basıldığında odağı bilgi çubuğuna taşır. Üç kez basıldığında bilgi
  çubuğunun içeriğini panoya kopyalar.
* NVDA+shift+A (masaüstü düzeni) / NVDA+kontrol+shift+A (dizüstü düzeni):
  İleti penceresindeki eklerin sayısını ve adlarını söyler. İki kez
  basıldığında odağı eklere taşır.
* NVDA+shift+M (masaüstü düzeni) / NVDA+kontrol+shift+M (dizüstü düzeni):
  Odağı ileti gövdesine taşır.
* NVDA+shift+N (desktop layout) / NVDA+control+shift+N (laptop layout):
  Reports the notification in a message window. If pressed twice, moves the
  focus to it. If pressed three times, copies its content to the clipboard.
* Kontrol+Q: İleti listesinde, seçilen iletiyi veya ileti grubunu okundu
  olarak işaretler.
* Kontrol+U: İleti listesinde, seçilen iletileri veya ileti grubunu okunmadı
  olarak işaretler.

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
  
## Notlar

Tüm komutlar NVDA'nın girdi hareketleri iletişim kutusundan
değiştirilebilir. Özellikle aşağıdaki durumlarda komutları değiştirmeniz
gerekebilir:

* Mesajları okundu veya okunmadı olarak işaretleme komutları İngilizce
  Outlook'a göre ayarlanmıştır. Komutlar kullandığınız Outlook diliyle
  eşleşmiyorsa onları değiştirmeniz gerekecektir.
* Başlıkları okuma komutları, Alt tuşu basılı tutulup klavyenin en üst
  sırasındaki tuşlara basılarak uygulanacak şekilde ayarlanmıştır. 11 ve
  12. başlığı okuma komutları klavye düzeninizle eşleşmiyorsa bunları
  yeniden ayarlamanız gerekebilir.

## Değişiklikler

### Version 2.1

* Removed the dev channel.
* Çeviriler güncellendi.

### Version 2.0

* Improve the user experience with notifications appearing when entering
  e-mail addresses which are not valid anymore or which send automatic out
  of office replies: a sound alerts when such notifications appear or are
  updated, a gesture allows to read it or to move to it, and navigation in
  this area with arrows is made more easy.

### Version 1.10

* Compatibility with NVDA 2023.1.
* Çeviriler güncellendi.

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
* Çeviriler güncellendi.

### Version 1.8

* Çeviriler güncellendi.
* Ensure that all the variable from the original Outlook appModule are still
  available.

### Sürüm 1.7

* Eklenti NVDA 2021.1 ile uyumlu hâle getirildi.
* Çeviriler güncellendi.

### Sürüm 1.6

* Outlook 365'te ileti başlıkları okunurken ortaya çıkan çeşitli sorunlar
  düzeltildi.
* Braille klavye kullanılırken ekleri okuma skriptinde ortaya çıkan bir
  sorun düzeltildi.
* Birim test çerçevesi eklendi.
* Çeviriler güncellendi.

### Sürüm 1.5

* Bilgi çubuğu NVDA 2019.3 ile okunabiliyor.
* NVDA 2019.3 ile adres defteri sonuçlarında tablo dolaşımı yapılabiliyor.

### Sürüm 1.4

* Odağı başlığa taşıma skripti düzeltildi.
* Odağı eke taşıma skripti birden fazla ek olduğunda da çalışıyor.
* Çeviriler eklendi.

### Sürüm 1.3

* Yeni Office 365 sürümleri için ileti başlığı okuma düzeltildi.
* NVDA'nın yeni sürümlerini desteklemek için güncellemeler (Python 2 ve 3
  ile uyumlu).
* Çeviriler eklendi.
* Yeni sürümler appveyor ile yayımlanıyor.

### Sürüm 1.2

* Toplantı iletirken başlık okuma düzeltildi.
* Çeviriler eklendi.

### Sürüm 1.1

* Çeviriler eklendi.

### Sürüm 1.0

* İlk sürüm.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=outlookextended

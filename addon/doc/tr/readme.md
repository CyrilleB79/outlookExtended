# geliştirilmiş Outlook desteği #

* Yazarlar: Cyrille Bougot, Ralf Kefferpuetz
* NVDA uyumluluğu: 2018.3 ve üzeri sürümler
* [kararlı sürüm][1]ü indir
* [geliştirme sürümü][2]nü indir

Bu eklenti bazı komutları seslendirerek ve yeni komutlar ekleyerek Microsoft
Outlook kullanımını geliştirir.

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
* Kontrol+Alt+Sol ve Kontrol+Alt+Sağ ok tuşları: Adres defteri arama
  sonuçları listesinde, seçili satırın alanları arasında dolaşır.
* Kontrol+Q: İleti listesinde, seçilen iletiyi veya ileti grubunu okundu
  olarak işaretler.
* Kontrol+U: İleti listesinde, seçilen iletileri veya ileti grubunu okunmadı
  olarak işaretler.

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

[1]: https://addons.nvda-project.org/files/get.php?file=outlookextended

[2]: https://addons.nvda-project.org/files/get.php?file=outlookextended-dev

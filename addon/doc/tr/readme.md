# Geliştirilmiş Outlook desteği #

* Yazarlar: Cyrille Bougot, Ralf Kefferpuetz
* NVDA uyumluluğu: 2019.3 ve üzeri sürümler
* [kararlı sürüm][1]ü indir

Bu eklenti, Microsoft Outlook'un NVDA ile kullanımını geliştirir: bazı yerel
komutları seslendirir ve ekstra komutlar ve özellikler ekler.

## Komutlar

* Alt+1-9, Alt+0, Alt+-, Alt+=: 1-12 sayılı iletinin, takvim öğesinin veya
  görev penceresinin başlık alanını söyler. İki kez basıldığında, mümkün
  olduğunda odağı  başlık alanına taşır. Üç kez basıldığında başlık alanının
  içeriğini panoya kopyalar.
* NVDA+shift+I (masaüstü düzeni) / NVDA+control+shift+I (dizüstü düzeni):
  iletinin, takvim öğesinin veya görev penceresinin bilgi çubuğunu okur. İki
  kez basıldığında odağı bilgi çubuğuna taşır. Üç kez basıldığında bilgi
  çubuğunun içeriğini panoya kopyalar.
* NVDA+shift+A (masaüstü düzeni) / NVDA+control+shift+A (dizüstü düzeni):
  
    * Mesaj penceresinde: eklerin sayısını ve adlarını söyler; iki kez
      basıldığında odağı eklere taşır.
    * Bir toplantı penceresinde, tüm katılımcılar sekmesinde: toplantının
      zaman dilimindeki katılımcıların durumunu göz atılabilir bir mesajda
      görüntüler.

* NVDA+shift+M (masaüstü düzeni) / NVDA+kontrol+shift+M (dizüstü düzeni):
  Odağı ileti gövdesine taşır.
* NVDA+shift+N (masaüstü düzeni) / NVDA+control+shift+N (dizüstü bilgisayar
  düzeni): Bildirimi bir mesaj penceresinde bildirir. İki kez basılırsa,
  odağı ona taşır. Üç kez basıldığında içeriğini panoya kopyalar.
* Kontrol+Q: İleti listesinde, seçilen iletiyi veya ileti grubunu okundu
  olarak işaretler.
* Kontrol+U: İleti listesinde, seçilen iletileri veya ileti grubunu okunmadı
  olarak işaretler.

## Ek iyileştirmeler

* Kime, Bilgi veya Gizli alanlarına girdiğiniz alıcı otomatik olarak ofis
  dışında yanıtları gönderdiğinde veya artık Exchange sunucusunda
  bulunmadığında, Outlook bunu ileti penceresinin bildirim alanında
  bildirir. Bu bildirim alanında, bu alıcıların adresini kaldırmak için
  düğmeler de vardır. Bu eklenti, bu bildirim alanı göründüğünde,
  kaybolduğunda veya güncellendiğinde sizi bir ding sesi ile
  bilgilendirecektir. Daha sonra okunması için NVDA+shift+N /
  NVDA+control+shift+N tuşlarına bir kez ve bu alana atlamak için iki kez
  basabilirsiniz. Ardından, alıcı düğmelerinin üzerindeki oklarla hareket
  edin ve ilgili alıcıyı kaldırmak için bir düğmeye basın.
* Adres defterinin sonuç listesinde, her sütunun içeriğini okumak için yatay
  tablo gezinme komutlarını kullanabilirsiniz.
  
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

### Sürüm 3.0

* Bir toplantı penceresinde, tüm katılımcılar sekmesinde, NVDA+shift+A
  (masaüstü düzeni) / NVDA+control+shift+A (dizüstü düzeni) tuşlarına
  basıldığında artık toplantının zaman dilimindeki katılımcıların durumu göz
  atılabilir bir mesajda görüntüleniyor.

### Sürüm 2.4

* Eklenti NVDA 2024.1 ile uyumlu hâle getirildi.
* İlgili komutlar artık isteğe bağlı konuşma modunda kullanılabilir.

### Sürüm 2.3

* Not: Artık çeviri güncellemeleri değişiklik günlüğünde görünmeyecek.

### Sürüm 2.2

* NVDA 2019.3.1 ile uyumluluk geri getirildi.
* Çeviriler güncellendi.

### Sürüm 2.1

* Geliştirici kanalı kaldırıldı.
* Çeviriler güncellendi.

### Sürüm 2.0

* Artık geçerli olmayan veya otomatik ofis dışı yanıtları gönderen e-posta
  adreslerini girerken görünen bildirimlerle kullanıcı deneyimi
  iyileştirildi: bu tür bildirimler göründüğünde veya güncellendiğinde sesli
  uyarılar, bir hareket onu okumaya veya ona geçmeye izin verir ve bu alanda
  oklarla gezinme daha kolay hale getirilir.

### Sürüm 1.10

* Eklenti NVDA 2023.1 ile uyumlu hâle getirildi.
* Çeviriler güncellendi.

### Sürüm 1.9

* Eklenti NVDA 2022.1 ile uyumlu hâle getirildi.
* NVDA sürümleri için uyumluluk 2019.3'ün altına düşürüldü.
* Sürüm artık appVeyor yerine bir GitHub eylemi sayesinde
  gerçekleştiriliyor.
* Kullanıcı alt+sayı kısayollarına üç kez bastığında çıkan duyuru
  düzeltildi.
* Outlook 365'in bazı sürümlerinin takvim öğeleri başlıklarının okunmasını
  engelleyen bir sorun düzeltildi.
* Eklentinin test ortamının iyileştirilmesi: sahte kök iletişim kutusunda
  gezinme.
* Çeviriler güncellendi.

### Sürüm 1.8

* Çeviriler güncellendi.
* Orijinal Outlook appModule'deki tüm değişkenlerin hala kullanılabilir
  durumda olduğundan emin olun.

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

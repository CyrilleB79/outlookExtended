# Genişletilmiş Outlook Desteği

* Yazarlar: Cyrille Bougot, Ralf Kefferpuetz
* NVDA uyumluluğu: 2019.3 ve sonrası

Bu eklenti, Microsoft Outlook'un NVDA ile kullanımını geliştirir.
İleti başlıkları, ekler, bilgi çubuğu, bildirim veya ileti gövdesi gibi bir iletinin çeşitli bölümlerini okumak, taşımak veya kopyalamak için komutlar sağlar.
Ayrıca uygulama içinde dolaşımı geliştirir ve belirli eylemleri gerçekleştirirken daha fazla geri bildirim sağlar.

## Komutlar

* Alt+1'den Alt+9'a, Alt+0, Alt+*, Alt+-: Bir ileti, takvim öğesi veya görev penceresindeki 1'den 12'ye kadar olan başlık alanını bildirir. İki kez basıldığında, mümkünse odağı bu alana taşır. Üç kez basıldığında içeriğini panoya kopyalar.
* `NVDA+control+shift+I`: Bir ileti, takvim öğesi veya görev penceresindeki bilgi çubuğunu seslendirir. İki kez basıldığında odağı ona taşır. Üç kez basıldığında içeriğini panoya kopyalar.
* `NVDA+control+shift+A`:

    * İleti penceresinde: eklerin sayısını ve adlarını seslendirir; iki kez basıldığında odağı oraya taşır.
    * Bir toplantı penceresinde, tüm katılımcılar sekmesinde: toplantı zaman aralığı için katılımcıların durumunu taranabilir bir iletişim kutusunda görüntüler.
    Bu yalnızca tüm katılımcılar sekmesinin bilgilerine tam olarak erişilemeyen eski Outlook sürümlerinde kullanışlıdır ve çalışır.

* 'NVDA+control+shift+M': Odağı ileti gövdesine taşır.
* `NVDA+control+shift+N`: Bildirimi bir mesaj penceresinde gösterir. İki kez basıldığında odağı ona taşır. Üç kez basıldığında içeriğini panoya kopyalar.
* Control+Q: İleti listesinde seçilen iletiyi veya ileti grubunu okundu olarak işaretler.
* Control+U: İleti listesinde seçilen iletiyi veya ileti grubunu okunmamış olarak işaretler.

## Ek iyileştirmeler

* Kime, Bilgi veya Gizli alanlarına girdiğiniz alıcı otomatik ofis dışında yanıtları gönderdiğinde veya artık Exchange sunucusunda bulunmadığında, Outlook bunu ileti penceresinin bildirim alanında bildirir.
  Bu bildirim alanında bu alıcıların adresini kaldırmak için de butonlar bulunur.
  Bu eklenti, bu bildirim alanı göründüğünde, kaybolduğunda veya güncellendiğinde sizi bir uyarı sesiyle uyarır.
  Daha sonra okumak için 'NVDA+control+shift+N' tuşuna bir kez, bu alana atlamak için iki kez basabilirsiniz.
  Daha sonra alıcı düğmelerinin üzerindeki oklarla hareket edin ve ilgili alıcıyı kaldırmak için bir düğmeye basın.
* Adres defterinin sonuç listesinde, her sütunun içeriğini okumak için yatay tablo dolaşım komutlarını kullanabilirsiniz.

## Notlar

Tüm hareketler NVDA Girdi hareketleri iletişim kutusunda değiştirilebilir. Özellikle aşağıdaki durumlarda bunları değiştirmek isteyebilirsiniz:

* İletileri okundu veya okunmadı olarak işaretlemeye yönelik varsayılan hareketler, Outlook'un İngilizce sürümündeki hareketlerdir. Outlook yerel sürümünüzdekilerden farklıysa, bunları uygun şekilde değiştirmeniz gerekecektir.
* Başlıkları okumak için varsayılan hareketler, alfanümerik klavyenin ilk satırındaki tuşlarla birleştirilmiş "alt" kullanıcısıdır.
  Eğer 11 ve 12 numaralı başlıkları okumak için kullanılan hareketler yerel klavye düzeninizle eşleşmiyorsa, hareketleri yeniden eşlemeniz gerekebilir.

## Sürüm Geçmişi

### Sürüm 3.4

* Ekleri, bilgi çubuğunu, bildirimi ve ileti gövdesini okumak veya bunlara gitmek için masaüstü düzenine ilişkin hareketler, dizüstü bilgisayar düzeniyle eşleşecek şekilde değiştirildi.

### Sürüm 3.3

* NVDA 2026.1 ile uyumluluk.

### Sürüm 3.2

* NVDA 2025.1 ile uyumluluk.

### Sürüm 3.0

* Bir toplantı penceresinde, tüm katılımcılar sekmesinde, NVDA+shift+A (masaüstü düzeni) / NVDA+control+shift+A (dizüstü bilgisayar düzeni) tuşlarına basıldığında artık toplantının zaman dilimindeki katılımcıların durumu taranabilir bir ileti penceresinde görüntüleniyor.

### Sürüm 2.4

* NVDA 2024.1 ile uyumluluk.
* İlgili komutlar artık isteğe bağlı konuşma modunda kullanılabilir.

### Sürüm 2.3

* Not: Artık çeviri güncellemeleri sürüm geçmişinde görünmeyecek.

### Sürüm 2.2

* NVDA 2019.3.1 ile uyumluluk geri getirildi.
* Yerelleştirmeler güncellendi.

### Sürüm 2.1

* Geliştirici kanalı kaldırıldı.
* Yerelleştirmeler güncellendi.

### Sürüm 2.0

* Artık geçerli olmayan veya otomatik ofis dışında yanıtlar gönderen e-posta adreslerini girdiğinizde görüntülenen bildirimlerle kullanıcı deneyimi geliştirildi:
  Bu tür bildirimler göründüğünde veya güncellendiğinde bir ses uyarısı verir, bir hareketle bildirimin okunmasına veya ona doğru hareket edilmesine olanak sağlanır ve bu alanda oklarla dolaşım daha kolay hale gelir.

### Sürüm 1.10

* NVDA 2023.1 ile uyumluluk.
* Yerelleştirmeler güncellendi.

### Sürüm 1.9

* NVDA 2022.1 ile uyumluluk.
* NVDA sürümlerinin uyumluluğu 2019.3'ün altına düşürüldü.
* Sürüm artık appVeyor yerine GitHub eylemi sayesinde gerçekleştiriliyor.
* Kullanıcı alt+sayı kısayollarına üç kez bastığında oluşan duyuru düzeltildi.
* Outlook 365'in bazı sürümlerinin takvim öğeleri üstbilgilerinin okunmasını engelleyen sorun düzeltildi.
* Eklentinin test ortamının iyileştirilmesi: sahte kök iletişim kutusunda dolaşma.
* Yerelleştirmeler güncellendi.

### Sürüm 1.8

* Yerelleştirmeler güncellendi.
* Orijinal Outlook appModule'deki tüm değişkenlerin hâlâ kullanılabilir olduğundan emin olun.

### Sürüm 1.7

* NVDA 2021.1 için güncelleme uyumluluğu.
* Yerelleştirmeler güncellendi.

### Sürüm 1.6

* Outlook 365'te ileti başlıklarını okurken oluşan çeşitli sorunlar düzeltildi.
* Braille klavyesi kullanıldığında Eklerin duyurulduğu Scriptdosyasında ortaya çıkan bir hata düzeltildi.
* Birim testi çerçevesi eklendi.
* Yerelleştirmeler güncellendi.

### Sürüm 1.5

* Bilgi çubuğunun okunması artık NVDA 2019.3 ile çalışıyor.
* Adres defteri sonuçlarındaki tablo dolaşımı artık NVDA 2019.3 ile çalışıyor.

### Sürüm 1.4

* Odağı başlıklara taşımaya yönelik script yeniden çalışıyor.
* Eklere taşıma script'i artık daha fazla ek mevcut olduğunda çalışıyor.
* Yerelleştirmeler eklendi.

### Sürüm 1.3

* Daha yeni Office 365 sürümü için okunan ileti üstbilgileri düzeltildi.
* NVDA'nın daha yeni sürümlerini desteklemek için güncellemeler (Python 2 ve 3 ile uyumlu).
* Yerelleştirmeler eklendi.
* Sürümler artık appveyor ile gerçekleştiriliyor.

### Sürüm 1.2

* Toplantıyı iletirken başlığın okunması düzeltildi.
* Yerelleştirmeler eklendi.

### Sürüm 1.1

* Yerelleştirmeler eklendi.

### Sürüm 1.0

* İlk sürüm.

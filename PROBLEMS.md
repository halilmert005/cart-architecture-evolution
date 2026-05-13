# Faz 0: Başlangıç Kodu Analizi ve Tasarım Sorunları

## Gördüğüm Sorunlar

1) **Karmaşık if-else Yapıları:** calculate_total_price metodu çok uzun ve okunması zor. İndirimler, VIP kontrolü ve kargo kuralları iç içe geçmiş durumda.
2) **Sabit Değerler:** Kargo ücreti ve indirimler doğrudan kod içerisine yazılmış durumda. Bu değerler değiştirilmek istendiğinde kod içersinden teker teker değiştirmek zorunda kalınır.
3) **Geliştirilebilirlik:** Sisteme yeni bir indirim getirilmek istendiğinde kod içerisine yeni bir if-else bloğu eklenmek zorundadır.
4) **Ürün Yaratma:** Ürün nesnelerini main içerisinde kendi elimle yaratıyorum. Ürün çeşitleri arttıkça burası da yönetilemez bir hal alabilir.
5) **Kargo ve Sepet Mantığı:** Sepetin asıl görevi ürünleri tutmak ama şu an kural hesaplamalrını da içerisinde bulunduruyor.
## Yapay Zekanın Gördüğü Sorunlar
1. **SRP İhlali / God Class:** ShoppingCart sınıfı her işi yapıyor. Ürün tutuyor, indirim hesaplıyor, kargo bedeli çıkarıyor. Sorumluluklar ayrılmalı.
2. **OCP İhlali:** İndirim tipleri if-elif ile kontrol ediliyor. Yeni indirim eklemek kodu değiştirmeyi gerektirir. (Çözüm: Strategy örüntüsü).
3. **Sihirli Sayılar:** Fiyat ve oranlar koda gömülü.
4. **Nesne Yaratımının Dağıtık Olması:** İstemci  kodu nesne yaratımına sıkı sıkıya bağlı. (Çözüm: Factory Method örüntüsü).
5. **Sıkı Bağlılık :** Kargo ve indirim kuralları ana hesaplama mantığına sıkı sıkıya bağlı. (Çözüm: Decorator örüntüsü).

## Karşılaştırma ve Farklar
Temelde ikimiz de aynı mimari darboğazları (if-else, sabit sayılar ve nesne yaratım zorluğu) tespit ettik. AI ek olarak bu sorunları hangi tasarım örüntüleriyle (Strategy, Factory, Decorator) çözeceğimin haritasını çıkarmış oldu.
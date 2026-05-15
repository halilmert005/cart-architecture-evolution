# Uygulanan Tasrım Örüntüleri
## 1) Facroty Method - [Faz 1]
- **Kullanılan Yer:** Product sınıfı ve product alt sınıfları.
- **Kullanılma Amacı:** Ürün yaratma mantığını main bloğundan ve ShoppingCart sınıfından ayırmak için.
- **kazançlar:** Nesne yaratma merkezileşti ve kod daha esnek hale geldi.

## Decorator - [Faz 2]
- **Kullanılan Yer:** ProductDecorator ve GiftWrapDecorator sınıflarında.
- **Kullanılma Amacı:** Mevcut ürün nesnelerinin sınıflarını bozmadan, dinamik olarak özellik eklemek için kullanıldı
- **Kazançlar:** Açık/Kapalı prensibi korundu. Yeni özellikler için sınıfları mirasla şişirmek yerine sarmalama kullanıldı.

## 3. Adapter - [Faz 2]
- **Kullanılan Yer:** ShippingAdapter sınıfında.
- **Kullanılma Amacı:** Sistemi dolar bazlı çalışan, müdahale edemediğimiz ExternalShippingAPI ile uyumlu hale getirmek için.
- **Kazançlar:** Dış sistem bağımlılığı izole edildi. API değişse bile ana kodumuz bu değişimden etkilenmeyecek hale getirildi.
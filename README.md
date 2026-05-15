# Evrimleşen Sistem-Tasarım Örüntüleri Ödevi

**Seçilen Konu:** D) E-Ticaret Sepeti

**Gerekçe:** E-ticaret sistemleri doğası gereği sürekli değişen asla aynı kalmayan sistemlerdir. Sürekli değişen sistemlerde tasarım örüntülerini daha iyi anlayabileceğimi düşünüyorum.

### Kullanılan Tasarım Örüntüleri

1. **Factory Method (Creational):** Ürünlerin yaratılma mantığını istemciden ayırmak için kullanıldı.
2. **Decorator (Structural):** Sınıfları değiştirmeden ürünlere dinamik olarak özellikler eklemek için kullanıldı.
3. **Adapter (Structural):** Dışarıdan gelen uyumsuz ve dolar bazlı kargo API'sini, ana sistemimize entegre etmek için kullanıldı.
4. **Strategy (Behavioral):** İndirim hesaplamalarındaki if-elif bloklarını yok etmek ve her indirim türünü kendi sınıfına ayırmak için kullanıldı.
5. **Observer (Behavioral):** Sepete ürün eklendiğinde loglama ve e-posta sistemlerini, sepet sınıfına sıkı sıkıya bağlamadan tetiklemek için kullanıldı.


### Mimari Diyagram
```mermaid
classDiagram
    class ShoppingCart {
        +products: List
        +calculate_total_price(DiscountStrategy)
        +attach_observer(CartObserver)
        +add_item(Product)
    }
    class DiscountStrategy {
        <<interface>>
        +apply_discount(total)
    }
    class CartObserver {
        <<interface>>
        +update(message)
    }
    ShoppingCart --> DiscountStrategy : Uses
    ShoppingCart --> CartObserver : Notifies
    ShoppingCart *-- ProductFactory : Creates
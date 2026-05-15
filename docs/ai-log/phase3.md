## Faz 3: Yapay Zeka Soru Cevap

### 1. Davranışsal Örüntü:Strategy
**Prompt:** Sepet tutarı hesaplanırken kullanılan indirim kodları if-elif bloklarıyla sürekli uzuyor. Yeni bir kampanya eklendiğinde bu metot tam bir spagetti koda dönüşüyor. OCP'yi bozmadan bunu hangi örüntü ile çözebilirim?

**Yapay Zekanın Yanıtı:** Yapay zeka indirim kurallarının çalışma zamanında değişebilen algoritmalar olduğunu belirterek strategy örüntüsünü önerdi. Her indirim tipinin kendi ayrı sınıfına taşınması gerektiğini söyledi.

**Kararım ve Uygulama:** Öneri mantıklıydı ve hemen uyguladım. calculate_total_price içindeki if-elif bloklarını silindi. Sepet artık dışarıdan enjekte edilen bir strateji nesnesi ile çalışıyor. Yeni bir kampanya geldiğinde ana sınıfa hiç dokunmadan sadece yeni bir strateji sınıfı ekleyeceğiz.



### 2. Davranışsal Örüntü:Observer
**Prompt:** Ödev gereksinimlerinde en az iki davranışsal örüntü isteniyor. Sepete yeni bir ürün eklendiğinde email atmak ve konsola log yazdırmak istiyorum. Ancak sepetin ShoppingCart içine Email veya Logger sınıflarını doğrudan yazıp sıkı bir bağımlılık yaratmak istemiyorum. Ne yapmalıyım?

**Yapay Zekanın Yanıtı:** Yapay zeka bu senaryo için en uygun yapının observer örüntüsü olduğunu söyledi. Sepeti bir yayıncı, e-posta ve log sistemlerini ise birer gözlemci olarak kurgulamamı tavsiye etti.

**Kararım ve Uygulama:** Yapay zekanın önerisi sistemi esnek tutmak adına güzel oldu. ShoppingCart sınıfına aboneleri tutacağı bir liste ve notify_observers metodu ekledim. Sepete ürün eklendiğinde sadece bu bildirim metodunu tetikliyor. Mail ve Log sınıfları dışarıdan bu olayları dinliyor. İleride mesaj gönderici eklesek bile ana sepet kodumuz bunu fark etmeyecek.
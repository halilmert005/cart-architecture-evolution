# Faz 1: Yapay Zeka Soru Cevap

**Prompt:** Nesne yaratma sorumluluğunu merkezi bir yapıya taşımak için hangi yaratımsal örüntü uygundur? Factory Method bu sistemde nasıl kurgulanmalı?

**Yapay Zeka Yanıtı:** Yapay zeka, ürünlerin farklı kategorilere ayrılmasının nesne yaratımını karmaşıklaştırdığını belirterek 'Factory Method' önerdi. Soyut bir Product sınıfı ve somut alt sınıflar üzerinden bir fabrika yapısı kurulmasını tavsiye etti.

**Uygulama:** Yapay zekanın önerdiği fabrika yapısı anlaşıldı ve ProductFactory sınıfı somutlaştırılarak uygulandı. İstemci kodu artık somut sınıflara değil, fabrika metoduna bağımlı hale getirildi.
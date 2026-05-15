from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self,total):
        pass

class FixedDiscountStrategy(DiscountStrategy):
    @abstractmethod
    def __init__(self,discount_amount):
        self.discount_amount=discount_amount

    def apply_discount(self,total):
        return total-self.discount_amount

class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self,percentage):
        self.percentage=percentage

    def apply_discount(self,total):
        return total*(1-(self.percentage/100))

class VipGiftStrategy(DiscountStrategy):
    def apply_discount(self,total):
        return total*0.65

class CartObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

class EmailNotifier(CartObserver):
    def update(self, message):
        print(f"[SİSTEM BİLDİRİMİ-EMAIL]: {message}")

class ConsoleLogger(CartObserver):
    def update(self, message):
        print(f"[SİSTEM LOGU]: {message}")

class Product(ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    @property
    @abstractmethod
    def category(self):
        pass

class Electronic(Product):
    @property
    def category(self):
        return 'electronic'

class Clothing(Product):
    @property
    def category(self):
        return 'clothing'

class ProductFactory:
    @staticmethod
    def create_product(product_type, name, price):
        if product_type == 'electronic':
            return Electronic(name,price)
        elif product_type == 'clothing':
            return Clothing(name,price)
        else:
            raise ValueError(f"Bilinmeyen Ürün Tipi: {product_type}")

class ExternalShippingAPI:
    def get_shipping_cost_in_usd(self, weight):
        return weight*2.5

class ShippingAdapter:
    def __init__(self, external_api):
        self.external_api=external_api
        self.usd_to_try_rate=44.0

    def calculate_shipping(self, weight):
        usd_cost=self.external_api.get_shipping_cost_in_usd(weight)
        return usd_cost*self.usd_to_try_rate

class ProductDecorator(Product):
    def __init__(self, product):
        self.product=product

    @property
    def name(self):
        return self.product.name
    @property
    def price(self):
        return self.product.price
    @property
    def category(self):
        return self.product.category

class GiftWrapDecorator(ProductDecorator):
    @property
    def name(self):
        return f"{self.product.name} (Hediye Paketi)"

    @property
    def price(self):
        return self.product.price +50

class User:
    def __init__(self,username,is_vip):
        self.username=username
        self.is_vip=is_vip

class ShoppingCart:
    def __init__(self,user):
        self.user=user
        self.products=[]
        self._observers=[]

    def attach_observer(self,observer):
        self._observers.append(observer)

    def notify_observers(self,message):
        for observer in self._observers:
            observer.update(message)

    def add_item(self, product):
        self.products.append(product)
        self.notify_observers(f"Seperte yeni ürün eklendi:{product.name}  {product.price} TL")

    def calculate_total_price(self, discount_strategy=None):
        total=0
        shipping_cost=50
        for product in self.products:
            total+=product.price

        if self.user.is_vip:
            total=total*0.90

        if total>500:
            shipping_cost=0
        else:
            for product in self.products:
                if product.category== 'electronic':
                    shipping_cost=100
                    break

        total+= shipping_cost

        if discount_strategy:
            total=discount_strategy.apply_discount(total)

        return total

if __name__== '__main__':
    user1=User('user1',True)
    cart=ShoppingCart(user1)

    email_notifier = EmailNotifier()
    logger = ConsoleLogger()
    cart.attach_observer(email_notifier)
    cart.attach_observer(logger)

    laptop = ProductFactory.create_product("electronic", "Laptop", 20000)
    tshirt = ProductFactory.create_product("clothing", "T-shirt", 400)
    gift_wrapped_tshirt=GiftWrapDecorator(tshirt)
    cart.add_item(laptop)
    cart.add_item(gift_wrapped_tshirt)

    external_api=ExternalShippingAPI()
    shipping_adapter=ShippingAdapter(external_api)
    print(f"Gelen Kargo Bedeli(TRY): {shipping_adapter.calculate_shipping(2)} TL")

    print(f"Sepetteki Ürünler: ")
    for product in cart.products:
        print(f"{product.name}: {product.price} TL")

    yuzde15_indirim=PercentageDiscountStrategy(15)
    print(f"Tutar: {cart.calculate_total_price(yuzde15_indirim)} TL")

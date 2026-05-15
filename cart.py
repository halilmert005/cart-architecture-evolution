from abc import ABC, abstractmethod

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

    def add_item(self, product):
        self.products.append(product)

    def calculate_total_price(self, discount_code=None):
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

        if discount_code=='BAHAR40':
            total=total-40
        elif discount_code=='YUZDE15':
            total=total*0.85
        elif discount_code=='VIPGIFT' and self.user.is_vip:
            total=total*0.65

        return total

if __name__== '__main__':
    user1=User('user1',True)
    cart=ShoppingCart(user1)
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

    print(f"Tutar: {cart.calculate_total_price('YUZDE15')}")

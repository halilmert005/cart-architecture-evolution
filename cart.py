class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

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
    cart.add_item(Product("Laptop", 20000, "electronic"))
    cart.add_item(Product("T-shirt", 400, "clothing"))
    cart.add_item(Product("Mouse", 5000, "electronic"))

    print(f"Tutar: {cart.calculate_total_price('YUZDE15')}")

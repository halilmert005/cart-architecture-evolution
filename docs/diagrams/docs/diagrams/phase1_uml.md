# Faz 1:Factory Method

```mermaid
classDiagram
    class ShoppingCart {
        +items: List
        +add_item(type, name, price)
    }
    
    class ProductFactory {
        +create_product(type, name, price) Product
    }
    
    class Product {
        <<interface>>
        +get_price()
    }
    
    class Electronic {
        +get_price()
    }
    
    class Clothing {
        +get_price()
    }

    ShoppingCart ..> ProductFactory : Uses
    ProductFactory ..> Product : Creates
    Electronic ..|> Product
    Clothing ..|> Product
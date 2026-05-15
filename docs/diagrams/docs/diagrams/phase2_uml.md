# Faz 2:Adapter ve Decorator

```mermaid
classDiagram
    class ShoppingCart {
        +calculate_total_price()
    }
    
    class ShippingAdapter {
        +get_shipping_cost_in_try(weight_kg)
    }
    
    class ExternalShippingAPI {
        +calculate_in_usd(weight_lbs)
    }
    
    class Product {
        <<interface>>
        +get_price()
    }
    
    class ProductDecorator {
        -product: Product
        +get_price()
    }
    
    class GiftWrapDecorator {
        +get_price()
    }

    ShoppingCart ..> ShippingAdapter : Uses
    ShippingAdapter --> ExternalShippingAPI : Adapts
    ProductDecorator ..|> Product : Implements
    ProductDecorator --> Product : Wraps
    GiftWrapDecorator --|> ProductDecorator : Extends
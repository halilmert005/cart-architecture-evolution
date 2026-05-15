# Faz 3:Strategy ve Observer

```mermaid
classDiagram
    class ShoppingCart {
        -observers: List
        -discount_strategy: DiscountStrategy
        +calculate_total_price()
        +attach_observer(CartObserver)
        +notify_observers()
    }
    
    class DiscountStrategy {
        <<interface>>
        +apply_discount(total)
    }
    
    class CartObserver {
        <<interface>>
        +update(message)
    }
    
    class ConsoleLogger {
        +update(message)
    }
    
    class EmailNotifier {
        +update(message)
    }

    ShoppingCart o-- DiscountStrategy : Has-A
    ShoppingCart o-- CartObserver : Has-A
    ConsoleLogger ..|> CartObserver : Implements
    EmailNotifier ..|> CartObserver : Implements
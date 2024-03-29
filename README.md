# Beautiful-Blooms
## Model

```mermaid
---
title: Animal example
---
classDiagram
    class Product{
        +String code
        +String name
        +Int price
        +String category
        +String status

        +display() Product
        +show() String
        +export_csv()  String
    }

    class Addon{
        +String code
        +String name
        +Int price
        +String status

        +display() Addon
        +show() String
        +export_csv() String
    }

    class Order{
        +String order_code
        +String item_code
        +String addon_code  
        +boolean deliver
        +String delivery_address
        +date delivery_date
        +Int same_day_delivery_charges
        +Int delivery_charges
        +String cust_name
        +String recipient_name
        +String message
        +String status

        +same_day_delivery() boolean
        +display() Order
    }

```
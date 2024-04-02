# Beautiful-Blooms
## Task 
The objective of this project is to allow students to design and implement a mini program  
  
**Language used** : Python

## Additional features that mention in the assignment question
- Using Python `Date` library
- Use Object Oriented Programming (OOP)
- Product popularity rating

## Model

```mermaid
---
title: Class Diagram and relationship
---
classDiagram
direction RL
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

    Order "*" -- "1" Product
    Order "*" -- "1" Addon


```

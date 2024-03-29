from datetime import date


class Product:
    def __init__(self, code=None, name=None, price=0, category=None, status='Out of stock'):
        self.code = code
        self.name = name
        self.price = price
        self.category = category
        self.status = status

    def display(self):
        return [self.code, self.name, f"${self.price}", self.category, self.status]

    def show(self):
        return f"Name: {self.name}\nPrice: ${self.price:.2f}\nStatus: {self.status}"

    def export_csv(self):
        return f"{self.code},{self.name},{self.category},{self.price},{self.status}\n"


class Addon:
    def __init__(self, code=None, name=None, price=0, status='Available'):
        self.code = code
        self.name = name
        self.price = price
        self.status = status

    def display(self):
        return [self.code, self.name, f"${self.price}", self.status]

    def show(self):
        return f"Name: {self.name}\nPrice: ${self.price:.2f}\nStatus: {self.status}"

    def export_csv(self):
        return f"{self.code},{self.name},{self.price},{self.status}\n"


order_status = ['Open', 'Cancelled', 'Preparing', 'Ready', 'Closed']


class Order:
    def __init__(self, order_code,
                 item_code,
                 addon_code,
                 deliver,
                 delivery_date,
                 same_day_delivery_charges,
                 delivery_charges,
                 cust_name,
                 recipient_name,
                 message=None,
                 status=order_status[0]):
        self.order_code = order_code
        self.item_code = item_code
        self.addon_code = addon_code
        self.deliver = deliver
        self.deliver_date = delivery_date
        self.same_day_delivery_charges = same_day_delivery_charges
        self.deliver_charges = delivery_charges
        self.cust_name = cust_name
        self.recipient_name = recipient_name
        self.message = message
        self.status = status

    def same_day_delivery(self):
        if self.deliver_date == date.today():
            return True
        else:
            return False

    def display(self):
        return [self.order_code]

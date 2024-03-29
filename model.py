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


class Order:
    def __init__(self, order_code, item_code, addon_code, ):
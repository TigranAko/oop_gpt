class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        return self.price * (1 - discount / 100)

    def save_to_database(self):
        print(f"Saving {self.name} to database")

class Product:
    def __init__(self, name, price, discount=None):
        self.name = name
        self.price = price
        self.price_with_discount = price if not discount else discount.discount(price)

    def __repr__(self):
        return f"Product({self.name=}, {self.price=}, {self.price_with_discount=})"

class ApplyDiscount:
    def __init__(self, discount):
        self.disc = discount

    def discount(self, price):
        return price * (1 - self.disc / 100)

class DatabaseSaver:
    @staticmethod
    def save_to_database(name):
        print(f"Saving {name} to database")

d = ApplyDiscount(50)
p = Product("laptop", 30000, d)
print(p)



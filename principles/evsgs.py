cart = []  # ❌ Глобальное состояние

def add_to_cart(item):
    cart.append(item)

def get_cart():
    return cart

class Cart:
    def __init__(self):
        self.cart = []

    def add(self, item):
        self.cart.append(item)

    def get(self):
        return self.cart

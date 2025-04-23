class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.stock = {}  # {Location: quantity}

    def add_stock(self, location, quantity):
        if location not in self.stock:
            self.stock[location] = 0
        self.stock[location] += quantity

    def remove_stock(self, location, quantity):
        if location not in self.stock or self.stock[location] < quantity:
            raise ValueError(f"Not enough stock at {location.name} for {self.name}")
        self.stock[location] -= quantity

    @property
    def stock_at_location(self):
        return [(loc, qty) for loc, qty in self.stock.items() if qty > 0]

    def __repr__(self):
        return f"Product(name: {self.name}, code: {self.code})"



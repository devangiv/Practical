# 1)Create one class named “location” with members “name”, “code”.
# 2)Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
# 3)Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”. 
# This method will return all “movement” objects which belong to the passed “product” as an argument.
# 4)Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary
# and it contains “location” as key and actual stock of that product on that location as value.
# 5)Create 4 different location objects.
# 6)Create 5 different product objects.(import product)
# 7)Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve. 
# 8)Display movements of each product using the “movement_by_product” method.
# 9)Display product details with its stock at various locations using “stock_at_locations”.
# 10)Display product list by location (group by location).


from product import Product


# 1) Location class
class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"Location(name: {self.name}, code: {self.code})"


# 2) Movement class
class Movement:
    movements = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        Movement.movements.append(self)

    @staticmethod
    def movements_by_product(product):
        return [m for m in Movement.movements if m.product == product]

    def __repr__(self):
        return (f"Movement(from={self.from_location.name}, "
                f"to={self.to_location.name}, product={self.product.name}, "
                f"quantity={self.quantity})")


# 3) Create locations
location1 = Location("Rajkot", "R001")
location2 = Location("Vadodra", "V001")
location3 = Location("Jamnagar", "J001")
location4 = Location("Surat", "S001")

# 4) Create products
product1 = Product("Product1", "P001")
product2 = Product("Product2", "P002")
product3 = Product("Product3", "P003")
product4 = Product("Product4", "P004")
product5 = Product("Product5", "P005")

# 5) Add initial stock 
product1.add_stock(location1, 50)
product2.add_stock(location1, 50)
product3.add_stock(location2, 150)
product4.add_stock(location3, 20)
product5.add_stock(location4, 20)

# 6) Move products
try:
    product1.remove_stock(location1, 30)
    product1.add_stock(location2, 30)
    Movement(location1, location2, product1, 30)

    product1.remove_stock(location1, 20)
    product1.add_stock(location3, 20)
    Movement(location1, location3, product1, 20)

    product2.add_stock(location2, 100)
    product2.remove_stock(location2, 100)
    product2.add_stock(location3, 100)
    Movement(location2, location3, product2, 100)

    product3.add_stock(location3, 20)
    product3.remove_stock(location3, 20)
    product3.add_stock(location4, 20)
    Movement(location3, location4, product3, 20)

    product4.add_stock(location4, 30)
    product4.remove_stock(location4, 30)
    product4.add_stock(location1, 30)
    Movement(location4, location1, product4, 30)

    
    product5.remove_stock(location4, 110)
    product5.add_stock(location2, 110)
    Movement(location4, location2, product5, 110)

except ValueError as e:
    print(f"Error: {e}")

# 7) Show product movements
print("\n  Product Movements ")
for product in [product1, product2, product3, product4, product5]:
    print(f"\nMovements for {product.name}:")
    for m in Movement.movements_by_product(product):
        print(f"  {m}")

# 8) Show product stocks
print("\n Product Stock by Location ")
for product in [product1, product2, product3, product4, product5]:
    print(f"\n{product.name} stock:")
    for loc, stock in product.stock_at_location:
        print(f"  {loc.name}: {stock}")

# 9) Group by location
location_groups = {}
for product in [product1, product2, product3, product4, product5]:
    for loc, stock in product.stock_at_location:
        if stock > 0:
            if loc not in location_groups:
                location_groups[loc] = []
            location_groups[loc].append(f"{product.name} (Stock: {stock})")

print("\n Products Grouped by Location")
for loc, products in location_groups.items():
    print(f"{loc.name}:")
    for p in products:
        print(f"  {p}")

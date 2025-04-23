

from product import Product

class CategoryBase:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Category(CategoryBase):
    def __init__(self, code, name, parent=None):
        super().__init__(code, name)
        self.parent = parent
        self.products = []
        self.display_name = self.generate_display_name()

    def generate_display_name(self):
        if self.parent:
            return f"{self.parent.display_name} > {self.name}"
        else:
            return self.name

    def add_product(self, product):
        self.products.append(product)

    def display_details(self):
        print(f"Category Code: {self.code}")
        print(f"Display Name: {self.display_name}")
        if self.products:
            for product in self.products:
                print(f"  - {product}")
        else:
            print("  No products available.")
        print()



cat1 = Category("C001", "Electronics")
cat2 = Category("C002", "Laptops", parent=cat1)
cat3 = Category("C003", "Smartphones", parent=cat1)

cat4 = Category("C004", "Clothing")
cat5 = Category("C005", "Men's Clothing", parent=cat4)



# Laptops
cat2.add_product(Product("Gaming Laptop", 2500))
cat2.add_product(Product("Business Laptop", 1500))
cat2.add_product(Product("Student Laptop", 1000))

# Smartphones
cat3.add_product(Product("Flagship Phone", 1200))
cat3.add_product(Product("Mid-Range Phone", 700))
cat3.add_product(Product("Budget Phone", 400))


cat1.add_product(Product("Smart TV", 999))
cat1.add_product(Product("Bluetooth Speaker", 199))
cat1.add_product(Product("Camera", 799))

# Clothing
cat4.add_product(Product("Jacket", 120))
cat4.add_product(Product("Hoodie", 60))
cat4.add_product(Product("T-Shirt", 25))

# Men's Clothing
cat5.add_product(Product("Men's Shirt", 35))
cat5.add_product(Product("Men's Jeans", 50))
cat5.add_product(Product("Men's Blazer", 150))


all_categories = [cat1, cat2, cat3, cat4, cat5]


print(" CATEGORY DETAILS ")
for category in all_categories:
    category.display_details()


print("PRODUCTS GROUPED BY CATEGORY")
for category in sorted(all_categories, key=lambda c: c.display_name):
    print(f"{category.display_name} ({category.code})")
    for prod in category.products:
        print(f"  - {prod}")
    print()

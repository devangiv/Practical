class Category:
    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products  

    def update_no_of_products(self, additional_products):
        self.no_of_products += additional_products

    def __str__(self):
        return f"Category: {self.name}, Code: {self.code}, Number of Products: {self.no_of_products}"


class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        self.category.update_no_of_products(1)

    def __str__(self):
        return f"Product Name: {self.name}, Code: {self.code}, Category: {self.category.name}, Price: {self.price}" 
    
    

category1 = Category("Electronics", "E001", 5)
category2 = Category("Clothing", "C001", 10)
category3 = Category("Furniture", "F001", 7)


product1 = Product("Laptop", "P001", category1, 1000)
product2 = Product("Smartphone", "P002", category1, 500)
product3 = Product("Tablet", "P003", category1, 300)
product4 = Product("Television", "P004", category1, 800)
product5 = Product("Headphones", "P005", category1, 150)
product6 = Product("Shirt", "P006", category2, 30)
product7 = Product("Jeans", "P007", category2, 40)
product8 = Product("Jacket", "P008", category2, 60)
product9 = Product("Couch", "P009", category3, 400)
product10 = Product("Table", "P010", category3, 200)


print(f"Category: {category1.name}, Number of Products = {category1.no_of_products}")
print(f"Category: {category2.name}, Number of Products = {category2.no_of_products}")
print(f"Category: {category3.name}, Number of Products = {category3.no_of_products}")



products = [product1, product2, product3, product4,product5,product6,product7,product8,product9,product10]

# (Low to High)
print("Products sorted by price (Low to High):")
for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if products[i].price > products[j].price:
            products[i], products[j] = products[j], products[i]

for product in products:
    print(product)

#  (High to Low)
print("\nProducts sorted by price (High to Low):")
for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if products[i].price < products[j].price:
            products[i], products[j] = products[j], products[i]

for product in products:
    print(product)

    def search_product_by_code(products, code):
     for product in products:
        if product.code == code:
            return product
     return None


code_to_search = input("Enter the product code to search: ")
product = search_product_by_code(products, code_to_search)

if product:
    print(f"\nProduct with code {code_to_search} found: {product}")
else:
    print(f"\nProduct with code {code_to_search} not found.")



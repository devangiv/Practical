import re
from datetime import datetime,date
from typing import List


class Customer:
    def __init__(self, name, email, phone, street, city, state, country, cust_type, company=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.type = cust_type
        self.company = company  

    def validate(self):
        errors = []

        # Validate type
        if self.type not in ["company", "contact", "billing", "shipping"]:
            errors.append("Invalid type. Must be company, contact, billing, or shipping.")

        # Validate no numbers in name, city, state, country
        if any(char.isdigit() for char in self.name):
            errors.append("Name should not contain numbers.")
        if any(char.isdigit() for char in self.city):
            errors.append("City should not contain numbers.")
        if any(char.isdigit() for char in self.state):
            errors.append("State should not contain numbers.")
        if any(char.isdigit() for char in self.country):
            errors.append("Country should not contain numbers.")

        # Validate email
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.email):
            errors.append("Invalid email format.")

        # Validate phone
        valid_phone = re.match(r'^\+?\d{10,15}$', self.phone) or \
                      re.match(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$', self.phone)
        if not valid_phone:
            errors.append("Invalid phone number format.")

        return errors
    

class OrderLine:
    def __init__(self, product_name, quantity, unit_price):
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

    def line_total(self):
        return self.quantity * self.unit_price


class Order:
    def __init__(self, number, date_value, company, billing, shipping, order_lines):
        self.number = number
        self.date = self.validate_date(date_value)
        self.company = self.validate_customer(company, "Company")
        self.billing = self.validate_customer(billing, "Billing")
        self.shipping = shipping
        self.order_lines = order_lines or []
        self.total_amount = self.calculate_total()

    def validate_date(self, date_val):
        if isinstance(date_val, str):
            try:
                date_val = datetime.strptime(date_val, "%Y-%m-%d").date()
            except ValueError:
                print("Error: Date must be in YYYY-MM-DD format.")
                exit()

        if date_val < date.today():
            print("Error: Order date cannot be in the past.")
            exit()
        return date_val

    def validate_customer(self, customer, label):
        if not isinstance(customer, Customer):
            print(f"Error: {label} must be a Customer instance.")
            exit()
        return customer

    def calculate_total(self):
        return sum(line.line_total() for line in self.order_lines)


def get_customer_input(label="Customer"):
    print(f"\nEnter {label} details:")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    country = input("Country: ")
    cust_type = input("Type (company/contact/billing/shipping): ").lower()

    customer = Customer(name, email, phone, street, city, state, country, cust_type)
    errors = customer.validate()

    if errors:
        print(f"\nValidation Errors in {label}:")
        for error in errors:
            print(f"- {error}")
        exit()
    return customer


def get_order_lines():
    lines = []
    while True:
        print("\nEnter product details:")
        product_name = input("Product Name: ")
        try:
            quantity = int(input("Quantity: "))
            unit_price = float(input("Unit Price: "))
        except ValueError:
            print("Invalid input. Quantity must be integer, Unit Price must be number.")
            continue

        lines.append(OrderLine(product_name, quantity, unit_price))

        more = input("Add another product? (y/n): ").lower()
        if more != 'y':
            break
    return lines


def create_order():
    print("\n--- Creating New Order ---")
    company = get_customer_input("Company")
    shipping = get_customer_input("shipping")
    billing = get_customer_input("Billing")
    order_lines = get_order_lines()

    number = input("\nOrder Number: ")
    date_input = input("Order Date (YYYY-MM-DD): ")

    order = Order(number, date_input, company,shipping,billing,order_lines)

    print("Order Created Successfully!")
    print(f"Order Number: {order.number}")
    print(f"Order Date: {order.date}")
    print(f"Total Amount: {order.total_amount:.2f}")
    print(f"Number of Items: {len(order.order_lines)}")
    for i, line in enumerate(order.order_lines, 1):
        print(f"  {i}. {line.product_name} x {line.quantity} @ {line.unit_price} = {line.line_total():.2f}")


if __name__ == "__main__":
    create_order()




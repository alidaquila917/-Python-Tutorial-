class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Available Quantity: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount

class InventorySystem:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)
        print(f"Added {product.name} to the inventory.")

    def display_inventory(self):
        print("Inventory:")
        for product in self.inventory:
            product.display_info()

    def update_product_quantity(self, product_name, amount):
        for product in self.inventory:
            if product.name == product_name:
                product.update_quantity(amount)
                print(f"Updated quantity of {product_name} by {amount}.")
                return
        print(f"Product {product_name} not found in the inventory.")

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.inventory)
        print(f"Total value of the inventory: ${total_value}")

# Test the Inventory System
inventory_system = InventorySystem()

# Adding products to the inventory
product1 = Product("Laptop", 1000, 10)
product2 = Product("Phone", 500, 20)
inventory_system.add_product(product1)
inventory_system.add_product(product2)

# Displaying the inventory
inventory_system.display_inventory()

# Updating product quantity
inventory_system.update_product_quantity("Laptop", -5)
inventory_system.update_product_quantity("Phone", 10)

# Displaying the updated inventory
inventory_system.display_inventory()

# Calculating total value of the inventory
inventory_system.calculate_total_value()

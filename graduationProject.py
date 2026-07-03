import os


class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def display(self):
        print("-" * 40)
        print(f"ID    : {self.id}")
        print(f"Name  : {self.name}")
        print(f"Price : {self.price}")
        print(f"Stock : {self.stock}")

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False


class Store:
    def __init__(self):
        self.products = {}
        self.inventory_file = "inventory.txt"
        self.sales_file = "sales_log.txt"
        self.load_inventory()

    def load_inventory(self):
        if not os.path.exists(self.inventory_file):
            return

        with open(self.inventory_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    product = Product(data[0], data[1], data[2], data[3])
                    self.products[product.name.lower()] = product

    def save_inventory(self):
        with open(self.inventory_file, "w") as file:
            for product in self.products.values():
                file.write(f"{product.id},{product.name},{product.price},{product.stock}\n")

    def add_product(self):
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")

        if name.lower() in self.products:
            print("Product already exists.")
            return

        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))

        self.products[name.lower()] = Product(product_id, name, price, stock)
        self.save_inventory()

        print("Product added successfully.")

    def show_products(self):
        if not self.products:
            print("No products available.")
            return

        for product in self.products.values():
            product.display()

    def sell_product(self):
        name = input("Enter Product Name: ").lower()

        if name not in self.products:
            print("Product not found.")
            return

        product = self.products[name]

        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Invalid quantity.")
            return

        if quantity > product.stock:
            print(f"Only {product.stock} items available.")
            return

        product.reduce_stock(quantity)

        total = quantity * product.price

        print("Sale completed.")
        print(f"Total Price = {total}")

        with open(self.sales_file, "a") as file:
            file.write(
                f"Sold: {product.name} | Quantity: {quantity} | "
                f"Total: {total} | Remaining: {product.stock}\n"
            )

        self.save_inventory()


store = Store()

while True:
    print("\n===== SMART STORE =====")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Sell Product")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        store.add_product()

    elif choice == "2":
        store.show_products()

    elif choice == "3":
        store.sell_product()

    elif choice == "4":
        print("Goodbye...")
        break

    else:
        print("Invalid choice.")
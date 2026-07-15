from models.product import Product
from utils.file_handler import load_data, save_data


class Inventory:
    """
    Manages all products in the inventory.
    """

    def __init__(self):
        self.products = []
        self.load_inventory()

    def load_inventory(self):
        data = load_data()

        for item in data:
            product = Product(
                item["product_id"],
                item["name"],
                item["category"],
                item["price"],
                item["quantity"]
            )
            self.products.append(product)

    def save_inventory(self):
        data = []

        for product in self.products:
            data.append({
                "product_id": product.product_id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": product.quantity
            })

        save_data(data)

    def add_product(self, product):
        self.products.append(product)
        self.save_inventory()
        print("\n✅ Product added successfully!")

    def view_products(self):
        if not self.products:
            print("\nInventory is empty.")
            return

        print("\n========== Inventory ==========")

        for product in self.products:
            print(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id.lower() == product_id.lower():
                return product

        return None

    def update_product(self, product_id, name, category, price, quantity):
        product = self.search_product(product_id)

        if product:
            product.name = name
            product.category = category
            product.price = price
            product.quantity = quantity

            self.save_inventory()
            return True

        return False

    def delete_product(self, product_id):
        product = self.search_product(product_id)

        if product:
            self.products.remove(product)
            self.save_inventory()
            return True

        return False
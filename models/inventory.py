from models.product import Product


class Inventory:
    """
    Manages all products in the inventory.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
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
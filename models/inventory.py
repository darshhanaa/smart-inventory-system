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

    def update_product(self, product_id, name, category, price, quantity):
        product = self.search_product(product_id)

        if product:
            product.name = name
            product.category = category
            product.price = price
            product.quantity = quantity
            return True

        return False

    def delete_product(self, product_id):
        product = self.search_product(product_id)

        if product:
            self.products.remove(product)
            return True

        return False
from models.product import Product
from models.inventory import Inventory


def main():
    inventory = Inventory()

    inventory.add_product(Product("P001", "Laptop", "Electronics", 75000, 8))
    inventory.add_product(Product("P002", "Mouse", "Electronics", 1200, 25))
    inventory.add_product(Product("P003", "Keyboard", "Electronics", 2500, 15))

    inventory.view_products()

    print("\n========== Search Result ==========")

    product = inventory.search_product("P002")

    if product:
        print(product)
    else:
        print("Product not found.")


if __name__ == "__main__":
    main()
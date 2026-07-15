from models.product import Product
from models.inventory import Inventory


def display_menu():
    print("\n========================================")
    print("      SMART INVENTORY SYSTEM")
    print("========================================")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")


def main():
    inventory = Inventory()

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n========== Add Product ==========")

            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))

            product = Product(product_id, name, category, price, quantity)
            inventory.add_product(product)

        elif choice == "2":
            inventory.view_products()

        elif choice == "3":
            print("\n========== Search Product ==========")

            product_id = input("Enter Product ID: ")

            product = inventory.search_product(product_id)

            if product:
                print("\nProduct Found:")
                print(product)
            else:
                print("\n❌ Product not found.")

        elif choice == "4":
            print("\n========== Update Product ==========")

            product_id = input("Enter Product ID: ")

            product = inventory.search_product(product_id)

            if product:
                print("\nCurrent Details:")
                print(product)

                name = input("Enter New Name: ")
                category = input("Enter New Category: ")
                price = float(input("Enter New Price: "))
                quantity = int(input("Enter New Quantity: "))

                inventory.update_product(
                    product_id,
                    name,
                    category,
                    price,
                    quantity
                )

                print("\n✅ Product updated successfully!")

            else:
                print("\n❌ Product not found.")

        elif choice == "5":
            print("\n========== Delete Product ==========")

            product_id = input("Enter Product ID: ")

            if inventory.delete_product(product_id):
                print("\n✅ Product deleted successfully!")
            else:
                print("\n❌ Product not found.")

        elif choice == "6":
            print("\nThank you for using Smart Inventory System!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
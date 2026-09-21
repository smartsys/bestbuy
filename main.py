import store
import products

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]

best_buy = store.Store(product_list)


def list_products(store_obj):
    """Print and return all active products."""
    active_products = store_obj.get_all_products()
    print("------")
    for index, item in enumerate(active_products, start=1):
        print(f"{index}. {item.name}, Price: ${item.price}, Quantity: {item.get_quantity()}")
    print("------")
    return active_products


def make_order(store_obj):
    """Ask for products and amounts, then place the order."""
    active_products = list_products(store_obj)
    print("When you want to finish order, enter empty text.")
    shopping_list = []

    while True:
        product_input = input("Which product # do you want? ")
        amount_input = input("What amount do you want? ")
        if product_input == "" or amount_input == "":
            break
        shopping_list.append((active_products[int(product_input) - 1], int(amount_input)))
        print("Product added to list!")
        print()

    total_price = store_obj.order(shopping_list)

    print("********")
    print(f"Order made! Total payment: ${total_price:.2f}")


def start(store_obj):
    """Show the store menu."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            print(f"Total of {store_obj.get_total_quantity()} items in store")
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            break


if __name__ == "__main__":
    start(best_buy)

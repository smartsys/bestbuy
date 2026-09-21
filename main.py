
import store
import product


# setup initial stock of inventory
product_list = [ product.Product("MacBook Air M2", price=1450, quantity=100),
                 product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 product.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = store.Store(product_list)

def start(store_obj):

    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == "4":
            break



if __name__ == "__main__":
    start(best_buy)

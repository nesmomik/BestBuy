import products
import store


def print_menu():
    print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
    """)


def print_and_return_all_active_products(
    store: store.Store,
) -> list[products.Product]:
    """
    Prints all products in store
    """
    store_products = store.get_all_products()

    print("------")
    for index, product in enumerate(store_products):
        print(f"{index + 1}. {product}")
    print("------")

    return store_products


def print_total_amount(store: store.Store):
    """
    Prints total amount of items in store
    """
    print(f"\nTotal of {store.get_total_quantity()} items in store.")


def make_order(store: store.Store):
    """
    Allows a user to add multiple products to an order
    Prints the total price of the order
    """
    print("When you want to finish order, enter empty text.")

    order_list = []

    store_products = print_and_return_all_active_products(store)

    while True:
        product_number = input("Which product # do you want? ")
        product_count = input("What amount do you want? ")

        # check for empty strings to quit
        if not product_number or not product_count:
            break
        try:
            order_list.append(
                (store_products[int(product_number) - 1], int(product_count))
            )
        except Exception:
            print("Error adding product!")

    try:
        total_price = store.order(order_list)
        print("********")
        print(f"Order made! Total payment: {total_price}")
    except Exception as e:
        print(e)


func_dict = {
    "1": print_and_return_all_active_products,
    "2": print_total_amount,
    "3": make_order,
}


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)

    while True:
        print_menu()

        choice = input("Please choose a number: ")

        if choice in ["1", "2", "3"]:
            func_dict[choice](best_buy)
        elif choice == "4":
            exit()


if __name__ == "__main__":
    main()

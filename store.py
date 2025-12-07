import products


class StoreError(Exception):
    pass


class Store:
    def __init__(self, product_list):
        self.product_list = product_list


    def add_product(self, product: products.Product):
        """
        Adds an instance of class Product the the product list.
        """
        if product in self.product_list:
            raise StoreError("Product already listed in the store.")

        self.product_list.append(product)


    def remove_product(self, product: products.Product):
        """
        Removes a product from store.
        """
        if product not in self.product_list:
            raise StoreError("Product not listed in the store.")

        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total.
        """
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()

        return total_quantity


    def get_all_products(self) -> list[products.Product]:
        """
        Returns all products in the store that are active.
        """
        return [product for product in self.product_list \
                if product.is_active()]


    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product(
            "Bose QuietComfort Earbuds", price=250, quantity=500
        ),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    store_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(store_products[0], 1), (store_products[1], 2)]))


if __name__ == "__main__":
    main()

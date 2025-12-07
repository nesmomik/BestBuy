class QuantityError(Exception):
    pass


class Product:
    def __init__(self, name, price, quantity):
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.active: bool = True


    def __str__(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity (int).
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        if type(quantity) is not int:
            raise TypeError("Quantity must be of type int.")

        if quantity < 0:
            raise ValueError("Quantity can not be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activates the product.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False


    def show(self):
        """
        Prints a string that represents the product
        """
        print(self)


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        When quantity not available, raises an Exception.
        Updates the quantity of the product.
        Returns the total price (float) of the purchase.
        """
        if self.quantity < quantity:
            raise QuantityError("Requested Quantity higher than availability.")

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)

        return quantity * self.price


def main():
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()

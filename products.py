class Product:
    """A product in the store."""

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name must not be empty.")
        if price < 0:
            raise ValueError("Price must not be negative.")
        if quantity < 0:
            raise ValueError("Quantity must not be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity, deactivate at 0."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Buy a quantity and return the total price."""
        if not self.active:
            raise ValueError("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        self.set_quantity(self.quantity - quantity)
        return float(self.price * quantity)


def main():
    """Test the Product class."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()

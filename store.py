from typing import List

import products


class Store:
    """A store holding a list of products."""

    def __init__(self, product_list):
        for product in product_list:
            if not isinstance(product, products.Product):
                raise TypeError("Store accepts only Product instances.")
        self.products = product_list

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[products.Product]:
        """Return all active products."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """Buy the products and return the total price."""
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price

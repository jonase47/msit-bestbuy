"""Store class that holds and manages products."""


class Store:
    """A store containing a list of products."""

    def __init__(self, product_list):
        self.products = list(product_list)

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        if product not in self.products:
            raise ValueError(f"{product.name} ist nicht im Store.")
        self.products.remove(product)

    def get_total_quantity(self):
        """Return the total number of items in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Return all active products."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """Buy a list of (product, quantity) tuples and return the total price."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} ist nicht im Store.")
            total_price += product.buy(quantity)
        return total_price
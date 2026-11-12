"""Product class for the store."""


class Product:
    """A product type with name, price, stock quantity and active status."""

    def __init__(self, name, price, quantity):
        if not name or not name.strip():
            raise ValueError("Name darf nicht leer sein.")
        if price < 0:
            raise ValueError("Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the stock quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the stock quantity; deactivate the product at 0."""
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print the product to the console."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Buy the given quantity and return the total price."""
        if not self.active:
            raise ValueError(f"{self.name} ist nicht aktiv und kann nicht gekauft werden.")
        if quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")
        if quantity > self.quantity:
            raise ValueError(
                f"Nicht genug auf Lager: {self.quantity} verfügbar, {quantity} angefragt."
            )

        total_price = self.price * quantity
        # Use the setter so the product gets deactivated when sold out
        self.set_quantity(self.quantity - quantity)
        return float(total_price)

class Product:
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
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if not self.active:
            raise Exception(f"{self.name} ist nicht aktiv und kann nicht gekauft werden.")
        if quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")
        if quantity > self.quantity:
            raise ValueError(
                f"Nicht genug auf Lager: {self.quantity} verfügbar, {quantity} angefragt."
            )

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return float(total_price)


def main():
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

    
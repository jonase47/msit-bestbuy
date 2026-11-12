"""Command-line interface for the Best Buy store."""

import products
import store


def list_products(store_obj):
    """Print all active products numbered and return them."""
    print("------")
    active_products = store_obj.get_all_products()
    number = 1
    for product in active_products:
        print(f"{number}. ", end="")
        product.show()
        number += 1
    print("------")
    return active_products


def make_order(store_obj):
    """Ask the user for products and quantities, then place the order."""
    active_products = list_products(store_obj)
    print("Wenn du die Bestellung abschließen willst, drücke einfach Enter.")

    shopping_list = []
    while True:
        product_input = input("Welche Produktnummer möchtest du? ")
        amount_input = input("Welche Menge möchtest du? ")

        if product_input == "" or amount_input == "":
            break

        try:
            product_index = int(product_input) - 1
            amount = int(amount_input)
        except ValueError:
            print("Bitte gib nur Zahlen ein.")
            continue

        if product_index < 0 or product_index >= len(active_products):
            print("Diese Produktnummer gibt es nicht.")
            continue

        shopping_list.append((active_products[product_index], amount))
        print("Produkt zur Liste hinzugefügt!\n")

    if len(shopping_list) == 0:
        print("Keine Produkte bestellt.")
        return

    try:
        total_price = store_obj.order(shopping_list)
        print(f"********\nBestellung erfolgreich! Gesamtpreis: {total_price} Dollar.")
    except ValueError as error:
        print(f"Fehler bei der Bestellung: {error}")


def start(store_obj):
    """Show the main menu until the user quits."""
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
            print("Bye!")
            break
        else:
            print("Ungültige Eingabe, bitte wähle 1 bis 4.")


def main():
    """Create the initial inventory and start the store menu."""
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
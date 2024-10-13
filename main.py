# main.py
from business.PizzaManager import Pizza

def list_all_pizzas(pizza_list):
    # Geht durch die Liste von Pizzen und zeigt jede Pizza an
    print("\nAlle verfügbaren Pizzen mit Details:")
    for pizza in pizza_list:
        pizza.display_pizza()

def list_pizzas_with_toppings(pizza_list, toppings_input):
    # Teilt die eingegebenen Beläge in eine Liste auf
    toppings = toppings_input.split()
    print("\nPizzen mit den Belägen:", ", ".join(toppings))

    # Durchläuft die Liste der Pizzen und filtert die passenden heraus
    for pizza in pizza_list:
        # Prüft, ob alle eingegebenen Beläge in den Belägen der Pizza enthalten sind
        if all(topping in pizza.toppings for topping in toppings):
            pizza.display_pizza()


def main():
    # Erste Aufgabe: Einzelne Pizza erstellen und testen
    margherita = Pizza("Margherita", ["Tomatensauce", "Mozzarella"], 7.50)

    # Zeige die Details der Pizza
    margherita.display_pizza()

    # Füge einen Belag hinzu und zeige die Pizza erneut
    margherita.add_topping("Basilikum")
    margherita.display_pizza()

    # Entferne einen Belag und zeige die Pizza erneut
    margherita.remove_topping("Tomatensauce")
    margherita.display_pizza()

    # Zweite Aufgabe: Liste von Pizzen erstellen
    pepperoni = Pizza("Pepperoni", ["Tomatensauce", "Mozzarella", "Pepperoni"], 8.50)
    hawaiian = Pizza("Hawaiian", ["Tomatensauce", "Mozzarella", "Schinken", "Ananas"], 9.00)

    # Liste von Pizzen erstellen
    pizza_list = [margherita, pepperoni, hawaiian]

    # Dritte Aufgabe: Funktionalität zum Auflisten aller Pizzen aufrufen
    list_all_pizzas(pizza_list)

if __name__ == "__main__":
    main()


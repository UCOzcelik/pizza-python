# main.py
from business.PizzaManager import Pizza

def main():
    # Erstelle eine Pizza
    pizza = Pizza("Margherita", ["Käse", "Tomaten"], 8.50)

    # Zeige die Pizza an
    pizza.display_pizza()

    # Füge einen Belag hinzu und zeige die Pizza erneut
    pizza.add_topping("Basilikum")
    pizza.display_pizza()

    # Entferne einen Belag und zeige die Pizza erneut
    pizza.remove_topping("Käse")
    pizza.display_pizza()

if __name__ == "__main__":
    main()


2. idee

# main.py
from business.PizzaManager import Pizza

def main():
    # Erstelle eine Pizza
    margherita = Pizza("Margherita", ["Käse", "Tomaten"], 8.50)

    # Zeige die Details der Pizza
    margherita.show_details()

    # Füge einen Belag hinzu und zeige die Pizza erneut
    margherita.add_topping("Basilikum")
    margherita.show_details()

    # Entferne einen Belag und zeige die Pizza erneut
    margherita.remove_topping("Käse")
    margherita.show_details()

if __name__ == "__main__":
    main()

from business.PizzaManager import Pizza

def main():
    # Erstelle eine neue Pizza mit Name, Belägen und Preis
    margherita = Pizza("Margherita", ["Tomatensauce", "Mozzarella"], 7.50)

    # Zeige die Details der Pizza
    margherita.display_pizza()

    # Füge einen Belag hinzu und zeige die Pizza erneut
    margherita.add_topping("Basilikum")
    margherita.display_pizza()

    # Entferne einen Belag und zeige die Pizza erneut
    margherita.remove_topping("Tomatensauce")
    margherita.display_pizza()

if __name__ == "__main__":
    main()


# main.py
from business.PizzaManager import Pizza

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

    # Zweite Aufgabe: Liste von Pizzen erstellen und anzeigen
    # Erstelle mehrere weitere Pizza-Objekte
    pepperoni = Pizza("Pepperoni", ["Tomatensauce", "Mozzarella", "Pepperoni"], 8.50)
    hawaiian = Pizza("Hawaiian", ["Tomatensauce", "Mozzarella", "Schinken", "Ananas"], 9.00)

    # Erstelle eine Liste von Pizzen und füge alle hinzu
    pizza_list = [margherita, pepperoni, hawaiian]

    # Zeige alle Pizzen in der Liste an
    print("\nVerfügbare Pizzen:")
    for pizza in pizza_list:
        pizza.display_pizza()

if __name__ == "__main__":
    main()

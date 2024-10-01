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

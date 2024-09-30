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


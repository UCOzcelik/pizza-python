# PizzaManager.py

class Pizza:
    def __init__(self, name, toppings, price):
        # Basis-Eigenschaften der Pizza
        self.name = name
        self.toppings = toppings
        self.price = price

    def display_pizza(self):
        # Zeigt die Pizzadetails: Name, Beläge, Preis
        print(self.name, "mit", ", ".join(self.toppings), "- Preis:", self.price, "€")

    def add_topping(self, topping):
        # Fügt Belag hinzu, kein doppelter Check
        self.toppings.append(topping)

    def remove_topping(self, topping):
        # Entfernt Belag (falls vorhanden)
        if topping in self.toppings:
            self.toppings.remove(topping)


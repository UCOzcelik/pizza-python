# PizzaManager.py

class Pizza:
    def __init__(self, name, toppings, price):
        # Initialisiere die Eigenschaften einer Pizza: Name, Beläge und Preis
        self.name = name
        self.toppings = toppings
        self.price = price

    def display_pizza(self):
        # Zeigt die Details der Pizza (Name, Beläge, Preis) an
        print(f"{self.name}: {', '.join(self.toppings)} - Preis: {self.price}€")

    def add_topping(self, topping):
        # Fügt einen neuen Belag zur Pizza hinzu
        self.toppings.append(topping)

    def remove_topping(self, topping):
        # Entfernt einen Belag von der Pizza, falls er vorhanden ist
        if topping in self.toppings:
            self.toppings.remove(topping)

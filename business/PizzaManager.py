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




2. idee 

# PizzaManager.py

class Pizza:
    def __init__(self, name, toppings, price):
        # Der Konstruktor initialisiert den Namen, die Beläge und den Preis der Pizza
        self.name = name
        self.toppings = toppings
        self.price = price

    def show_details(self):
        # Gibt die Details der Pizza in einem lesbaren Format aus
        print(f"{self.name}: {', '.join(self.toppings)} - Preis: {self.price:.2f}€")
        def add_topping(self, topping):
        # Fügt einen Belag hinzu, wenn er noch nicht vorhanden ist
        if topping not in self.toppings:
            self.toppings.append(topping)

    def remove_topping(self, topping):
        # Entfernt den Belag, falls er vorhanden ist
        if topping in self.toppings:
            self.toppings.remove(topping)



class Pizza:
    def __init__(self, name, toppings, price):
        # Basis-Eigenschaften der Pizza
        self.name = name
        self.toppings = toppings
        self.price = price


class Pizza:
    def __init__(self, name, toppings, price):
        """
        Initialisiert eine Pizza mit Name, Belägen und Preis.
        :param name: Name der Pizza (z.B. 'Margherita')
        :param toppings: Liste der Beläge (z.B. ['Käse', 'Tomaten'])
        :param price: Preis der Pizza (z.B. 8.50)
        """
        self.name = name
        self.toppings = toppings
        self.price = price

    def __str__(self):
        """
        Gibt eine lesbare Darstellung der Pizza zurück.
        :return: Zeichenkette mit Name, Belägen und Preis der Pizza
        """
        toppings_str = ", ".join(self.toppings)
        return f'{self.name} mit {toppings_str} - {self.price:.2f} Euro'

    def add_topping(self, topping):
        """
        Fügt einen neuen Belag hinzu.
        :param topping: Neuer Belag
        """
        self.toppings.append(topping)

    def remove_topping(self, topping):
        """
        Entfernt einen Belag.
        :param topping: Belag, der entfernt werden soll
        """
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print(f"{topping} ist nicht auf der Pizza.")

    def apply_discount(self, discount_code):
        """
        Wendet einen Rabatt an, falls der Gutscheincode 'PIZZA10' eingegeben wird.
        :param discount_code: Gutscheincode
        :return: Rabattierter Preis, falls der Code korrekt ist, sonst der Originalpreis.
        """
        if discount_code == "PIZZA10":
            return self.price * 0.9  # 10% Rabatt
        return self.price


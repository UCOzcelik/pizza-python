# main.py
from business.PizzaManager import Pizza

def list_all_pizzas(pizza_list):
    # Geht durch die Liste von Pizzen und zeigt jede Pizza an
    print("\nAlle verfügbaren Pizzen mit Details:")
    for pizza in pizza_list:
        pizza.display_pizza()

def list_pizzas_with_toppings(pizza_list, toppings_input):
    toppings = toppings_input.split()
    print("\nPizzen mit den Belägen:", ", ".join(toppings))
    filtered_pizzas = [pizza for pizza in pizza_list if all(topping in pizza.toppings for topping in toppings)]
    for pizza in filtered_pizzas:
        pizza.display_pizza()
    return filtered_pizzas

def select_pizza_by_name(pizza_list):
    # Benutzer nach dem Namen der gewünschten Pizza fragen
    pizza_name = input("\nGib den Namen der Pizza ein, die du auswählen möchtest: ")
    # Suche nach der Pizza in der Liste
    for pizza in pizza_list:
        if pizza.name.lower() == pizza_name.lower():
            print("\nGewählte Pizza:")
            pizza.display_pizza()
            return         
    # Falls die Pizza nicht gefunden wird
    print(f"Die Pizza '{pizza_name}' ist nicht verfügbar.")


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

    # Neue Funktionalität: Filter für Pizzen nach eingegebenen Belägen anwenden
    toppings_input = input("\nGib die gewünschten Beläge ein (z.B. 'Schinken Ananas'): ")
    list_pizzas_with_toppings(pizza_list, toppings_input)

    # Fehlender Aufruf von select_pizza_by_name wird hier ergänzt
    select_pizza_by_name(pizza_list)

if __name__ == "__main__":
    main()


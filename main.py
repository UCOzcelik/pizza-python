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
    
    # Debugging Zeile hinzugefügt, um alle Pizzen mit ihren Belägen zu überprüfen
    for pizza in pizza_list:
        print(f"Pizza {pizza.name} hat die Beläge: {', '.join(pizza.toppings)}")

    # Filtert die Pizzen basierend auf den eingegebenen Belägen
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
            
            # Abfrage des Gutscheincodes
            code = input("\nGib einen Gutscheincode ein, falls vorhanden: ")
            if code == "PIZZA10":
                rabattierter_preis = pizza.price * 0.9  # 10% Rabatt
                print(f"Preis mit Rabatt: {rabattierter_preis:.2f} €")
            else:
                print(f"Normaler Preis: {pizza.price:.2f} €")
            return
    # Falls die Pizza nicht gefunden wird
    print(f"Die Pizza '{pizza_name}' ist nicht verfügbar.")


def main():
    # Einzelne Pizza erstellen und testen
    margherita = Pizza("Margherita", ["Tomatensauce", "Mozzarella"], 7.50)

    # Zeige die Details der Pizza
    margherita.display_pizza()

    # Füge einen Belag hinzu und zeige die Pizza erneut
    margherita.add_topping("Basilikum")
    margherita.display_pizza()

    # Entferne einen Belag und zeige die Pizza erneut
    margherita.remove_topping("Tomatensauce")
    margherita.display_pizza()

    # Liste von Pizzen erstellen
    pepperoni = Pizza("Pepperoni", ["Tomatensauce", "Mozzarella", "Pepperoni"], 8.50)
    hawaiian = Pizza("Hawaiian", ["Tomatensauce", "Mozzarella", "Schinken", "Ananas"], 9.00)

    # Liste von Pizzen erstellen
    pizza_list = [margherita, pepperoni, hawaiian]

    # Zeige alle verfügbaren Pizzen mit ihren Belägen
    list_all_pizzas(pizza_list)

# Filter der Pizzen basierend auf den eingegebenen Belägen
    toppings_input = input("\nGib die gewünschten Beläge ein (z.B. 'Schinken Ananas'): ")
    filtered_pizzas = list_pizzas_with_toppings(pizza_list, toppings_input)

    # Überprüfung, ob gefilterte Pizzen vorhanden sind, bevor nach dem Namen gefragt wird
    if filtered_pizzas:
        select_pizza_by_name(filtered_pizzas)  # Neu: Auswahl nur auf gefilterte Pizzen anwenden
    else:
        print("Keine Pizzen mit den angegebenen Belägen verfügbar.")  # Ausgabe, wenn keine passenden Pizzen

if __name__ == "__main__":
    main()


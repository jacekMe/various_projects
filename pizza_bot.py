# pizza bot - ordering

from enum import IntEnum


Restaurants = IntEnum("Restaurants", ['Mexican', "Indian", "Thai", "Polish", "Pizza", "Kebab"])

choose_res = int(input("""Available restaurants:
    1. Mexican
    2. Indian
    3. Thai
    4. Polish
    5. Pizza
    6. Kebab
Hello. What would you eat today? (please enter the number): """))

if choose_res == Restaurants.Mexican:
    print("""   Welcome in probably mexican restaurant. 
    Today we recommend awesome Burrito.
            """)
    burrito = input("Do you want to try? ").lower().split(' ')
    burrito_yes = ["yes", "please", "try", "yeah", "yep", "gladly"]
    
    if any(element in burrito_yes for element in burrito):
        print("Great choice. We are already preparing for you.")
    else:
        mex_menu = {'1': 'Nachos',
                    '2': 'Quesadillas',
                    '3': 'Chili con Carne',
                    '4': 'Sopa de Albondigas',
                    '5': 'Crema de Frijoles',
                    '6': 'Fajitas',
                    '7': 'Ensaladas',
                    '8': 'Brocheta de Cerdo',
                    '9': 'Enchiladas de Credo',
                    '10': 'Coronartia'}

        choose_menu = input("""So, how can I help you?
                                This is our menu:
                                1. Nachos
                                2. Quesadillas
                                3. Chili con Carne
                                4. Sopa de Albondigas
                                5. Crema de Frijoles
                                6. Fajitas
                                7. Ensaladas
                                8. Brocheta de Cerdo
                                9. Enchiladas de Credo
                                10.Coronarita
                                Can I take your order?(please enter the number): """)
        if choose_menu in mex_menu:
            print("Good choice. Order accepted. We are already preparing your {}.".format(mex_menu[choose_menu]))
        else:
            print("Thanks...")


elif choose_res == Restaurants.Indian:
    print("Menu in preparation.")
    
elif choose_res == Restaurants.Thai:
    print("Menu in preparation.")

elif choose_res == Restaurants.Polish:
    print("Menu in preparation.")

elif choose_res == Restaurants.Pizza:
    print("Menu in preparation.")

elif choose_res == Restaurants.Kebab:
    print("Menu in preparation.")
    
else:
    print("See you again!;)")

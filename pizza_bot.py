# pizza bot - ordering

print("""Available restaurants:
    1: Mexican restaurant
    2: Indian restaurant
    3: Thai restaurant
    4: Polish restaurant
    5: Pizaa
    6: Kebab
    """)
choose_res = input("Hello. What would you eat today? (please enter the number): ")

if choose_res == "1":
    print("""Welcome in probably mexican restaurant.
            Today we recommend awesome Burrito.
            """)
    burrito = input("Do you want to try? ").lower().split(' ')
    burrito_yes = ["yes", "please", "try", "yeah", "yep", "gladly"]
    
    if any(element in burrito_yes for element in burrito):
        print("Great choice. We are already preparing for you.")
    else:
        other_choose = input("""So, how can I help you?
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
                                    10. Coronarita
                                Can I take your order?(please enter the number): """)                  
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

        if other_choose in mex_menu:
            print("Good choice. Order accepted. We are already preparing your {}.".format(mex_menu[other_choose]))
        else:
            print("Thanks...")


elif choose_res == '2':
    print("Menu in preparation.")
    
elif choose_res == '3':
    print("Menu in preparation.")

elif choose_res == '4':
    print("Menu in preparation.")

elif choose_res == '5':
    print("Menu in preparation.")

elif choose_res == '6':
    print("Menu in preparation.")
    
else:
    print("See you again!;)")

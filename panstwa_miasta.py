# gra państwa/miasta
""" Jak ma wyglądać rozgrywka:
    1. 10 rund do rozegrania pomiędzy komputerem, a graczem
    2. wylosowanie i wyświetlenie litery oraz przypisanie jej do listy, żeby się nie powtórzyła w następnej rundzie
    3. odliczanie czasu (60s na każdą rundę)
    4. pobranie od gracza nazwy państwa
    5. wyświetlenie nazwy państwa komputera
    6. porównanie wyników (państwa) i przypisanie pkt
    7. pobranie od gracza nazwy miasta
    8. wyświetlenie nazwy miasta komputera
    9. porównanie wyników (miasta) i przypisanie pkt
    10. zliczenie i wyświetlenie punktacji po rundzie
    11. po wszystkich rundach zsumowanie pkt i wyświetlenie zwycięzcy
"""

# POTRZEBNE BIBLIOTEKI
import sys
import random
import string
import time


# ALFABET
def alphabet():
    abc = list(string.ascii_uppercase)
    abc.append("Ł")
    black_list = ["Q", "X", "Y"]
    for letter in black_list:
        abc.remove(letter)
    return abc


# GRACZ
def player():
    global player_name
    player_name = input("Podaj swoje imię: ").capitalize()
    print("\nCześć", player_name + "!\nZaczynamy grę!", "\n")
    return player_name

drawn_letter = []
# LOSOWANIE LITERY
def letter():
    global letter_draw

    letter_draw = random.choice(alphabet())
    print("Wylosowana litera to: ", letter_draw)
    if letter_draw in drawn_letter:
        print(letter_draw, "JUŻ BYŁO. KOLEJNE LOSOWANIE")
        letter()
    drawn_letter.append(letter_draw)
    return letter_draw


# SPRAWDZANIE ODPOWIEDZI I PRZYPISANIE PKT
def countries_answer(player, letter):
    player_countries_answer = input("Podaj nazwę państwa: ").capitalize()
    wrong_name_country = player_countries_answer[0] != letter_draw
    if wrong_name_country:
        print("Podana nazwa kraju nie zaczyna się na literę " + letter_draw)
    bot_countries_answer = random.choice(countries[letter_draw])
    for key in countries:
        if key == letter_draw:
            print(bot_countries_answer)

    if player_countries_answer == '' or wrong_name_country:
        player_points.append(0)
        bot_points.append(15)
    elif player_countries_answer != bot_countries_answer:
        player_points.append(10)
        bot_points.append(10)
    elif player_countries_answer == bot_countries_answer:
        player_points.append(5)
        bot_points.append(5)
    else:
        print("Coś poszło nie tak")

def cities_answer( player, letter):
    player_cities_answer = input("Podaj nazwę miasta: ").capitalize()
    wrong_name_city = player_cities_answer[0] != letter_draw
    if wrong_name_city:
        print("Podana nazwa miasta nie zaczyna się na literę " + letter_draw)
    bot_cities_answer = random.choice(cities[letter_draw])
    for key in cities:
        if key == letter_draw:
            print(bot_cities_answer)

    if player_cities_answer == '' or wrong_name_city:
        player_points.append(0)
        bot_points.append(15)
    elif player_cities_answer != bot_cities_answer:
        player_points.append(10)
        bot_points.append(10)
    elif player_cities_answer == bot_cities_answer:
        player_points.append(5)
        bot_points.append(5)
    else:
        print("Coś poszło nie tak")


# CZAS NA ROUNDĘ (60 SEK)
def countdown(n):
    for x in reversed(range(n+1)):
        sys.stdout.write('\r' + str(x))
        time.sleep(1)
    print()
    print("KONIEC CZASU")


# ZWYCIĘŻCA
def winner(arg):
    if sum(player_points) > sum(bot_points):
        print("Wygrywa", arg + "!")
    elif sum(player_points) < sum(bot_points):
        print("Wygrywa komputer!")
    else:
        print("Remis")

### DODATKOWE ROZWIĄZANIA
# czy porównywać odpowiedzi gracza ze słownikiem?
# jak duży powinien być ten słownik, bo gracz może napisać jakąkolwiek odp?
# sprawdzenie czy pierwsza litera zaczyna się na wylosowaną literę?
# czas na odpowiedź gracza? jeśli minie czas i jest brak odp to 0pkt?
# kolejne słowniki?
# kolejni gracze?

countries = {
    "A": ["Afganistan", "Albania", "Algieria", "Andora", "Angola", "Antigua i Barbuda", "Arabia Saudyjska", "Argentyna",
          "Armenia", "Australia", "Austria", "Azerbejdżan"],
    "B": ["Bahamy", "Bahrajn", "Bangladesz", "Barbados", "Belgia", "Belize", "Benim", "Bhutan", "Białoruś", "Boliwia",
          "Bośnia i Hercegowina", "Botswana", "Brazylia", "Brunei", "Bułgaria", "Burkina Faso", "Burundi"],
    "C": ["Chile", "Chiny", "Chorwacja", "Cypr", "Czad", "Czarnogóra", "Czechy"],
    "D": ["Dania", "Demokratyczna Republika Konga", "Dominikana", "Dżibuti"],
    "E": ["Egipt", "Ekwador", "Erytrea", "Estonia", "Eswatini", "Etiopia"],
    "F": ["Fidżi", "Filipiny", "Finlandia", "Francja"],
    "G": ["Gabon", "Gambia", "Ghana", "Grecja", "Grenada", "Gruzja", "Gujana", "Gwatemala", "Gwinea", "Gwinea Bissau", "Gwinea Równikowa"],
    "H": ["Haiti", "Hiszpania", "Holandia", "Honduras"],
    "I": ["Indie", "Indonezja", "Irak", "Iran", "Irlandia", "Islandia", "Izrael"],
    "J": ["Jamajka", "Japonia", "Jemen", "Jordania"],
    "K": ["Kambodża", "Kamerun", "Kanada", "Katar", "Kazachstan", "Kenia", "Kirgistan", "Kiribati", "Kolumbia", "Komory",
          "Kongo", "Korea Południoa", "Korea Północna", "Kostaryka", "Kuba", "Kuwejt"],
    "L": ["Laos", "Lesotho", "Liban", "Liberia", "Libia", "Liechtenstein", "Litwa", "Luksemburg"],
    "Ł": ["Łotwa"],
    "M": ["Macedonia Północna", "Madagaskar", "Malawi", "Malediwy", "Malezja", "Mali", "Malta", "Maroko", "Mauretania",
          "Mauritus", "Meksyk", "Mikronezja", "Mjanma", "Mołdawia", "Monako", "Mongolia", "Mozambik"],
    "N": ["Namibia", "Nauru", "Nepal", "Niemcy", "Niger", "Nigeria", "Nikaragua", "Norwegia", "Nowa Zelandia"],
    "O": ["Oman"],
    "P": ["Pakistan", "Palau", "Panama", "Papua-Nowa Gwinea", "Paragwaj", "Peru", "Polska", "Południowa Afryka", "Portugalia"],
    "R": ["Republika Środkowoafrykańska", "Republika Zielonego Przylądka", "Rosja", "Rumunia", "Rwanda"],
    "S": ["Saint Kitts i Nevis", "Saint Lucia", "Saint Vincent i Grenadyny", "Salwador", "Samoa", "San Marino", "Senegal",
          "Serbia", "Seszele", "Sierra Leone", "Singapur", "Słowacja", "Słowenia", "Somalia", "Sri Lanka",
          "Stany Zjednoczone", "Sudan", "Sudan Południowy", "Surinam", "Syria", "Szwajcaria", "Szwecja"],
    "T": ["Tadżykistan", "Tajlandia", "Tanzania", "Timor Wschodni", "Togo", "Tonga", "Trynidad i Tobago", "Tunezja", "Turcja",
          "Turkmenistan", "Tuvalu"],
    "U": ["Uganda", "Ukraina", "Urugwaj", "Uzbekistan"],
    "V": ["Vanuatu"],
    "W": ["Watykan", "Wenezuela", "Węgry", "Wielka Brytania", "Wietnam", "Włochy", "Wybrzeże Kości Słoniowej", "Wyspy Marshalla",
          "Wyspy Salomona", "Wyspy Świętego Tomasza i Książeca"],
    "Z": ["Zambia", "Zimbabwe", "Zjednoczone Emiraty Arabskie"]
    }

cities = {
    "A": ["Augustów", "Aleksandrów Łódzki", "Andrychów", "Aleksandrów Kujawski", "Alwernia", "Annopol", "Andrespol", "Ankara",
          "Amman", "Abu Zabi", "Amsterdam", "Ateny", "Austin"],
    "B": ["Bełchatów", "Białystok", "Bielsko-Biała", "Biłgoraj", "Biskupiec", "Bochnia", "Brzeg", "Bydgoszcz", "Bytom", "Bagdad",
          "Baku", "Barcelona", "Belgrad", "Berlin", "Bilbao", "Bogota", "Bombaj", "Boston", "Bratysława",
          "Budapeszt", "Buenos Aires", "Bukareszt"],
    "C": ["Cedynia", "Chełm", "Chojnice", "Chorzów", "Ciechanów", "Ciechocinek", "Cieszyn", "Czaplinek", "Częstochowa", "Canberra",
          "Caracas", "Casablanca", "Charków", "Chartum", "Chicago"],
    "D": ["Darłowo", "Dąbrowa Górnicza", "Dębica", "Dęblin", "Dębno", "Dobre Miasto", "Dakar", "Dallas", "Denver", "Detroit", "Doha",
          "Dortmund", "Drezno", "Dubaj", "Dublin", "Dżakarta"],
    "E": ["Elbląg", "Ełk", "Edmonton", "Edynburg", "El Paso", "Erywań", "Essen"],
    "F": ["Frampol", "Frombork", "Filadelfia", "Florencja", "Frankfurt"],
    "G": ["Gdańsk", "Gdynia", "Giżycko", "Gliwice", "Głogów", "Gniezno", "Gorlice", "Gorzów Wielkopolski", "Grudziądz", "Gryfice",
          "Genewa", "Genua", "Georgetown", "Goteborg", "Graz", "Guadalajara", "Gwatemala"],
    "H": ["Hajnówka", "Hel", "Hrubieszów", "Haga", "Hamburg", "Hanoi", "Hawana", "Helsinki", "Hong Kong", "Houston"],
    "I": ["Iława", "Imielin", "Inowrocław", "Indianapolis", "Irkuck", "Istanbuł"],
    "J": ["Jasło", "Jastarnia", "Jaworzno", "Jelenia Góra", "Jordanów", "Jakuck", "Jerozolima", "Johannesburg"],
    "K": ["Kalisz", "Katowice", "Kęty", "Kielce", "Kłodzko", "Kołobrzeg", "Kostrzyn", "Kraków", "Krosno", "Krynic-Zdrój", "Kutno",
          "Kair", "Kansas", "Kazań", "Kiszyniów", "Kolonia", "Kopenhaga", "Kuala Lampur"],
    "L": ["Legnica", "Leszno", "Limanowa", "Lublin", "Lubin", "Lidzbark Warmiński", "Lagos", "Las Vegas", "Lipsk", "Lizbona",
          "Liverpool", "Londyn", "Los Angeles", "Lwów", "Lyon"],
    "Ł": ["Łódź", "Łańcut", "Łagów", "Łeba", "Łęczna", "Łęknica", "Łomża", "Łowicz"],
    "M": ["Malbork", "Mielec", "Mielno", "Międzyzdroje", "Mikołajki", "Morąg", "Madryt", "Malaga", "Malmo", "Manchester",
          "Manila", "Marsylia", "Medellin", "Mediolan", "Meksyk", "Melbourne", "Miami", "Mińsk", "Monachium",
          "Monako", "Montevideo", "Montreal", "Moskwa"],
    "N": ["Nowa Ruda", "Nowy Sącz", "Nowy Targ", "Nysa", "Nairobi", "Nantes", "Neapol", "Nicea", "Nikozja", "Norymberga",
          "New Delhi", "New York"],
    "O": ["Olkusz", "Olsztyn", "Olsztynek", "Opole", "Ostrołęka", "Ostróda", "Oświęcim", "Otwock", "Odessa", "Oklahoma",
          "Orlando", "Osaka", "Oslo", "Ostrawa", "Ottawa"],
    "P": ["Pabianice", "Pacanów", "Piła", "Płock", "Prószków", "Przemyśl", "Pułtusk", "Palermo", "Paryż", "Pekin", "Perth",
          "Phoneix", "Porto", "Praga"],
    "R": ["Racibórz", "Radom", "Ruda Śląska", "Rybnik", "Rzeszów", "Rejkiawik", "Rio de Janeiro", "Rotterdam", "Ryga", "Rzym"],
    "S": ["Sandomierz", "Sanok", "Słupsk", "Sopot", "Sosnowiec", "Stalowa Wola", "Suwałki", "Szczecin", "Sacramento", "Saloniki",
          "Salt Lake City", "San Diego", "San Francisco", "Santiago", "Sao Paulo", "Sapporo",
          "Saragossa", "Sarajewo", "Seattle", "Sewila", "Sofia", "Sydney", "Sztokholm"],
    "T": ["Tarnobrzeg", "Tarnów", "Tczew", "Tomaszów Mazowiecki", "Toruń", "Tychy", "Tel Aviv", "Texas", "Tibilisi", "Tirana",
          "Tokyo", "Toronto", "Turyn", ],
    "U": ["Ujazd", "Ujście", "Uniejów", "Ustka", "Ustroń", "Ustrzyki Dolne", "Utrecht"],
    "V": ["Vancouver", "Virgina Beach", "Vitoria", "Vicenza", "Valencia", "Veracruz", "Verona"],
    "W": ["Wadowice", "Wałbrzych", "Warka", "Warszawa", "Wieliczka", "Władysławowo", "Wrocław", "Washington", "Wuhan",
          "Winnipeg", "West Bromwich", "Watford", "Wolfsburg"],
    "Z": ["Zakopane", "Zamość", "Zgierz", "Zabrze", "Złotoryja", "Zagrzeb", "Zadar", "Zurych", ]
    }

things = {}
plants = {}


player_points = []
bot_points = []

def countries_cities():
    print("GRA W PAŃSTWA I MIASTA\n")
    player()
    round = 0
    while round < 10:
        print('|| RUNDA', round + 1, "||\n")
        letter()
        print("CZAS START")
        countdown(1)
        countries_answer(player_name, letter_draw)
        cities_answer(player_name, letter_draw)
        print()
        print(player_name + ":", player_points)
        print("Komputer:", bot_points,"\n")
        print("===== WYNIKI PO RUNDZIE " + str(round + 1) + " =====")
        print(player_name + ":", sum(player_points))
        print("Komputer: ", sum(bot_points))
        print("===============================")

        round += 1
        print()
        if round == 10:
            print("KONIEC GRY!\n")


countries_cities()
winner(player_name)
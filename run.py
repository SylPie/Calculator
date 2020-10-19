def cyfry():
    liczba = 0
    lista = []
    while liczba != "=":
        liczba = input("Podaj liczbę lub wpisz '=' jesli chcesz przejsc do wyniku: ")
        if(liczba != "="):
            lista.append(float(liczba))
        else:
            break
    return lista

def doda():
    wynik = 0
    lista = cyfry()
    for liczby in lista:
        wynik = wynik + liczby
    print("\n --> Wynik dodawania liczb", lista, "to", wynik, "<-- \n")

def odej():
    wynik = 0
    lista = cyfry()
    for liczby in lista:
        wynik = liczby - wynik
    print("\n --> Wynik odejmowania liczb", lista, "to", wynik, "<-- \n")

def mnoz():
    wynik = 1
    lista = cyfry()
    for liczby in lista:
        wynik = wynik * liczby
    print("\n --> Wynik mnożenia liczb", lista, "to", wynik, "<-- \n")

def dzie():
    wynik = 1
    lista = cyfry()
    for liczby in lista:
        wynik = wynik / liczby
    print("\n --> Wynik dzielenia liczb", lista, "to", wynik, "<-- \n")

def pote():
    a = int(input("Podaj liczbę którą chcesz podnieść do potęgi: "))
    b = int(input("Podaj potęgę do której chcesz podnieść liczbę: "))
    print("\n --> Wynik potegowania to", a ** b, "<-- \n")
######################################################################
#                               PROGRAM                              #
######################################################################
print("""
|==========|
|KALKULATOR|
|==========| \n""")


while True:
    print("Co chcesz wykonać?")
    print("""
    1.DODAWANIE
    2.ODEJMOWANIE
    3.MNOŻENIE
    4.DZIELENIE
    5.POTĘGOWANIE
    6.ZAKOŃCZYĆ \n""")
    wybor = input("Podaj odpowiedni numer: ") 

    if(wybor == "1"):
        doda()
    elif(wybor == "2"):
        odej()
    elif(wybor == "3"):
        mnoz()
    elif(wybor == "4"):
        dzie()
    elif(wybor == "5"):
        pote()
    elif(wybor == "6"):
        break
    else:
        print("Wybrales zla liczbe!")
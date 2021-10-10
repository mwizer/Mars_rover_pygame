def funkcja(a, b):
    print(a ** b)  # wypisuje a do potęgi b


def polacz_slowo(s1, s2):
    return s1 + s2


zmienna = 8
slowo = "cos"
x = 2
y = 4
z = x + y  # + - * / ** -> dodawnaie, odejmowanie, mnożenie, dzielenie, potęgowanie
print(z)

# rodzaje list

x = (12, 23, 13)  # tuple / krotka

lista = [4, "koza", 17, 321]  # zwykła lista
lista.append("mango")  # dodanie na koniec listy
lista.pop()  # usunięcie ostatniej wartości
lista.pop(2)  # usunięcie wartości z podanego indesku
lista.remove("koza") # usunięcie wartości z listy

print(lista)

slownik = {"ssak": "delfin", "gad": "jaszczurki"}
slownik['płazy'] = "żaba" # dodanie nowego klucza z wartością
slownik['ssak'] = "Pepe Pan dziobak" # nadpisanie wartości dla klucza ssak, inną wartością
print(slownik['płazy'])
print(slownik)

# instrukcje warunkowe if
# < > == != <= >=   -> mniejsze, większe, równe, nierówne, mniejsze lub równe, wieksze lub równe

x = "cos"
y = "sin"
z = "cos"
if 4 < 17:
    print("To prawda, że 4<17")

    if x == y:
        print("Y to cos")
    elif x == z:
        print("z to cos")
    else:
        print('Nie ma cos')



# ~~~~~~ pętle while i for

stan = True
i = 0
while stan: # pętla while wykonuje się tak długo, jak przyjmuje prawdę
    i += 1
    print(i)
    if i == 10:
        # stan = False
        break  # zatrzymuje pętle

literki = ['a', 'b', 'c']

for i in literki: # pętla for przyjmuje kolejne wartości w podanej liście
    print(i)

for i in range(5, 10): # pętla for z otworzeniem listy liczb od 5 do 10
    print(i)


# przykłady funkcji

a, b = 10, 15
funkcja(2, 4) # wywołanie własnej funkcji
funkcja(a, b)

slowo = polacz_slowo(x, y)
print(slowo)
print(polacz_slowo(x, y))


# import zazwyczaj wstawiamy na samej górze pliku
# tutaj wstawiłem na dole, żeby pokazać różnicę pomiędzy różnymi sposobami importowania

import random

print(random.randint(0, 10))

from random import randint, random

print(randint(11, 20))

import random as rn

print(rn.randint(21, 30))

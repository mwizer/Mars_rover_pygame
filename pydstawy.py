def funkcja(a, b):
    print(a ** b)  # wypisuje a do potęgi b


def polacz_slowo(s1, s2):
    return s1 + s2


zmienna = 8
slowo = "cos"
x = 2
y = 4
z = x + y  # + - * / **
print(z)

x = (12, 23, 13)  # tuple / krotka

lista = [4, "koza", 17, 321]  # zwykła lista
lista.append("mango")  # dodanie na koniec listy
lista.pop()  # usunięcie ostatniej wartości
lista.pop(2)  # usunięcie wartości z podanego indesku
lista.remove("koza")

print(lista)

slownik = {"ssak": "delfin", "gad": "jaszczurki"}
slownik['płazy'] = "żaba"
slownik['ssak'] = "Pepe Pan dziobak"
print(slownik['płazy'])
print(slownik)

# < > == != <= >=

print()
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

stan = True
i = 0
while stan:
    i += 1
    print(i)
    if i == 10:
        # stan = False
        break  # zatrzymuje pętle

literki = ['a', 'b', 'c']

for i in literki:
    print(i)

for i in range(5, 10):
    print(i)

a, b = 10, 15
funkcja(2, 4)
funkcja(a, b)

slowo = polacz_slowo(x, y)
print(slowo)
print(polacz_slowo(x, y))

import random

print(random.randint(0, 10))

from random import randint, random

print(randint(11, 20))

import random as rn

print(rn.randint(21, 30))

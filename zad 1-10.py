

# zd.1
# Napisz funkcję odejmowanie(x,y), 
# która odejmuje od siebie podane argumenty,

# def odejmowanie(x, y):
#     roznica = x - y
#     return roznica

# print("Podaj pierwszą liczbę")
# pierwsza = int(input())
# print("Podaj drugą liczbę")
# druga = int(input())

# wynik = odejmowanie(pierwsza, druga)
# print("Wynikiem odejmowania tych liczb jest", wynik)


# zd. 2
# Napisz funkcję ostatni(lista), która zwraca ostatni element listy,


# def ostatni(lista):
#     for i in range(len(lista)):
#         return (lista[-1])
    
# lista = [1,2,3,4,5]

# wynik = ostatni(lista)
# print(wynik)



# zd. 3
# Napisz funkcję ogon(lista), która zwraca wszystko 
# poza pierwszym elementem listy


# def ogon(lista):
#     for i in range(len(lista)):
#         return(lista[1:])
    
# lista = [1,2,3,4,5]

# wynik = ogon(lista)
# print(wynik)


# zd 4
# Napisz funkcję dlugosc(x), która zwraca wielkość listy 
# (bez wykorzystania funkcji len)


# def dlugosc(lista):
#     ile = 0
#     for i in lista:
#         ile = ile + 1
#     return ile

# lista = [1,2,3,4,5,6,7]
# wynik = dlugosc(lista)
# print("Ta lista ma", wynik, "elementów")


# zd 5
# Napisz funkcję maksimum(lista), i minimum(lista), które zwracają
# maksymalny i minimalny element listy (bez wykorzystania
# funkcji min i max). Jeśli chcesz skorzystać 
# z len() skorzystaj z funkcji dlugosc() z poprzedniego zadania



# def maksimum(lista):
#     max = lista[0]
#     for i in lista:
#         if i > max:
#             max = i
#     return max

# def minimum(lista):
#     min = lista[0]
#     for i in lista:
#         if i < min:
#             min = i
#     return min


# lista = [1,2,3,4,5,6]
# wynik1 = minimum(lista)
# wynik2= maksimum(lista)
# print("Najmniejszy to", wynik1)
# print("Największy to", wynik2)

# zd 6
# Napisz funkcję nta(lista,n), która zwraca n-ty element listy,

# def nta(lista,n):
#     return(lista[n])

# lista = [1,2,3,4,5,6]
# print("Który element listy chcesz wyświetlić?")
# wybor = int(input())

# ktory = nta(lista, (wybor-1))
# print(ktory)


# zd.7
# Napisz funkcję alternatywa(x,y), która przyjmuje tylko 1 lub 0


# def alternatywa(x,y):
#     if x == 0 and y == 0:
#         wynik = 0
#     else:
#         wynik = 1
#     return wynik 
        

# print("wpisz wartość x")
# x = int(input())
# print("Wpisz wartość y")
# y = int(input())

# wynik = alternatywa(x,y)
# print(wynik)



# zd. 8
# Napisz funkcję koniunkcja(x,y), która przyjmuje tylko 1 lub 0,

# def koniungcja(x,y):
#     if x == 1 and y == 1:
#         wynik = 1
#     else:
#         wynik = 0
#     return wynik


# print("wpisz wartość x")
# x = int(input())
# print("Wpisz wartość y")
# y = int(input())

# wynik = koniungcja(x,y)
# print(wynik)




# zd9.
# Napisz funkcję implikacja(x,y), która przyjmuje tylko 1 lub 0,

# def implikacja(x,y):
#     if x == 1 and y == 0:
#         wynik = 0
#     else:
#         wynik = 1
#     return wynik


# print("wpisz wartość x")
# x = int(input())
# print("Wpisz wartość y")
# y = int(input())

# wynik = implikacja(x,y)
# print(wynik)



# zd 10
# Napisz funkcję, która oblicza kwadrat lub sześcian podanej liczby
# (powinniśmy wybrać móc wybrać opcję)


# def liczenie(odp, x):
#     if odp == "kwadrat":
#         return x*x
#     if odp == "sześcian":
#         return x * x * x
    

# print("Co chcesz zrobić")
# co = input()
    
# print("Wpisz liczbę")
# liczba = int(input())


# wynik = liczenie(co, liczba)
# print(wynik)



"""
Mulțimi (set)

Documentatia oficiala python: https://docs.python.org/3/tutorial/datastructures.html#sets.

O multime poate fi definita cu acolade {}

"""
import functools

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1)  # {1, 2, 3}
print(set2)  # {3, 4, 5}

multime1 = {'ana', 'maria', 'ion'}
multime_vida = {}
print(multime1)

"""
Multimile au următoarele caracteristici:

Sunt neordonate.
Elementele multimilor sunt unice. Elementele duplicat nu sunt permise.
O multime în sine poate fi modificata, dar elementele conținute în multime trebuie să fie de tip 
imuabil (obiectele imuabile sunt obiecte a căror valoare nu poate fi modificată după inițializare).
Multimile (sets) suportă operații matematice precum unirea, intersecția, diferența și diferența simetrică.
"""

set1.add(3)
print(set1)  # 3 exista deja in multime, deci nu avem valori duplicat

diferenta = set1 - set2  # elemente care exista in set 1 dar nu si in set 2
print(f"diferenta dintre {set1} si {set2}: {diferenta}")  # {1, 2}

unire = set1 | set2  # elemente care exista in set 1 sau in set 2
print(f"unirea dintre {set1} si {set2}: {unire}")  # {1, 2, 3, 4, 5}

intersectie = set1 & set2  # elemente care exista in set 1 si in set 2
print(f"intersectia dintre {set1} si {set2}: {intersectie}")  # {3}

diferenta_simetrica = set1 ^ set2  # elemente care exista in set 1 sau in set 2, dar nu in ambele
print(f"diferenta simetrica dintre {set1} si {set2}: {diferenta_simetrica}")  # {1, 2, 4, 5}

"""
Funcția len() returnează numărul de elemente dintr-o mulțime, iar operatorii in și not in pot fi folosiți pentru a testa apartenența.
"""

print(f"Numarul de elemente ale multimii {set1} este {len(set1)}")
print(f"Numarul 3 este in set1: {3 in set1}")
print(f"Numarul 7 este in set1: {7 in set1}")
print(f"Numarul 70 NU este in set1: {70 not in set1}")

"""
Cautarea in structura de date de tipul set este foarte performanta (nu doar in Python)
Exemplu:

"""


def exemplu_performanta_set():
    import random
    import time

    random_set = set(random.sample(range(10 ** 7), 10 ** 6))  # generam 1 milion de numere intr-un set
    random_list = list(random_set)  # convertim in lista

    search_number = random.choice(list(random_set))  # luam un numar random pe care sa-l cautam in cele doua structuri

    start_time = time.time()  # masuram timpul pentru set
    for i in range(0, 100):  # cautam de 100 de ori numarul in set
        if search_number in random_set:
            print(f"Numarul {search_number} exista in multime.", end=" ")
        else:
            print(f"Numarul {search_number} exista in multime.", end=" ")
    set_search_time = time.time() - start_time

    start_time = time.time()  # masuram timpul pentru list
    for i in range(0, 100):
        if search_number in random_list:
            print(f"Numarul {search_number} exista in lista.", end=" ")
        else:
            print(f"Numarul {search_number} exista in lista.", end=" ")
    list_search_time = time.time() - start_time

    print(f"\nSet search: {set_search_time} seconds.")
    print(f"List search: {list_search_time} seconds.")


# exemplu_performanta_set()


"""
Parcurgerea multimilor cu ajutorul functiei reduce()
"""


def afisare_multime(mul):
    functools.reduce(lambda acc, el: print(el, end=" "), mul, None)


afisare_multime({1, 2, 3, 4, 5})

"""
Suma elementelor unei multimi
"""


def suma(multime):
    return functools.reduce(lambda suma, el: suma + el, multime, 0)


print(f"\nsuma = {suma({2, 3, 4})}")

"""
1. Scrieți o funcție care ia ca parametru o mulțime și o tipărește pe o linie, între acolade { } și cu spatiu între elemente. 

Input: {1,2,3}; Output: {1,2,3}
"""
import sys


def afisare_multime_format(mul):
    print("{", end="")
    functools.reduce(lambda acc, el: print(el, end=" "), mul, None)
    sys.stdout.write('\b')
    print("}")


afisare_multime_format({1, 2, 3, 4, 5})

"""
2. Scrieți o funcție care ia o listă de perechi (de tip precizat) și returnează mulțimea elementelor de pe prima poziție din 
fiecare pereche (variante: a doua poziție; ambele poziții, dacă sunt de același tip).

Input: [(1,2), (3,4)]; Output: {1,3}
"""


def prime(lista):
    return functools.reduce(lambda multime, pereche: multime | {pereche[0]}, lista, set())


print(prime([(1, 2), (3, 4), (7, 9)]))


def prime_rec(lista):
    if len(lista) == 0:
        return set()
    else:
        a, b = lista[0]
        return {a} | prime_rec(lista[1:])


print(prime_rec([(1, 2), (3, 4), (7, 9)]))

"""
3. Implementați funcția standard filter care ia ca parametri o funcție booleană f și o mulțime s și returnează mulțimea
elementelor din s care satisfac funcția f.

Input: lambda x: x % 2 == 0, {1, 2, 3, 4}; Output: {2, 4}
"""


def filter(f, multime):
    return functools.reduce(lambda multime_noua, element: multime_noua | {element} if f(element) else multime_noua,
                            multime, set())


print(filter(lambda x: x % 2 == 0, {1, 2, 3, 4, 5, 6}))

# TODO: TEMA EX 4,5,6

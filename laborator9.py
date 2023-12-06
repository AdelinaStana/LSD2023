
"""
MULTIMI
Scrieți o funcție care primește o listă de șiruri de caractere și returnează o mulțime conținând literele unice din toate șirurile.

Input: ['apple', 'banana', 'cherry']; Output: {'a', 'b', 'c', 'e', 'h', 'l', 'n', 'p', 'r', 'y'}
"""
import functools


# TODO: exercitiu

def multime_caractere(lista_siruri):
    return functools.reduce(lambda multime, sir: multime | set(sir), lista_siruri, set())

def sir_to_mul(sir):
    if len(sir) > 0:
        return set(sir[0]) | sir_to_mul(sir[1:])
    else:
        return set()

def multime_caractere2(lista_siruri):
    return functools.reduce(lambda multime, sir: multime | sir_to_mul(sir), lista_siruri, set())

print(multime_caractere2(['apple', 'banana', 'cherry']))

"""
DICTIONARE
Scrieți o funcție care primește o funcție și un dicționar și returnează maximul valorilor funcției pentru toate intrările dicționarului.
Funcția-parametru are ca argumente cheia și valoarea unei intrări, și poate returna valori arbitrare. 
Folosiți reduce pentru parcurgere, și max (definită implicit pentru orice tip) pentru a 
compara valorile returnate de funcția parametru.
"""
# TODO: exercitiu


def maxim_dictionar(functie, dictionar):
    first = list(dictionar.items())[0]
    first = functie(first)
    return functools.reduce(lambda maxim, pereche: max(maxim, functie(pereche)), dictionar.items(), first)


def func(pereche):
    cheie, valoare = pereche
    return valoare * 2


print(maxim_dictionar(func, {'a': 5, 'b': 7, 'c': 1}))

"""
ARBORI

Definiti un arbore binar cu valori intregi pozitive, apoi scrieti o functie care:
 A. calculeaza suma tuturor nodurilor din arbore.
 B. calculeaza maximul tuturor nodurilor din arbore.
"""


cheie = "cheie"
stanga = "stanga"
dreapta = "dreapta"


nod1 = {cheie: 1, stanga: None, dreapta: None}  # frunza
nod7 = {cheie: 7, stanga: None, dreapta: None}  # frunza
nod4 = {cheie: 4, stanga: None, "dreapta": None}  # frunza
nod5 = {cheie: 15, stanga: nod4, dreapta: nod7}
radacina = {cheie: 2, stanga: nod1, dreapta: nod5}

# TODO: exercitiu

def suma(arbore):
    if arbore is not None:
        return arbore[cheie] + suma(arbore[stanga]) + suma(arbore[dreapta])
    else:
        return 0

print(suma(radacina))


def maxim(arbore):
    if arbore is not None:
        return max(arbore[cheie], maxim(arbore[stanga]), maxim(arbore[dreapta]))
    else:
        return 0

print(maxim(radacina))

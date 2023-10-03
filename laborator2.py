"""
Python tratează funcțiile ca orice valoare (int, float, ...) pe care ați întâlnit-o până acum.
Remarcați tipul pe care îl are variabila suma_numere.
"""


def suma(x, y):
    return x + y


suma_nr = suma

print(f"suma = {suma_nr(3, 4)}")
print(f"tipul functiei suma = {type(suma_nr)}")

"""
O funcție poate la randul său să fie trimisă ca parametru altei funcții. 
"""


def increment(x):
    return x + 1


def afisare(x):
    print(f"functia afisare cu valoarea {x}")


def aplica_functia(functie, valoare):
    return functie(valoare)


print(f"aplica_functia(increment, 5) = {aplica_functia(increment, 5)}")
print("aplica_functia(afisare, 5)", end=" -> ")  # pentru a evita ca functia print sa creeze o linie noua in consola,
# setati parametru end. Valoarea by default a parametrului 'end=' este '\n'
aplica_functia(afisare, 5)

"""
Funcții cu parametrii impliciți (default)

Python ne premite să declarăm funcții cu parametrii care au o valoare implicită. Astfel de funcții pot fi apelate și 
normal, dar și fără a da o valoare parametrului cu valoare implicită. În acest caz, parametrul va fi egal cu 
valoarea implicită. Mai jos se poate vedea un exemplu de funcție care are un parametru implicit.
"""


def test(a, b=0, c=0):
    print(f"a = {a}; b = {b}; c= {c}")


test(1, 2, 3)
test(3)
test(3, c=4)

"""
Exercitiu: Scrie o funcție numită 'calculeaza_suprafata' care calculează și returnează aria unui dreptunghi. 
Funcția ar trebui să primească doi parametri: lungime și lățime. Dacă parametrul pentru lățime nu este furnizat,
acesta ar trebui să aibă implicit valoarea 1.

Formula pentru calcularea ariei unui dreptunghi este lungime * lățime.
"""

# TODO: exercitiu

"""
Operatorii sunt funcții. Pentru a avea acces la operatori trebuie sa importam modulul operator. 

"""
import operator

print(f"operator.mul(5, 6) = {operator.mul(5, 6)}")
print(f"operator.add(5, 6) = {operator.add(5, 6)}")
print(f"tipul functiei operator.add = {type(operator.add)}")


def aplica_operator(operator, a, b):
    return operator(a, b)


print(f"aplica_operator(operator.add, 3, 7) = {aplica_operator(operator.add, 3, 7)}")
print(f"aplica_operator(operator.mul, 3, 7) = {aplica_operator(operator.mul, 3, 7)}")

"""
Exercitiu: Definiți o funcție numită 'calculeaza_si_afiseaza' care primește trei argumente: 
operator (o funcție), a și b. Această funcție ar trebui să aplice operatorul asupra lui a și b, 
să calculeze rezultatul și să-l afișeze pe ecran.
"""

# TODO: exercitiu

"""
Funcții anonime

Notația lambda argument : expresie definește în Python o funcție anonimă (funcție lambda). 
Aceasta este o expresie de tip funcție și poate fi deci folosită în alte expresii.
Putem evalua direct fără a fi nevoie să dăm întâi un nume funcției. 
"""
print("lambda:", end=": ")
print((lambda x: x + 5)(9))

lambda1 = lambda x: x + 5

print(lambda1(9))

"""
Una din cele mai simple și larg folosite operații cu funcții este compunerea lor,
în acest fel putem obține ușor funcții (prelucrări) complexe pornind de la funcții simple. 
"""


def f(x):
    return x + 3


def g(x):
    return x * 2


def comp(f, g):
    return lambda x: f(g(x))


fg = comp(f, g)

print(f"fg(2)={fg(2)}")

"""
Exercitiu: Scrieți o funcție numită 'compune' care primește o funcție f. 
Funcția compune ar trebui să returneze o nouă funcție care să aplice funcția f de 3 ori.
"""

# TODO: exercitiu

"""
Exercițiul 1: valori distincte

Scrieți o funcție cu trei parametri (de același tip oarecare), care returnează câte valori distincte există între 
argumentele primite (unul, două sau trei) și tipărește, după caz, un mesaj: "toate argumentele sunt distincte/egale"
sau "argumentele 1 și 2 (resp. 2 și 3, sau 1 și 3) sunt egale". Evitați pe cât posibil duplicarea de cod: 
pentru porțiuni de cod similare, creați (și apelați) o funcție care conține partea comună și are ca 
parametri valorile care diferă.
"""
# TODO: exercitiu

# TODO: TEMA EX 3, 4

'''
Arbore binar:
            2
           /\
          1  5
             /\
            4  7
'''

# ca sa nu mai scriem numele in ghilimele de fiecare data

cheie = "cheie"
stanga = "stanga"
dreapta = "dreapta"


nod1 = {cheie: 1, stanga: None, dreapta: None}  # frunza
nod7 = {cheie: 7, stanga: None, dreapta: None}  # frunza
nod4 = {cheie: 4, stanga: None, dreapta: None}  # frunza
nod5 = {cheie: 5, stanga: nod4, dreapta: nod7}
radacina = {cheie: 2, stanga: nod1, dreapta: nod5}

print(f"Arborele: {radacina}")
print(f"Stanga: {radacina[stanga]}")

'''
Afisarea in inordine: stanga - radacina - dreapta
Afisarea in preordine: radacina - stanga - dreapta
Afisare in postordine: stanga - dreapta - radacina
'''


def afisare_inordine(arbore):
    if arbore is not None:
        afisare_inordine(arbore[stanga])
        print(arbore[cheie], end=", ")
        afisare_inordine(arbore[dreapta])


print("Afisare inordine: ", end=" ")
afisare_inordine(radacina)  # ce se intampla daca print(f"Afisare inordine: {afisare_inordine(radacina)}", end=" ") ?

#TODO: Afisare preordine si postordine


def afisare_preordine(arbore):
    if arbore is not None:
        print(arbore[cheie], end=", ")
        afisare_preordine(arbore[stanga])
        afisare_preordine(arbore[dreapta])


print("Afisare preordine: ", end=" ")
afisare_preordine(radacina)


def afisare_postordine(arbore):
    if arbore is not None:
        afisare_postordine(arbore[stanga])
        afisare_postordine(arbore[dreapta])
        print(arbore[cheie], end=", ")


print("Afisare postordine: ", end=" ")
afisare_postordine(radacina)


"""
Calculare inaltime arbore binar.
"""

def inaltime(arbore):
    if arbore is not None:
        return 1 + max(inaltime(arbore[stanga]), inaltime(arbore[dreapta]))
    else:
        return 0

print("\ninaltime arbore : ", end="")
print(inaltime(radacina))

'''
Afisare nivel n din arbore binar.
'''


def afisare_nivel(arbore, nivel, nivel_curent=1):
    if arbore is not None:
        if nivel == nivel_curent:
            print(arbore[cheie], end= ", ")
        else:
            afisare_nivel(arbore[stanga], nivel, nivel_curent+1)
            afisare_nivel(arbore[dreapta], nivel, nivel_curent+1)
    else:
        print("", end="")

print("\nafisare nivel 2: ")
afisare_nivel(radacina, 2)

"""
Scrieti o functie care primeste ca parametru un arbore si construieste lista tuturor frunzelor arborelui.
"""

# TODO: exercitiu


def frunze(arbore):
    if arbore is not None:
        if arbore[stanga] is None and arbore[dreapta] is None:
            return [arbore[cheie]]
        else:
            return frunze(arbore[stanga]) + frunze(arbore[dreapta])
    else:
        return []


print(f"\nFrunze: {frunze(radacina)}")

"""
Scrieti o functie care primeste ca parametru un arbore si o functie conditie si returneaza multimea tuturor nodurilor care
respecta conditia data.
"""
# TODO: exercitiu


def arbore_conditie(arbore, functie):
    if arbore is not None:
        if functie(arbore[cheie]):
            return {arbore[cheie]} | arbore_conditie(arbore[stanga], functie) | arbore_conditie(arbore[dreapta], functie)
        else:
            return arbore_conditie(arbore[stanga], functie) | arbore_conditie(arbore[dreapta], functie)
    else:
        return set()


print(f"Conditie: {arbore_conditie(radacina, lambda x: x % 2 == 0)}")


# TODO: TEMA ex 1, 2, 4

"""

1. Scrieți o funcție care ia un arbore binar și returnează lista nodurilor care au un singur fiu. Ordinea nodurilor în 
listă va fi cea din traversarea în inordine.

2. Scrieți o funcție careia un arbore binar și returnează numărul total de noduri din arbore.

4. Tipărire indentată Scrieți o funcție care afișează un arbore binar de întregi în preordine, câte un nod pe linie, 
precedând valoarea din nod cu un număr de spații egal cu dublul adâncimii la care se află 
(câte două spații pentru fiecare nivel).
"""

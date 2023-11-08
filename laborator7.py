import functools
"""
Un dicționar constă dintr-o colecție de perechi cheie-valoare. Fiecare pereche cheie-valoare mapează cheia cu valoarea asociată.

Pentru a defini un dicționar prin folosirea unei liste, separate prin virgulă, de perechi cheie-valoare între acolade({}).
Două puncte (:) separă fiecare cheie de valoarea asociată.
"""
dictionar_capitale = {
    'Bucuresti': 'Romania',
    'Budapesta': 'Ungaria',
    'Chisinau': 'Moldova'
}

print(dictionar_capitale)  # {'Bucuresti': 'Romania', 'Budapesta': 'Ungaria', 'Chisinau': 'Moldova'}

"""
Dictionarele au urmatoarele caracterisitici:
o anumită cheie poate apărea într-un dicționar o singură dată, cheile duplicate nu sunt permise.
"""

dictionar_capitale['Bucuresti'] = 'RO'  # schimbarea valorii asociate unei chei
print(dictionar_capitale)

"""
Cheia trebuie să fie de un tip imuabil (de exemplu, nu poate sa fie o lista)
"""
# dictionar_capitale[['a']] = 'b' # "TypeError: unhashable type: 'list'"


"""
Accesarea tuturor elementelor din dictionar de tipul cheie-valoare se face cu ajutorul items().
Accesarea tuturor cheilor din dictionar se face cu ajutorul keys().
Accesarea tuturor valorilor din dictionar se face cu ajutorul values().

Lungimea unui dictionar (numarul de elemente) se obtine cu ajutorul functiei len
"""
print(f"elemente: {dictionar_capitale.items()}")  # dict_items([('Bucuresti', 'RO'), ('Budapesta', 'Ungaria'), ('Chisinau', 'Moldova')])
print(f"chei:{dictionar_capitale.keys()}")  # dict_keys(['Bucuresti', 'Budapesta', 'Chisinau'])
print(f"valori:{dictionar_capitale.values()}")  # dict_values(['RO', 'Ungaria', 'Moldova'])
print(f"lungimea:{len(dictionar_capitale)}")

elev_nota = {
    'Alex': 10,
    'Mihai': 9,
    'Ioana': 10
}

print(elev_nota.items())  # dict_items([('Alex', 10), ('Mihai', 9), ('Ioana', 10)])


def functie_suma(acc, elev):
    nume, nota = elev  # despachetam fiecare tuplu primit ca parametru (exemplu: ('Alex', 10))
    return acc + nota


def medie_elevi(dictionar):
    suma_note = functools.reduce(functie_suma, dictionar.items(), 0)
    return suma_note / len(dictionar)


def medie_elevi2(dictionar):
    suma_note = functools.reduce(lambda suma, elev:suma + elev[1], dictionar.items(), 0)
    return suma_note / len(dictionar)


print(f"Media elevilor {elev_nota} este {medie_elevi(elev_nota)}")
print(f"Media elevilor {elev_nota} este {medie_elevi2(elev_nota)}")


"""
Parcurgerea recursiva a dictionarelor. Pentru parcurgerea recursiva a dictionarelor, convertim dictionarul primit ca
 parametru in 'dict_items', apoi convertim 'dict_items' intr-o lista pe care o sa o parcurgem recursiv.
"""

def suma_recursiva(dict_list):
    if len(dict_list) > 0:
        nume, nota = dict_list[0]
        return nota + suma_recursiva(dict_list[1:])
    else:
        return 0


def medie_elevi_recursiva(dictionar):
    suma_note = suma_recursiva(list(dictionar.items()))
    return suma_note / len(dictionar)


print(f"Media elevilor {elev_nota} este {medie_elevi_recursiva(elev_nota)}")


"""
1. Scrieți o funcție care ia o listă de asociere cu perechi de tip (șir, întreg) și creează un dicționar în care 
fiecare șir e asociat cu suma tuturor valorilor cu care e asociat în listă.

Input: [('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]; Output: {'a': 10, 'b': 8, 'c': 2}
"""

# TODO: impreuna

def adauga_pereche_in_dictionar(dictionar, pereche):
    cheie, valoare = pereche
    if cheie in dictionar.keys():
        dictionar[cheie] = dictionar[cheie] + valoare
    else:
        dictionar[cheie] = valoare

    return dictionar

def convert_pair(lista_perechi):
    return functools.reduce(lambda dictionar, pereche: adauga_pereche_in_dictionar(dictionar, pereche) , lista_perechi, {} )

print(convert_pair( [('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]))

"""
2. Scrieți o funcție care ia o listă de șiruri de caractere și creează un dicționar în care fiecare șir e asociat cu 
numărul aparițiilor din listă.

Input: ["aaa", "bbb", "aabbb"]; Output: {'a': 5, 'b': 6}
"""

# TODO: exercitiu

def string_to_pairs(sirul):
    return functools.reduce(lambda acc, character: acc + [(character, 1)], list(sirul), [])


def nr_aparitii(lista_siruri):
    toate_perechile = functools.reduce(lambda lista_perechi, sir: lista_perechi + string_to_pairs(sir), lista_siruri, [])
    return convert_pair(toate_perechile)


print(nr_aparitii(["aaa", "bbb", "aabbb"]))

"""
3. Implementați cu ajutorul lui reduce funcția filter care creează un nou dicționar doar cu perechile din dicționarul 
dat care satisfac o funcție dată.

Input: dict: {'a': 5, 'b': 7, 'c': 1}; conditie: valoare >= 5; Output: {'a': 5, 'b': 7}
"""

# TODO: exercitiu

def adauga_pereche(pereche, dictionar):
    cheie, valoare = pereche
    dictionar[cheie] = valoare

    return dictionar

def filter_dict(dictionar, conditie):
    return functools.reduce(lambda dict_nou, pereche: adauga_pereche(pereche, dict_nou) if conditie(pereche[1]) else dict_nou, dictionar.items(), {})

print(filter_dict({'a': 5, 'b': 7, 'c': 1}, lambda x: x < 5))


# TEMA: ex 4,5,6

"""
4. Pentru tipurile colecție (liste, mulțimi, dicționare) e util să avem funcții care ne spun dacă există un element care satisface o anume condiție, respectiv dacă toate elementele satisfac condiția.
Implementați funcțiile exists și for_all pentru dicționare, folosind reduce. Ele iau ca parametru o funcție booleană de cheie și valoare (care exprimă condiția) și dicționarul în care se face căutarea. 

Input: dict: {'a': 5, 'b': 7, 'c': 1}; conditie: valoare >= 5; Output: exists: True, for_all: False

5. Implementați cu ajutorul lui reduce funcția map care construiește un dicționar în care toate valorile au fost transformate folosind o funcție dată ca parametru.

Input: {'a': 5, 'b': 7, 'c': 6}, lambda x: x + 1; Output: {'a': 6, 'b': 8, 'c': 7}

6. Scrieți o funcție care primește un dicționar de la șiruri la întregi și o listă de șiruri și returnează mulțimea tuturor valorilor din dicționar care corespund șirurilor din listă.

Input: {'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']; Output: {5, 7}

"""

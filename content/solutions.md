---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Toutes les solutions

(ex5.1_sol)=
## Exercice 5.1

```{code-cell}
def compte_prefix(s, prefix):
    compteur = 0
    for mot in s.split():
        if mot.startswith(prefix):
            compteur += 1
    return compteur

print(compte_prefix("la vie est belle au bord du lac", "la"))
```

(ex5.2_sol)=
## Exercice 5.2

```{code-cell}
def compte_sans_casse(s, mot_cible):
    compteur = 0
    mot_cible_minuscules = mot_cible.lower()
    for mot in s.split():
        if mot.lower() == mot_cible_minuscules:
            compteur += 1
    return compteur
```

(ex5.3_sol)=
## Exercice 5.3

```{code-cell}
def affiche_liste(liste):
    for i, elt in enumerate(listent):
        print(f"L'entier d'indice {i:2n} est |{elt:12n}|")

listent = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890, 12345678901]
affiche_liste(listent)
```

(ex6.1_sol)=
## Exercice 6.1

```{code-cell}
def compte_occurrences(s):
    d = {}
    for mot in s.split():
        d[mot] = d.get(mot, 0) + 1
    return d

print(compte_occurrences("la vie est belle c'est la vie"))
```

(ex6.2_sol)=
## Exercice 6.2

```{code-cell}
def somme_valeurs(d):
    s = 0
    for v in d.values():
        s += v
    return s

print(somme_valeurs({"a": 12, "zz": 1.5, "AAA": 0}))
```

(ex7.1_sol)=
## Exercice 7.1

```
import os

def nb_lignes(nom_fichier):
    n = 0
    fp = open(nom_fichier, "r")
    for ligne in fp.readlines():
        n += 1
    return n

def nb_lignes_repertoire(repertoire):
    for nom_fichier in os.listdir(repertoire):
        if nom_fichier.endswith(".txt"):
            nom_complet_fichier = os.path.join(repertoire, nom_fichier)
            n = nb_lignes(nom_complet_fichier)
            print(nom_complet_fichier, n)

nb_lignes_repertoire(".")
```

(ex7.2_sol)=
## Exercice 7.2

```
import os

def compte_fichiers(repertoire):
    compteur = 0
    for f in os.listdir(repertoire):
        if os.path.isfile(os.path.join(repertoire, f)):
            compteur += 1
    return compteur

print(compte_fichiers("."))
```

(ex8.1_sol)=
## Exercice 8.1

* Solution 1

```{code-cell}
import requests

def affiche_api(liste_userId):
    url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"
    contenu = requests.get(url)
    list_taches = contenu.json()
    for tache in list_taches:
        if tache["completed"] and tache["userId"] in liste_userId:
            print(tache)

affiche_api([1, 3])
```

* Solution 2 : en utilisant les paramètres d'URL

```{code-cell}
import requests

def affiche_api(liste_userId):
    url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"
    contenu = requests.get(url, params="completed=true")
    list_taches = contenu.json()
    for tache in list_taches:
        if tache["userId"] in liste_userId:
            print(tache)

affiche_api([1, 3])
```

(ex9.1_sol)=
## Exercice 9.1

```{code-cell}
def bissextile(annee):
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    elif annee % 400 == 0:
        return True
    else:
        return False

def nb_jours(mois, annee):
    if mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mois in [4, 6, 9, 11]:
        return 30
    else:  # Mois de février
        if bissextile(annee):
            return 29
        else:
            return 28

def lendemain(jour, mois, annee):
    if jour < nb_jours(mois, annee):
        return jour + 1, mois, annee
    elif mois < 12:  # Dernier jour du mois mais pas de l'année
        return 1, mois + 1, annee
    else:  # Dernier jour de l'année
        return 1, 1, annee + 1

# Tests de la fonction bissextile
print(bissextile(2004))  # True car divisible par 4 et non par 100
print(bissextile(1900))  # False car divisible par 100 et non par 400
print(bissextile(2000))  # True car divisible par 400
print(bissextile(1999))  # False car divisible ni par 4 ni par 100

# Tests de la fonction nb_jours
print(nb_jours(3, 2010))  # Mars : 31
print(nb_jours(4, 2010))  # Avril : 30
print(nb_jours(2, 2010))  # Février d'une année non bissextile : 28
print(nb_jours(2, 2004))  # Février d'une année bissextile : 29

# Tests de la fonction lendemain
print(lendemain(12, 2, 2010))  # 13, 2, 2010
print(lendemain(28, 2, 2010))  #  1, 3, 2010
print(lendemain(31, 12, 2010)) #  1, 1, 2011
```

(ex9.2_sol)=
## Exercice 9.2

```{code-cell}
def bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

print(bissextile(2004))  # True car divisible par 4 et non par 100
print(bissextile(1900))  # False car divisible par 100 et non par 400
print(bissextile(2000))  # True car divisible par 400
print(bissextile(1999))  # False car divisible ni par 4 ni par 100
```

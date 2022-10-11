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

(sec:numpy)=
# `numpy` et le calcul matriciel

Ce chapitre traite d'un module en particulier : le module `numpy`.
`numpy` est un raccourci pour _Numerical Python_ : cette librairie a donc pour vocation de fournir des outils de calcul numérique en Python.
Ce module permet donc de manipuler des vecteurs et des matrices (voire des tenseurs d'ordre supérieur).

Avant toute chose, vous devrez importer ce module :

```{code-cell} ipython3
import numpy as np
```

Vous remarquez ici que lors de l'import, le nom du module est renommé en `np` : il s'agit d'une habitude très répandue qui permet de ne pas surcharger inutilement la suite de votre code.

De plus, sachez que ce chapitre est très succinct et très loin de couvrir l'ensemble des fonctionnalités `numpy`, vous êtes donc fortement incités à utiliser [la documentation `numpy`](https://numpy.org/doc/stable/) pour trouver ce qui pourrait vous être utile pour votre usage.

## Tableaux multi-dimensionnels

Les tableaux multi-dimensionnels sont les objets de base en `numpy`.
On peut créer un vecteur comme suit :

```{code-cell} ipython3
vec = np.array([1, 4, 6, 7])

print(vec.ndim)
```

Dans ce chapitre, nous allons nous concentrer sur des vecteurs (`ndim = 1`, comme dans l'exemple ci-dessus) et des matrices (`ndim = 2`), mais il faut savoir que les tableaux multi-dimensionnels `numpy` peuvent stocker des tenseurs d'ordre quelconque.

Voici quelques exemples de manipulations élémentaires sur les tableaux `numpy` :

```{code-cell} ipython3
# Multiplication par une constante
print(2.5 * vec)

# Accès au type des données stockées
print(vec.dtype)

# Accès à la taille du vecteur
print(vec.shape)

# Définition d'une matrice
A = np.array([[0, 1], [2, 3]])
print(A)

# Transposition
print(A.T)
```

On remarque d'ores et déjà que les tableaux `numpy` ont un type associé. 
On ne pourra donc pas stocker dans un tableau `numpy` des données de types hétérogènes, comme on peut le faire dans le cas des listes Python par exemple.

## Produit matriciel et opérations "élément à élément"

Une chose importante à comprendre en `numpy` est que le produit par défaut entre deux tableaux est le produit élément à élément, et non pas le produit matriciel, comme on peut le voir dans cet exemple :

```{code-cell} ipython3
A = np.array([[0, 1], [2, 3]])
print(A)
```

```{code-cell} ipython3
I = np.array([[1, 0], [0, 1]])
print(I)
```

```{code-cell} ipython3
A * I
```

Il est toutefois possible d'effectuer un produit matriciel à l'aide de l'opérateur `@`, et alors on retrouve bien la propriété attendue qui est que le produit de `A` par la matrice identité retourne la matrice `A` :

```{code-cell} ipython3
A @ I
```

De même, lorsqu'on écrit `A ** 2`, on obtient l'élévation au carré de chacun des éléments de `A` et non pas le produit de `A` par lui-même :

```{code-cell} ipython3
A ** 2
```

```{code-cell} ipython3
A @ A
```

Les choses sont plus simples pour l'addition puisqu'il n'y a alors pas de confusion possible :

```{code-cell} ipython3
A + A
```

## Constructeurs de tableaux usuels

`numpy` permet de définir très simplement des tableaux remplis de 0, de 1, la matrice identité, ou des séquences de valeurs :

```{code-cell} ipython3
np.zeros((2, 3))  # (2, 3) est la taille de la matrice à produire
```

```{code-cell} ipython3
np.ones((2, 3))  # (2, 3) est la taille de la matrice à produire
```

```{code-cell} ipython3
np.eye(2)  # eye -> matrice identité
```

```{code-cell} ipython3
np.arange(10)  # arange -> équivalent de range pour les listes
```

```{code-cell} ipython3
# Vecteur de 11 valeurs espacées régulièrement entre 0 et 1
np.linspace(0, 1, 11)
```

## Accès à des sous-parties des tableaux

Comme pour les listes, les tableaux `numpy` peuvent être accédés par "tranches" (_slice_), comme dans les exemples suivants :

```{code-cell} ipython3
M = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
M
```

```{code-cell} ipython3
# Indices de ligne jusqu'à 2 (exclu)
# Indices de colonne à partir de 3 (inclus)
M[:2, 3:]
```

```{code-cell} ipython3
# Indices de colonne de 1 (inclus) à 3 (exclu)
# Tous les indices de colonne
M[1:3, :]
```

## Opérations élémentaires sur les tableaux

Une fois un tableau défini, on peut très facilement calculer :

* la somme de ses éléments :

```{code-cell} ipython3
np.sum(M)  # Peut aussi s'écrire M.sum()
```

* sa plus petite / plus grande valeur :

```{code-cell} ipython3
np.min(M)  # Peut aussi s'écrire M.min()
```

```{code-cell} ipython3
np.max(M)  # Peut aussi s'écrire M.max()
```

* la moyenne / l'écart-type de ses éléments :

```{code-cell} ipython3
np.mean(M)  # Peut aussi s'écrire M.mean()
```

```{code-cell} ipython3
np.std(M)  # Peut aussi s'écrire M.std()
```

Il est à noter que pour toutes ces opérations, deux syntaxes co-existent :

```{code-cell} ipython3
print(np.min(M))
print(M.min())
```

De plus, on peut également effectuer ces opérations ligne par ligne, ou colonne par colonne, comme ci-dessous :

```{code-cell} ipython3
# On somme sur les lignes (dimension numéro 0)
# Donc on obtient un résultat par colonne
M.sum(axis=0)
```

Enfin, on peut très facilement créer des masques binaires, tels que :

```{code-cell} ipython3
M > 5  # Vaut True à chaque position telle que l'élément correspondant dans M est > 5
```

Ce qui permet de compter simplement le nombre de valeurs d'un tableau vérifiant une condition :

```{code-cell} ipython3
np.sum(M > 5)
```

## Bonnes pratiques

Vous devrez, tant que faire se peut, utiliser les fonctions prédéfinies en `numpy` pour vos manipulations de tableaux multi-dimensionnels, plutôt que de recoder les opérations élémentaires.
Il est notamment fortement déconseillé de parcourir les valeurs d'un tableau `numpy` au sein d'une boucle, pour des raisons d'efficacité (autrement dit, de temps de calcul), comme illustré ci-dessous :

```{code-cell} ipython3
vec = np.ones((100, 10))
```

```{code-cell} ipython3
%%timeit  
# timeit permet de mesurer le temps d'exécution d'un morceau de code
vec.sum()
```

```{code-cell} ipython3
%%timeit  
# timeit permet de mesurer le temps d'exécution d'un morceau de code 
s = 0
for v in vec:  # À ne JAMAIS faire !
    s += v
```

## Exercices

```{admonition} Exercice 10.1
Calculez, en `numpy`, la somme des `n` premiers entiers, pour `n` fixé.
```

````{admonition} Solution
:class: tip, dropdown

```python
import numpy as np

n = 10
print(np.arange(n).sum())
```
````

````{admonition} Exercice 10.2
Supposons qu'on ait stocké dans le tableau suivant les notes reçues par 2 étudiants à 3 examens :
```python
notes = np.array(
  [[10, 12],
   [15, 16],
   [18, 12]]
)
```

1. Calculez la moyenne de chacun des deux étudiants.
2. Calculez le nombre de notes supérieures à 12 contenues dans ce tableau
````

````{admonition} Solution
:class: tip, dropdown

```python
import numpy as np

notes = np.array(
  [[10, 12],
   [15, 16],
   [18, 12]]
)

moyennes = notes.mean(axis=0)
n_notes_sup_12 = np.sum(notes > 12)
```
````
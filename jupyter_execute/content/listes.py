# Les listes

En Python, les listes stockent des séquences d'éléments.
Il n'est pas nécessaire que tous les éléments d'une liste soient du même type, même si dans les exemples que nous considérerons, ce sera souvent le cas.

On peut trouver des informations précieuses sur le sujet des listes dans l'aide en ligne de Python disponible à l'adresse : <https://docs.python.org/3/tutorial/datastructures.html>.

## Avant-propos : listes et itérables

Dans la suite, nous parlerons de listes, qui est un type de données bien spécifique en Python. Toutefois, une grande partie de notre propos pourra se transposer à l'ensemble des itérables en Python (c'est-à-dire l'ensemble des objets Python dont on peut parcourir les éléments un à un).

Il existe toutefois une différence majeure entre listes et itérables : nous verrons dans la suite de ce chapitre que l'on peut accéder au $i$-ème élément d'une liste simplement, alors que ce n'est généralement pas possible pour un itérable (pour ce dernier, il faudra parcourir l'ensemble de ses éléments et s'arrêter lorsque l'on est effectivement rendu au $i$-ème).

Toutefois, si l'on a un itérable `iterable`, il est possible de le transformer en liste simplement à l'aide de la fonction `list` :

```
l = list(iterable)
```

## Création de liste

Pour créer une liste contenant des éléments définis (par exemple la liste contenant les entiers 1, 5 et 7), il est possible d'utiliser la syntaxe suivante :

liste = [1, 5, 7]

De la même façon, on peut créer une liste vide (ne contenant aucun élément) :

liste = []
print(len(liste))

On voit ici la fonction `len` qui retourne la taille d'une liste passée en argument (ici 0 puisque la liste est vide).

Toutefois, lorsque l'on souhaite créer des listes longues (par exemple la liste des 1000 premiers entiers), cette méthode est peu pratique.
Heureusement, il existe des fonctions qui permettent de créer de telles listes.
Par exemple, la fonction `range(a, b)` retourne un itérable contenant les entiers de `a` (inclus) à `b` (exclu) :

l = range(1, 10)     # l = [1, 2, 3, ..., 9]
l = range(10)        # l = [0, 1, 2, ..., 9]
l = range(0, 10, 2)  # l = [0, 2, 4, ..., 8]

On remarque que, si l'on ne donne qu'un argument à la fonction `range`, l'itérable retourné débute à l'entier 0.
Si, au contraire, on passe un troisième argument à la fonction `range`, cet argument correspond au pas utilisé entre deux éléments successifs.

## Accès aux éléments d'une liste

Pour accéder au $i$-ème élément d'une liste, on utilise la syntaxe :

```
l[i]
```

Attention, toutefois, le premier indice d'une liste est 0, on a donc :

l = [1, 5, 7]
print(l[1])

print(l[0])

On peut également accéder au dernier élément d'une liste en demandant l'élément d'indice `-1` :

l = [1, 5, 7]
print(l[-1])

print(l[-2])

print(l[-3])

De la même façon, on peut accéder au deuxième élément en partant de la fin _via_ l'indice `-2`, _etc._

Ainsi, pour une liste de taille $n$, les valeurs d'indice valides sont les entiers compris entre $-n$ et $n - 1$ (inclus).

Il est également à noter que l'accès aux éléments d'une liste peut se faire en lecture (lire l'élément stocké à l'indice `i`) comme en écriture (modifier l'élément stocké à l'indice `i`) :

l = [1, 5, 7]
print(l[1])

l[1] = 2
print(l)

Enfin, on peut accéder à une sous-partie d'une liste à l'aide de la syntaxe `l[d:f]` où  `d` est l'indice de début et `f` est l'indice de fin (exclu). Ainsi, on a :

l = [1, 5, 7, 8, 0, 9, 8]
print(l[2:4])

Lorsque l'on utilise cette syntaxe, si l'on omet l'indice de début, la sélection commence au début de la liste et si l'on omet l'indice de fin, elle s'étend jusqu'à la fin de la liste :

l = [1, 5, 7, 8, 0, 9, 8]
print(l[:3])

print(l[5:])

## Parcours d'une liste

Lorsque l'on parcourt une liste, on peut vouloir accéder :

* aux éléments stockés dans la liste uniquement ;
* aux indices de la liste uniquement (même si c'est rare) ;
* aux indices de la listes et aux éléments associés.

Ces trois cas de figure impliquent trois parcours de liste différents, décrits dans ce qui suit.

**Attention.**
Quel que soit le parcours de liste utilisé, il est fortement déconseillé de supprimer ou d'insérer des éléments dans une liste pendant le parcours de celle-ci.

### Parcours des éléments

Pour parcourir les éléments d'une liste, on utilise une boucle `for` :

l = [1, 5, 7]
for elem in l:
    print(elem)

Dans cet exemple, la variable `elem` va prendre successivement pour valeur chacun des éléments de la liste.

### Parcours par indices

Pour avoir accès aux indices (positifs) de la liste, on devra utiliser un subterfuge.
On sait que les indices d'une liste sont les entiers compris entre 0 (inclus) et la taille de la liste (exclu).
On va donc utiliser la fonction `range` pour cela :

l = [1, 5, 7]
n = len(l)  # n = 3 ici
for i in range(n):
    print(i)

### Parcours par éléments et indices

Dans certains cas, enfin, on a besoin de manipuler simultanément les indices d'une listes et les éléments associés.
Cela se fait à l'aide de la fonction `enumerate` :

l = [1, 5, 7]
for i, elem in enumerate(l):
    print(i, elem)

On a donc ici une boucle `for` pour laquelle, à chaque itération, on met à jour les variables `i` (qui contient l'indice courant) et `elem` (qui contient l'élément se trouvant à l'indice `i` dans la liste `l`).

Pour tous ces parcours de listes, il est conseillé d'utiliser des noms de variables pertinents, afin de limiter les confusions dans la nature des éléments manipulés. Par exemple, on pourra utiliser `i` ou `j` pour noter des indices, mais on préfèrera `elem` ou `val` pour désigner les éléments de la liste.

### Exercice

**Exercice 4.1**
Écrivez une fonction en Python qui permette de calculer l'argmax d'une liste, c'est-à-dire l'indice auquel est stockée la valeur maximale de la liste.

## Manipulations de listes

Nous présentons dans ce qui suit les opérations élémentaires de manipulation de listes.

### Insertion d'élément

Pour insérer un nouvel élément dans une liste, on peut :

* rajouter un élément à la fin de la liste à l'aide de la méthode `append` ;
* insérer un élément à l'indice `i` de la liste à l'aide de la méthode `insert`.

Comme vous pouvez le remarquer, il est ici question de méthodes et non plus de fonctions.
Pour l'instant, sachez que les méthodes sont des fonctions spécifiques à certains objets, comme les listes par exemples.
L'appel de ces méthodes est un peu particulier, comme vous pouvez le remarquer dans ce qui suit :

l = [1, 5, 7]
l.append(2)
print(l)

l.insert(2, 0)  # insère la valeur 0 à l'indice 2
print(l)

### Suppression d'élément

Si l'on souhaite, maintenant, supprimer un élément dans une liste, deux cas de figures peuvent se présenter.
On peut souhaiter :

* supprimer l'élément situé à l'indice `i` dans la liste, à l'aide de la méthode `pop` ;
* supprimer la première occurrence d'une valeur donnée dans la liste à l'aide de la méthode `remove`.

l = [1, 5, 7]
l.pop(1)  # l'élément d'indice 1 est le deuxième élément de la liste !
print(l)

l.pop()  # par défaut, supprime le dernier élément de la liste
print(l)

l = [7, 5, 1]
l.remove(1) # supprime la première occurence de 1 dans la liste
print(l)

On peut noter que la méthode `pop` retourne la valeur supprimée, ce qui peut s'avérer utile :

l = [1, 5, 7]
v = l.pop(1)
print(v)

print(l)

### Recherche d'élément

Pour trouver l'indice de la première occurrence d'une valeur dans une liste, on utilisera la méthode `index` :

l = [1, 5, 7]
print(l.index(7))

Si l'on ne cherche pas à connaître la position d'une valeur dans une liste mais simplement à savoir si une valeur est présente dans la liste, on peut utiliser le mot-clé `in` :

l = [1, 5, 7]
if 5 in l:
    print("5 est dans l")

### Création de listes composites

On peut également concaténer deux listes (c'est-à-dire mettre bout à bout leur contenu) à l'aide de l'opérateur `+` :

l1 = [1, 5, 7]
l2 = [3, 4]
l = l1 + l2
print(l)

Dans le même esprit, l'opérateur `*` peut aussi être utilisé pour des listes :

l1 = [1, 5]
l2 = 3 * l1
print(l2)

Bien entendu, vu le sens de cet opérateur, on ne peut multiplier une liste que par un entier.

### Tri de liste

Enfin, on peut trier les éléments contenus dans une liste à l'aide de la fonction `sorted` :

l = [4, 5, 2]
l2 = sorted(l)
print(l2)

### Exercices

**Exercice 4.2**
Écrivez une fonction qui prenne deux listes en entrée et retourne l'intersection des deux listes (c'est-à-dire une liste contenant tous les éléments présents dans les deux listes).

**Exercice 4.3**
Écrivez une fonction qui prenne deux listes en entrée et retourne l'union des deux listes (c'est-à-dire une liste contenant tous les éléments présents dans au moins une des deux listes) sans doublon.

## Copie de liste

Pour la plupart des variables, en Python, la copie ne pose pas de problème :

a = 12
b = a
a = 5
print(a, b)

Cela ne se passe pas de la même façon pour les listes.
En effet, si `l` est une liste, lorsque l'on écrit :

l2 = l

on ne recopie pas le contenu de `l` dans `l2`, mais on crée une variable `l2` qui va "pointer" vers la même position dans la mémoire de votre ordinateur que `l`.
La différence peut sembler mince, mais cela signifie que si l'on modifie `l` même après l'instruction `l2 = l`, la modification sera répercutée sur `l2` :

l = [1, 5, 7]
l2 = l
l[1] = 2
print(l, l2)

Lorsque l'on souhaite éviter ce comportement, il faut effectuer une copie explicite de liste, à l'aide par exemple de la fonction `list` :

l = [1, 5, 7]
l2 = list(l)
l[1] = 2
print(l, l2)

## Bonus : listes en compréhension

Il est possible de créer des listes en filtrant et/ou modifiant certains éléments d'autres listes ou itérables.
Supposons par exemple que l'on souhaite créer la liste des carrés des 10 premiers entiers naturels.
Le code qui suit présente deux façons équivalentes de créer une telle liste :

# Façon "classique"
l = []
for i in range(10):
    l.append(i ** 2)
print(l)

# En utilisant les listes en compréhension
l = [i ** 2 for i in range(10)]
print(l)

On remarque que la syntaxe de liste en compréhension est plus compacte.
On peut également appliquer un filtre sur les éléments de la liste de départ (ici `range(10)`) à considérer à l'aide du mot-clé `if` :

l = [i ** 2 for i in range(10) if i % 2 == 0]
print(l)

Ici, on n'a considéré que les entiers pairs.
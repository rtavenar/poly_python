# Les chaînes de caractères

Nous nous intéressons maintenant à un autre type de données particulier du langage Python : les chaînes de caractères (type `str`).
Pour créer une chaîne de caractères, il suffit d'utiliser des guillemets, simples ou doubles (les deux sont équivalents) :

s1 = "abc"
s2 = 'bde'

Comme pour les listes (et peut-être même plus encore), il est fortement conseillé de se reporter à l'aide en ligne dédiée lorsque vous avez des doutes sur la manipulation de chaînes de caractères :
<https://docs.python.org/3/library/stdtypes.html#string-methods>

## Conversion d'une chaîne en nombre

Si une chaîne de caractères représente une valeur numérique (comme la chaîne `"10.2"`{.haskell} par exemple), on peut la transformer en un entier ou un nombre à virgule, afin de l'utiliser ensuite pour des opérations arithmétiques. On utilise pour cela les fonctions de conversion, respectivement `int` et `float`.

s = '10.2'
f = float(s)
print(f)

print(f == s)

print(f + 2)

s = '10'
i = int(s)
print(i)

print(i == s)

print(i - 1)

## Analogie avec les listes

Les chaînes de caractères se manipulent en partie comme des listes.
On peut ainsi obtenir la taille d'une chaîne de caractères à l'aide de la fonction `len`, ou accéder à la $i$-ème lettre d'une chaîne de caractères avec la notation `s[i]`.
Comme pour les listes, il est possible d'indicer une chaîne de caractères en partant de la fin, en utilisant des indices négatifs :

s = "abcdef"
print(len(s))

print(s[0])

print(s[-1])

De même, on peut sélectionner des sous-parties de chaînes de caractères à partir des indices de début et de fin de la sélection. Comme pour les listes, l'indice de fin correspond au premier élément exclu de la sélection :

s = "abcdef"
print(s[2:4])

Comme pour les listes, on peut concaténer deux chaînes de caractères à l'aide de l'opérateur `+` ou répéter une chaîne de caractères avec l'opérateur `*` :

s = "ab" + ('cde' * 3)
print(s)

On peut également tester la présence d'une sous-chaîne de caractères dans une chaîne avec le mot-clé `in` :

s = "abcde"
print("a" in s)

print("bcd" in s)

print("bCd" in s)

**Attention.**
Toutefois, l'analogie entre listes et chaînes de caractères est loin d'être parfaite.
Par exemple, on peut accéder au $i$-ème élément d'une chaîne de caractères en lecture, mais pas en écriture.
Si `s` est une chaîne de caractères, on ne peut pas exécuter `s[2] = "c"` par exemple.

## Principales méthodes de la classe `str`

La liste de méthodes de la classe `str` qui suit n'est pas exhaustive, il est conseillé de consulter l'aide en ligne de Python pour plus d'informations.

* `ch.count(sub)`: Retourne le nombre d'occurrences de `sub` dans `ch`
* `ch.endswith(suffix)`: Retourne `True` si `ch` se termine par `suffix`
* `ch.startswith(prefix)`: Retourne `True` si `ch` commence par `prefix`
* `ch.find(sub)`: Retourne l'indice du début de la première occurrence de `sub` dans `ch`
* `ch.rfind(sub)`: Retourne l'indice du début de la dernière occurrence de `sub` dans `ch`
* `ch.islower()`: Retourne `True` si `ch` est constituée uniquement de caractères minuscules
* `ch.isupper()`: Retourne `True` si `ch` est constituée uniquement de caractères majuscules
* `ch.isnumeric()`: Retourne `True` si `ch` est constituée uniquement de chiffres
* `ch.lower()`: Retourne la version minuscule de `ch`
* `ch.upper()`: Retourne la version majuscule de `ch`
* `ch.replace(old, new)`: Retourne une copie de `ch` dans laquelle toutes les occurrences de `old` ont été remplacées par `new`
* `ch.split(sep=None)`: Retourne une liste contenant des morceaux de `ch` découpée à chaque occurrence de `sep` (par défaut, la chaîne est decoupée à chaque espace ou retour à la ligne)
* `ch.strip()`: Retourne une version "nettoyée" de `ch` dans laquelle on a enlevé tous les espaces en début et en fin de chaîne
* `ch.format(...)`: Remplace les caractères `{}` dans la chaîne `ch` par le contenu des variables passées en argument (voir [ici](#anchor-format) pour un exemple d'utilisation)

## Exercices

**Exercice 5.1**
Écrivez une fonction qui prenne en argument deux chaînes de caractères `s` et `prefix` et retourne le nombre de mots de la chaîne `s` qui débutent par la chaîne `prefix`.

**Exercice 5.2**
Écrivez une fonction qui prenne en argument deux chaînes de caractères `s` et `mot_cible` et retourne le nombre d'occurrences du mot `mot_cible` dans la chaîne `s` en ne tenant pas compte de la casse.
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

# Les chaînes de caractères

Nous nous intéressons maintenant à un autre type de données particulier du langage Python : les chaînes de caractères (type `str`).
Pour créer une chaîne de caractères, il suffit d'utiliser des guillemets, simples ou doubles (les deux sont équivalents) :

```{code-cell}
s1 = "abc"
s2 = 'bde'
```

Comme pour les listes (et peut-être même plus encore), il est fortement conseillé de se reporter à l'aide en ligne dédiée lorsque vous avez des doutes sur la manipulation de chaînes de caractères :
<https://docs.python.org/3/library/stdtypes.html#string-methods>

## Conversion d'une chaîne en nombre

Si une chaîne de caractères représente une valeur numérique (comme la chaîne `"10.2"` par exemple), on peut la transformer en un entier ou un nombre à virgule, afin de l'utiliser ensuite pour des opérations arithmétiques. On utilise pour cela les fonctions de conversion, respectivement `int` et `float`.

```{code-cell}
s = '10.2'
f = float(s)
print(f)
```

```{code-cell}
print(f == s)
```

```{code-cell}
print(f + 2)
```

```{code-cell}
s = '10'
i = int(s)
print(i)
```

```{code-cell}
print(i == s)
```

```{code-cell}
print(i - 1)
```

## Analogie avec les listes

Les chaînes de caractères se manipulent en partie comme des listes.
On peut ainsi obtenir la taille d'une chaîne de caractères à l'aide de la fonction `len`, ou accéder à la $i$-ème lettre d'une chaîne de caractères avec la notation `s[i]`.
Comme pour les listes, il est possible d'indicer une chaîne de caractères en partant de la fin, en utilisant des indices négatifs :

```{code-cell}
s = "abcdef"
print(len(s))
```

```{code-cell}
print(s[0])
```

```{code-cell}
print(s[-1])
```

De même, on peut sélectionner des sous-parties de chaînes de caractères à partir des indices de début et de fin de la sélection. Comme pour les listes, l'indice de fin correspond au premier élément exclu de la sélection :

```{code-cell}
s = "abcdef"
print(s[2:4])
```

Comme pour les listes, on peut concaténer deux chaînes de caractères à l'aide de l'opérateur `+` ou répéter une chaîne de caractères avec l'opérateur `*` :

```{code-cell}
s = "ab" + ('cde' * 3)
print(s)
```

On peut également tester la présence d'une sous-chaîne de caractères dans une chaîne avec le mot-clé `in` :

```{code-cell}
s = "abcde"
print("a" in s)
```

```{code-cell}
print("bcd" in s)
```

```{code-cell}
print("bCd" in s)
```

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
* `ch.format(...)`: Remplace les caractères `{}` dans la chaîne `ch` par le contenu des variables passées en argument

## Formatage des chaînes de caractères

Lorsque l'on souhaite ajouter, dans une chaîne de caractères, du contenu stocké dans une variable, on pourra utiliser la méthode format listée ci-dessus.

Commençons par un exemple :

```{code-cell}
age = 12
prenom = "Micheline"
s = "{} a {} ans".format(prenom, age)
print(s)
```

Ainsi, la méthode `.format()` recherche dans la chaîne de caractères les `{}` et les remplace par les valeurs des variables fournies.
Il est possible de maîtriser plus finement la mise en forme de ces variables, et même de les nommer (ce qui peut s'avérer très utile si la chaîne de caractères est longue et inclut de nombreuses variables).

Voici quelques exemples :

```{code-cell}
age_enfant = 12
prenom_enfant = "Micheline"
s = "{prenom} a {age} ans".format(prenom=prenom_enfant, age=age_enfant)
print(s)
```

```{code-cell}
age_enfant = 12
prenom_enfant = "Micheline"
s = "{prenom} a {age:.3f} ans".format(prenom=prenom_enfant, age=age_enfant)
print(s)
```


Vous trouverez une présentation plus exhaustive de ces questions dans la [documentation Python sur ce point](https://docs.python.org/fr/3.5/library/string.html#format-string-syntax).

### Pour aller plus loin : les f-strings

````{margin}
```{admonition} Pour info
  :class: tip
Les f-strings existent en Python depuis la version 3.6.
```
````

Il existe une autre façon de mettre en forme les chaînes de caractères, qui consiste en l'utilisation de f-strings.
Pour définir une f-string, il suffit d'ajouter un f avant la chaîne de caractères :

```{code-cell}
s = f"Ceci est une f-string"
print(s)
```

Jusqu'ici, rien de bien révolutionnaire.
Mais ces f-strings deviennent fort pratiques dès lors que l'on souhaite ajouter des données issues de variables précédemment définies :

```{code-cell}
age = 12
prenom = "Micheline"
s = f"{prenom} a {age} ans"
print(s)
```

Cette syntaxe est beaucoup plus concise que ce que l'on pouvait avoir en utilisant la méthode `.format()`.
On peut même effectuer des calculs à la volée dans les f-strings :

```{code-cell}
age_chat = 12
s = f"Ce chat a {age_chat} ans, ce qui lui fait {age_chat * 6} ans en âge équivalent humain"
print(s)
```



## Exercices

**Exercice 5.1**
Écrivez une fonction qui prenne en argument deux chaînes de caractères `s` et `prefix` et retourne le nombre de mots de la chaîne `s` qui débutent par la chaîne `prefix`.

**Exercice 5.2**
Écrivez une fonction qui prenne en argument deux chaînes de caractères `s` et `mot_cible` et retourne le nombre d'occurrences du mot `mot_cible` dans la chaîne `s` en ne tenant pas compte de la casse.

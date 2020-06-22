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

# Les dictionnaires

Comme une liste, un dictionnaire est une collection de données.
Mais, à la différence des listes, les dictionnaires ne sont pas ordonnés (ou, tout du moins, ils le sont dans un ordre qui ne nous est pas naturel).
Chaque entrée dans un dictionnaire est une association entre une **clé** (équivalente à un indice pour une liste) et une **valeur**.
Alors que les indices d'une liste sont forcément les entiers compris entre 0 et la taille de la liste exclue, les clés d'un dictionnaire sont des valeurs quelconques, la seule contrainte étant qu'on ne peut pas avoir deux fois la même clé dans un dictionnaire.
Notamment, ces clés ne sont pas nécessairement des entiers, on utilisera en effet souvent des dictionnaires lorsque l'on souhaite stocker des valeurs associées à des chaînes de caractères (qui seront les clés du dictionnaire).

Pour définir un dictionnaire par ses paires clé-valeur en Python, on peut utiliser la syntaxe suivante :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
print(mon_dico)
```

On remarque ici que l'ordre dans lequel on a entré des paires clé-valeur n'est pas conservé lors de l'affichage.

## Modification du contenu d'un dictionnaire

Pour modifier la valeur associée à une clé d'un dictionnaire, la syntaxe est similaire à celle utilisée pour les listes, en remplaçant les indices par les clés :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
mon_dico["a"] = 1000
print(mon_dico)
```

De même, on peut créer une nouvelle paire clé-valeur en utilisant la même syntaxe :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
mon_dico["c"] = -1
print(mon_dico)
```

Enfin, pour supprimer une paire clé-valeur d'un dictionnaire, on utilise le mot-clé `del` :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
del mon_dico["a"]
print(mon_dico)
```

## Lecture du contenu d'un dictionnaire

Pour lire la valeur associée à une clé du dictionnaire, on peut utiliser la même syntaxe que pour les listes :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
print(mon_dico["a"])
```

Par contre, si la clé demandée n'existe pas, cela génèrera une erreur.
Pour éviter cela, on peut utiliser la méthode `get` qui permet de définir une valeur par défaut à retourner si la clé n'existe pas :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
print(mon_dico.get("a", 0))
```

```{code-cell}
print(mon_dico.get("b", 0))
```

## Parcours d'un dictionnaire

Pour parcourir le contenu d'un dictionnaire, il existe, comme pour les listes, trois possibilités.

### Parcours par valeurs

Si l'on souhaite uniquement accéder aux valeurs stockées dans le dictionnaire, on utilisera la méthode `values` :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
for val in mon_dico.values():
    print(val)
```

### Parcours par clés

Si l'on souhaite uniquement accéder aux clés stockées dans le dictionnaire, on utilisera la méthode `keys` :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
for cle in mon_dico.keys():
    print(cle)
```

### Parcours par couples clés/valeurs

Si l'on souhaite accéder simultanément aux clés stockées dans le dictionnaire et aux valeurs associées, on utilisera la méthode `items` :

```{code-cell}
mon_dico = {"a" : 123, "z" : 7, "bbb" : None}
for cle, valeur in mon_dico.items():
    print(cle, valeur)
```

## Exercices

````{admonition} **Exercice 6.1**
Écrivez une fonction qui compte le nombre d'occurrences de chacun des mots d'une chaîne de caractères et retourne le résultat sous forme de dictionnaire :

```
# [...]
print(compte_occurrences("la vie est belle c'est la vie"))
# [Sortie] {"c'est": 1, 'la': 2, 'belle': 1, 'est': 1, 'vie': 2}
```

[{ref}`Corrigé <ex6.1_sol>`]
````

```{admonition} **Exercice 6.2**
Écrivez une fonction qui retourne la somme des *valeurs* d'un dictionnaire fourni en argument.

[{ref}`Corrigé <ex6.2_sol>`]
```

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

# Les _sets_ et les _tuples_

Nous avons vu jusqu'à présent deux types qui permettent de stocker des collections de données : les listes et les dictionnaires.
Dans ce chapitre, nous nous intéressons à deux autres structures qui permettent elles aussi de stocker des collections : les _sets_ et les _tuples_.

## Les _tuples_

Commençons par les tuples, car vous en avez déjà manipulé sans même vous en rendre compte.
Prenons l'exemple de la fonction suivante :

```{code-cell}
def comment_tu_tappelles():
    prenom = "Pierre"
    nom = "Lapin"
    return prenom, nom
```

Vous remarquez que cette fonction retourne deux valeurs, séparées par une virgule.
Ces deux valeurs forment un _tuple_.

Pour définir un nouveau tuple, on peut écrire :

```{code-cell}
# Les parenthèses sont facultatives
a = 1, 2, 3
b = ("a", "b", "c")

print(a)
print(b)
```

Un _tuple_ ressemble en de nombreux points à une liste, mais il est impossible de modifier les données d'un _tuple_ une fois défini.
Il n'est donc pas possible d'ajouter / supprimer des données (comme on le faisait avec `l.append()` ou `l.remove()` pour les listes par exemple).
Il n'est pas non plus possible de modifier un élément d'un _tuple_ (si `a` est un _tuple_, on ne peut donc pas écrire `a[0] = 5` comme on l'aurait fait pour une liste).

## Les _sets_

Les _sets_, pour leur part, permettent de stocker des ensemble de valeurs, sans ordre et sans répétition.
On peut ainsi voir les _sets_ comme des dictionnaires qui auraient des clés, mais pas de valeurs associées.
Cela fait d'ailleurs écho à la syntaxe utilisée en Python pour définir un set, qui utilise les accolades, comme pour les dictionnaires :

```{code-cell}
c = {1, 2, 3}
d = {"truc", "machin", "chose"}

print(c)
print(d)
```

Vous pouvez remarquer, dans l'exemple ci-dessus, que, comme pour les dictionnaires, l'ordre dans lequel les éléments sont déclarés dans un _set_ n'est pas préservé lors de l'affichage.

Puisque les _sets_ ne peuvent pas stocker de valeurs répétées, lorsqu'on convertit une liste en set, on obtient une liste sans doublon (mais on perd la notion d'ordre) :

```{code-cell}
ma_liste = ["truc", "machin", "truc", "chose", "machin", "machin"]
mon_set = set(ma_liste)  # Convertit la liste en set

print(mon_set)
```

Une fois un _set_ défini, on ne peut plus modifier les valeurs qu'il contient, mais on peut lui supprimer / ajouter des valeurs :

```{code-cell}
mon_set = {"truc", "machin", "chose"}

# Ajouter un élément
mon_set.add("bidule")

# Supprimer un élément
mon_set.remove("truc")

print(mon_set)
```

## Tableau récapitulatif

Voici un tableau de ce qu'on peut / ne peut pas faire avec l'un ou l'autre des types de base pour les collections de données :

|   | Listes | Dictionnaires | _Sets_ | _Tuples_ |
|---|---|---|---|---|
| Définition | `[1, 4]` | `{"a": 1, "b": 4}` | `(1, 4)` | `{1, 4}` |
| Possibilité d'insérer / <br> supprimer des éléments | ✅ | ✅ | ❌ | ✅ |
| Possibilité de modifier <br> des éléments | ✅ | valeurs : ✅ <br>clés : ❌ | ❌ | ❌ |
| Possibilité de stocker <br>des valeurs dupliquées | ✅ | ✅$^*$ | ✅ | ❌ |
| Valeurs ordonnées | ✅ | ❌$^{**}$ | ✅ | ❌ |

* $^*$ : dans un dictionnaire, les valeurs peuvent être dupliquées, mais pas les clefs
* $^{**}$ : en fait, à partir de la version 3.7 de Python, les dictionnaires sont ordonnés, mais pour que votre code tourne de manière identique quelle que soit la version de Python utilisée, il est préférable de ne pas faire d'hypothèse sur l'ordre des paires clés-valeurs dans les dictionnaires
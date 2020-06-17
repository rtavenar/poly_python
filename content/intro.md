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

# Introduction

Ce document est une tentative de polycopié associé au module de Python pour la deuxième année de licence MIASHS de l'Université de Rennes 2.
Il est distribué librement (sous licence [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) plus précisément) et se veut évolutif, n'hésitez donc pas à faire vos remarques à son auteur dont vous trouverez le contact sur [sa page web](http://people.irisa.fr/Romain.Tavenard/).
Ce polycopié a notamment bénéficié des apports d'Aurélie Lemaitre et d'Agnès Maunoury.

Durant la lecture de ce polycopié, vous trouverez des blocs de code tels que celui-ci :

```{code-cell}
def f(v):
	return v ** 2

x = 5
y = f(3 * x + 2)
print(y)
```

Dans ce document, nous allons donc nous intéresser au langage Python.
Pour tester les exemples présentés au fil de ce document ou réaliser les exercices proposés, vous aurez deux possibilités.
La première consiste à ouvrir une **console Python**, à l'aide de la commande suivante (si vous êtes sous Unix, en supposant que le symbole `$` corresponde au prompt de votre _shell_) :

```
$ python
Python 3.5.1 (default, Dec  9 2015, 11:28:16)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Lors de l'exécution de cette commande, on peut remarquer plusieurs choses.
Tout d'abord, au démarrage, la console Python nous indique la version de Python qui est exécutée.
Cela est important, car il existe notamment une importante différence entre les versions 2 (2.x.y) et 3 (3.x.y) de Python.
Dans ce document, nous supposons l'utilisation de Python dans sa version 3, comme dans la console affichée plus haut.
Enfin, une fois la console démarrée, on voit apparaître un prompt Python (`>>>`) qui indique que vous pouvez, à partir de ce point, entrer du code Python et en demander l'exécution en appuyant sur la touche _retour chariot_ (ou "Entrée") de votre clavier.

L'autre façon de programmer en Python, plus adaptée dès lors que l'on souhaite conserver une trace de ce qu'on a écrit, consiste à enregistrer vos commandes dans un fichier texte (en respectant la convention qui consiste à utiliser l'extension `.py` pour le nom de fichier) puis à faire exécuter votre programme par l'interpréteur Python :

```
$ python nom_de_mon_fichier.py
[...]
```

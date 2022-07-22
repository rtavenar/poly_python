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

# Structures de données et structures de contrôle

Dans ce chapitre, on s'intéresse aux éléments de base de la syntaxe Python : les structures de données d'une part et les structures de contrôle d'autre part.
Les structures de données vont permettre de stocker dans la mémoire de l'ordinateur (dans le but de les traiter ensuite) des données tandis que les structures de contrôle vont servir à définir nos interactions avec ces données.

## Variables

En Python, les données sont stockées dans des variables.
On ne peut pas, comme c'est le cas dans d'autres langages, définir de constante (qui sont, dans ces langages, des moyens de stocker des valeurs n'ayant pas vocation à être modifiées au cours de l'exécution du programme).
Une variable est une association entre un symbole (le nom de la variable) et une valeur, cette dernière pouvant varier au cours de l'exécution du programme.

### Types des variables Python

Les types de base existant en Python sont les suivants :

* `int` : entier ;
* `float` : nombre à virgule ;
* `complex` : nombre complexe (peu utilisé en pratique dans ce cours) ;
* `str` : chaîne de caractères ;
* `bool` : booléen (pouvant prendre les valeurs `True` ou `False`).

De plus, il existe un type spécial (`NoneType`) ne permettant qu'une seule valeur : la valeur `None` qui signifie "pas de valeur" ou "valeur manquante".

Le choix du type utilisé pour une variable impliquera :

 * une certaine façon d'encoder les données en mémoire (mais cette partie vous sera largement masquée, c'est l'interpréteur qui s'en chargera) ;
 * un certain nombre d'opérations autorisées sur la variable (opérations arithmétiques sur les variables numériques, concaténation sur les chaînes de caractères, _etc._)

Les variables Python sont typées dynamiquement, ce qui signifie qu'une variable, à un moment donné de l'exécution d'un programme, a un type précis qui lui est attribué, mais que celui-ci peut évoluer au cours de l'exécution du programme.
En Python, le type d'une variable n'est pas déclaré par l'utilisateur : il est défini par l'usage (la valeur effective que l'on décide de stocker dans la variable en question).

+++

Par exemple, l'instruction suivante (dite opération d'affectation) en Python attribue la valeur `12` à la variable `v`, qui devient donc automatiquement de type entier :

```{code-cell}
v = 12
```

Ainsi, les instructions suivantes ont toutes une incidence sur le type des variables considérées :

```{code-cell}
v = 12     # v est alors de type entier
c = "abc"  # c est de type chaîne de caractères
d = 'abc'  # d est également de type chaîne de caractères
           # les contenus de c et d sont identiques
v = 12.    # v change de type et est désormais de type nombre à virgule
```

Pour vérifier le type d'une variable, il suffit d'utiliser la fonction `type` de la librairie standard :

```{code-cell}
print(type(v))  # la fonction print(.) permet d'afficher
                # une information dans le terminal
```

### Opération d'affectation

Comme le montrent les exemples précédents, pour pouvoir utiliser des variables, on doit leur donner un nom (placé à gauche du signe égal dans l'opération d'affectation).
Ces noms de variables doivent respecter certaines contraintes :

* ils doivent débuter par une lettre (minuscule ou majuscule, peu importe) ou par le symbole `_` ;
* ils ne doivent contenir que des lettres, des chiffres et des symboles `_` ;
* ils ne doivent pas correspondre à un quelconque mot réservé du langage Python, dont voici la liste :

```
and del for is raise assert elif from lambda return break else global
not try nonlocal True False class except if or while continue import
pass yield None def finally in as with
```

* ils ne doivent pas correspondre à des noms de fonction de la librairie standard de Python (cette dernière condition n'est en fait qu'une bonne pratique à observer) : vous apprendrez au fur et à mesure les noms de ces fonctions.

Les noms de variable en Python sont sensibles à la casse, ainsi les variables `maVariable` et `mavariable` ne pointent pas sur les mêmes données en mémoire. Pour s'en convaincre, on peut exécuter le code suivant :

```{code-cell}
mavariable = 12
maVariable = 15
print(mavariable)
```

```{code-cell}
print(maVariable)
```

Comme on l'a vu plus haut, on utilise en Python l'opérateur `=` pour affecter une valeur à une variable.
La sémantique de cet opérateur est la suivante : "affecter la valeur contenue dans le membre de droite à la variable du membre de gauche".
Ainsi, il est tout à fait valide d'écrire, en Python :

```
x = 3.9 * x * (1 - x)
```

Pour exécuter cette instruction, l'interpréteur Python commencera par évaluer le membre de droite en utilisant la valeur courante de la variable `x`, puis affectera la valeur correspondant au résultat de l'opération `3.9 * x * (1 - x)` dans la variable `x`.

Ainsi, voici le résultat de l'exécution suivante :


```{code-cell}
x = 2
print(x)
```

```{code-cell}
x = 3.9 * x * (1 - x)
print(x)
```

Si l'on souhaite obtenir un affichage plus riche, on pourra utiliser la méthode `format` comme suit :

```{code-cell}
x = 2
x = 3.9 * x * (1 - x)
print("La valeur courante de x est {}".format(x))
```

### Opérateurs et priorité

On le voit dans l'exemple précédent, pour manipuler des variables, on utilisera des opérateurs (dont les plus connus sont les opérateurs arithmétiques).
Le tableau suivant dresse une liste des opérateurs définis pour les variables dont le type est l'un des types numériques (entier, nombre à virgule, nombre complexe) :

| Opérateur | Opération |
|:---:|:---:|
| `+` | Addition |
| `-` | Soustraction |
| `*` | Multiplication |
| `/` | Division |
| `**` | Élévation à la puissance |
| `%` | Modulo (non défini pour les nombres complexes) |
| `//` | Division entière |


De plus, pour chacun de ces opérateurs, il existe un opérateur associé qui réalise successivement l'opération demandée puis l'affectation de la nouvelle valeur à la variable en question.
Ainsi, l'instruction suivante :

```{code-cell}
x = x + 2
```

qui ajoute 2 à la valeur courante de `x` puis stocke le résultat du calcul dans `x` peut se réécrire :

```{code-cell}
x += 2
```

Ceci est purement un raccourci de notation, s'il ne vous semble pas évident à maîtriser au premier abord, vous pouvez vous en passer et toujours utiliser la notation `x = x + 2`.

Enfin, lorsque l'évaluation d'une expression implique plusieurs opérateurs, les règles de priorité sont les suivantes (de la priorité maximale à la priorité minimale) :

1. parenthèses ;
2. élévation à la puissance ;
3. multiplication / division ;
4. addition / soustraction ;
5. de gauche à droite.

Pour prendre un exemple concret, pour évaluer l'expression :

```
3.9 * x * (1 - x)
```

l'interpréteur Python commencera par évaluer le contenu de la parenthèse puis, les 2 opérations restantes étant toutes des multiplications, il les effectuera de gauche à droite.

De plus, lorsqu'une opération est effectuée entre deux variables de types différents, le type le plus générique est retenu.
Par exemple, si l'on multiplie un entier par un nombre à virgule, le résultat sera de type `float`.
De même, le résultat de l'addition entre un nombre complexe et un nombre à virgule est un complexe.

**Attention.** Comme indiqué en introduction, ce polycopié suppose que vous utilisez Python dans sa version 3.
Il est à noter qu'il existe une différence importante entre Python 2 et Python 3 dans la façon d'effectuer des opérations mêlant nombres entiers et flottants.
Par exemple, l'opération suivante :

```{code-cell}
x = 2 / 3
```

stockera, en Python 2, la valeur 0 (résultat de la division **entière** de 2 par 3) dans la variable `x` alors qu'en Python 3, la division **flottante** sera effectuée et ainsi `x` contiendra `0.666666...`
En Python 3, si l'on souhaite effectuer une division entière, on pourra utiliser l'opérateur `//` :

```{code-cell}
print(2 // 3)
```

## Structures de contrôle

Un programme est une séquence d'instructions dont l'ordre doit être respecté.
Au-delà de cet aspect séquentiel, on peut souhaiter :

* n'effectuer certaines instructions que si une condition est vérifiée ;
* répéter certaines instructions ;
* factoriser une sous-séquence d'instructions au sein d'une fonction pour pouvoir y faire appel à plusieurs reprises dans le programme.

Les structures de contrôle associées à ces différents comportements sont décrits dans la suite de cette section.

### Structures conditionnelles

On peut indiquer à un programme de n'exécuter une instruction (ou une séquence d'instructions) que si une certaine condition est remplie, à l'aide du mot-clé `if` :

```{code-cell}
x = 12
if x > 0:
    print("X est positif")
    print("X n'est pas négatif")
```

On remarque ici que la condition est terminée par le symbole `:`, de plus, la séquence d'instructions à exécuter si la condition est remplie est **indentée**, cela signifie qu'elle est décalée d'un "cran" (généralement une tabulation ou 4 espaces) vers la droite.
Cette indentation est une bonne pratique recommandée quel que soit le langage que vous utilisez, mais en Python, c'est même une obligation (sinon, l'interpréteur Python ne saura pas où commence et où se termine la séquence à exécuter sous condition).

Dans certains cas, on souhaite exécuter une série d'instructions si la condition est vérifiée et une autre série d'instructions si elle ne l'est pas.
Pour cela, on utilise le mot-clé `else` comme suit :

```{code-cell}
x = -1
if x > 0:
    print("X est positif")
    print("X n'est pas négatif")
else:
    print("X est négatif")
```

Là encore, on remarque que l'indentation est de rigueur pour chacun des deux blocs d'instructions.
On note également que le mot-clé `else` se trouve au même niveau que le `if` auquel il se réfère.

Enfin, de manière plus générale, il est possible de définir plusieurs comportements en fonction de plusieurs tests successifs, à l'aide du mot-clé `elif`. `elif` est une contraction de `else if`, qui signifie sinon si.

```{code-cell}
x = -1
if x > 0:
    print("X est positif")
    x = 4
elif x > -2:
    print("X est compris entre -2 et 0")
elif x > -4:
    print("X est compris entre -4 et -2")
else:
    print("X est inférieur à -4")
```

Pour utiliser ces structures conditionnelles, il est important de maîtriser les différents opérateurs de comparaison à votre disposition en Python, dont voici une liste non exhaustive :

| Opérateur | Comparaison effectuée | Exemple |
|:---:|:---:|:---:|
| `<` | Plus petit que | `x < 0` |
| `>` | Plus grand que | `x > 0` |
| `<=` | Plus petit ou égal à | `x <= 0` |
| `>=` | Plus grand ou égal à | `x >= 0` |
| `==` | Égal à | `x == 0` |
| `!=` | Différent de | `x != 0` |
| `is` | Test d'égalité pour le cas de la valeur `None` | `x is None` |
| `is not` | Test d'inégalité pour le cas de la valeur `None` | `x is not None` |
| `in` | Test de présence d'une valeur dans une liste | `x in [1, 5, 7]` |

Il est notamment important de remarquer que, lorsque l'on souhaite tester l'égalité entre deux valeurs, l'opérateur à utiliser est `==` et non `=` (qui sert à affecter une valeur à une variable).

(ex2.1)=
#### Exercice

```{admonition} Exercice 2.1 : Température de l'eau
Écrivez une expression conditionnelle, qui à partir d'une température d'eau stockée dans une variable `t` affiche dans le terminal si l'eau à cette température est à l'état liquide, solide ou gazeux.
```

<div id="pad_2.1" class="pad"></div>
<script>
    Pythonpad('pad_2.1', 
              {'id': '2.1', 
               'title': 'Testez votre solution ici', 
               'src': 't = -3\n# Complétez ce code'})
</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
t = -5
if t <= 0:
	print("l'eau est sous forme solide")
elif t < 100:
	print("l'eau est sous forme liquide")
else :
	print("l'eau est sous forme gazeuse")
```
````

### Boucles

Il existe, en Python comme dans une grande majorité des langages de programmation, deux types de boucles :

* les boucles qui s'exécutent tant qu'une condition est vraie ;
* les boucles qui répètent la même série d'instructions pour différentes valeurs d'une variable (appelée **variable de boucle**).

#### Boucles `while`

Les premières ont une syntaxe très similaire à celle des structures conditionnelles simples :

```{code-cell}
x = 0
while x <= 10:
    print(x)
    x = 2 * x + 2
```

On voit bien ici, en analysant la sortie produite par ces quelques lignes, que le contenu de la boucle est répété plusieurs fois.
En pratique, il est répété jusqu'à ce que la variable `x` prenne une valeur supérieure à 10 (14 dans notre cas).
Il faut être très prudent avec ces boucles `while` car il est tout à fait possible de créer une boucle dont le programme ne sortira jamais, comme dans l'exemple suivant :


```
x = 2
y = 0
while x > 0:
    y = y - 1
    print(y)
print("Si on arrive ici, on a fini")
```

En effet, on a ici une boucle qui s'exécutera tant que `x` est positif, or la valeur de cette variable est initialisée à 2 et n'est pas modifiée au sein de la boucle, la condition sera donc toujours vérifiée et le programme ne sortira jamais de la boucle.
Pour information, si vous vous retrouvez dans un tel cas, vous pourrez interrompre l'exécution du programme à l'aide de la combinaison de touches `Ctrl + C`.

#### Boucles `for`

```{admonition} Information
  :class: tip

Si vous avez appris à programmer dans un autre langage que Python, il est possible que vous ayez été habitué(e) à ce que les boucles `for` soient utilisées pour itérer sur des entiers (par exemple les indices des éléments d'une liste).
En Python, le principe de base est légèrement différent : par défaut, on itère sur les éléments d'une liste. Vous verrez dans le chapitre de ce polycopié dédié aux listes {ref}`comment faire lorsque l'on souhaite itérer sur les indices <parcours-liste>`.
```

Le second type de boucle repose en Python sur l'utilisation de listes (ou, plus généralement, d'itérables) dont nous reparlerons plus en détail dans la suite de cet ouvrage.
Sachez pour le moment qu'une liste est un ensemble ordonné d'éléments.
On peut alors exécuter une série d'instructions pour toutes les valeurs d'une liste :

```{code-cell}
for x in [1, 5, 7]:
    print(x)
print("Fin de la boucle")
```

Cette syntaxe revient à définir une variable `x` qui prendra successivement pour valeur chacune des valeurs de la liste `[1, 5, 7]` dans l'ordre et à exécuter le code de la boucle (ici, un appel à la fonction `print`) pour cette valeur de la variable `x`.

Il est fréquent d'avoir à itérer sur les `n` premiers entiers.
Cela peut se faire à l'aide de la fonction `range` (qui est abordée plus en détail dans {ref}`la section de ce cours sur les listes <creation-liste>`) :

```{code-cell}
for i in range(1, 10):
    print(i)
```

```{admonition} Quelle boucle choisir ?
  :class: tip

Lorsque l'on débute la programmation en Python, il peut être difficile de choisir, pour un problème donné, entre les boucles `for` et `while` présentées ici.
De manière générale, dès lors que l'on souhaite parcourir les éléments d'une liste ou d'un dictionnaire, on utilisera la boucle `for`.
De même, si l'on connait à l'avance le nombre d'itérations que l'on souhaite effectuer, on utilisera une boucle `for` (couplée avec un appel à la fonction `range`).
Comme son nom l'indique, la boucle `while` sera utilisée dès lors que l'on souhaite répéter une action **tant qu'** une condition est vérifiée.
```

(ex2.2)=
#### Exercice

```{admonition} Exercice 2.2 : Nombres impairs
Écrivez une boucle permettant d'afficher tous les nombres impairs inférieurs à une valeur `n` initialement fixée.
```

<div id="pad_2.2" class="pad"></div>
<script>
    Pythonpad('pad_2.2', 
              {'id': '2.2', 
               'title': 'Testez votre solution ici', 
               'src': 'n = 20\n# Complétez ce code'})
</script>

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

* Version avec utilisation du modulo

```python
n = 8
i = 0
while(i < n):
    if i % 2 != 0:
        print(i)
    i+=1
```

* Version sans utilisation du modulo

```python
n = 8
i = 1
while(i < n):
    print(i)
    i += 2
```
````

### Fonctions

Nous avons déjà vu dans ce qui précède, sans le dire, des fonctions.
Par exemple, lorsque l'on écrit :


```{code-cell}
print(x)
```

on demande l'appel à une fonction, nommée `print` et prenant un **argument** (ici, la variable `x`).
La fonction `print` ne retourne pas de valeur, elle ne fait qu'afficher la valeur contenue dans `x` sur le terminal.
D'autres fonctions, comme `type` dont nous avons parlé plus haut, **retournent une valeur** et cette valeur peut être utilisée dans la suite du programme, comme dans l'exemple suivant :

```{code-cell}
x = type(1)  # On stocke dans x la valeur retournée par type
y = type(2.)
if x == y:
    print("types identiques")
else:
    print("types différents")
```

En pratique, dans un programme, on aura recours à la définition de fonctions pour décomposer un problème global en sous-problèmes, chaque sous-problème étant géré par une fonction qui pourra elle-même, au besoin, faire appel à d'autres fonctions.

#### Définition d'une fonction

Lorsqu'un ensemble d'instructions est susceptible d'être utilisé à plusieurs occasions dans un ou plusieurs programmes, il est recommandé de l'isoler au sein d'une fonction.
Cela présentera les avantages suivants :

* en donnant un nom à la fonction et en listant la liste de ses arguments, on explicite la sémantique de l'ensemble d'instructions en question, ses entrées et sorties éventuelles, ce qui rend le code beaucoup plus lisible ;
* s'il est nécessaire d'adapter à l'avenir le code pour résoudre un _bug_ ou le rendre plus générique, vous n'aurez à modifier le code qu'à un endroit (dans le corps de la fonction) et non pas à chaque fois que le code est répété.

Pour définir une fonction en Python, on utilise le mot-clé `def` :

```{code-cell}
def f(x):
    y = 5 * x + 2
    z = x + y
    return z // 2
```

On a ici défini une fonction

* dont le nom est `f` ;
* qui prend un seul argument, noté `x` ;
* qui retourne une valeur, comme indiqué dans la ligne débutant par le mot-clé `return`.

Il est possible, en Python, d'écrire des fonctions retournant plusieurs valeurs.
Pour ce faire, ces valeurs seront séparées par des virgules dans l'instruction `return` :

```{code-cell}
def f(x):
    y = 5 * x + 2
    z = x + y
    return z // 2, y
```

Enfin, en l'absence d'instruction `return`, une fonction retournera la valeur `None`.

Il est également possible d'utiliser le nom des arguments de la fonction lors de l'appel, pour ne pas risquer de se tromper dans l'ordre des arguments.
Par exemple, si l'on a la fonction suivante :

```{code-cell}
def affiche_infos_personne(poids, taille):
    print("Poids: ", poids)
    print("Taille: ", taille)
```

Les trois appels suivants sont équivalents :

```{code-cell}
affiche_infos_personne(80, 180)
```

```{code-cell}
affiche_infos_personne(taille=180, poids=80)
```

```{code-cell}
affiche_infos_personne(poids=80, taille=180)
```

Notons qu'il est alors possible d'interchanger l'ordre des arguments lors de l'appel d'une fonction si on précise leur nom.
Évidemment, pour que cela soit vraiment utile, il est hautement recommandé d'utiliser des **noms d'arguments explicites** lors de la définition de vos fonctions.

#### Argument(s) optionnel(s) d'une fonction

Certains arguments d'une fonction peuvent avoir une valeur par défaut, décidée par la personne qui a écrit la fonction.
Dans ce cas, si l'utilisateur ne spécifie pas explicitement de valeur pour ces arguments lors de l'appel à la fonction, c'est la valeur par défaut qui sera utilisée dans la fonction, dans le cas contraire, la valeur spécifiée sera utilisée.

Par exemple, la fonction `print` dispose de plusieurs arguments facultatifs, comme le caractère par lequel terminer l'affichage (par défaut, un retour à la ligne, `"\n"`) :

```{code-cell}
print("La vie est belle")
```

```{code-cell}
print("Life is beautiful")
```

```{code-cell}
print("La vie est belle", end="--")
```

```{code-cell}
print("Life is beautiful", end="*-*")
```

Lorsque vous définissez une fonction, la syntaxe à utiliser pour donner une valeur par défaut à un argument est la suivante :

```{code-cell}
def f(x, y=0):  # La valeur par défaut pour y est 0
    return x + 5 * y
```

Attention toutefois, les arguments facultatifs (_ie._ qui disposent d'une valeur par défaut) doivent impérativement se trouver, dans la liste des arguments, après le dernier argument obligatoire.
Ainsi, la définition de fonction suivante **n'est pas correcte** :

```
def f(x, y=0, z):
    return x - 2 * y + z
```

(ex2.3)=
### Exercices 

```{admonition} Exercice 2.3 : Triangle équilatéral
Écrivez une fonction en Python qui prenne en argument une longueur `long` et retourne l'aire du triangle équilatéral de côté `long`.
```

<div id="pad_2.3" class="pad"></div>
<script>
    Pythonpad('pad_2.3', 
              {'id': '2.3', 
               'title': 'Testez votre solution ici', 
               'src': '# Complétez ce code'})
</script>

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
import math

def aire_equi(long):
    base = long
    hauteur = long * math.sin(math.pi / 3)
    return base * hauteur / 2

print(aire_equi(1.))
```
````

```{admonition} Exercice 2.4 : Suite récurrente
:name: ex2.4
Écrivez une fonction en Python qui affiche tous les termes plus petits que 1000 de la suite $(u_n)$ définie comme :

$$
\begin{array}{rcc}u_0 & = & 2 \\
\forall n \geq 1, \, u_n & = & u_{n-1}^2\end{array}
$$
```

<div id="pad_2.4" class="pad"></div>
<script>
    Pythonpad('pad_2.4', 
              {'id': '2.4', 
               'title': 'Testez votre solution ici', 
               'src': '# Complétez ce code'})
</script>

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

* Version itérative (avec une boucle)

```python
def affiche_u_n():
    u = 2
    while u < 1000:
        print(u)
        u = u ** 2

affiche_u_n()
```

* Version récursive (avec des appels de fonction)

```python
def affiche_u_n(u=2):
    if u < 1000:
        print(u)
        affiche_u_n(u ** 2)

affiche_u_n()
```

Ici, on a fixé une valeur par défaut à l'argument `u` correspondant à l'initialisation de la suite, pour que l'appel initial se fasse comme pour la version itérative de la fonction (`affiche_u_n()`).
````

## Les modules en Python

Jusqu'à présent, nous avons utilisé des fonctions (comme `print`) issues de la librairie standard de Python.
Celles-ci sont donc chargées par défaut lorsque l'on exécute un script Python.
Toutefois, il peut être nécessaire d'avoir accès à d'autres fonctions et/ou variables, définies dans d'autres librairies.
Pour cela, il sera utile de charger le **module** correspondant.

Prenons l'exemple du module `math` qui propose un certain nombre de fonctions mathématiques usuelles (`sin` pour le calcul du sinus d'un angle, `sqrt` pour la racine carrée d'un nombre, _etc._) ainsi que des constantes mathématiques très utiles comme `pi`.
Le code suivant charge le module en mémoire puis fait appel à certaines de ses fonctions et/ou variables :

```{code-cell}
import math

print(math.sin(0))
```

```{code-cell}
print(math.pi)
```

```{code-cell}
print(math.cos(2 * math.pi))
```

```{code-cell}
print(math.sqrt(2))
```

Vous remarquerez ici que l'instruction d'import du module se trouve nécessairement avant les instructions faisant référence aux fonctions et variables de ce module, faute de quoi ces dernières ne seraient pas définies.
De manière générale, vous prendrez la bonne habitude d'écrire les instructions d'import en tout début de vos fichiers Python, pour éviter tout souci.

## Liste des exercices de ce chapitre

1. [Température de l'eau](ex2.1)
2. [Nombres impairs](ex2.2)
3. [Triangle équilatéral](ex2.3)
4. [Suite récurrente](ex2.4)

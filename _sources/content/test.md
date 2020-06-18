# Tester son code

```{admonition} Pour info
  :class: tip

  Il existe en Python des outils dédiés au test de programmes.
  Toutefois, ce chapitre ne traite pas de l'utilisation de ces outils, mais plutôt de l'intérêt des tests en général.
```

Dans ce document, nous avons jusqu'à présent supposé que tout se passait bien, que votre code ne retournait jamais d'erreur et qu'il ne contenait jamais de _bug_.
Quel que soit votre niveau d'expertise en Python, ces deux hypothèses sont peu réalistes.
Nous allons donc nous intéresser maintenant aux moyens de vérifier si votre code fait bien ce qu'on attend de lui et de mieux comprendre son comportement lorsque ce n'est pas le cas.

## Les erreurs en Python

Étudions ce qu'il se passe lors de l'exécution du code suivant :
```
x = "12"
y = x + 2
```

Nous obtenons la sortie suivante :
```bash
Traceback (most recent call last):
  File "[...]", line 2, in <module>
    y = x + 2
TypeError: Can't convert 'int' object to str implicitly
```

Ce type de message d'erreur ne doit pas vous effrayer, il est là pour vous aider.
Il vous fournit de précieuses informations :

1. l'erreur se produit à la ligne 2 de votre script Python ;
2. le problème est que Python ne peut pas convertir un objet de type `int` en chaîne de caractères (`str`) de manière implicite.

Reste à se demander pourquoi, dans le cas présent, Python voudrait transformer un entier en chaîne de caractères.
Pour le comprendre, rendons-nous à la ligne 2 de notre script et décortiquons-la.
Dans cette ligne (`y = x + 2`), deux opérations sont effectuées :

* la première consiste à effectuer l'opération `+` entre les opérandes `x` et `2` ;
* la seconde consiste à assigner le résultat de l'opération à la variable `y`.

Nous avons vu dans ce document que Python savait effectuer l'opération `+` avec des opérandes de types variés (nombre `+` nombre, liste `+` liste, chaîne de caractères `+` chaîne de caractères, et il en existe d'autres).
Intéressons-nous ici au type des opérandes considérées.
La variable `x` telle que définie à la ligne 1 est de type chaîne de caractères.
La valeur `2` est de type entier.
Il se trouve que Python n'a pas défini d'addition entre chaîne de caractères et entier et c'est pour cela que l'on obtient une erreur.
Plus précisément, l'interpréteur Python nous dit : "si je pouvais convertir la valeur entière en chaîne de caractères à la volée, je pourrais faire l'opération `+` qui serait alors une concaténation, mais je ne me permets pas de le faire tant que vous ne l'avez pas écrit de manière explicite".

Maintenant que nous avons compris le sens de ce _bug_, il nous reste à le corriger.
Si nous souhaitons faire la somme du nombre 12 (stocké sous forme de chaîne de caractères dans la variable `x`) et de la valeur 2, nous écrivons :
```python
x = "12"
y = int(x) + 2
```
et l'addition s'effectue alors correctement entre deux valeurs numériques.


## Les tests unitaires

Pour pouvoir être sûr du code que vous écrivez, il faut l'avoir testé sur un ensemble d'exemples qui vous semble refléter l'ensemble des cas de figures auxquels votre programme pourra être confronté.
Or, cela représente un nombre de cas de figures très important dès lors que l'on commence à écrire des programmes un tant soit peu complexes.
Ainsi, il est hautement recommandé de découper son code en fonctions de tailles raisonnables et qui puissent être testées indépendamment.
Les tests associés à chacune de ces fonctions sont appelés **tests unitaires**.

Tout d'abord, en mettant en place de tels tests, vous pourrez détecter rapidement un éventuel _bug_ dans votre code et ainsi gagner beaucoup de temps de développement. De plus, vous pourrez également vous assurer que les modifications ultérieures de votre code ne modifient pas son comportement pour les cas testés.
En effet, lorsque l'on ajoute une fonctionnalité à un programme informatique, il faut avant toute choses s'assurer que celle-ci ne cassera pas le bon fonctionnement du programme dans les cas classiques d'utilisation pour lesquels il avait été à l'origine conçu.

Prenons maintenant un exemple concret.
Supposons que l'on souhaite écrire une fonction `bissextile` capable de dire si une année est bissextile ou non.
En se renseignant sur [le sujet](https://fr.wikipedia.org/wiki/Année_bissextile), on apprend qu'une année est bissextile si :

* si elle est divisible par 4 et non divisible par 100, ou
* si elle est divisible par 400.

On en déduit un ensemble de tests adaptés :
```python
print(bissextile(2004))  # True car divisible par 4 et non par 100
print(bissextile(1900))  # False car divisible par 100 et non par 400
print(bissextile(2000))  # True car divisible par 400
print(bissextile(1999))  # False car divisible ni par 4 ni par 100
```

On peut alors vérifier que le comportement de notre fonction `bissextile` est bien conforme à ce qui est attendu.


## Le développement piloté par les tests

Le développement piloté par les tests (ou _Test-Driven Development_) est une technique de programmation qui consiste à rédiger les tests unitaires de votre programme avant même de rédiger le programme lui-même.

L'intérêt de cette façon de faire est qu'elle vous obligera à réfléchir aux différents cas d'utilisation d'une fonction avant de commencer à la coder.
De plus, une fois ces différents cas identifiés, il est probable que la structure globale de la fonction à coder vous apparaisse plus clairement.

Si l'on reprend l'exemple de la fonction `bissextile` citée plus haut, on voit assez clairement qu'une fois que l'on a rédigé l'ensemble de tests, la fonction sera simple à coder et reprendra les différents cas considérés pour les tests:
```python
def bissextile(annee):
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    elif annee % 400 == 0:
        return True
    else:
        return False
```

## Exercice


**Exercice 9.1**
En utilisant les méthodes de développement préconisées dans ce chapitre, rédigez le code et les tests d'un programme permettant de déterminer le lendemain d'une date fournie sous la forme de trois entiers (jour, mois, année).

**Exercice 9.2**
Proposez une ré-écriture de la fonction bissextile ci-dessus qui tienne en une ligne de la forme :

```python
def bissextile(annee):
    return CONDITION_COMPLEXE
```

où `CONDITION_COMPLEXE` est un booléen calculé à partir de la valeur de `annee`.
Assurez-vous que cette nouvelle fonction passe bien les tests énoncés ci-dessus.

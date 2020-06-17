# Les dates

Dans la partie précédente, nous avons présenté les types de base du langage Python et les opérateurs associés aux types numériques.
Lorsque l'on souhaite manipuler des dates et des heures, on devra avoir recours à un autre type de données, défini dans le module `datetime`.
Pour cela, il faudra commencer par charger ce module en ajoutant l'instruction :

import datetime

en en-tête de votre script Python.

Pour créer une nouvelle variable de ce type, on utilisera la syntaxe :

```
d = datetime.datetime(annee, mois, jour, heure, minutes)
```

La syntaxe `datetime.datetime`, qui peut vous sembler bizarre au premier coup d'oeil signifie à l'interpréteur Python qu'il doit chercher dans le module `datetime` une fonction dont le nom est `datetime` et l'appeler.

En fait, on pourrait rajouter lors de l'appel de `datetime.datetime` un argument pour spécifier les secondes, puis éventuellement un autre pour les microsecondes, si l'on avait besoin d'une heure plus précise.
Si, au contraire, on ne spécifie pas l'heure lors de l'appel de la fonction, l'heure `00h00` sera choisie par défaut.

Par exemple :

import datetime  # Cette commande doit se trouver en début de fichier

# [...] (ici, du code concernant autre chose si besoin)

d = datetime.datetime(2019, 8, 27, 17, 23)
print(d)

d = datetime.datetime(2019, 8, 27, 17, 23, 32)
print(d)

d = datetime.datetime(2019, 8, 27)
print(d)

Les opérateurs de comparaison vus au chapitre précédent (`<`, `>`, `<=`, `>=`, `==`) fonctionnent de manière naturelle avec ce type de données :

d1 = datetime.datetime(2019, 8, 27, 17, 23)
d2 = datetime.datetime(2019, 8, 27, 17, 28)
d3 = datetime.datetime(2019, 8, 27, 17, 23)
print(d1 < d2)

print(d1 == d3)

print(d1 > d3)

Il existe d'autres moyens de construire des variables de type date.
On peut générer une date correspondant à l'heure actuelle avec la fonction `datetime.now` du module `datetime` :

date_actuelle = datetime.datetime.now()

## Transformation d'une date en chaîne de caractères

Si l'on souhaite transformer une date en chaîne de caractères (par exemple pour l'afficher), on peut lui appliquer la fonction `str` :

print(str(datetime.datetime(2019, 8, 27)))

Dans ce cas, on ne peut pas gérer la façon dont se fait cette transformation.
Pour contourner cette limitation, il convient alors d'utiliser `strftime` :

```
d1 = datetime.datetime(...)
s = d1.strftime(format)
```

L'attribut `format` que l'on passe à cette fonction va servir à définir comment on souhaite représenter la date en question.
Il s'agit d'une chaîne de caractères qui pourra contenir les éléments suivants :

| Code | Signification |
|------|---------------|
| `%Y` | Année         |
| `%m` | Mois          |
| `%d` | Jour          |
| `%H` | Heure         |
| `%M` | Minutes       |

Remarquez que la casse n'est pas neutre pour les codes à utiliser : `%M` et `%m` ont des significations tout à fait différentes.
Notez également qu'il existe d'autres codes permettant de générer des chaînes de caractères plus variées encore.
Une liste de ces codes est disponible sur [la page d'aide du module `datetime`](https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior).

Vous pouvez vous référer aux exemples ci-dessous pour mieux comprendre le fonctionnement de la fonction `strftime` :

d = datetime.datetime(2019, 8, 27, 17, 23)

print(d.strftime("%d-%m-%Y, %H:%M"))

print(d.strftime("%d-%m-%Y"))

print(d.strftime("%H:%M"))

print(d.strftime("%d/%m/%Y %Hh%M"))

Il est également possible d'effectuer l'opération inverse (lire une date contenue dans une chaîne de caractères, étant donné un format connu).
Cela se fait avec la fonction `datetime.strptime` (attention aux confusions possibles entre `strftime` et `datetime.strptime`) :

```
d1 = datetime.datetime.strptime(chaine_a_lire, format)
```

Voici deux exemples d'utilisation de cette fonction :

d1 = datetime.datetime.strptime("2019/8/27, 17:23", "%Y/%m/%d, %H:%M")
d2 = datetime.datetime.strptime("27-08-2019", "%d-%m-%Y")

## Calcul de temps écoulé

On peut ensuite souhaiter calculer la différence entre deux dates.
Le résultat de cette opération est une **durée**, représentée en Python par le type `timedelta` (lui aussi défini dans le module `datetime`).

d1 = datetime.datetime(2019, 8, 27, 17, 23)
d2 = datetime.datetime(2019, 8, 27, 17, 28)
intervalle_de_temps = d1 - d2
print(type(intervalle_de_temps))

Très souvent, il est utile pour manipuler une durée de la convertir en un nombre de secondes et de manipuler ce nombre ensuite.
Cela se fait à l'aide de la commande :

d1 = datetime.datetime(2019, 8, 27, 17, 23)
d2 = datetime.datetime(2019, 8, 27, 17, 28)
intervalle_de_temps = d1 - d2
print(intervalle_de_temps.total_seconds())

On remarque ici que l'intervalle obtenu est négatif, ce qui était prévisible car il s'agit de l'intervalle `d1 - d2` et on a `d1 < d2`.

Notez enfin que l'on peut tout à fait ajouter une durée à une date :

d1 = datetime.datetime(2019, 8, 27, 17, 23)
d2 = datetime.datetime(2019, 8, 27, 17, 28)
d3 = datetime.datetime(2019, 8, 27, 18, 00)
intervalle_de_temps = d2 - d1
print(d3 + intervalle_de_temps)

## Exercices

**Exercice 3.1** S'est-il écoulé plus de temps (i) entre le 2 Janvier 1920 à 7h32 et le 4 Mars 1920 à 5h53 ou bien (ii) entre le 30 Décembre 1999 à 17h12 et le 1er Mars 2000 à 15h53 ?

**Exercice 3.2** À l'aide des fonctions du module `datetime` vues plus haut, affichez, pour chaque année civile comprise entre 2010 et 2030, si elle est bissextile ou non.
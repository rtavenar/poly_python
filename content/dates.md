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

# Les dates

Dans la partie précédente, nous avons présenté les types de base du langage Python et les opérateurs associés aux types numériques.
Lorsque l'on souhaite manipuler des dates et des heures, on devra avoir recours à un autre type de données, défini dans le module `datetime`.
Pour cela, il faudra commencer par charger ce module en ajoutant l'instruction :

```{code-cell}
import datetime
```

en en-tête de votre script Python.

Pour créer une nouvelle variable de ce type, on utilisera la syntaxe :

```
d = datetime.datetime(annee, mois, jour, heure, minutes)
```

La syntaxe `datetime.datetime`, qui peut vous sembler bizarre au premier coup d'oeil signifie à l'interpréteur Python qu'il doit chercher dans le module `datetime` une fonction dont le nom est `datetime` et l'appeler.

En fait, on pourrait rajouter lors de l'appel de `datetime.datetime` un argument pour spécifier les secondes, puis éventuellement un autre pour les microsecondes, si l'on avait besoin d'une heure plus précise.
Si, au contraire, on ne spécifie pas l'heure lors de l'appel de la fonction, l'heure `00h00` sera choisie par défaut.

Par exemple :

```{code-cell}
import datetime  # Cette commande doit se trouver en début de fichier

# [...] (ici, du code concernant autre chose si besoin)

d = datetime.datetime(2020, 8, 27, 17, 23)
print(d)
```

```{code-cell}
d = datetime.datetime(2020, 8, 27, 17, 23, 32)
print(d)
```

```{code-cell}
d = datetime.datetime(2020, 8, 27)
print(d)
```

Les opérateurs de comparaison vus au chapitre précédent (`<`, `>`, `<=`, `>=`, `==`, `!=`) fonctionnent de manière naturelle avec ce type de données :

```{code-cell}
d1 = datetime.datetime(2020, 8, 27, 17, 23)
d2 = datetime.datetime(2020, 8, 27, 17, 28)
d3 = datetime.datetime(2020, 8, 27, 17, 23)
print(d1 < d2)
```

```{code-cell}
print(d1 == d3)
```

```{code-cell}
print(d1 > d3)
```

Il existe d'autres moyens de construire des variables de type date.
On peut générer une date correspondant à l'heure actuelle avec la fonction `datetime.now` du module `datetime` :

```{code-cell}
date_actuelle = datetime.datetime.now()
```

## Transformation d'une date en chaîne de caractères

Si l'on souhaite transformer une date en chaîne de caractères (par exemple pour l'afficher), on peut lui appliquer la fonction `str` :

```{code-cell}
print(str(datetime.datetime(2020, 8, 27)))
```

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

```{code-cell}
d = datetime.datetime(2020, 8, 27, 17, 23)

print(d.strftime("%d-%m-%Y, %H:%M"))
```

```{code-cell}
print(d.strftime("%d-%m-%Y"))
```

```{code-cell}
print(d.strftime("%H:%M"))
```

```{code-cell}
print(d.strftime("%d/%m/%Y %Hh%M"))
```

````{margin}
```{admonition} Attention !
  :class: warning

Attention aux confusions possibles entre `datetime.strftime` et `datetime.strptime` :

* `datetime.strftime` : le `f` signifie _format_, il s'agit donc de mettre en forme une date, selon un format donné, dans une chaîne de caractères
* `datetime.strptime` : le `p` signifie _parse_ (en anglais), il s'agit donc de reconnaître une date dans une chaîne de caractères et de retourner la date en question
```
````

Il est également possible d'effectuer l'opération inverse (lire une date contenue dans une chaîne de caractères, étant donné un format connu).
Cela se fait avec la fonction `datetime.strptime` :

```
d1 = datetime.datetime.strptime(chaine_a_lire, format)
```

Voici deux exemples d'utilisation de cette fonction :

```{code-cell}
d1 = datetime.datetime.strptime("2020/8/27, 17:23", "%Y/%m/%d, %H:%M")
print(d1)
```

```{code-cell}
d2 = datetime.datetime.strptime("27-08-2020", "%d-%m-%Y")
print(d2)
```

## Attributs des objets `datetime`

Lorsque l'on définit une date de type `datetime.datetime`, on peut accéder à certains de ses attributs directement :

```{code-cell}
d1 = datetime.datetime.strptime("2020/8/27, 17:23", "%Y/%m/%d, %H:%M")
print(d1)
```

```{code-cell}
print(d1.year)
```

```{code-cell}
print(d1.month)
```

```{code-cell}
print(d1.day)
```

```{code-cell}
print(d1.hour)
```

```{code-cell}
print(d1.minute)
```

```{code-cell}
print(d1.second)
```

## Calcul de temps écoulé

On peut ensuite souhaiter calculer la différence entre deux dates.
Le résultat de cette opération est une **durée**, représentée en Python par le type `timedelta` (lui aussi défini dans le module `datetime`).

```{code-cell}
d1 = datetime.datetime(2020, 8, 27, 17, 23)
d2 = datetime.datetime(2020, 8, 27, 17, 28)
intervalle_de_temps = d1 - d2
print(type(intervalle_de_temps))
```

Une autre façon de créer une durée au format `timedelta` est d'utiliser la fonction du même nom :

```{code-cell}
duree = datetime.timedelta(weeks=0, days=10, hours=3, minutes=10, seconds=23)
print(duree)
```

Très souvent, il est utile pour manipuler une durée de la convertir en un nombre de secondes et de manipuler ce nombre ensuite.
Cela se fait à l'aide de la commande :

```{code-cell}
d1 = datetime.datetime(2020, 8, 27, 17, 23)
d2 = datetime.datetime(2020, 8, 27, 17, 28)
intervalle_de_temps = d1 - d2
print(intervalle_de_temps.total_seconds())
```

On remarque ici que l'intervalle obtenu est négatif, ce qui était prévisible car il s'agit de l'intervalle `d1 - d2` et on a `d1 < d2`.

Notez enfin que l'on peut tout à fait ajouter une durée à une date :

```{code-cell}
d1 = datetime.datetime(2020, 8, 27, 17, 23)
d2 = datetime.datetime(2020, 8, 27, 17, 28)
d3 = datetime.datetime(2020, 8, 27, 18, 00)
intervalle_de_temps = d2 - d1
print(d3 + intervalle_de_temps)
```

## Exercices

```{admonition} Exercice 3.1
S'est-il écoulé plus de temps (i) entre le 2 Janvier 1920 à 7h32 et le 4 Mars 1920 à 5h53 ou bien (ii) entre le 30 Décembre 1999 à 17h12 et le 1er Mars 2000 à 15h53 ?
```

<div id="pad_3.1" class="pad"></div>
<script>
    Pythonpad('pad_3.1', 
              {'id': '3.1', 
               'title': 'Testez votre solution ici', 
               'src': 'import datetime\n# Complétez ce code'})
</script>

````{admonition} Solution
:class: tip, dropdown

```python
import datetime

interv1_date1 = datetime.datetime(1920, 1, 2, 7, 32)
interv1_date2 = datetime.datetime(1920, 3, 4, 5, 53)
duree1 = interv1_date2 - interv1_date1

interv2_date1 = datetime.datetime(1999, 12, 30, 17, 12)
interv2_date2 = datetime.datetime(2000, 3, 1, 15, 53)
duree2 = interv2_date2 - interv2_date1

if duree1 > duree2:
    print("Le premier intervalle est le plus grand.")
else:
    print("Le second intervalle est le plus grand.")
```
````

```{admonition} Exercice 3.2
À l'aide des fonctions du module `datetime` vues plus haut, affichez, pour chaque année civile comprise entre 2010 et 2030, si elle est bissextile ou non.
```

<div id="pad_3.2" class="pad"></div>
<script>
    Pythonpad('pad_3.2', 
              {'id': '3.2', 
               'title': 'Testez votre solution ici', 
               'src': 'import datetime\n# Complétez ce code'})
</script>

````{admonition} Solution
:class: tip, dropdown

```python
import datetime

duree_annee_normale = 365 * 24 * 60 * 60

for annee in range(2010, 2031):
    date_debut = datetime.datetime(annee, 1, 1)
    date_fin = datetime.datetime(annee + 1, 1, 1)
    duree_anne_courante = date_fin - date_debut
    if duree_anne_courante.total_seconds() > duree_annee_normale:
        print(annee, "est bissextile")
    else:
        print(annee, "n'est pas bissextile")
```
````
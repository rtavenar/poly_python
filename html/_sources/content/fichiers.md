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

# Lecture et écriture de fichiers textuels

Dans ce chapitre, nous nous intéressons à la lecture/écriture de fichiers textuels par un programme Python.
Un premier élément qu'il est nécessaire de maîtriser pour lire ou écrire des fichiers textuels est la notion d'encodage.
Il faut savoir qu'il existe plusieurs façons d'encoder un texte.
Nous nous focaliserons ici sur les deux encodages que vous êtes les plus susceptibles de rencontrer (mais sachez qu'il en existe bien d'autres) :

* l'encodage Unicode 8 bits (UTF-8), dont le code en python est `"utf-8"` ;
* l'encodage Latin-1 (ISO-8859-1) dont le code en python est `"iso-8859-1"`.

La principale différence entre ces deux encodage réside dans leur façon de coder les accents.
Ainsi, si le texte que vous lisez/écrivez ne contient aucun accent ou caractère spécial, il est probable que la question de l'encodage ne soit pas problématique dans votre cas.
Au contraire, s'il est possible que vous utilisiez de tels caractères, il faudra bien faire attention à l'encodage utilisé, que vous spécifierez à l'ouverture du fichier.
Si votre programme doit lire un fichier, il faudra donc vous assurer de l'encodage associé à ce fichier (en l'ouvrant par exemple avec un éditeur de texte qui soit suffisamment avancé pour vous fournir cette information).
Si vous écrivez un programme qui écrit un fichier, il faudra vous poser la question de l'utilisation future qui sera faite de ce fichier : s'il est amené à être ouvert par un autre utilisateur, il serait pertinent de vous demander quel encodage sera le moins problématique pour cet utilisateur, par exemple.

Si vous n'avez pas de contrainte extérieure pour ce qui est de l'encodage, vous utiliserez l'encodage UTF-8 par défaut.

## Lecture de fichiers textuels

Ce que nous appelons lecture de fichiers textuels en Python consiste à copier le contenu d'un fichier dans une (ou plusieurs) chaîne(s) de caractères.
Cela implique deux étapes en Python :

1. ouvrir le fichier en lecture ;
2. parcourir le contenu du fichier.

La première étape d'ouverture du fichier en lecture est commune à tous les types de fichiers textuels.
En supposant que le nom du fichier à ouvrir soit stocké sous forme de chaîne de caractères dans la variable `nom_fichier`, le code suivant ouvre un fichier en lecture avec l'encodage UTF-8 et stocke dans la variable `fp` un pointeur sur l'endroit où nous sommes rendus dans notre lecture du fichier (pour l'instant, le début du fichier) :

```
fp = open(nom_fichier, "r", encoding="utf-8")
```

Le second argument (`"r"`) indique que le fichier doit être ouvert en mode _read_, donc en lecture.

### Fichiers textuels génériques

Une fois le fichier ouvert en lecture, on peut le lire ligne par ligne à l'aide de la boucle suivante :

```
fp = open(nom_fichier, "r", encoding="utf-8")
for ligne in fp.readlines():
    print(ligne)
```

Ici, la variable `ligne`, de type chaîne de caractères, contiendra successivement le texte de chacune des lignes du fichier considéré.

### Fichiers _Comma-Separated Values_ (CSV)

Les fichiers _Comma-Separated Values_ (CSV) permettent de stocker des données organisées sous la forme de tableaux dans des fichiers textuels.
À l'origine, ces fichiers étaient organisées par ligne et au sein de chaque ligne les cellules du tableau (correspondant aux différentes colonnes) étaient séparées par des virgules (d'où le nom de ce type de fichiers).
Aujourd'hui, la définition de ce format ([lien](https://tools.ietf.org/html/rfc4180)) est plus générale que cela et différents délimiteurs sont acceptés.
Pour manipuler ces fichiers, il existe en Python un module dédié, appelé `csv`.
Ce module contient notamment une fonction `reader` permettant de simplifier la lecture de fichiers CSV.
La syntaxe d'utilisation de cette fonction est la suivante (vous remarquerez la présence de l'attribut `delimiter`) :

```{code-cell}
import csv

nom_fichier = "simple.csv"

# Contenu supposé du fichier :
# 1;2;3;4;5
# a;b;c;d;e
# xx;xx;xx;xx;xx
# 0.4;0.5;0.7;0.8;0.9

fp = open(nom_fichier, "r", encoding="utf-8")
for ligne in csv.reader(fp, delimiter=";"):
    for cellule in ligne:
        print(cellule)
    print("Fin de ligne")
```

On remarque ici que, contrairement au cas de fichiers textuels génériques, la variable de boucle `ligne` n'est plus une chaîne de caractères mais une liste de chaînes de caractères.
Les éléments de cette liste sont les cellules du tableau représenté par le fichier CSV.

#### Cas des fichiers à en-tête

Souvent, les fichiers CSV comprennent une première ligne d'en-tête, comme dans l'exemple suivant :

```csv
NOM;PRENOM;AGE
Lemarchand;John;23
Trias;Anne;
```

Si l'on souhaite que, lors de la lecture du fichier CSV, chaque ligne soit représentée par un dictionnaire dont les clés sont les noms de colonnes (lus dans l'en-tête) et les valeurs associées sont celles lues dans la ligne courante, on utilisera `csv.DictReader` au lieu de `csv.reader` :

```{code-cell}
import csv

nom_fichier = "entete.csv"

# Contenu supposé du fichier :
# NOM;PRENOM;AGE
# Lemarchand;John;23
# Trias;Anne;

fp = open(nom_fichier, "r", encoding="utf-8")
for ligne in csv.DictReader(fp, delimiter=";"):
    for cle, valeur in ligne.items():
        print(cle, valeur)
    print("--Fin de ligne--")
```

#### Un peu de magie...

Dans certains cas, on ne sait pas à l'avance quel délimiteur est utilisé pour le fichier CSV à lire. On peut demander au module CSV de deviner le _dialecte_[^dialect] d'un fichier en lisant le début de ce fichier.
Dans ce cas, la lecture du fichier se fera en 4 étapes :

1. Ouverture du fichier en lecture ;
2. Lecture des _n_ premiers caractères du fichier pour tenter de deviner son dialecte ;
3. "Rembobinage" du fichier pour recommencer la lecture au début ;
4. Lecture du fichier en utilisant le dialecte détecté à l'étape 2.

Le choix du paramètre _n_ doit être un compromis : il faut lire suffisamment de caractères pour que la détection de dialecte soit fiable, tout en sachant que lire beaucoup de caractères prendra du temps.
En pratique, lire les 1000 premiers caractères d'un fichier est souvent suffisant pour déterminer son dialecte.

On obtient alors une syntaxe du type :

```{code-cell}
import csv

nom_fichier = "simple.csv"

# Contenu supposé du fichier :
# 1,2,3
# a,b

fp = open(nom_fichier, "r", encoding="utf-8")  # Étape 1.
dialecte = csv.Sniffer().sniff(fp.read(1000))  # Étape 2.
fp.seek(0)                                     # Étape 3. À ne pas oublier !
for ligne in csv.reader(fp, dialect=dialecte): # Étape 4.
    for cellule in ligne:
        print(cellule)
    print("Fin de ligne")
```

[^dialect]: Le _dialecte_ d'un fichier CSV définit, en fait, bien plus que le caractère de séparation des cellules, comme décrit dans [ce document](https://tools.ietf.org/html/rfc4180).

### Fichiers _JavaScript Object Notation_ (JSON)

Les fichiers _JavaScript Object Notation_ (JSON) permettent de stocker des données structurées (par exemple avec une organisation hiérarchique). Un document JSON s'apparente à un dictionnaire en Python (à la nuance près que les clés d'un document JSON sont forcément des chaînes de caractères).
Voici un exemple de document JSON :
```json
{
    "num_etudiant": "21300000",
    "notes": [12, 5, 14],
    "date_de_naissance": {
        "jour": 1,
        "mois": 1,
        "annee": 1995
    }
}
```

En Python, pour lire de tels fichiers, on dispose du module `json` qui contient une fonction `load` :

```{code-cell}
import json

nom_fichier = "simple.json"

# Contenu supposé du fichier :
# {
#    "num_etudiant": "21300000",
#    "notes": [12, 5, 14],
#    "date_de_naissance": {
#        "jour": 1,
#        "mois": 1,
#        "annee": 1995
#    }
# }

fp = open(nom_fichier, "r", encoding="utf-8")
d = json.load(fp)
print(d)
```

Il est à noter qu'un fichier JSON peut également contenir une liste de dictionnaires, comme dans l'exemple suivant :

```json
[{
    "num_etudiant": "21300000",
    "notes": [12, 5, 14],
    "date_de_naissance": {
        "jour": 1,
        "mois": 1,
        "annee": 1995
    }
},
{
    "num_etudiant": "21300001",
    "notes": [14],
    "date_de_naissance": {
        "jour": 1,
        "mois": 6,
        "annee": 1989
    }
}]
```

Dans ce cas, `json.load` retournera une liste de dictionnaires au lieu d'un dictionnaire, bien évidemment.

Enfin, si l'on a stocké dans une variable une chaîne de caractères dont le contenu correspond à un document JSON, on peut également la transformer en dictionnaire (ou en liste de dictionnaires) à l'aide de la fonction `json.loads` (attention au "s" final) :

```{code-cell}
ch = '{"num_etudiant": "21300000",  "notes": [12, 5, 14]}'
d = json.loads(ch)  # loads : load (from) string
print(d)
```

## Écriture de fichiers textuels

Ce que nous apellons écriture de fichiers textuels en Python consiste à copier le contenu d'une (ou plusieurs) chaîne(s) de caractères dans un fichier.
Cela implique trois étapes en Python :

1. ouvrir le fichier en écriture ;
2. ajouter du contenu dans le fichier ;
3. fermer le fichier.

La première étape d'ouverture du fichier en écriture est commune à tous les types de fichiers textuels.
En supposant que le nom du fichier à ouvrir est stocké sous forme de chaîne de caractères dans la variable `nom_fichier`, le code suivant ouvre un fichier en écriture avec l'encodage UTF-8 et stocke dans la variable `fp` un pointeur sur l'endroit où nous sommes rendus dans notre écriture du fichier (pour l'instant, le début du fichier) :

```
fp = open(nom_fichier, "w", encoding="utf-8", newline="\n")
```

Le second argument (`"w"`) indique que le fichier doit être ouvert en mode _write_, donc en écriture.

Si le fichier en question existait déjà, son contenu est tout d'abord écrasé et on repart d'un fichier vide.
Si l'on souhaite au contraire ajouter du texte à la fin d'un fichier existant, on utilisera le mode _append_, symbolisé par la lettre `"a"` :

```
fp = open(nom_fichier, "a", encoding="utf-8", newline="\n")
```

Une fois les instructions d'écriture exécutées (voir plus bas), on doit fermer le fichier pour s'assurer que l'écriture sera effective :

```
fp.close()
```

Il est à noter que l'on peut, dans certains cas, se dispenser de fermer explicitement le fichier.
Par exemple, si notre code est inclus dans un script Python, dès la fin de l'exécution du script, tous les fichiers ouverts en écriture par le script sont automatiquement fermés.

### Fichiers textuels génériques

Pour ajouter du contenu à un fichier pointé par la variable `fp`, il suffit ensuite d'utiliser la méthode `write` :

```
fp.write("La vie est belle\n")
```

Notez que, contrairement à la fonction `print` à laquelle vous êtes habitué, la méthode `write` ne rajoute pas de caractère de fin de ligne après la chaîne de caractères passée en argument, il faut donc inclure ce caractère `"\n"` à la fin de la chaîne de caractères passée en argument, si vous souhaitez inclure un retour à la ligne.

### Fichiers CSV

Le module `csv` déjà cité plus haut contient également une fonction `writer` permettant de simplifier l'écriture de fichiers CSV.
La syntaxe d'utilisation de cette fonction est la suivante :

```{code-cell}
import csv

nom_fichier = "ecriture.csv"

fp = open(nom_fichier, "w", encoding="utf-8", newline="\n")
csvfp = csv.writer(fp, delimiter=";")
csvfp.writerow([1, 5, 7])
csvfp.writerow([2, 3])
fp.close()
# Après cela, le fichier contiendra les lignes suivantes :
# 1;5;7
# 2;3
```

La méthode `writerow` prend donc une liste en argument et écrit dans le fichier les éléments de cette liste, séparés par le délimiteur `";"` spécifié lors de l'appel à la fonction `writer`.
Le retour à la ligne est écrit directement par la méthode `writerow`, vous n'avez pas à vous en occuper.

### Fichiers JSON

Le module `json` déjà cité plus haut contient également une fonction `dump` permettant d'écrire le contenu d'un dictionnaire (ou d'une liste de dictionnaires) dans un fichier JSON.
La syntaxe d'utilisation de cette fonction est la suivante :

```{code-cell}
import json

nom_fichier = "ecriture.json"

liste = [
    {"a": 5},
    {"b": 3, "a": 7}
]

fp = open(nom_fichier, "w", encoding="utf-8", newline="\n")
json.dump(liste, fp)
fp.close()
# Après cela, le fichier contiendra la ligne suivante :
# [{"a": 5}, {"b": 3, "a": 7}]
```

Vous pouvez vous référer à [la documentation de cette fonction](https://docs.python.org/fr/3/library/json.html#basic-usage) pour maîtriser plus finement la mise en forme du contenu du fichier de sortie.

## Manipulation de fichiers en Python avec le module `os`

Lorsque l'on lit ou écrit des fichiers, il est fréquent de vouloir répéter la même opération sur plusieurs fichiers, par exemple sur tous les fichiers avec l'extension `".txt"` d'un répertoire donné.
Pour ce faire, on peut utiliser en Python le module `os` qui propose un certain nombre de fonctions standard de manipulation de fichiers.
On utilisera notamment la fonction `listdir` de ce module qui permet de lister l'ensemble des fichiers et sous-répertoires contenus dans un répertoire donné :

```{code-cell}
import os

for nom_fichier in os.listdir("donnees"):
    print(nom_fichier)
```

La fonction `listdir` peut prendre indifféremment un chemin absolu ou relatif (dans notre exemple, il s'agit d'un chemin relatif qui pointe sur le sous-répertoire `"donnees"` contenu dans le répertoire de travail courant du programme).

Si vous exécutez le code ci-dessus et que votre répertoire `"donnees"` n'est pas vide, vous remarquerez que le nom du fichier stocké dans la variable `nom_fichier` ne contient pas le chemin vers ce fichier.
Or, si l'on souhaite ensuite ouvrir ce fichier (que ce soit en lecture ou en écriture), il faudra bien spécifier ce chemin.
Pour cela, on utilisera la syntaxe suivante :

```
import os

repertoire = "donnees"
for nom_fichier in os.listdir(repertoire):
    nom_complet_fichier = os.path.join(repertoire, nom_fichier)
    print(nom_fichier)
    print(nom_complet_fichier)
    fp = open(nom_complet_fichier, "r", encoding="utf-8")
    # [...]
```

La fonction `path.join` du module `os` permet d'obtenir le chemin complet vers le fichier à partir du nom du répertoire dans lequel il se trouve et du nom du fichier isolé.
Il est préférable d'utiliser cette fonction plutôt que d'effectuer la concaténation des chaînes de caractères correspondantes car la forme des chemins complets dépend du système d'exploitation utilisé, ce que gère intelligemment `path.join`.

## Exercices

**Exercice 7.1**
Écrivez une fonction qui affiche, pour chaque fichier d'extension `".txt"` d'un répertoire passé en argument, le nom du fichier ainsi que son nombre de lignes.

**Exercice 7.2**
Écrivez une fonction qui retourne le nombre de fichiers présents dans un répertoire dont le nom est passé en argument.
Vous pourrez vous aider pour cela de la documentation du sous-module `path` du module `os` ([lien](https://docs.python.org/3.5/library/os.path.html)).

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

# La Programmation Orientée Objet

Dans ce chapitre, nous allons parler de programmation orientée objet.
Pour cela, nous allons tout d'abord donner une description de ce qu'est un objet et revenir sur des objets que vous avez déjà manipulé en Python.
Nous verrons ensuite comment définir vos propres objets et les utiliser.

## Les objets du quotidien

En Python, toutes les variables que vous manipulez sont en fait des objets.
Dans la suite de ce chapitre, nous allons prendre l'exemple d'un type que vous utilisez souvent, le type _chaîne de caractères_ (`str`).
En termes de vocabulaire, on dit que `"abc"` est un **objet** de la **classe** `str`.

Nous avons vu dans le chapitre dédié que l'on disposait, pour les chaînes de caractères, de fonctions permettant des manipulations élémentaires, comme par exemple passer la chaîne de caractères en minuscule :

```{code-cell}}
s = "abcDEf"
print(s.upper())
```

Vous vous êtes peut-être déjà habitué à cette syntaxe, pourtant il s'agit bien d'une syntaxe spécifique aux objets.
En fait, ici, vous demandez d'appeler la **méthode** `upper()` de l'objet `s`.
Une méthode est une fonction rattachée à un objet.

En plus des méthodes, les objets peuvent avoir des **attributs**, qui les décrivent.
Jetons un oeil à un type un peu particulier, le type _nombre complexe_ :

```{code-cell}
nombre_complexe = 10 + 5j
```

Notez qu'ici `j` permet d'identifier la partie imaginaire.
Les objets de ce type ont, en Python, un attribut qui stocke leur partie entière et un autre pour leur partie imaginaire :

```{code-cell}
print(nombre_complexe.real)
print(nombre_complexe.imag)
```

On dit que `real` et `imag` sont des **attributs** (on parle aussi de propriétés) de l'objet nombre complexe.

En résumé, nos objets ont des méthodes (qui sont des fonctions) et des attributs, et pour y accéder, on utilise la notation `objet.methode()` ou `objet.attribut`.
Il est à noter qu'une méthode peut avoir des arguments, comme toute fonction, comme dans l'exemple suivant :

```{code-cell}
print(s.find("b"))
```

## Définir vos propres objets

La librairie Python standard propose déjà un nombre important de classes (c'est-à-dire de types) pré-définies.
Pour définir une nouvelle classe, on utilise la syntaxe suivante :

```{code-cell}
class Voiture:
    def __init__(self):
        self.couleur = "rouge"
        self.nombre_roues = 4
    
    def repeindre(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur
```

On a défini ici une nouvelle classe : la classe `Voiture`.
Les objets de cette classe ont deux attribut : `couleur` et `nombre_roues` et une méthode `repeindre(nouvelle_couleur)`.

Voyons comment créer un nouvel objet de cette classe :

```{code-cell}
ma_twingo = Voiture()
```

Lors de la définition d'un nouvel objet, la méthode `__init__()` est appelée pour "construire" ce nouvel objet, et lui attribuer les bonnes propriétés.
On peut accéder à la couleur de `ma_twingo` pour s'en convaincre :

```{code-cell}
print(ma_twingo.couleur)
```

De même, on peut utiliser ses méthodes :

```{code-cell}
ma_twingo.repeindre("rose")
print(ma_twingo.couleur)
```

````{admonition} Le mot-clé self
:class: warning

Dans tous les cas que vous rencontrerez dans ce cours, le premier argument d'une méthode sera `self`.
Cet argument dénote l'objet sur lequel on est en train de travailler.
Ainsi, lorsqu'on écrit :

```python
    def repeindre(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur
```

le sens de ce code est le suivant : 

* on définit une méthode `repeindre` qui aura **un seul** argument (il ne faut pas compter `self` qui est un argument spécial)
* lorsque l'on appelle cette méthode avec une syntaxe du type `ma_twingo.repeindre("rose")`, cette méthode a pour effet de modifier la valeur de l'attribut `couleur` de l'objet `ma_twingo` (celui sur lequel la méthode est appelée)
````

### La notion d'héritage

Dès lors que l'on va introduire plusieurs nouvelles classes dans nos programmes, il arrivera que nos classes partagent un certain nombre d'attributs, voire de méthodes.
Si l'on reprend l'exemple de notre classe `Voiture` et que l'on imagine qu'il doive exister une classe `Velo`, il peut s'avérer pertinent de définir une classe **mère**, nommée `Vehicule`, comme suit :

```{code-cell}
class Vehicule:
    def __init__(self):
        self.couleur = "rouge"

    def repeindre(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur


class Voiture(Vehicule):
    def __init__(self):
        super().__init__()
        self.nombre_roues = 4


class Velo(Vehicule):
    def __init__(self):
        super().__init__()
        self.nombre_roues = 2
    
    def repeindre(self, nouvelle_couleur):
        print("Quelle joie de repeindre mon vélo !")
        self.couleur = nouvelle_couleur
```

Dans le code ci-dessous, on décide que lors de la construction d'un nouveau véhicule, sa couleur sera `"rouge"` et on disposera d'une méthode pour le repeindre.
On fait aussi le choix de dire que les classes `Voiture` et `Velo` **héritent** de la classe `Vehicule` (on le spécifie en écrivant `class Voiture(Vehicule)`).
En héritant de cette classe, elles récupèrent tout ce qui existait pour cette classe (la couleur par défaut et la méthode pour repeindre).
Chacune des classes définit en outre un attribut `nombre_roues`.

Pour créer un nouvel objet `Voiture` ou `Velo`, on peut alors faire :

```{code-cell}
ma_twingo = Voiture()
mon_vtt = Velo()

print(ma_twingo.couleur, ma_twingo.nombre_roues)
print(mon_vtt.couleur, mon_vtt.nombre_roues)
```

De plus, même si on ne le voit pas directement dans le code, grâce à l'héritage, la méthode `repeindre` existe pour les objets de ces classes :

```{code-cell}
ma_twingo.repeindre("bleu")
print(ma_twingo.couleur)
```

Regardons de plus près ce qui se passe lorsqu'on crée un nouvel objet `Velo`.

```python
class Velo(Vehicule):
    def __init__(self):
        super().__init__()
        self.nombre_roues = 2
```

Lors de la création d'un nouvel objet, comme pour n'importe quelle classe, la méthode `__init__` est appelée.
À l'intérieur de cette méthode, deux choses sont faites :

1. `super().__init__()` signifie que l'on appelle le constructeur de la classe mère, soit `Vehicule` : cela permet de définir un attribut `couleur` dont la valeur sera `"rouge"`
2. `self.nombre_roues = 2` permet de définir un nouvel attribut `nombre_roues` dont la valeur est fixée à 2

De plus, vous remarquez que la classe `Velo` redéfinit la méthode `repeindre`.
On dit que la classe `Velo` **surcharge** la méthode `repeindre`.

Dans ce cas, au lieu de réutiliser la méthode `repeindre` de `Vehicule`, si l'on appelle la méthode `repeindre` pour un objet de la classe `Velo`, c'est cette nouvelle version qui sera utilisée :

```{code-cell}
mon_vtt.repeindre("bleu")
```

```{code-cell}
print(mon_vtt.couleur)
```


### Les méthodes spéciales

Il existe des opérations "spéciales" que l'on peut vouloir effectuer sur des objets.
On peut par exemple vouloir les afficher via `print()`, ou les sommer.
Pour cela, on fait appel à des **méthodes spéciales**.

Prenons un nouvel exemple : supposons que l'on veuille créer une classe pour stocker des vecteurs du plan (des paires de flottants, autrement dit).
Une première définition pour la classe `Vecteur` correspondante pourrait être la suivante :

```{code-cell}
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

En d'autres termes, on définit un nouveau vecteur en spécifiant ses coordonnées dans le plan, ce qui donne :

```{code-cell}
v0 = Vecteur(1.5, -1.)
print(v0)
```

Ici, on a bien défini notre nouveau vecteur, mais par contre l'affichage laisse à désirer (en tout cas, il ne nous permet pas de savoir ce que contient notre vecteur).
On va donc ajouter une nouvelle méthode dont le nom nous est imposé : la méthode `__repr__()` qui permet de définir la **représentation** sous forme de chaîne de caractères d'un objet :

```{code-cell}
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"


v0 = Vecteur(1.5, -1.)
print(v0)
```

On voit bien ici que, même si on n'appelle pas explicitement la méthode `__repr__`, elle est appelée dès lors que l'on doit obtenir une représentation d'un objet sous la forme d'une chaîne de caractères.

De la même façon, on peut vouloir définir le résultat de l'opération `v0 + v1` où `v0` et `v1` sont des vecteurs.
On devra pour cela définir une méthode `__add__` :

```{code-cell}
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"
    
    def __add__(self, autre_vecteur):
        nouveau_vecteur = Vecteur(x=self.x + autre_vecteur.x,
                                  y=self.y + autre_vecteur.y)
        return nouveau_vecteur


v0 = Vecteur(1.5, -1.)
v1 = Vecteur(1., 0.)
v_somme = v0 + v1
print(v_somme)
```

Ici, lorsque l'on écrit `v0 + v1`, tout se passe comme si cette expression était remplacée par `v0.__add__(v1)`.

De nombreuses méthodes spéciales peuvent ainsi être définies :

Méthode spéciale | Opérateur
---|---
`__add__(self, o)` | `+`
`__sub__(self, o)` | `-`
`__mul__(self, o)` | `*`
`__truediv__(self, o)` | `/`
`__pow__(self, o)` | `**`
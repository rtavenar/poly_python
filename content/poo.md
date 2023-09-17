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

```{code-cell}
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
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def translation(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
```

On a défini ici une nouvelle classe : la classe `Vecteur`.
Les objets de cette classe ont deux attribut : `x` et `y` et une méthode `translation(self, delta_x, delta_y)`.

Voyons comment créer un nouvel objet de cette classe :

```{code-cell}
mon_vecteur = Vecteur(0., 2.)
```

Lors de la définition d'un nouvel objet, la méthode `__init__()` est appelée pour "construire" ce nouvel objet, et lui attribuer les bonnes propriétés.
On peut accéder aux attributs de `mon_vecteur` pour s'en convaincre :

```{code-cell}
print(mon_vecteur.x, mon_vecteur.y)
```

De même, on peut utiliser ses méthodes :

```{code-cell}
mon_vecteur.translation(delta_x=1., delta_y=0.)
print(mon_vecteur.x, mon_vecteur.y)
```

````{admonition} Le mot-clé self
:class: warning

Dans tous les cas que vous rencontrerez dans ce cours, le premier argument d'une méthode sera `self`.
Cet argument dénote l'objet sur lequel on est en train de travailler.
Ainsi, lorsqu'on écrit :

```python
    def translation(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
```

le sens de ce code est le suivant : 

* on définit une méthode `translation` qui aura **deux** arguments (il ne faut pas compter `self` qui est un argument spécial)
* lorsque l'on appelle cette méthode avec une syntaxe du type `mon_vecteur.translation(delta_x=1., delta_y=0.)`, cette méthode a pour effet de modifier la valeur des attributs `x` et `y` de l'objet `mon_vecteur` (celui sur lequel la méthode est appelée)
````

### Les méthodes spéciales

Il existe des opérations "spéciales" que l'on peut vouloir effectuer sur des objets.
On peut par exemple vouloir les afficher via `print()`, ou les sommer.
Pour cela, on fait appel à des **méthodes spéciales**.

Définissons par exemple un nouveau vecteur en spécifiant ses coordonnées dans le plan, et affichons-le :

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

### Les attributs calculés

Dans certains cas, on aimerait rajouter à nos objets des attributs qui pourraient être calculés à la volée.
Si l'on reprend l'exemple de la classe `Vecteur` plus haut, on peut d'ores et déjà accéder à ses attributs `x` et `y` :

```{code-cell}
v1 = Vecteur(1., 0.)
print(v1.x, v1.y)
```

On pourrait vouloir accéder à la norme de ce vecteur _via_ un attribut qui serait calculé à la volée, en fonction des valeurs des attributs `x` et `y`, et cela est possible en Python.
Pour cela, il faut définir une méthode `norme` qui ne prenne que `self` comme argument et la "décorer" avec le décorateur `@property` (on rappelle que les attributs peuvent également être qualifiés de propriétés) :

```{code-cell}
from math import sqrt

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def norme(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"
    
    def __add__(self, autre_vecteur):
        nouveau_vecteur = Vecteur(x=self.x + autre_vecteur.x,
                                  y=self.y + autre_vecteur.y)
        return nouveau_vecteur


v1 = Vecteur(1., 0.)
print(v1.norme)
```

## La notion d'héritage

Dès lors que l'on va introduire plusieurs nouvelles classes dans nos programmes, il arrivera que nos classes partagent un certain nombre d'attributs, voire de méthodes.

Prenons pour cela un nouvel exemple.
Imaginons que l'on souhaite représenter des véhicules, qui pourront être des vélos ou bien des voitures.
Dans ce cas, on va définir une classe **mère**, nommée `Vehicule`, et deux classes filles `Voiture` et `Velo` comme suit :

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

Dans le code ci-dessus, on décide que lors de la construction d'un nouveau véhicule, sa couleur sera `"rouge"` et on disposera d'une méthode pour le repeindre.
On fait aussi le choix de dire que les classes `Voiture` et `Velo` **héritent** de la classe `Vehicule` (on le spécifie en écrivant `class Voiture(Vehicule)`).
En héritant de cette classe, elles récupèrent tout ce qui existait pour cette classe (la couleur par défaut et la méthode pour repeindre).
Chacune des classes définit en outre un attribut `nombre_roues`.

Enfin, les instructions `super().__init__()` sont à comprendre comme "exécuter la méthode `__init__` de la classe parente", le mot-clé `super()` étant l'équivalent de `self` pour la classe parente.

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

### L'héritage multiple

Dans certains cas, on souhaitera qu'une classe hérite de deux (ou plus) classes parentes à la fois.
Ce mécanisme s'appelle l'héritage multiple et il est tout à fait possible de le mettre en oeuvre en Python :

```{code-cell}
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

Dans le code ci-dessus, on définit une classe `C` qui hérite des classes `A` et `B`.

Dans le cas de l'héritage multiple, le rôle de `super()` est ambigu puisqu'on a plusieurs classes parentes.
Développons un petit peu le code du dessus pour mieux voir comment tout cela se déroule :

```{code-cell}
class A:
    def __init__(self):
        print("Init A")
        super().__init__()

class B:
    def __init__(self):
        print("Init B")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("Init C")
        super().__init__()

c = C()
```

L'affichage nous démontre que les constructeurs des deux classes parentes ont bien été appelés, dans l'ordre dans lequel elles ont été déclarées par `class C(A, B)` (donc le constructeur de `A` est appelé avant celui de `B`).

Il est important de noter ici que, pour que cet ordre d'appel soit effectif, il faut que chacune des classes concernées fasse appel au constructeur de sa classe parente (`super().__init__()`) dans son propre constructeur.

### Classes abstraites

Les classes abstraites sont des classes un peu spéciales au sens où on ne pourra pas les instancier.
Ces classes servent en conséquence à définir un modèle dont d'autres classes hériteront, et ce sont ces classes filles qui pourront être instanciées.

En Python, pour définir une classe abstraite, il suffit de la faire hériter de la classe `ABC` (_Abstract Base Class_) du module `abc` :

```{code-cell}
---
tags: [raises-exception]
---

from abc import ABC

class Vehicule(ABC):
    def __init__(self):
        self.couleur = "rouge"

    def repeindre(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur


class Voiture(Vehicule):
    def __init__(self):
        super().__init__()
        self.nombre_roues = 4

v = Vehicule()
```

Comme vous le voyez dans le code ci-dessus, si l'on tente d'instancier la classe abstraite `Vehicule`, on obtient une erreur.

Par contre, on peut toujours instancier la classe fille `Voiture` :

```{code-cell}
v = Voiture()
v.repeindre("bleu")
print(v.nombre_roues, v.couleur)
```

Dans certains cas, on voudra spécifier dans la classe mère abstraite des méthodes (ou attributs calculés) à implémenter dans la ou les classes filles.
Cela peut se faire en définissant ces méthodes dans la classe mère et en les décorant avec les décorateurs `@abstractmethod` (ou `@abstractproperty`, selon le cas) comme dans l'exemple suivant :

```{code-cell}

from abc import abstractmethod

class Vehicule(ABC):
    def __init__(self):
        self.couleur = "rouge"

    def repeindre(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur

    @abstractmethod
    def reinitialiser(self):
        # Le code ci-dessous importe peu puisque 
        # la méthode devra être redéfinie dans les 
        # classes filles
        pass


class Voiture(Vehicule):
    def __init__(self):
        super().__init__()
        self.nombre_roues = 4
    
    def reinitialiser(self):
        self.nombre_roues = 4
        self.repeindre("rouge")

v = Voiture()
```

Si, par contre, on n'implémente pas la méthode abstraite dans l'une des classes filles, cette classe ne pourra pas être instanciée :

```{code-cell}
---
tags: [raises-exception]
---

class Velo(Vehicule):
    def __init__(self):
        super().__init__()
        self.nombre_roues = 2

v = Velo()
```

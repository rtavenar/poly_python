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

# Récupération de données à partir d'API web

De nombreux services web fournissent des API (_Application Programming Interface_) pour mettre des données à disposition du grand public. Le principe de fonctionnement de ces API est le suivant : l'utilisateur effectue une requête sous la forme d'une requête HTTP, le service web met en forme les données correspondant à la requête et les renvoie à l'utilisateur, dans un format défini à l'avance.

Voici une liste (très loin d'être exhaustive) d'API web d'accès aux données :

* Google Maps
    * Directions API : permet de calculer des itinéraires ;
    * Elevation API : permet de calculer l'altitude d'un point sur le globe terrestre ;
    * Distance Matrix API : permet de calculer des distances entre points du globe ;
    * Geocoding API : permet d'associer une coordonnée GPS à une adresse.
* Twitter
    * Twitter API : permet de récupérer des informations sur les utilisateurs du réseau et leurs _tweets_.
* Facebook
    * Facebook Graph API : permet de récupérer des informations sur des utilisateurs Facebook .
* STAR (Transports en commun rennais)
    * Horaires des bus ;
    * Disponibilité des vélos dans les relais VéloStar.

+++

Pour manipuler en Python de telles données, il faudra donc être capable :

1. d'envoyer une requête HTTP et de récupérer le résultat ;
2. de transformer le résultat en une variable Python facilement manipulable.

Pour ce qui est du second point, la plupart des API web offrent la possibilité de récupérer les données au format JSON.
Nous avons vu précédemment dans ce cours que ce format était facilement manipulable en Python, notamment parce qu'il est très proche de la notion de dictionnaire.
Ce chapitre se focalise donc sur la réalisation de requêtes HTTP en Python.

## Requêtes HTTP en Python

### Format d'une requête HTTP

Dans un premier temps, étudions le format d'une requête HTTP, telle que vous en effectuez des dizaines chaque jour, par l'intermédiaire de votre navigateur web.
Lorsque vous entrez dans la barre d'adresse de votre navigateur l'URL suivante :

```
http://people.irisa.fr/Romain.Tavenard/index.php?page=3
```

votre navigateur va envoyer une requête au serveur concerné (cette requête ne contiendra pas uniquement l'URL visée mais aussi d'autres informations sur lesquelles nous ne nous attarderons pas ici).
Dans l'URL précédente, on distingue 4 sous parties :

* `http://` indique le protocole à utiliser pour effectuer la requête (ici HTTP). Dans ce chapitre, nous ne nous intéresserons qu'aux protocoles HTTP et HTTPS (version sécurisée du protocole HTTP) ;
* `people.irisa.fr` est le nom de domaine du serveur (_ie._ de la machine) à contacter pour obtenir une réponse ;
* `/Romain.Tavenard/index.php` indique le chemin du fichier à récupérer sur cette machine ;
* `?page=3` indique que l'on doit passer la valeur `3` au paramètre `page` lors de la requête.

De la même façon, lors d'un appel à une API web, on spécifiera le protocole à utiliser, la machine à contacter, le chemin vers la ressource voulue et un certain nombre de paramètres qui décriront notre requête.
Voici un exemple de requête à une API web (l'API Google Maps Directions en l'occurrence) :
```
https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal
```

Vous pouvez copier/coller cette URL dans la barre d'adresse de votre navigateur et observer ce que vous obtenez en retour.
Observez que le résultat de cette requête est au format JSON.
En fait, si vous étudiez plus précisément l'URL fournie, vous verrez que c'est nous qui avons demandé à obtenir le résultat dans ce format.
De plus, on a spécifié dans l'URL que l'on souhaitait obtenir les informations d'itinéraire pour aller de Toronto (paramètre `origin`) à Montreal (paramètre `destination`).

Vous devez aussi remarquer que, en réponse à cette requête, l'API Google Maps renvoie en fait un message d'erreur.
En effet, pour être autorisé à utiliser cette API, il faut disposer d'une clé d'API et renseigner cette clé sous la forme d'un paramètre supplémentaire (nommé `key` dans les API Google Maps par exemple).
Ainsi, la requête précédente deviendrait :
```
https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=VOTRE_CLE
```

dans laquelle vous devrez remplacer `VOTRE_CLE` par une clé que vous aurez préalablement générée et qui vous permettra d'utiliser le service web de manière authentifiée.
Pour créer une clef d'API, il faut se rendre sur l'interface développeur de l'API concernée ([ici](https://developers.google.com/maps/documentation/directions/start?hl=fr) pour l'API _Google Maps Directions_ par exemple).

### Utilisation du module `requests`

```{admonition} Les requêtes HTTP en (très) bref
  :class: tip

Dans le protocole HTTP, il existe plusieurs types de requêtes pour réaliser l'échange entre le client et le serveur.
En particulier les requêtes de type GET sont très utilisées lorsque le client demande une ressource au serveur.
Il s'agit d'une requête de téléchargement d'un document.
Il est possible de transmettre des paramètres pour filtrer la réponse ; dans ce cas, les paramètres seront transférés "en clair" (dans l'URL utilisée pour la requête).

Les requêtes de type POST permettent comme GET de télécharger un document du serveur vers le client mais avec un plus de sophistication : les paramètres sont masqués et il est possible de demander de mettre à jour des données sur le serveur à l'occasion de la requête.

Il existe d'autres requêtes HTTP que nous ne détaillons pas ici.
```

````{margin}
```{admonition} Installer un paquet Python
  :class: tip

Le module `requests` ne fait pas partie de la librairie standard en Python.
Il faut donc l'installer avant de pouvoir l'utiliser.
Pour ce faire, on peut utiliser le gestionnaire de paquets `pip`.

Si vous utilisez Anaconda, la documentation en ligne disponible à [cette adresse](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/) explique la marche à suivre pour installer de nouveaux paquets dans votre version de Python fournie par Anaconda.
Si vous utilisez plutôt l'IDE PyCharm et une version de Python non fournie par Anaconda, vous pourrez trouver de la documentation [à cette adresse](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html).
```
````

La section précédente proposait un rappel sur le format des requêtes HTTP et vous avez été invités à effectuer des requêtes HTTP à l'aide de votre navigateur.
Si maintenant on souhaite récupérer de manière automatique le résultat d'une requête HTTP pour le manipuler en Python, le plus commode est d'effectuer la requête HTTP depuis Python.
Pour cela, on utilise le module `requests`.
Ce module contient notamment une fonction `get` qui permet d'effectuer des requêtes HTTP de type GET (je vous laisse deviner le nom de la fonction qui permet d'effectuer des requêtes HTTP POST :) :

```{code-cell}
import requests

url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

reponse = requests.get(url)
print(reponse)
```

On voit ici que l'on a reçu une réponse de code 200, ce qui signifie que la requête s'est déroulée correctement.

```{admonition} Codes de retour HTTP
  :class: tip, dropdown

Voici quelques codes de retour de requêtes HTTP qui peuvent vous être utiles :
* 20x : la transaction s'est bien déroulée
  * _ex._ 200 : la requête s'est effectuée correctement
* 40x : erreur "due au client"
  * _ex._ 404 : page non trouvée
* 50x : erreur "due au serveur"
  * _ex._ 504 : Temps imparti écoulé
```

```{code-cell}
contenu_txt = reponse.text
print(type(contenu_txt))
```

```{code-cell}
contenu = reponse.json()
print(type(contenu))
```

```{code-cell}
print(contenu)
```

On voit ici qu'il est possible d'obtenir le résultat de notre requête sous deux formes : le texte brut du résultat qui est stocké dans `reponse.text` et la version mise en forme (sous la forme de dictionnaire ou de liste) de ce résultat que l'on obtient via `reponse.json()`.

De plus, si l'on souhaite passer des paramètres à la requête HTTP (ce qui se trouvait après le symbole `?` dans les URL ci-dessus), il est possible de le faire lors de l'appel à `requests.get` :

```{code-cell}
import requests

url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

reponse = requests.get(url, params="userId=3")
contenu = reponse.json()
print(contenu)
```

Le code ci-dessus correspond ainsi à ce que vous obtiendriez dans votre navigateur en entrant l'URL <http://my-json-server.typicode.com/rtavenar/fake_api/tasks?userId=3>.

En pratique, dans de nombreux cas, des modules Python existent pour permettre d'utiliser les API grand public sans avoir à gérer les requêtes HTTP directement.
C'est par exemple le cas des modules [`tweepy`](http://docs.tweepy.org/en/latest/) (pour l'API Twitter) ou [`graphh`](https://graphh.readthedocs.io/en/latest/) (qui permet d'accéder à l'API GraphHopper qui est un équivalent libre de Google Maps)[^graphh].

[^graphh]: Notez que le module `graphh` a été développé par d'anciens étudiants de Licence 2 et Licence 3 MIASHS de l'Université de Rennes 2.

## Exercice

```{admonition} **Exercice 9.1**
Écrivez une fonction qui prenne en entrée une liste de `userId` et affiche l'ensemble des entrées de l'API <http://my-json-server.typicode.com/rtavenar/fake_api/tasks> pour lesquelles l'attribut `completed` vaut `True`.
```

````{admonition} Solution
:class: tip, dropdown

* Solution 1

```python
import requests

def affiche_api(liste_userId):
    url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"
    contenu = requests.get(url)
    list_taches = contenu.json()
    for tache in list_taches:
        if tache["completed"] and tache["userId"] in liste_userId:
            print(tache)

affiche_api([1, 3])
```

* Solution 2 : en utilisant les paramètres d'URL

```python
import requests

def affiche_api(liste_userId):
    url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"
    contenu = requests.get(url, params="completed=true")
    list_taches = contenu.json()
    for tache in list_taches:
        if tache["userId"] in liste_userId:
            print(tache)

affiche_api([1, 3])
```
````
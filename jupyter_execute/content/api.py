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

### Utilisation du module `requests`

La section précédente proposait un rappel sur le format des requêtes HTTP et vous avez été invités à effectuer des requêtes HTTP à l'aide de votre navigateur.
Si maintenant on souhaite récupérer de manière automatique le résultat d'une requête HTTP pour le manipuler en Python, le plus commode est d'effectuer la requête HTTP depuis Python.
Pour cela, on utilise le module `requests`. Ce module contient notamment une fonction `get` qui permet d'effectuer des requêtes HTTP de type GET (je vous laisse deviner le nom de la fonction qui permet d'effectuer des requêtes HTTP POST :) :

import requests

url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

reponse = requests.get(url)
print(reponse)

contenu_txt = reponse.text
print(type(contenu_txt))

contenu = reponse.json()
print(type(contenu))

print(contenu)

On voit ici qu'il est possible d'obtenir le résultat de notre requête sous deux formes : le texte brut du résultat qui est stocké dans `reponse.text` et la version JSON de ce résultat que l'on obtient via `reponse.json()`.

De plus, si l'on souhaite passer des paramètres à la requête HTTP (ce qui se trouvait après le symbole `?` dans les URL ci-dessus), il est possible de le fait lors de l'appel à `requests.get` :

import requests

url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

reponse = requests.get(url, params="userId=3")
contenu = reponse.json()
print(contenu)

Le code ci-dessus correspond ainsi à ce que vous obtiendriez dans votre navigateur en entrant l'URL <http://my-json-server.typicode.com/rtavenar/fake_api/tasks?userId=3>.

En pratique, dans de nombreux cas, des modules Python existent pour permettre d'utiliser les API grand public sans avoir à gérer les requêtes HTTP directement.
C'est par exemple le cas des modules [`tweepy`](http://docs.tweepy.org/en/latest/) (pour l'API Twitter) ou [`graphh`](https://graphh.readthedocs.io/en/latest/) (qui permet d'accéder à l'API GraphHopper qui est un équivalent libre de Google Maps)[^graphh].

[^graphh]: Notez que le module `graphh` a été développé par d'anciens étudiants de Licence 2 et Licence 3 MIASHS de l'Université de Rennes 2.

## Exercice

**Exercice 8.1**
Écrivez une fonction qui prenne en entrée une liste de `userId` et affiche l'ensemble des entrées de l'API <http://my-json-server.typicode.com/rtavenar/fake_api/tasks> pour lesquelles l'attribut `completed` vaut `True`.
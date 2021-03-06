# ThreePebbles


>Projet de création d'*une* IA par supervision sur le jeu : **Les 3 cailloux**


## Règles du jeu


Le jeu des **3 cailloux** est un célèbre jeu français compréhensible par tous.
Il consiste dans sa forme la plus simple en une confrontation de 2 joueurs possèdent chacun 3 cailloux.
La partie se déroule sous forme de tour ayant le même fonctionnement hormi le fait que la personne qui *prédit* en premier alterne à chacun des tours.

- Au début de la partie, on tire au sort le joueur qui commencera.
- Les 2 joueurs choisissent sans montrer à leur adversaire un nombre de cailloux qu'ils mettent dans leur main. (Ce nombre doit être compris entre 0 et le nombre de cailloux que possède le joueur.)
- Les 2 tendent ensuite leurs mains remplis de cailloux sur une table afin d'éviter une tricherie éventuelle.
- Le joueur tiré au sort donne sa prédiction sur le nombre total de cailloux que les 2 joueurs ont dans leurs mains.
- C'est ensuite au tour du second joueur de donner sa prédiction qui doit être forcément différente de celle de son adversaire.
- Les 2 joueurs ouvrent alors leurs mains ce qui implique 2 possibilités :
1. -  Aucun des 2 joueurs n'a deviné le nombre total de cailloux, ils reprennent donc tous les 2 leurs cailloux.
2. - Un des 2 joueurs a réussi à deviner le nombre total de cailloux présents. Auquel cas, celui-ci s'allège d'un de ses cailloux qu'il pose sur la table.
- La partie reprend donc en inversant la personne qui donne sa prédiction en premier jusqu'à ce qu'un des joueurs n'est plus aucun cailloux, faisant ainsi de lui le vainqueur de la partie.

>A noter qu'une partie pourrait dans l'absolu avoir un nombre illimité de joueurs et de cailloux au départ.


## Préparation

Pour pouvoir utiliser les différents programmes, vous allez devoir installer plusieurs modules.
Ceux-ci sont obligatoires afin que le code puisse s'executer.
Pour cela, veuillez les installer grace à **pip** (par exemple).

Liste les bibliotèques :

- csv
- joblib
- math
- matplotlib
- numpy
- pandas
- pickle
- random
- sklearn
- sys
- time
- warnings

>Tous les modules utilisés sont trouvables dans `./Code/main/modules.py`


## Utilisation du programme

Afin d'utiliser les différents programmes, veuiller vous munir d'une version de **Python3**.

>Nous executerons les différentes parties du projets depuis la racine de ce dernier.

 Pour lancer la partie pricipale de programme :
 
`python3 ./Code/main/main.py`

>A noter que les différents modèles des IA sont déjà présents, vous pouvez cependant regénérer des données pour générer les votres.


## Génération des données et entrainement de l'IA

>Des datasets sont déjà présents dans `./DataSets/` mais vous pouvez aussi générer le votre.

Pour cela : 

`python3 ./Code/main/generator.py`

>Vous pouvez vous rendre dans le fichier `./Code/main/generator.py` pour modifier différentes valeurs suivant ce que vous voulez obtenir.

Pensez ensuite à déplacer le dataset créé dans le sous dossier de `./DataSets/` que vous désirez.

>std = Standart (3 cailloux), +1 = 4 cailloux ...

Ensuite :

`python3 ./Code/IA/script.py`

>Ce fichier permet de "générer" les 2 IA qui serviront à jouer au jeu.
>Veuillez ensuite déplacer les 2 modèles créés dans le dossier `./Modeles` ou exécuter la commande dans ce dernier en changement le chemin relatif.


## Tournois (comparaison des modèles)

>Vous pouvez réaliser des tournois grâce aux différents modèles pour tester leur efficacité.

Pour le tournoi contre un joueur jouant aléatoirement :

`python3 ./Code/main/tournoiIAvsRandom.py`

Pour tester les différents modèles les uns contre les autres :

`python3 ./Code/main/tournoiIAvsIA.py`


## Jouez vous même au jeu

Vous avez 2 choix possibles :

- Jouer contre un *joueur aléatoire* (qui joue de manière aléatoire).
- Jouer contre l'IA (qui prend les 2 modèles spécifiés dans `./Code/games/gameHumanvsIA`).

Pour cela :

`python3 ./Code/games/gameHumanvsRandom.py`
ou
`python3 ./Code/games/gameHumanvsIA.py`

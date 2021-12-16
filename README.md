# ThreePebbles

Projet de création d'une IA par renforcement sur le jeu : Les 3 cailloux.

## Règles du jeu

Le jeu des "3 cailloux" est un célèbre jeu français comprehensible par tous.
Il consiste dans sa forme la plus simple en une confrontation de 2 joueurs possèdant chacun 3 cailloux.
La partie se déroule sous forme de tour, chacun ayant le même fonctionnement hormi le fait que la personne qui "prédit" un premier alterne à chacun des tours.

- Au début de la partie, on dire au sort le joueur qui commencera.
- Les 2 joueurs choisissent sans le montrer à leur adversaire un nombre de cailloux qu'ils mettent dasn le main. (Celui-ci peut être nul et a pour valeur maxiamle le nombre de cailloux qu'ils possèdent.)
- Les 2 tendent ensuite la main remplie de cailloux sur une table afin d'éviter une tricherie éventuelle.
- Le jeu tiré au sort donne donc sa prédiction sur le nombre total de cailloux que les 2 joueurs ont dasn leurs mains.
- C'est au tour du second joueur de donner sa prédiction qui doit être forcément différente de celle de son adversaire.
- Les 2 joueurs ouvrent alors leurs mains ce qui implique 2 possibilités :
-- 1. Aucun des 2 joueurs n'a deviné le nombre total de cailloux, ils reprennet donc tous les 2 leur cailloux.
-- 2. Un des 2 joueurs a réussi à deviner le nombre total de cailloux présent. Au quel cas, celui-ci s'allège d'un de ses cailloux qu'il pose sur la table.
- La partie reprend donc en inversant la personne qui donne sa prédiction en premier jusqu'à ce qu'un des joueurs n'est plus aucun cailloux, faisant ainsi de lui le vainqueur de la partie.

A noter qu'une partie pourrait dans l'absolu avoir un nombre illimité de joueurs et des cailloux au départ.

# Open the Lock

## Description:
Pour ouvrir le cadenas, tu as quatre roues circulaires devant toi. Chaque roue a dix positions : de '0' à '9'. Les roues peuvent tourner librement et revenir à leur position initiale : par exemple, on peut passer de '9' à '0', ou de '0' à '9'. Chaque mouvement consiste à tourner une roue d'une position.

Le cadenas démarre initialement à '0000', une chaîne représentant l'état des quatre roues.

On te donne une liste de codes bloquants, ce qui signifie que si le cadenas affiche l'un de ces codes, les roues du cadenas s'arrêteront de tourner et tu ne pourras pas l'ouvrir.

Étant donné une cible représentant la valeur des roues qui déverrouillera le cadenas, retourne le nombre total minimum de mouvements nécessaires pour ouvrir le cadenas, ou -1 s'il est impossible de l'ouvrir.

## Algorithme et Data Structure:
* Breadth First Search (BFS)
* Array 
* Queue
* Hash Map 
* String

## Excecution du programme
* Clone le projet
```
git clone https://github.com/bylaye/OpenTheLock.git
```
* Place sur le repertoire du projet et run le main file
```
python3 main.py
```

## References:
Leetcode 752. Open The Lock
https://leetcode.com/problems/open-the-lock/description/
# Calcul des nombres pernicieux dans un intervalle

Ce programme en Python permet de calculer le nombre de nombres pernicieux dans un intervalle donné [x, y]. 

## Nombre "pernicieux" ? 

Un nombre est dit "pernicieux" s'il a un nombre premier de facteurs premiers impairs.

## Comment utiliser le programme

Le programme se compose de deux fonctions : "isPrime(n)" et "countPerniciousNumbers(x, y)".

La fonction "isPrime(n)" prend un nombre entier en entrée et renvoie True s'il est premier, sinon False.

La fonction "countPerniciousNumbers(x, y)" prend deux arguments x et y, qui définissent l'intervalle dans lequel nous voulons chercher des nombres pernicieux. 
La fonction utilise une boucle pour parcourir tous les nombres de x à y. Pour chaque nombre, elle calcule le nombre de facteurs premiers impairs en utilisant une boucle imbriquée. Si ce nombre de facteurs premiers impairs est lui-même premier, alors le nombre est pernicieux et le compteur est incrémenté. Enfin, la fonction renvoie le nombre total de nombres pernicieux dans l'intervalle.

Pour utiliser le programme, vous pouvez ouvrir le fichier "pernicious_numbers.py" dans votre éditeur de code Python et exécuter la fonction "countPerniciousNumbers(x, y)" avec les arguments x et y de votre choix.

Voici un exemple de code qui utilise la fonction "countPerniciousNumbers" pour calculer le nombre de nombres pernicieux dans l'intervalle [1, 100] :

```python
from pernicious_numbers import countPerniciousNumbers

count = countPerniciousNumbers(1, 100)
print(f"Nombre de nombres pernicieux dans l'intervalle [1, 100] : {count}")
```


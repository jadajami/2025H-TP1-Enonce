#Exo 5 

import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
print("Vitesse initiale (en m/s): ")
vitesseact=float(input())

# Demander l'angle de lancement
print("Angle de lancer (en degrés): ")
angle=float(input())

# Convertir l'angle en radians

anglerad=angle*(math.pi/180)

# Calculer la distance maximale en x

distance=((vitesseact**2)*math.sin(2*anglerad))/g

# Afficher la distance maximale arrondie à 2 chiffres après la virgule

print("La distance maximale est de : ",round(distance,2),"m")


# Exemple:
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m
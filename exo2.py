
#Exo 2

# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie

print("Entrez le niveau de charge actuel de la batterie : ")
batterieact=float(input())

# Vérifiez si le niveau de charge est valide
if 0<=batterieact<=100:
    # Arrondir le pourcentage à la dizaine la plus proche

    round(batterieact)

    # Calculer le nombre de barres

    nbrbarre=int(batterieact/12)
    round(nbrbarre)
    barre="❚"

    # Afficher la représentation graphique de la charge de la batterie

    barreaff=print(barre*nbrbarre)
    print(batterieact,"%")

else:
    print("Erreur : niveau de charge invalide.")

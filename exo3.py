#Exo 3 
import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

# Calculer le discriminant et assigner la valeur dans la variable "delta"
# delta = ...

delta=b**2 - 4*a*c
print(delta)
# Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
# naPasDeSolution = ...

naPasDeSolution=delta<0

if naPasDeSolution:
    print("Aucune racine!")
    pass

else:
    # Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    # aUneSeuleSolution = ...

    aUneSeuleSolution=delta==0


    if aUneSeuleSolution:
        # ces ligne de code seront executé si il y'a une seule racine
        print("Une seule racine")

        x1=-b/2*a

        print("x1 = ",x1)
        pass

    else:
        # Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
        # aDeuxSolutions = ...

        aDeuxSolutions=delta>0

        if aDeuxSolutions:
            # afficher sur l'écran "Deux racines"
            print("Deux racines")
            # calculer la prmiere racine, assigner la a "x1"
            x1=(-b+((b**2-4*a*c)**0.5))/2*a
            # calculer la deuxieme racine, assigner la a "x2"
            x2=(-b-((b**2-4*a*c)**0.5))/2*a
            print("x1 = ", x1, ", x2 = ", x2)
            pass

# Exemple d'utilisation:
# Pour a = 1, b = -3, c = 2
# delta = 1
# Deux racines
# x1 = 1.0, x2 = 2.0
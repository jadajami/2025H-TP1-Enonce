# Exo 4

secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# Nombre de secondes dans chaque unité de temps

SECONDES_PAR_MINUTE = 60
SECONDES_PAR_HEURE = 60 * SECONDES_PAR_MINUTE
SECONDES_PAR_JOUR = 24 * SECONDES_PAR_HEURE
SECONDES_PAR_SEMAINE = 7 * SECONDES_PAR_JOUR
SECONDES_PAR_ANNEE = 365 * SECONDES_PAR_JOUR

# Calcul des années
annees = secondes // SECONDES_PAR_ANNEE   #division entière
secondes = secondes % SECONDES_PAR_ANNEE  # Restant

# Calcul des semaine
semaines = secondes // SECONDES_PAR_SEMAINE   #division entière
secondes = secondes % SECONDES_PAR_SEMAINE    # Restant

# Calcul des jour
jours = secondes // SECONDES_PAR_JOUR     #division entière
secondes = secondes % SECONDES_PAR_JOUR  # Restant

# Calcul des heures
heures = secondes // SECONDES_PAR_HEURE   #division entière
secondes = secondes % SECONDES_PAR_HEURE  # Restant

# Calcul des minutes
minutes = secondes // SECONDES_PAR_MINUTE   #division entière
secondes = secondes % SECONDES_PAR_MINUTE  # Restant

print(annees, semaines, jours, heures, minutes, secondes)
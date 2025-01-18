import unittest

from module_runner import ModuleRunner

class TestExercice1(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo1")
        self.input_questions = "Veuillez entrer votre nom complet : Veuillez entrer votre âge : "

    def test_nom_complet_vide(self):
        simulated_inputs = "Mark Doe\n20\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Bonjour Mark Doe\nVous êtes né(e) en 2005\n"
        self.assertEqual(expected, output)

class TestExercice2(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo2")
        self.input_questions = "Entrez le niveau de charge actuel de la batterie : "

    def test_valeur_valide(self):
        simulated_inputs = "75\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚❚❚❚❚❚❚  ]\n75%\n"
        self.assertEqual(expected, output)

    def test_valeur_hors_intervalle(self):
        simulated_inputs = "110\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Erreur : niveau de charge invalide.\n"
        self.assertEqual(expected, output)

    def test_valeur_hors_intervalle_2(self):
        simulated_inputs = "-5\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Erreur : niveau de charge invalide.\n"
        self.assertEqual(expected, output)

    def test_valeur_limite(self):
        simulated_inputs = "0\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[          ]\n0%\n"
        self.assertEqual(expected, output)

    def test_charge_complete(self):
        simulated_inputs = "100\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚❚❚❚❚❚❚❚❚]\n100%\n"
        self.assertEqual(expected, output)

    def test_charge_22_pourcent(self):
        simulated_inputs = "22\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚        ]\n22%\n"
        self.assertEqual(expected, output)

    def test_charge_46_pourcent(self):
        simulated_inputs = "46\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}[❚❚❚❚❚     ]\n46%\n"
        self.assertEqual(expected, output)

class TestExercice3(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo3")
        self.input_questions = "Entrez a, non nul: Entrez b: Entrez c:"

    def test_aucune_solution(self):
        simulated_inputs = "1\n2\n3\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Aucune racine\n"
        self.assertEqual(expected, output)
    
    def test_une_seule_solution(self):
        simulated_inputs = "1\n2\n1\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Une seule racine\n-1.0\n"
        self.assertEqual(expected, output)

    def test_deux_solutions(self):
        simulated_inputs = "1\n-3\n2\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Deux racines\n1.0 2.0\n"
        self.assertEqual(expected, output)
    
    def test_deux_solutions_2(self):
        simulated_inputs = "1\n-5\n6\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Deux racines\n2.0 3.0\n"
        self.assertEqual(expected, output)
    
    def une_seule_solution_3(self):
        simulated_inputs = "1\n-6\n9\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Une seule racine\n3.0\n"
        self.assertEqual(expected, output)
    
    def test_deux_solutions_4(self):
        simulated_inputs = "1\n-6\n8\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Deux racines\n2.0 4.0\n"
        self.assertEqual(expected, output)

class TestExercice4(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo4")
        self.input_questions = "Entrez un nombre de secondes :"

    def test_une_seconde(self):
        simulated_inputs = "1\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 0 0 0 0 0 1\n"
        self.assertEqual(expected, output)

    def test_une_minute(self):
        simulated_inputs = "60\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 0 0 0 0 1 0\n"
        self.assertEqual(expected, output)

    def test_une_heure(self):
        simulated_inputs = "3600\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 0 0 0 1 0 0\n"
        self.assertEqual(expected, output)

    def test_un_jour(self):
        simulated_inputs = "86400\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 0 0 1 0 0 0\n"
        self.assertEqual(expected, output)

    def test_une_semaine(self):
        simulated_inputs = "604800\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 0 1 0 0 0 0\n"
        self.assertEqual(expected, output)

    def test_un_an(self):
        simulated_inputs = "31536000\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 1 0 0 0 0 0\n"
        self.assertEqual(expected, output)

    def test_une_seconde_de_plus(self):
        simulated_inputs = "2\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 0 0 0 0 0 2\n"
        self.assertEqual(expected, output)

    def test_une_minute_de_plus(self):
        simulated_inputs = "61\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 0 0 0 0 1 1\n"
        self.assertEqual(expected, output)

    def test_grande_valeur(self):
        simulated_inputs = "100000000\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} 3 8 6 9 46 40\n"
        self.assertEqual(expected, output)

class TestExercice5(unittest.TestCase):
    def setUp(self):
        self.runner = ModuleRunner("exo5")
        self.input_questions = "Vitesse initiale (en m/s): Angle de lancer (en degrés):"

    def test_vitesse_0_angle_0(self):
        simulated_inputs = "0\n0\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Distance parcourue: 0.00m\n"
        self.assertEqual(expected, output)

    def test_vitesse_10_angle_0(self):
        simulated_inputs = "10\n0\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Distance parcourue: 0.00m\n"
        self.assertEqual(expected, output)

    def test_vitesse_10_angle_45(self):
        simulated_inputs = "10\n45\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Distance parcourue: 10.20m\n"
        self.assertEqual(expected, output)

    def test_vitesse_10_angle_90(self):
        simulated_inputs = "10\n90\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Distance parcourue: 0.00m\n"
        self.assertEqual(expected, output)

    def test_vitesse_10_angle_30(self):
        simulated_inputs = "10\n30\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions} Distance parcourue: 8.84m\n"
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
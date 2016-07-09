# -*- coding: utf-8 -*-
import unittest

from language_detector import detect_language, LANGUAGES


class TestLanguageDetector(unittest.TestCase):

    def setUp(self):
        self.languages = [
            {
                'name': 'Spanish',
                'common_words': [
                    'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se',
                    'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar',
                    'tener', 'le', 'lo', 'lo', 'todo', 'pero', 'más', 'hacer',
                    'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la',
                    'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él',
                    'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre',
                    'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta'
                ]
            },
            {
                'name': 'German',
                'common_words': [
                    'das', 'ist', 'du', 'ich', 'nicht', 'die', 'es', 'und',
                    'der', 'was', 'wir', 'zu', 'ein', 'er', 'in', 'sie', 'mir',
                    'mit', 'ja', 'wie', 'den', 'auf', 'mich', 'dass', 'so',
                    'hier', 'eine', 'wenn', 'hat', 'all', 'sind', 'von',
                    'dich', 'war', 'haben', 'für', 'an', 'habe', 'da', 'nein',
                    'bin', 'noch', 'dir', 'uns', 'sich', 'nur',
                    'einen', 'kann', 'dem'
                ]
            },
            {
                'name': 'English',
                'common_words': [
                    'the', 'is', 'of', 'what', 'and', 'with', 'one', 'has', 'know',
                    'speak', 'for', 'with', 'you', 'because', 'is', 'all', 'but',
                    'yes', 'my','go', 'because', 'where', 'who', 'why', 'other',
                    'always', 'me', 'also', 'day', 'us', 'to', 'have', 'not', 'on',
                    'be'
                ]
            }
        ]
        self.texts = {
            "spanish": """
                Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
                conocido como Leo Messi, es un futbolista argentino11 que juega
                como delantero en el Fútbol Club Barcelona y en la selección
                argentina, de la que es capitán. Considerado con frecuencia el
                mejor jugador del mundo y calificado en el ámbito deportivo como el
                más grande de todos los tiempos, Messi es el único futbolista en la
                historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
                ellos en forma consecutiva– y el primero en
                recibir tres Botas de Oro.
                """,
            "german": """
                Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
                Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
                der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
                erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
                Erstligatore erzielt und ist damit Rekordtorschütze
                der Primera División.
                """,
            "english": """
                Three successful seasons followed, with Messi winning three 
                consecutive FIFA Ballons d'Or, including an unprecedented 
                fourth. His personal best campaign to date was the 2011–12 
                season, in which he set the La Liga and European records for 
                most goals scored in a single season, while establishing himself
                as Barcelona's all-time top scorer in official competitions in 
                March 2012. He again struggled with injury during the following 
                two seasons, twice finishing second for the Ballon d'Or behind 
                Cristiano Ronaldo, his perceived career rival. Messi regained 
                his best form during the 2014–15 campaign, breaking the all-time
                goalscoring records in both La Liga and the Champions League in 
                November 2014, and led Barcelona to a historic second treble.
                """,
                
        }

    def test_detect_language_spanish_with_our_language_specification(self):
        result = detect_language(self.texts["spanish"], self.languages)
        self.assertEqual(result.lower(), 'spanish')

    def test_detect_language_spanish_with_module_language_specification(self):
        result = detect_language(self.texts["spanish"], LANGUAGES)
        self.assertEqual(result.lower(), 'spanish')

    def test_detect_language_german_with_our_language_specification(self):
        result = detect_language(self.texts["german"], self.languages)
        self.assertEqual(result.lower(), 'german')

    def test_detect_language_german_with_module_language_specification(self):
        result = detect_language(self.texts["german"], LANGUAGES)
        self.assertEqual(result.lower(), 'german')
        
    def test_detect_language_english_with_our_language_specification(self):
        result = detect_language(self.texts["english"], self.languages)
        self.assertEqual(result.lower(), 'english')

    def test_detect_language_english_with_module_language_specification(self):
        result = detect_language(self.texts["english"], LANGUAGES)
        self.assertEqual(result.lower(), 'english')
        
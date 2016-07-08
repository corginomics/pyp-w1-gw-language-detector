# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here
    
    
    '''
    Algorithm
    We should go through the user input, and see which language it corresponds to.
    The language with the most words is the language that we're going to return
    
    Dictionary with our languages as keys. And a counter as the value
    Iterate through the user input, and check each word to see what language it is
    Then go to our dictionary and increment the counter
    At the end, we have a dictionary the # of [language] words
    The highest value is going to be the language that we return
    '''
    
    numOfTimesLanguageOccurs = {}
    
    for word in text.split():
        #if 'our' in text:
        
        #print(word)
        whichLanguageIsIt(word)


    

def whichLanguageIsIt(word):
    for dict in LANGUAGES:
        if word in dict['common_words']:
            print(word, "is in", dict['name'])
            
    

#words = LANGUAGES[0]['common_words']

#if text[x] in LANGUAGES[0]:
#    counter += 1





text = "the this of what anthony steven"



texts = {
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
                """
        }
        
#detect_language(texts["spanish"], languages=LANGUAGES)
detect_language(text, languages=LANGUAGES)
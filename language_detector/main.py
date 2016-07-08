# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
 
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
        #print(word)
        language = whichLanguageIsIt(word)
        
        if language is not None:
            addToDictionary(language, numOfTimesLanguageOccurs)
    
    print(numOfTimesLanguageOccurs)
    return getHighestOccurringLanguage(numOfTimesLanguageOccurs)

def whichLanguageIsIt(word):
    for dict in LANGUAGES:
        if word in dict['common_words']: 
            #print(dict['name'])
            return dict['name']
            #print(word, "is in", dict['name'])

def addToDictionary(language, dictionary):
        if language in dictionary: dictionary[language] += 1
        else: dictionary[language] = 1

def getHighestOccurringLanguage(dictionary):
    return max(dictionary.iterkeys(), key=(lambda key: dictionary[key]))

def languageIsNotNull(language):
    return language is None


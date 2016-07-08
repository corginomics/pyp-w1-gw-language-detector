# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    numOfTimesLanguageOccurs = {}
    
    for word in text.split():
        language = whichLanguageIsIt(word)
        if language is not None:
            addToDictionary(language, numOfTimesLanguageOccurs)
    return getHighestOccurringLanguage(numOfTimesLanguageOccurs)

def whichLanguageIsIt(word):
    for dict in LANGUAGES:
        if word in dict['common_words']: 
            return dict['name']

def addToDictionary(language, dictionary):
        if language in dictionary: dictionary[language] += 1
        else: dictionary[language] = 1

def getHighestOccurringLanguage(dictionary):
    return max(dictionary.iterkeys(), key=(lambda key: dictionary[key]))

def languageIsNotNull(language):
    return language is None


# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected lang of given text."""
    numOfTimesLanguageOccurs = {}

    for word in text.split():
        lang = whichLanguageIsIt(word, languages)
        if lang is not None:
            addToDictionary(lang, numOfTimesLanguageOccurs)
    return getHighestOccurringLanguage(numOfTimesLanguageOccurs)

def whichLanguageIsIt(word, language_list ):
    for dict in language_list:
        if word in dict['common_words']: 
            return dict['name']

def addToDictionary(lang, dictionary):
        if lang in dictionary: dictionary[lang] += 1
        else: dictionary[lang] = 1

def getHighestOccurringLanguage(dictionary):
    return max(dictionary.keys(), key=(lambda key: dictionary[key]))
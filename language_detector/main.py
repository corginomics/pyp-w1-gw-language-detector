# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected lang of given text."""
    numOfTimesLanguageOccurs = {}

    for word in text.split():
        lang = which_language_is_it(word, languages)
        if lang is not None:
            add_to_dictionary(lang, numOfTimesLanguageOccurs)
            
    mostOccuringLanguage = max(numOfTimesLanguageOccurs.keys(),
                               key=(lambda key: numOfTimesLanguageOccurs[key]))
    
    return mostOccuringLanguage


def which_language_is_it(word, language_list ):
    for dict in language_list:
        if word in dict['common_words']: 
            return dict['name']

def add_to_dictionary(lang, dictionary):
    dictionary [lang] = dictionary.get(lang, 0)  + 1

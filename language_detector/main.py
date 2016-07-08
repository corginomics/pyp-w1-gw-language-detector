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
    return get_most_occurring_language(numOfTimesLanguageOccurs)

def which_language_is_it(word, language_list ):
    for dict in language_list:
        if word in dict['common_words']: 
            return dict['name']

def add_to_dictionary(lang, dictionary):
        if lang in dictionary: dictionary[lang] += 1
        else: dictionary[lang] = 1

def get_most_occurring_language(dictionary):
    return max(dictionary.keys(), key=(lambda key: dictionary[key]))
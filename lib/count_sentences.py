#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return "." in self._value

    def is_question(self):
        return "?" in self._value
    
    def is_exclamation(self):
        return "!" in self._value
    
    def count_sentences(self):
        sentences = [s.strip() for s in self._value.split() if s.strip()]
        sentence_count = 0
        for sentence in sentences:
            if sentence.endswith(('.', '!', '?')):
                sentence_count += 1
        return sentence_count
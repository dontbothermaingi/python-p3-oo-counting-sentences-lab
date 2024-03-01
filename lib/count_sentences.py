#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            print("Thealue must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace common separators with a period, then split on the period
        sentences = re.split(r'[.!?]', self.value)
        # Remove empty strings (e.g., due to consecutive separators) and return the count
        return len([s for s in sentences if s.strip()])

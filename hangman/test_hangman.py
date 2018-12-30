# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 05:34:04 2018

@author: Bill Lueckenbach

"""
import unittest
from unittest.mock import patch
from contextlib import contextmanager

import string     
# Import modules to be tested from hangman
from hangman import is_word_guessed
from hangman import get_available_letters
from hangman import get_guessed_word
from hangman import update_warnings_and_guesses_left
from hangman import get_guess

# Define Letters Guessed Constants
APLE =      ['a', 'p', 'l', 'e']
AELP =      ['a', 'e', 'l', 'p']
APLE_NO_A=  [     'p', 'l', 'e']
APLE_NO_AP= [          'l', 'e']
APLE_NO_APL=[               'e']

NO_APLE = [     'b', 'c', 'd',      'f', 'g', 'h', 'i', 'j', 'k',      'm', 
           'n', 'o',      'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NO_A =    [     'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
GOOD_GUESS_EXTRA_ON_END = ['a', 'p', 'l', 'e', 'b', 'u','z']
GOOD_GUESS_EXTRA_ON_START = ['b', 'u','z', 'a', 'p', 'l', 'e']
GOOD_GUESS_EXTRA_ALLOVER = ['b', 'u','z', 'a', 'q', 'p', 'l', 'e', 'w']
SINGLE_LETTER =['a']
NO_LETTERS = []
ALL_LETTERS = string.ascii_lowercase
ALREADY_GUESSED = -1
NOT_A_LETTER = -2

###################### Define mock functions ##################
# Use a contextmanager to enable switching input() to mock_input.
# You have to save the original input() function then point to the
# mock_input() function.  After we are done need to restore input()
# Using a context manager makes this process cleaner
# Got help from following site: 
# <https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests>
    
@contextmanager

# Replace builtin input function
def mock_input(mock):
    original_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_input
#################### End of mock functions #########################
    
    
# Define test class that inherits from unittest.testcase() #########
class test_hangman(unittest.TestCase):

    
    def test_is_word_guessed(self):
       
        #Test word is guessed
        self.assertTrue(is_word_guessed('apple', APLE))
        self.assertTrue(is_word_guessed('apple', AELP))
        self.assertTrue(is_word_guessed('apple', ALL_LETTERS))
        self.assertTrue(is_word_guessed('apple', GOOD_GUESS_EXTRA_ON_END))
        self.assertTrue(is_word_guessed('apple', GOOD_GUESS_EXTRA_ON_START))
        self.assertTrue(is_word_guessed('apple', GOOD_GUESS_EXTRA_ALLOVER))
        
        #Test word is not guessed
        self.assertFalse(is_word_guessed('apple', SINGLE_LETTER))
        self.assertFalse(is_word_guessed('apple', NO_LETTERS))
        
    def test_get_available_letters(self):
        
        #Test get_available_letters
        #Note:  get available_letters takes a list as an input and 
        #       returns a string.  Need to join the letters guessed constants
        #       to make them a string to compare to the return value.
        #
        #Note2  get_available_letters returns the string in alphabetical order
        #       so we need to sort the letters guessed constants before we 
        #       join them.
        self.assertEqual(get_available_letters(APLE),
                         "".join(NO_APLE))      
        self.assertEqual(get_available_letters(NO_APLE),
                         "".join(sorted(APLE)))
        self.assertEqual(get_available_letters(NO_LETTERS),
                         "".join(ALL_LETTERS))
        self.assertEqual(get_available_letters(ALL_LETTERS),
                         "".join(NO_LETTERS))          
        self.assertEqual(get_available_letters('a'),
                         "".join(NO_A))
        
    def test_get_guessed_word(self):
        self.assertEqual(get_guessed_word('apple', APLE),
                         "apple")
        self.assertEqual(get_guessed_word('apple', AELP),
                         "apple")        
        self.assertEqual(get_guessed_word('apple', APLE_NO_A),
                         " _pple")        
        self.assertEqual(get_guessed_word('apple', APLE_NO_AP),
                         " _ _ _le")        
        self.assertEqual(get_guessed_word('apple', APLE_NO_APL),
                         " _ _ _ _e")        
        self.assertEqual(get_guessed_word('apple', NO_LETTERS),
                         " _ _ _ _ _")        
        self.assertEqual(get_guessed_word('apple', APLE_NO_A),
                         " _pple")        
        self.assertEqual(get_guessed_word('apple', ALL_LETTERS),
                         "apple")        
        self.assertEqual(get_guessed_word('apple', NO_LETTERS),
                         " _ _ _ _ _")
        
    def test_update_warnings_and_guesses_left(self):
        #Test good guess, 3 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left('a', 'apple',(3,6)),
                         (3,6))
        #Test bad vowel guess, 3 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left('u','apple',(3,6)),
                         (3,4))
        #Test bad consenet guess, 3 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left('b','apple',(3,6)),
                         (3,5))
        #Test ALREADY_GUESSED, 3 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left(ALREADY_GUESSED,
                                                          'apple',(3,6)),
                         (2,6))
        #Test ALREADY_GUESSED, 1 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left(ALREADY_GUESSED,
                                                          'apple',(1,6)),
                         (0,6))
        #Test ALREADY_GUESSED, 0 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left(ALREADY_GUESSED,
                                                          'apple',(0,6)),
                         (-1,5))
        #Test ALREADY_GUESSED, -1 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left(ALREADY_GUESSED,
                                                          'apple',(-1,6)),
                         (-1,5))
        #Test ALREADY_GUESSED, -1 warnings, 0 guesses
        self.assertEqual(update_warnings_and_guesses_left(ALREADY_GUESSED,
                                                          'apple',(-1,0)),
                         (-1,-1))
        #Test NOT_A_LETTER, 3 warnings, 6 guesses
        self.assertEqual(update_warnings_and_guesses_left(NOT_A_LETTER,
                                                          'apple',(3,6)),
                         (2,6))
        
    def test_get_guess(self):
        
        # Test valid lower case; no letters guessed; 3 warnings; 6 guesses
        with mock_input('b'):
            self.assertEqual(get_guess(NO_LETTERS, (3, 6)), 'b')
        
        # Test valid upper case; no letters guessed; 0 warnings; 1 guesses
        with mock_input('B'):
            self.assertEqual(get_guess(NO_LETTERS, (0, 1)), 'b')        
        
        # Test NOT_A_LETTER  case; no letters guessed; -1 warnings; 3 guesses
        with mock_input(' '):
            self.assertEqual(get_guess(NO_LETTERS, (-1, 6)), NOT_A_LETTER)
                                                          
        # Test ALREADY_GUESSED case;  APLE guessed; 3 warnings; 6 guesses
        with mock_input('a'):
            self.assertEqual(get_guess(APLE, (3, 6)), ALREADY_GUESSED)

        
if __name__ == '__main__':
    unittest.main()
    


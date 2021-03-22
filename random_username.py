"""
File: random_username.py
------------------
This program generates a random username consisting of an english adjective
followed by a noun and a number. 
This file specifically, contains the function used to generate the actual string. 
"""

import random 


def get_random_username():
    # returns the random username 
    rand_adjective = get_random_word('common-adjectives.txt')
    rand_noun = get_random_word('common-nouns.txt')
    rand_number = str(random.randint(0, 99))
    return rand_adjective + rand_noun + rand_number 


def get_random_word(file_name): 
    """
    This function picks the random word from the file passed in and returns the
    random word.  
    Parameters: 
        - file_name: the name of the file that the word will be picked from randomly. 
    Return: This function returns a random word from the file passed in. 
    """ 

    file = open(file_name) 
    word_list = [] # for storing all the words in the file 

    for line in file: 
        line = line.strip()
        word_list.append(line)

    rand_index = random.randint(0, len(word_list) - 1) # 0 to number of lines in list - 1 (so that the list index is not out of bounds) 

    word = word_list[rand_index].lower()
    
    return word.capitalize() # camelcase 

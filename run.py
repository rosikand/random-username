"""
File: run.py
------------------
This program generates a random username consisting of an english adjective
followed by a noun and a number. 
This file specifically is the runner file. Execute this file
to run the program! 
"""

from random_username import get_random_username 

while True:
    get_input = input("Press anything to generate a random username. Say 'no' to stop: ")
    if (get_input == 'no'):
        break
    print(get_random_username())
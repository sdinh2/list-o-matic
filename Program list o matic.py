# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:59:07 2017

@author: sdinh
"""


def list_o_matic():
    animals = ["dog", "cat", "horse", "zebra"]
    while animals:
        print("Look at all the animals", animals) 
        phrase = input("Enter the name of an animal: ")
        if phrase in animals:
            animals.remove(phrase)
            statement = print("1 instance of",phrase,"removed from list\n")
        elif phrase.lower() == "quit":
            statement = print("Goodbye!")
            break
        elif phrase == "":
            statement = print(animals.pop(),"popped from list\n")
            if animals == []:
                statement = print("There's no more animals in the list. Goodbye!")
        else:
            animals.append(phrase)
            statement = print("1 instance of",phrase,"appended to list\n")
            
    return statement

list_o_matic()

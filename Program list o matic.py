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
            print("1 instance of ",phrase,"removed from list")
        elif phrase.lower() == "quit":
            print("Goodbye!")
            break
        elif phrase == "":
            print(animals.pop(),"popped from list")
            if animals == []:
                print("There's no more animals in the list. Goodbye!")
        else:
            animals.append(phrase)
            print("1 instance of ",phrase,"appended to list")
            
    return list_o_matic

list_o_matic()
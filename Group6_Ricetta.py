#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:56:44 2018

95888-C2 Group 6 Final Project

Main module 

@author: Thara P., Jessica S., Carol X., Zina O.
"""
import Function1
import Function2 
import Function3

inputCorrect = False

while(inputCorrect == False):
    print("Welcome to Ricetta")
    print("Your one-stop shop for your individualized recipe cookbook")
    print("1. Find recipes by ingredient")
    print("2. Find the most popular recipes on social media")
    print("3. Find recipes by category")
    print("Simply press enter to exit")
    menuInput = input()
    try:
        if len(menuInput) == 0:
            print("Thank you for using Ricetta")
            break
        choice = int(menuInput)
        if choice < 1 or choice > 3:
            print("Invalid input. Please choose between menu 1-3\n")
    except:
        print("Invalid input. Please choose between menu 1-3\n")
      
## If user choose function 1
    if choice == 1:
        legalInput = False
        while (legalInput == False):
            ingredient = input("Please enter ingredients you want to cook, separated by comma: ")
            if all(x.isalpha() or x.isspace() or x == ',' for x in ingredient):
                legalInput = True
            else:
                print("Invalid input. Please enter only character, space and comma.")
        Function1.randomrecipe(ingredient)
        
## If user choose function 2
    elif choice == 2:
        legalInput = False
        while (legalInput == False):
            ingredient = input("Please enter the ingredient you want to cook: ")
            if all(x.isalpha() or x.isspace() for x in ingredient):
                legalInput = True
            else:
                print("Invalid input. Please enter only character and space.")
        Function2.recipe_query(ingredient)

## If user choose function 3
    else:
        #if use csv file put True; if use json put False
        i=True
        df = Function3.cat_char(i)
        
        legalInput = False
        while (legalInput == False):
            category = input("Please enter the dietary category that you are interested: ")
            if all(x.isalpha() or x.isspace() for x in category):
                recf = Function3.search_char(category, df)
                if len(recf) == 0:
                    print("Category not found. Please enter the category shown on the graph.")
                else:
                    legalInput = True
            else:
                print("Invalid input. Please enter only character and space.")

        legalInput = False
        while (legalInput == False):
            ingredient = input("Please enter the ingredient you want to cook: ")
            if all(x.isalpha() or x.isspace() for x in ingredient):
                legalInput = True
            else:
                print("Invalid input. Please enter only character and space.")
        
        
        Function3.search_ing(ingredient, recf)
            
  

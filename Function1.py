# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:02:27 2018

Function 1

Purpose: Take user ingredient input and return 10 random recipes from EatingWellRecipes,
AllRecipes and recipepuppy api combined.

@author: Thara P., Carol X.
"""

import urllib.request, json 
import pandas as pd
from xlrd import open_workbook


# function to load data from a xlsx file
def loadData(fileName):
    recipies = dict()
    book = open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    
    recipeName = []
    recipeId = []
    url = []
    ingredients = []
    
    for row_index in range(0, sheet.nrows):
        recipeId.append(sheet.cell(row_index, 0).value)
        recipeName.append(sheet.cell(row_index, 1).value)
        url.append(sheet.cell(row_index, 2).value)
        ingredients.append(sheet.cell(row_index, 3).value)
        
    recipies['recipeId'] = recipeId
    recipies['recipeName'] = recipeName
    recipies['url'] = url
    recipies['ingredients'] = ingredients
    df = pd.DataFrame(recipies)
    return df

# function to print 10 random recipes based on ingredient string
def randomrecipe(ingredient):
    # load EatingWellRecipes and AllRecipes scraped and saved in xlsx beforehand
    totalRecipes = loadData('EatingWellRecipes.xlsx')
    totalRecipes.append(loadData('AllRecipes.xlsx'))
    
    # pull recipes from the combined EatingWellRecipes and AllRecipes
    validRecipes = dict()
    
    recipeName = []
    url = []
    ingredients = []
    for index, row in totalRecipes.iterrows():
        count = 0
        for ing in ingredient.split(','):
            if ing in row['ingredients']:
                count = count + 1
                 #recipieId.append(row['recipieId'])
        if count==len(ingredient.split(',')):
             recipeName.append(row['recipeName'])
             url.append(row['url'])
             ingredients.append(row['ingredients'])
          
    validRecipes['recipeName'] = recipeName
    validRecipes['url'] = url
    validRecipes['ingredients'] = ingredients
    validRecipesDf = pd.DataFrame(validRecipes)
    
    # determine how many more recipes need to be pulled from the third source
    if (validRecipesDf['recipeName'].count() >= 10):
        validRecipesDf = validRecipesDf[:10]
    else:
        more = 10 - validRecipesDf['recipeName'].count()
    
    # pull more recipes from recipepuppy api
    ingred = ingredient.replace(' ', '%20')
    datap = pd.DataFrame()
    with urllib.request.urlopen(
            "http://www.recipepuppy.com/api/?i=%(i)s&q=&p=3s" % {'i': ingred}
            ) as url:
            data_add = json.loads(url.read().decode())
            
    datap = datap.append(pd.DataFrame(data_add))

    datap2 = pd.DataFrame(datap['results'])
    recipes = datap2['results'].apply(pd.Series)[:more]
    del recipes['thumbnail']
    recipes.columns = ['recipeName', 'url', 'ingredients']
    
    recipes = recipes.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    recipes = recipes.apply(lambda x: x.str.replace('&amp;', '&') if x.dtype == "object" else x)
    
    # combine search results from EatingWellRecipes, AllRecipes and recipepuppy
    validRecipesDf=validRecipesDf.append(recipes)
    validRecipesDf.index = range(1,11)
    
    for index, row in validRecipesDf.iterrows():
        print('Recipe', index, ':', row['recipeName'])
        print('    URL', ':', row['url'])
        print('    Ingredients:', row['ingredients'])
        print()

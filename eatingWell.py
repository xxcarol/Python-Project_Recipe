# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 01:11:56 2018

@author: pthar
"""

import numpy as np
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

## Insert chromedriver's path here
path = ''

options = Options()
options.add_argument('--headless')
recipes = {}
workbook = xlsxwriter.Workbook('EatingWellRecipes.xlsx')
cleaned = workbook.add_worksheet("Cleaned")
raw = workbook.add_worksheet("Raw")
row = 0
col = 0
row2 = 0
ids= [np.random.randint(249900, 255500) for a in range(2)]

for i in ids:
    driver = webdriver.Chrome(path,chrome_options=options)
    id = str(i)  
    ing = []
    url = "http://www.eatingwell.com/recipe/"+id
    driver.get(url)  
    nameelem = driver.find_elements_by_class_name("recipeDetailSummary")
    if nameelem != []:
        name = nameelem[0].get_attribute("ng-init").split("', '")[1]
        name.replace("&amp;", "&")  
    else:
        ids.append([np.random.randint(260000, 269000) for i in range(1)][0])
        continue
        
    source = driver.page_source
    raw.write(row, col, source)
    row+=1
    ing.append(id)
    ing.append(name)
    ing.append(url)
    elem = driver.find_elements_by_class_name("checkListListItem")
    ingredients = ''
    for j in elem:
        string = j.text.rstrip('\n')
        if ('In Stores Only' not in string and 'See Everyday Low Price' not in string):
            ingredients = ingredients + string + ", "
    ing.append(ingredients[:-2])
    col2 = 0
    for k in ing:
        print(k)
        cleaned.write(row2, col2, k)
        col2+=1
        
    row2+=1
    driver.quit()
workbook.close()
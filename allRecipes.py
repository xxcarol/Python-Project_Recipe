# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 01:02:20 2018

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
workbook = xlsxwriter.Workbook('AllRecipes.xlsx')
cleaned = workbook.add_worksheet("Cleaned")
raw = workbook.add_worksheet("Raw")
row = 0
col = 0
row2 = 0
ids= [np.random.randint(200000, 300000) for a in range(100)]

for i in ids:
    driver = webdriver.Chrome(path,chrome_options=options)
    id = str(i)  
    ing = []
    url = "https://www.allrecipes.com/recipe/"+id
    driver.get(url)  
    nameelem = driver.find_element_by_xpath("//meta[1]")
    name = nameelem.get_attribute("content")
    if (name in ing) or (name == "Allrecipes - File Not Found"):
            ids.append([np.random.randint(7000, 100000) for i in range(1)][0])
            continue
        
    source = driver.page_source
    raw.write(row, col, source)
    row+=1
    ing.append(id)
    ing.append(name)
    ing.append(url)
    elem = driver.find_elements_by_class_name("checkList__item")
    for j in elem:
        ing.append(j.text.rstrip('\n'))
    ing = ing[:-1]
    col2 = 0
    for k in ing:
        print(k)
        cleaned.write(row2, col2, k)
        col2+=1
        
    row2+=1
    driver.quit()
workbook.close()
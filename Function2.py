#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:57:14 2018

95888-C2 Group 6 Final Project

Fuction 2: FoodtoFork module 

Purpose: Take user ingredient input and return the top 10 most popular recipe on social media

@author: Zina Ouyang
"""

import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

food_api = '3993f2ccdadd2549ec649d352dee0bf5'


def recipe_query(query):
    key = food_api
    url = 'https://www.food2fork.com/api/search?key=' + key
    ingredients = query.replace(' ', '%20')
    final_url = url + '&q=' + ingredients
    
    req = Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    soup = BeautifulSoup(webpage.read(), "lxml")

    results=json.loads(str(soup.text))
    
    df = pd.DataFrame(results['recipes'], columns=['publisher', 'ftf_url', 'title', 'source_url', 'recipe_id',
                      'image_url', 'social_rank', 'publisher_url'])
  
    del df['ftf_url']
    del df['image_url']
    del df['publisher_url']
    del df['recipe_id']
    
    df.index = list(range(1, len(df) + 1))
    
    df.rename(columns = {'title':'Recipe_Name', 'source_url':'Recipe_url'}, inplace=True)
    
    #print the top 10 recipe
    for index, row in df.loc[:10].iterrows():
        print('Recipe', index, ':', row['Recipe_Name'])
        print('    Social Rank', ':', row['social_rank'])
        print('    URL', ':', row['Recipe_url'])
        print('    Publisher:', row['publisher'])
        print()

 

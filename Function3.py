# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:45:28 2018

Function 3 Module

Purpose: Generate the categories of recipe and let user choose which dietary restrictions they
are interested in. Then take user input ingredient and return recipes in the category. 

@author: jslee
"""
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from ast import literal_eval
import random
from PIL import Image
from os import path
import os

def read_json():
    rec = {}
    with open('full_format_recipes.json', 'rb') as data_file:
        your_json = json.loads(data_file.read())
    row  =0
    for item in your_json:
        if(str(item)[1:-1] == ""):
            continue
        rec[row] = item;
        row+=1
    df = pd.DataFrame(data=rec)
    df.to_csv("JSON_Recipe_Data.csv")
    return df

def read_csv_file():
    df = pd.read_csv("JSON_Recipe_Data.csv",index_col=0)
    for i in df.keys():
        df.loc["categories"][i] = literal_eval(df.loc["categories"][i])
        df.loc["ingredients"][i] = literal_eval(df.loc["ingredients"][i])
        df.loc["directions"][i] = literal_eval(df.loc["directions"][i])
    return df


def cat_char(i):
    if i == False:
        df = read_json()
    else:
        df = read_csv_file()
    
    categories = ["Peanut Free", "Soy Free","Tree Nut Free", "Vegetarian", "Kosher","Pescatarian","Wheat/Gluten-Free","Dairy Free","Sugar Conscious","Healthy","Vegan","Kid-Friendly","Other"]
    catcount = {"Other": 0}
    a =0
    for j, row in df.iteritems():
        a+=1
        catfound = False
        for i in categories:
            if i in row[1]:
                catfound = True
                if i in catcount:
                    catcount[i] += 1
                else:
                    catcount[i] = 1
        if catfound == False:
            catcount["Other"] += 1
    
    catkeys = []
    catct = []
    for key, value in catcount.items():
        catkeys.append(key)
        catct.append(value)
    catdf = pd.DataFrame({'Category': catkeys, 'RecipeCount':catct})
    catdf = catdf.sort_values(by='RecipeCount')
    catdf.to_csv("recipe_cat.csv")
    catdf.plot(x='Category', y='RecipeCount', kind='barh')
    plt.show()
    return df
    
def grey_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    h = 359
    s = 88
    l = int(100.0 * float(random_state.randint(130, 190)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h,s,l)

def search_char(s, df): 
    recfound1 = {};
    
    categories = ["Peanut Free", "Soy Free","Tree Nut Free", "Vegetarian", "Kosher","Pescatarian","Wheat/Gluten-Free","Dairy Free","Sugar Conscious","Healthy","Vegan","Kid-Friendly","Other"]
    if s.title() in categories:
        df3 = df.sort_values(by='rating', axis=1,ascending =False)
        ing = ''
        inglist = []
        count =0
        for j, row in df3.iteritems():
            catfound = False
            if s.title() == "Other":
                for cat in categories:
                    if cat in row[1]:
                        catfound = True
                        break;
                if catfound == False:
                    recfound1[j] = row
            else:
                if s.title() in row[1]:
                    recfound1[j] = row
        if len(recfound1) != 0:  
            for key, val in recfound1.items():  
                ing = ing + ",".join(val[1]) +","
            
            inglist = ing.split(",")
            ingdict = {}
            for i in inglist:
                if i in ingdict:
                    ingdict[i] +=1
                else:
                    ingdict[i] = 1
            for i in ["Quick & Easy", "Bon Appétit","Peanut Free", "Soy Free",'Tree Nut Free', "Vegetarian", "Kosher","Pescatarian","Wheat/Gluten-Free","Dairy Free","Sugar Conscious","Healthy","Vegan","Kid-Friendly"]:
                if i in ingdict.keys():
                    ingdict.pop(i)
            d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            mask = np.array(Image.open(path.join(d,"table-place-setting.jpg")))
            wordcloud = WordCloud(mask=mask, background_color="white",margin=10,random_state=1).generate_from_frequencies(ingdict)   
            plt.figure(figsize=[10,10])
            plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3))
            plt.axis("off") 
            #plt.tight_layout(pad = 0)
            #plt.figure()
            plt.show()
    return recfound1
    
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

def search_ing(s, recf):
    df4 = pd.DataFrame(data=recf)
    df4 = df4.sort_values(by='rating', axis=1,ascending =False)
    recfound2 = {}
    i = 0
    for j, row in df4.iteritems():
        for d in row[6]:
            if((d.lower()).__contains__(s.lower())):
                recfound2[j] = row
                i+=1
        if(i>=10):
            break
    recf2 = pd.DataFrame(data=recfound2)
    z = 1
    key = {}
    for k, v in recf2.iteritems():
        for k2, v2 in v.items():
            if k2 == "title":
                key[k]=str(v2.rstrip("\n")) 
    recf2 = recf2.rename(index=str,columns=key)
    recf2 = recf2.drop('title')
    ind = ["desc", "rating", "ingredients","directions","categories","calories","fat","protein","sodium"]
    recf2 = recf2.reindex(ind)
    pd.set_option('display.max_colwidth', -1)
    for j, row in recf2.iteritems():
        print("Recipe " + str(z) +": " + j)
        for key, row2 in row.items():
            if key=="desc":
                print("Recipe Description")
            else:
                print(str(key).title())
            if key=="desc" or key=="date":
                print(row2)
            elif key=="categories" or key =="ingredients":
                print(','.join(row2)) 
            elif key=="directions":
                for v in row2:
                    print(v)
            else: 
                print(row2)
        z+=1
        print()

#i=True
#df = cat_char(i)
#recf = search_char("Other", df)
#search_ing("bb", recf)


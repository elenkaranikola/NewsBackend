import pandas as pd
import unicodedata
import string
import json
import csv
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from settings import DB_CREDS
from utilities import finalNormalize, readText

#get all the data from the articles table
sql_command = "SELECT id,topic,article_date FROM articles"
df = readText(sql_command)
df = df.fillna(" ")

#get the unique categories
categories = df.topic.unique()

#group articles by their date
culture_articles = df.groupby(['article_date']).nunique()

list_of_dicts = []

for i in range (2020,2012,-1):
    list_of_dicts.append({'year': str(i), 'World': 0, 'Sport': 0, 'Culture': 0, 'Society': 0, 'Economics': 0, 'Environment': 0, 'Politics': 0, 'Tech': 0, 'Food': 0, 'Style': 0})

# thelw ana katigoria na metraw ana xronia ta arthra

list_index = 0
for i_year in range(2020,2012,-1):
    for category in categories:
        counter = 0
        sql_command = "SELECT article_date FROM articles WHERE topic = '{}'".format(category)
        df2 = readText(sql_command)
        df2 = df2.fillna(" ")
        size = df2.shape[0]
        for index in range(0,size):
            article_date = df2.iloc[index]['article_date']
            if article_date.year == i_year :
                counter += 1
        list_of_dicts[list_index][category] = counter
    
    list_index += 1


with open("/Users/elenikaranikola/Desktop/NewsBackend/dependencies/api_charts/articles_per_year.csv", "w") as write_file:
    json.dump(list_of_dicts, write_file)
 

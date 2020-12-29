import pandas as pd
import unicodedata
import string
import json
import csv
import sys
import re
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from utilities import removeAccents,normalize,readText
from settings import countries_list

#get all the data from the articles table
sql_command = "SELECT topic,website FROM articles"
df = readText(sql_command)
df = df.fillna(" ")

#List unique values in the df['topic'] column
categories = list(df.topic.unique())

#List unique values in the df['website'] column
websites = list(df.website.unique())

#dict of dicts
websites_dict = {k:{c:0 for c in categories} for k in websites }

for index, row in df.iterrows():
    websites_dict[row['website']][row['topic']] += 1

##print (websites_dict)
final_list = []
for i in websites_dict:
    final_list.append(dict([("website",i),("articles",sum(websites_dict[i].values())),("pie",list(dict([("count",websites_dict[i][key]),("topic",key)]) for key in websites_dict[i]))]))


#print(final_list)
with open("/Users/elenikaranikola/Desktop/NewsBackend/dependencies/api_charts/sites_analysis.csv", "w") as write_file:
    json.dump(final_list, write_file)


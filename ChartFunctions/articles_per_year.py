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
sql_command = "SELECT id,article_date FROM articles"
df = readText(sql_command)

df = df.fillna(" ")
culture_articles = df.groupby(['article_date']).nunique()

my_list = []
my_dict = {}
for i, row in culture_articles.iterrows():
    date = str(i.day) + '-' + str(i.month) + '-' + str(i.year)
    my_dict["date"] = date 
    my_dict["counter"] = int(row[('id')])
    my_list.append(my_dict)

#s = pd.Series(my_dict, name='DateValue')
#
#print(s.to_json('/Users/elenikaranikola/Desktop/NewsBackend/dependencies/articles_per_year.json',orient='index'))   
with open('/Users/elenikaranikola/Desktop/NewsBackend/dependencies/articles_per_year.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(my_list)


#                               !!! WRONG FORM
#my_dict = {}
#for i, row in culture_articles.iterrows():
#    date = str(i.day) + '-' + str(i.month) + '-' + str(i.year)
#    my_dict[date] = int(row[('id')])
#
#s = pd.Series(my_dict, name='DateValue')
#
#print(s.to_json('/Users/elenikaranikola/Desktop/NewsBackend/dependencies/articles_per_year.json',orient='index'))   

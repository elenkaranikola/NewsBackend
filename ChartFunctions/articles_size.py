import pandas as pd
import unicodedata
import string
import json
import csv
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from settings import DB_CREDS
from utilities import finalNormalize, readText, finalNormalizeFullPath

#get all the data from the articles table
sql_command = "SELECT article_body FROM articles"
df = readText(sql_command)
df = df.fillna(" ")

dict_len = {}

for article in df['article_body']:
    word_list = article.split()
    #find the different words
    unique = set(word_list)
    #get its length
    words = len(unique)
    if words in dict_len:
        dict_len[words] += 1
    else: dict_len[words] = 1

#sorted_len = sorted(dict_len.items(), reverse=True)
sorted_by_count = sorted(dict_len.items(), key=lambda x: x[1], reverse=True)
sorted_by_count_dict = dict(sorted_by_count[0:10])
sorted_len = sorted(sorted_by_count_dict.items(), reverse=True)


list_of_dicts = []
for i in sorted_len[0:10]:
    list_of_dicts.append(dict([("words",i[0]),("count",i[1])]))

with open("/Users/elenikaranikola/Desktop/NewsBackend/dependencies/api_charts/articles_size.csv", "w") as write_file:
    json.dump(list_of_dicts, write_file)
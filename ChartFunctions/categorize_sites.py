import pandas as pd
import unicodedata
import string
import json
import csv
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from settings import DB_CREDS
from utilities import finalNormalize, readText, finalNormalizeFullPath

#read the data
df = pd.read_csv('/Users/elenikaranikola/Desktop/NewsBackend/output.csv')

#fill all null values in the table
df = df.fillna(" ")

#List unique values in the df['topic'] column
websites = df.website.unique()

dict_avlen = {}
counter_web = {}

#group all articles by their topic
for website in websites:
    web_articles = df.groupby(['website']).get_group(website)['article_body']

    sum_all = 0
    counter = 0
    for article in web_articles:
        #split the articles to words
        word_list = article.split()
        #find the different words
        unique = set(word_list)
        #get its length
        article_len = len(unique)
        sum_all += article_len
        counter += 1
    
    average = sum_all/counter
    dict_avlen[website] = average
    counter_web[website] = counter*100/35737  #percentage of each website



sort_websites = sorted(dict_avlen.items(), key=lambda x: x[1], reverse=True)

onethird = sort_websites[0][1]/3

list_of_dicts = []
for i in sort_websites:
    average = i[1]
    website = i[0]
    if average < onethird :
        temp = dict([("website",website),("difficulty","beginner"),("value",average)])
    elif average < 2*onethird :
        temp = dict([("website",website),("difficulty","intermediate"),("value",average)])
    else:
        temp = dict([("website",website),("difficulty","expert"),("value",average)])
    list_of_dicts.append(temp)

print(list_of_dicts)


with open("/Users/elenikaranikola/Desktop/NewsBackend/dependencies/api_charts/beginner_reading.csv", "w") as write_file:
    json.dump(list_of_dicts[0:8], write_file)
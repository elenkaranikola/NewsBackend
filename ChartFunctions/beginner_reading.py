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



sort_websites = sorted(dict_avlen.items(), key=lambda x: x[1], reverse=False)

list_of_dicts = []
for i in sort_websites[0:8]:
    website = i[0]
    percentage = counter_web[website]
    temp = dict([("website",website),("percentage",percentage)])
    list_of_dicts.append(temp)

with open("/Users/elenikaranikola/Desktop/NewsBackend/dependencies/api_charts/beginner_reading.csv", "w") as write_file:
    json.dump(list_of_dicts[0:8], write_file)
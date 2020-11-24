import pandas as pd
import unicodedata
import string
import json
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from settings import DB_CREDS
from utilities import finalNormalize, readText, writeData

#get all the data from the articles table
sql_command = "SELECT * FROM articles"
df = readText(sql_command)

#save each column in a different variable
id = df['id']
topic = df['topic']
subtopic = df['subtopic']
website = df['website']
article_date = df['article_date']
author = df['author']
url = df['url']

article_body = []
title = []

#for each article preprocess its body
for x in df['article_body']:
    final_text = finalNormalize(x)
    res = " ".join(final_text)
    article_body.append(res)

#for each article preprocess its title
for x in df['title']:
    final_title = finalNormalize(x)
    res = " ".join(final_title)
    title.append(res)

#save all data to a dictionary
dict = {'id':id, 'topic':topic, 'subtopic':subtopic, 'website': website, 'article_date':article_date, 'author':author, 'title':title, 'article_body':article_body, 'url':url}

#add dict t dataframe
new_df = pd.DataFrame(dict) 
  
#saving the dataframe in a csv file
new_df.to_csv("dependencies/output.csv", index=False)     


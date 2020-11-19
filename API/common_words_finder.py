from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import statistics 
import collections
from collections import Counter,defaultdict,OrderedDict,namedtuple 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from statistics import stdev
import mysql.connector  
from settings import DB_CREDS
from utilities import finalNormalize, readText, writeData, writeCell

#get all the data from the articles table
sql_command = "SELECT id FROM articles"
indexes = readText(sql_command)

#print(indexes.values)
for i in indexes.to_numpy():
    index = (i[0]).item()
    #this will be the input
    #index = 36588

    #we will connect with the database and get data
    df = pd.read_csv('output.csv', index_col='id')

    #fill all null values in the table
    df = df.fillna(" ")

    #create empty dictionary
    my_dict = {k:0 for k in df.index}

    #this will be the set o words from our input
    setA = set((df.at[index,'article_body']).split())

    #get intersection for this for all the articles from our data
    for x in df.index:
        setB = set((df.at[x,'article_body']).split())
        my_dict.update({x:len(setA.intersection(setB))})


    sort_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

    key1 =  (sort_dict[1])[0] 
    key2 =  (sort_dict[2])[0]
    key3 =  (sort_dict[3])[0]
    key4 =  (sort_dict[4])[0]
    key5 =  (sort_dict[5])[0]

    #write result to database
    writeCell(index,key1,key2,key3,key4,key5)

    

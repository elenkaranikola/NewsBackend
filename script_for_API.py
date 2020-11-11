from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import statistics 
import collections
from collections import Counter,defaultdict,OrderedDict,namedtuple 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from statistics import stdev

#this will be the input
index = 36588

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
#we get results for the second to the forth, obviously the first is going to be the id of the article its self 
# we will want to return this as response
print(sort_dict[1:4])

#    article_words = set(x.split())
    

#------------------------               DESCRIPTION                 ----------------------------------
#this file contains all the funtions used in other files
#-----------------------------------------------------------------------------------------------------

import pandas as pd
import unicodedata
import re
import string
import json
import itertools
import statistics 
from joblib import Parallel, delayed
import collections
import mysql.connector  
from collections import Counter,defaultdict,OrderedDict,namedtuple
from settings import DB_CREDS


#establish connection with database
cnx = mysql.connector.connect(
    host = DB_CREDS['host'],
    user = DB_CREDS['user'],
    passwd = DB_CREDS['pass'],
    database = DB_CREDS['db']   
)

#make all small function
def removeAccents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return (u"".join([c for c in nfkd_form if not unicodedata.combining(c)])).lower()

#keep all small words
def normalize (i):
    all_small = removeAccents(i)
    split_to_tokens = re.findall(r'[α-ω]+',all_small)
    return(split_to_tokens)

def finalNormalize (i):
    text = normalize(i)
    f = open("dependencies/filter_words.txt", "r")
    f.readline()
    stop_words=f.readline()
    short_words=f.readline()
    f.close()
    f = open("dependencies/imported_stop_words.txt", "r")
    fix_words=f.readline()
    f.close()
    filtered_sentence = list(filter(lambda i: i not in stop_words, text))
    second_filter = list(filter(lambda i: i not in short_words, filtered_sentence))
    third_filter = list(filter(lambda i: i not in fix_words, second_filter))
    return(third_filter)

def uselessWords(input_str):
    #combine all the words from every article and to it parallel
    all_words = Parallel(n_jobs=-1, backend="loky")(map(delayed(normalize), input_str))

    #put them in one list
    all_articles_combined = list(itertools.chain.from_iterable(all_words))

    #find the shortest in length
    short_words = sorted(list(set(all_articles_combined)),key=len)
    short = short_words[0:500]

    #find the 118 most commonly used words
    most_common_words = Counter(all_articles_combined).most_common(300)

    #keep the most common words    
    stop_words = []
    for i in most_common_words:
        stop_words.append(i[0])
    
    return (stop_words,short)

def SortMyDict(df,index):

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
    return (sort_dict)

#read function
def readText(i):
    df = pd.read_sql(i, con=cnx)
    return (df)

#write funtion
def writeData (out_file,text):
    fname = out_file
    with open(fname, 'a+') as f:
        f.write('\n')
        f.write(text)


#function that gets as input text and returns a dict with the 100 most popular ones
def FindTop(articles):
    #initiate an empty list to save all the words of all the articles
    all_words_compined = []
    
    for words in articles:
        #split the articles to words
        word_list = words.split()
        #save the words to our list
        all_words_compined.extend(word_list)
        
    #find the 500 most common
    top = Counter(all_words_compined).most_common(100)
    return top

def CombineArticles(category,df):
    culture_articles = df.groupby(['topic']).get_group(category)['article_body']
    #set an empty variable to save all the words 
    category_words_combined = []

    #combine all words from each article
    for words in culture_articles:
        word_list = words.split()
        category_words_combined.extend(word_list) 
    
    return(category_words_combined)


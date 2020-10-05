#------------------------               DESCRIPTION                 ----------------------------------
#this file contains all the funtions used in other files
#-----------------------------------------------------------------------------------------------------

import pandas as pd
import unicodedata
import re
import string
import json
import itertools
from joblib import Parallel, delayed
import collections
import mysql.connector  
from collections import Counter,defaultdict,OrderedDict,namedtuple
#from settings import stop_words, short_words
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
    filtered_sentence = list(filter(lambda i: i not in (stop_words or short_words), text))
    return(filtered_sentence)

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

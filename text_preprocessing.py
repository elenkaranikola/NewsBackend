import pandas as pd
import unicodedata
import re
import string
import json
import itertools
from joblib import Parallel, delayed
import collections
from collections import Counter,defaultdict,OrderedDict,namedtuple     
import mysql.connector  
from settings import DB_CREDS
from settings import stop_words
   
#make all small function
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return (u"".join([c for c in nfkd_form if not unicodedata.combining(c)])).lower()

#keep all small words
def normalize (i):
    all_small = remove_accents(i)
    split_to_tokens = re.findall(r'[α-ω]+',all_small)
    filtered_sentence = list(filter(lambda i: i not in stop_words, split_to_tokens))
    return(filtered_sentence)

#establish a connection with the database
cnx = mysql.connector.connect(
    host = DB_CREDS['host'],
    user = DB_CREDS['user'],
    passwd = DB_CREDS['pass'],
    database = DB_CREDS['db']   
)

#get all the data from the articles table
df = pd.read_sql('SELECT * FROM articles', con=cnx)

#for each article preprocess its body
for x in df['article_body']:
    final_text = normalize(x)
    res = [" ".join(final_text)]
    print(res)
    break



#query = ("SELECT article_body FROM articles ")
#cursor = cnx.cursor()
#cursor.execute(query)


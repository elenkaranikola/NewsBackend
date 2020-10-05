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
from utilities import finalNormalize, readText, writeData

#get all the data from the articles table
sql_command = "SELECT * FROM articles"
df = readText(sql_command)

#for each article preprocess its body
for x in df['article_body']:
    final_text = finalNormalize(x)
    res = " ".join(final_text)
    writeData("dependencies/output.csv",res)
    print(res)
    break
    


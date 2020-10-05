#------------------------               DESCRIPTION                 ----------------------------------
#in this python file we find and extract the most common words in the given file
#the extracted data are being saved in dependencies/filter_words.csv
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
from settings import DB_CREDS
from utilities import finalNormalize, cnx

fname = 'dependencies/filter_words.txt'

#get all data
df = pd.read_sql('SELECT * FROM articles', con=cnx)

#save in the text variable tha articles body
text = df['article_body']

#normalize the extracted data
file_data = finalNormalize(text)
data1 = file_data[0]
data2 = file_data[1]

#write our extracted data in filter_words.txt
with open(fname, 'a+') as f:
    f.write('\n')
    f.write(', '.join(map(str, data1)))
    f.write('\n')
    f.write(', '.join(map(str, data2)))

import pandas as pd
import unicodedata
import re
import string
import json
import itertools
from joblib import Parallel, delayed
import collections
import most_common_words 
from collections import Counter,defaultdict,OrderedDict,namedtuple       
   
#make all small function
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return (u"".join([c for c in nfkd_form if not unicodedata.combining(c)])).lower()

#keep all small words
def normalize (i):
    all_small = remove_accents(i)
    split_to_tokens = re.findall(r'[α-ω]+',all_small)
    filtered_sentence = list(filter(lambda i: i not in most_common_words.stop_words, split_to_tokens))
    return(filtered_sentence)

#get data from jason file
data = pd.read_json('/Users/elenikaranikola/Desktop/articles.json')
text = data["article_body"]

for i in text[:2]:    
    final_text = normalize(i)
    print(final_text)

#print (sorted(set(itertools.chain.from_iterable(all_words)),key=len)[:250])

#closing file
#f.close()

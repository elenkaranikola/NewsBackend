import pandas as pd
import unicodedata
import string
import json
import csv
import sys
import re
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from utilities import removeAccents,normalize
from settings import countries_list

#read the data
df = pd.read_csv('/Users/elenikaranikola/Desktop/NewsBackend/output.csv')

#fill all null values in the table
df = df.fillna(" ")

#normalize the countries list and save the to normal_list list
normal_list = []

for x in countries_list:   
    all_in_one_string = " "
    temp = normalize(x)
    all_in_one_string = temp[0]
    for y in temp[1:]:
        all_in_one_string = all_in_one_string + " " + y
    normal_list.append(all_in_one_string)

#create a countries_dict, economics_dict, world_dict, politics_dict with key the countries name and value zero
countries_dict = {k:0 for k in normal_list}

for x in df['article_body']:
    
    #get a the article splitted by words in a list
    article = x
    article_list = x.split()
    
    #rotate over each dict key and count the times it is appeared
    for y in countries_dict:
        res = re.search(rf"\b(?=\w){y}(?!\w)", article, re.IGNORECASE)
        if res != None:
            countries_dict.update({y:countries_dict[y]+1}) 

sorted_len = sorted(countries_dict.items(), key=lambda x: x[1], reverse=True)
 
list_of_dicts = []
for i in sorted_len:
    list_of_dicts.append(dict([("name",i[0]),("value",i[1])]))


with open('/Users/elenikaranikola/Desktop/NewsBackend/dependencies/api_charts/countries.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(list_of_dicts)
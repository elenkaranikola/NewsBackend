import numpy as np
import pandas as pd
import statistics 
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsCleanser')
from utilities import writeCell,SortMyDict

#get all the data from the articles table
sql_command = "SELECT id FROM articles"
indexes = readText(sql_command)

for i in indexes.to_numpy():
    index = (i[0]).item()

    #we will connect with the database and get data
    df = pd.read_csv('output.csv', index_col='id')

    #call a function to pass our articles an our index and get back for each index in our database the 5 closest articles 
    sort_dict = SortMyDict(df,index)

    key1 =  (sort_dict[1])[0] 
    key2 =  (sort_dict[2])[0]
    key3 =  (sort_dict[3])[0]
    key4 =  (sort_dict[4])[0]
    key5 =  (sort_dict[5])[0]

    #write result to database
    writeCell(index,key1,key2,key3,key4,key5)
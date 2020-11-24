import numpy as np
import pandas as pd
import statistics 
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsCleanser')
from utilities import WriteCell,SortMyDict

#get all the data from the articles table
sql_command = "SELECT id FROM articles"
indexes = readText(sql_command)

for i in indexes.to_numpy():
    index = (i[0]).item()

    #we will connect with the database and get data
    df = pd.read_csv('output.csv', index_col='id')

    #call a function to pass our articles an our index and get back for each index in our database the 5 closest articles 
    sort_dict = SortMyDict(df,index)

    keys = [0]*5
    for i in range(0,5):
        keys[i] = (sort_dict[i+1])[0] 

    #write result to database
    WriteCell(index,keys)
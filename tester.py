#------------------------               DESCRIPTION                 ----------------------------------
#this file is the tester for the classifiers succes rate, if you want to create a diagram for 
#different values for the the classifier uncomment the sections as mentioned in the file
#-----------------------------------------------------------------------------------------------------

# coding: utf-8
import pandas as pd
import collections
from matplotlib import pyplot as plt
from collections import Counter
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from utilities import Predictor,finalNormalizeFullPath, ClassifierTester



#read input
#shuffle data and splint in 70%, 30% for testing
df = pd.read_csv('/Users/elenikaranikola/Desktop/NewsBackend/output.csv', index_col='id')
df = df.fillna(" ")

first_split  = df.sample(frac = 0.7)

df2=df.drop(first_split.index)

# uncomment for diagramm
#y_list = []
#x_list = []

#for i in range (100,40000,1000):
max = 0
sum = 0
correct_category = 0
wrong_category = 0
all_categories =  ClassifierTester(first_split,2000,df)

#y_list.append(i) -- code for diagramm
for x in df2.index:
    article = df2.at[x,'article_body'] 
    clean_input = finalNormalizeFullPath(article)
    category = Predictor(clean_input,all_categories)
    if category == df2.at[x,'topic']:
        correct_category += 1
    else:
        wrong_category += 1


final_res = correct_category*100/(wrong_category + correct_category)
print("success rate: ", final_res, " percent for 2000 most important words")

# uncomment for diagramm
#x_list.append(final_res)

#plt.title("Classifiers prediction success") 
#plt.xlabel("% persentage of correct results") 
#plt.ylabel("number of words used for the classifier") 
#plt.plot(x_list,y_list) 
#plt.grid(axis='y')
#plt.grid(axis='x')
#plt.show()
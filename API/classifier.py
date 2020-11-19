# coding: utf-8
from matplotlib import pyplot as plt
import pandas as pd
import collections
from collections import Counter,defaultdict,OrderedDict,namedtuple 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from utilities import FindTop,CombineArticles

#read input
df = pd.read_csv('/Users/elenikaranikola/Desktop/NewsBackend/output.csv')
df = df.fillna(" ")                  #fill all null values, otherwise there will be problems during our text editing
articles = list(df['article_body'])  #get the article body
top_words = FindTop(articles)       #get the 100 most popular words in a list    

words_dict = {}

#from the list of words create a dictionary with key the word and value the times we counted it in all our data
for word in top_words:
    words_dict[word[0]]=word[1]

#List unique values in the df['topic'] column
categories = df.topic.unique()

all_categories = {}

#for each category combine all it articles words
#and calculate the percent of appearance based on the top 100 words
#and save in a new dict with key the category and value another dict with key the word and value the percentage
for category in categories:
    category_words_combined = CombineArticles(category,df)
    sub_dict = {}
    cnt = Counter(category_words_combined)

    for word in words_dict:
        persentage = cnt[word] / words_dict[word]
        sub_dict[word] = persentage
        
    all_categories[category] = sub_dict

###--------------------------------------------------------------------------------------------------------------
### Tester to see the success we have, read again all our database and see if we guess right each category
###--------------------------------------------------------------------------------------------------------------

#main tester
df2 = pd.read_csv('/Users/elenikaranikola/Desktop/NewsBackend/output.csv', index_col='id')
df2 = df2.fillna(" ")
c = 0
w = 0
for x in df2.index:
    article = df2.at[x,'article_body'] 
    input_to_tokens = set(article.split())

    max  = 0
    for category in all_categories:
        sum = 0
        for i in input_to_tokens:
            #print(i)
            if i in all_categories[category]:
                sum += all_categories[category][i]
                #print(sum)
        if max < sum :
            max = sum
            final_category = category
    if final_category == df2.at[x,'topic']:
        c += 1
    else:
        w += 1


final_res = c/w * 100
print(final_res)





#input_to_tokens = set(my_input.split())
#
#max  = 0
#for category in all_categories:
#    sum = 0
#    for i in input_to_tokens:
#        #print(i)
#        if i in all_categories[category]:
#            sum += all_categories[category][i]
#            #print(sum)
#    if max < sum :
#        max = sum
#        final_category = category
#
#print(" ")
#print('FINAL RESULT IS!')
#print(final_category)


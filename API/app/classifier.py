# coding: utf-8
import pandas as pd
import collections
from collections import Counter
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from utilities import FindTop,CombineArticles,MainTester,Predictor,finalNormalizeFullPath
from settings import cleaned_output,categories

#read input
def Classifier(my_input):
    df = pd.read_csv(cleaned_output)
    df = df.fillna(" ")                
    articles = list(df['article_body'])  
    top_ten_words = FindTop(articles)        

    words_dict = {}

    #from the list of words create a dictionary with key the word and value the times we counted it in all our data
    for word in top_ten_words:
        words_dict[word[0]]=word[1]

    all_categories = {}

    #for each category combine all its articles words
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

    #run the tester
    #result = MainTester(all_categories)
    clean_input = finalNormalizeFullPath(my_input)
    result = Predictor(clean_input,all_categories)
    return result
    #print(result)

#use all categories to see where our input belongs




import csv
import pandas as pd


#with open('../dataset/DO_NOT_ALTER/sample_english.csv', 'r') as f:
    #reader = csv.DictReader(f)
#reading csv
dataset = pd.read_csv ('../dataset/DO_NOT_ALTER/sample_english.csv')


#counting retweet 
retweets = dataset['is_retweet'].value_counts()

print (retweets)

linecount = 29943

#calculating retweets as percentage 
percent_retweets = (retweets / linecount) * 100


#spits out info to new csv
with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow (['number of tweets' , 'percent of tweets'])
    writer.writerow (retweets)
    writer.writerow (percent_retweets)


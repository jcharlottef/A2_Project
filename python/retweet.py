import csv
import pandas as pd


#with open('../dataset/DO_NOT_ALTER/sample_english.csv', 'r') as f:
    #reader = csv.DictReader(f)

dataset = pd.read_csv ('../dataset/DO_NOT_ALTER/sample_english.csv')


retweets = dataset['is_retweet'].value_counts()

print (retweets)

linecount = 29943

percent_retweets = (retweets / linecount) * 100

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow (['number of tweets' , 'percent of tweets'])
    writer.writerow (retweets)
    writer.writerow (percent_retweets)


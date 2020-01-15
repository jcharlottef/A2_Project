import csv

with open('../dataset/DO_NOT_ALTER/sample_english.csv', 'r') as f:
    reader = csv.DictReader(f)

retweets = df['is_retweet'].value_counts()

percent_retweets = retweets / 


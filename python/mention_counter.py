#!/usr/bin/env python3
import csv
import sys

#read data from STDIN and split on each newline
data = sys.stdin.read().splitlines()


# use python's csv library to create a csv reader and a writer
reader = csv.DictReader(data)

mention = 0
word = "hillary clinton"



# loop through tweets and count number of mentions
for row in reader:
	# filter rows
    if word in row['tweet_text'].lower():
    	# write rows that match above filter
      mention = mention + 1 


linecount = 29943

# puts mentions into percent format
percent_mention =  (mention / linecount) * 100


#prints number and percent of mentions
print(word) 
print(" is mentioned in ")
print(percent_mention) 
print(" percent of tweets")
print (" ")



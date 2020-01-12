#!/usr/bin/env python3
import csv
import sys

#read data from STDIN and split on each newline
data = sys.stdin.read().splitlines()

Trump_mention = 0


# loop through tweets and count number of mentions
for row in reader:
	# filter rows
    if "Trump" in row['tweet_text']:
    	# write rows that match above filter
       Trump_mention = Trump_mention + 1 


linecount = 29943

percent_Trump_mention =  Trump_mention / linecount

print(percent_Trump_mention)
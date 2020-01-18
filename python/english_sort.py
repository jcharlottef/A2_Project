
#!/usr/bin/env python3
#this script filters out only english lanauge tweets
import csv
import sys

#read data from STDIN and split on each newline
data = sys.stdin.read().splitlines()

# use python's csv library to create a csv reader and a writer
reader = csv.DictReader(data)
writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)

# write the header (first line of the csv)
writer.writeheader()

# loop through the rows in the original csv
for row in reader:
	# filter rows by english langauge
    if row['tweet_language'] == 'en':
    	# write rows that match above filter
        writer.writerow(row)

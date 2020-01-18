#!/usr/bin/env python3
import csv
import sys
import pandas as pd

#This script makes a list of unique User ID adn outputs it to a new file


# define columns to keep
include_columns = ['userid', 'account_creation_date' , 'follower_count' , 'following_count', 'account_language']
# load the data into pandas
df = pd.read_csv(sys.stdin)
df = df[[x for x in df.columns if x in include_columns]]
# drop duplicates
df = df.drop_duplicates()
# output the file
df.to_csv(sys.stdout, index=False)
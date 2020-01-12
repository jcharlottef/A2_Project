#!/usr/bin/env python3
import csv
import sys
import pandas as pd
# define columns to keep
include_columns = ['userid', 'account_creation_date']
# load the data into pandas
df = pd.read_csv(sys.stdin)
#df = df[[x for x in df.columns if x in include_columns]]
# drop duplicates
df = df.drop_duplicates()
# output the file
df.to_csv(sys.stdout, index=False)
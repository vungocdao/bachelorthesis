import pandas as pd
from textblob import TextBlob

df = pd.read_csv("Restaurant_Review_1001.csv", sep = ',')

print(df)


"""
Test with csv (only works with iterating rows as of now)

import csv
from textblob import TextBlob

infile = 'xxx.csv'

with open(infile, 'r') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            sentence = row[0], column[0]
            blob = TextBlob(sentence)
            print(sentence)
            print(blob.sentiment)
"""

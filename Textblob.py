import csv
from textblob import TextBlob as tb

infile = 'xxx.csv'

with open(infile, 'r') as csvfile:
        columns = csv.reader(csvfile)
        for column in columns:
            sentence = column[2]
            blob = TextBlob(sentence)
            print(sentence)
            print(blob.sentiment)

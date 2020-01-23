import csv
from textblob import TextBlob

infile = 'Restaurant_Review_1001.csv'

with open(infile, 'r') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            sentence = row[0], column[0]
            blob = TextBlob(sentence)
            print(sentence)
            print(blob.sentiment)

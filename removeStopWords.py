import pandas as pd

ds1 = "Amazon_Reviews.csv"
ds2 = "Amazon_Reviews_sample.csv"
ds3 = "IMDB_Reviews.csv"
ds4 = "IMDB_Reviews_sample.csv"
ds5 = "Restaurant_Reviews.csv"
ds6 = "Restaurant_Reviews_sample.csv"
ds7 = "Uber_Ride_Reviews.csv"
ds8 = "Uber_Ride_Reviews_sample.csv"
ds9 = "Yelp_Reviews.csv"
ds10 = "Yelp_Reviews_sample.csv"

def removeStopWords(File):
    df = pd.read_csv(File)
    df['Review'] = df['Review'].replace()
    df.to_csv(File, index=False)

removeStopWords(ds1)
removeStopWords(ds2)
removeStopWords(ds3)
removeStopWords(ds4)
removeStopWords(ds5)
removeStopWords(ds6)
removeStopWords(ds7)
removeStopWords(ds8)
removeStopWords(ds9)
removeStopWords(ds10)

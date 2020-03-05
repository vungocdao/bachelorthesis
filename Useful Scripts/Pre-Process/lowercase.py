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

def lowercase(File):
    df = pd.read_csv(File)
    df['Review'] = df['Review'].str.lower()
    df.to_csv(File, index = False)

lowercase(ds1)
lowercase(ds2)
lowercase(ds3)
lowercase(ds4)
lowercase(ds5)
lowercase(ds6)
lowercase(ds7)
lowercase(ds8)
lowercase(ds9)
lowercase(ds10)

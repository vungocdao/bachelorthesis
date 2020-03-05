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

def removeSpecialCharacters(File):
    df = pd.read_csv(File)
    df['Review'] = df['Review'].replace(r'[^A-Za-z ]+', '', regex = True)
    df.to_csv(File, index=False)

removeSpecialCharacters(ds1)
removeSpecialCharacters(ds2)
removeSpecialCharacters(ds3)
removeSpecialCharacters(ds4)
removeSpecialCharacters(ds5)
removeSpecialCharacters(ds6)
removeSpecialCharacters(ds7)
removeSpecialCharacters(ds8)
removeSpecialCharacters(ds9)
removeSpecialCharacters(ds10)

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

def removeUnnamed(ds):
    df = pd.read_csv(ds)
    df.drop(df.filter(regex="Unnamed"),axis=1,inplace=True)
    df.to_csv(ds,index=False)

removeUnnamed(ds2)
removeUnnamed(ds3)
removeUnnamed(ds4)
removeUnnamed(ds5)
removeUnnamed(ds6)
removeUnnamed(ds7)
removeUnnamed(ds8)
removeUnnamed(ds9)
removeUnnamed(ds10)
removeUnnamed(ds1)

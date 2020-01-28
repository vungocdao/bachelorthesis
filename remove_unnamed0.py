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

def remove_unnamed(ds):
    df = pd.read_csv(ds)
    df.drop(df.filter(regex="Unname"),axis=1,inplace=True)
    df.to_csv(ds,index=False)

remove_unnamed(ds2)
remove_unnamed(ds3)
remove_unnamed(ds4)
remove_unnamed(ds5)
remove_unnamed(ds6)
remove_unnamed(ds7)
remove_unnamed(ds8)
remove_unnamed(ds9)
remove_unnamed(ds10)
remove_unnamed(ds1)

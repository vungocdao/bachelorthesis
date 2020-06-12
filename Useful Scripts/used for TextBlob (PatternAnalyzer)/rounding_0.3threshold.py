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

def round(ds):
    df = pd.read_csv("Textblob_Analysed_" + ds)
    df.loc[(df['Polarity_result'] >= 0.3), 'Polarity_rounded'] = 1
    df.loc[(df['Polarity_result'] <= -0.3), 'Polarity_rounded'] = -1
    df.loc[(df['Polarity_result'] < 0.3) & (df['Polarity_result']> -0.3), 'Polarity_rounded'] = 0
    df['Polarity_rounded'] = df['Polarity_rounded'].astype(int)
    df.to_csv("Textblob_Analysed_Rounded_0.3_" + ds, index=False)
round(ds1)
# round(ds2)
round(ds3)
# round(ds4)
round(ds5)
# round(ds6)
round(ds7)
# round(ds8)
round(ds9)
# round(ds10)

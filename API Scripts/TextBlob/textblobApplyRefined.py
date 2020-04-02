import pandas as pd
from textblob import TextBlob

# Variables with name of csv file
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

# Iterates through the Column and applies textblob.sentiment
def sentiment_calc(Review):
    try:
        return TextBlob(Review).sentiment.polarity
    except:
        return None

# Initializes DataFrame, Applies API and creates 'Result' column, saves into new File
def apply_analysis(ds):
    df = pd.read_csv(ds)
    df['Polarity_result'] = df['Review'].apply(sentiment_calc)
    df.to_csv('Textblob_Analysed_PA_' + ds, index=False)

apply_analysis(ds1)
# apply_analysis(ds2)
apply_analysis(ds3)
# apply_analysis(ds4)
apply_analysis(ds5)
# apply_analysis(ds6)
apply_analysis(ds7)
# apply_analysis(ds8)
apply_analysis(ds9)
# apply_analysis(ds10)

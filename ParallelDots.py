import pandas as pd
import paralleldots

# Initializes a DataFrame out of the csv file
df = pd.read_csv("Yelp_Reviews_sample.csv")

# Iterates through the Column and applies paralleldots.sentiment
def sentiment_calc(Review):
    try:
        return paralleldots.sentiment(Review)
    except:
        return None

df['Result'] = df['Review'].apply(sentiment_calc)

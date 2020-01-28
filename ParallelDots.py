import pandas as pd
import paralleldots

paralleldots.set_api_key("BGRkdyykQLRFR4ZAsDQqC21cCfKhAhbB29OESIGZn7Y")
# Initializes a DataFrame out of the csv file
df = pd.read_csv("Yelp_Reviews_sample.csv")

# Iterates through the Column and applies paralleldots.sentiment
def sentiment_calc(Review):
    try:
        return paralleldots.sentiment(Review)
    except:
        return None

df['Result'] = df['Review'].apply(sentiment_calc)

df.to_csv("Analysed_Yelp_Reviews_sample.csv", index=False)

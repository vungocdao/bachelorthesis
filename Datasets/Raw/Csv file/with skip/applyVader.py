from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

ds1 = "Amazon_Reviews"
ds2 = "IMDB_Reviews"
ds3 = "Restaurant_Reviews"
ds4 = "Uber_Ride_Reviews"
ds5 = "Yelp_Reviews"
ds6 = "Amazon_Reviews_sample"
sid = SentimentIntensityAnalyzer()

def sentiment_calc(Review):
    try:
        return sid.polarity_scores(Review)
    except:
        return None

def getVaderScore(file):
    df = pd.read_csv(file + ".csv")
    df['Polarity_result'] = df['Review'].apply(sentiment_calc)
    df.to_csv("Vader_Analysed_" + file + ".csv", index=False)

getVaderScore(ds1)
getVaderScore(ds2)
getVaderScore(ds3)
getVaderScore(ds4)
getVaderScore(ds5)

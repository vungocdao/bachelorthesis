import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

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
ds11 = "Negation_Dataset.csv"
ds12 = "Bias_Dataset.csv"

# Iterates through the Column and applies textblob.sentiment
def sentiment_calc(Review):
    try:
        return TextBlob(Review, analyzer=NaiveBayesAnalyzer()).sentiment
    except:
        return None

# Initializes DataFrame, Applies API and creates 'Result' column, saves into new File
def apply_analysis(ds):
    df = pd.read_csv(ds)
    df['Result'] = df['Review'].apply(sentiment_calc)
    # Splits the Result Column into Polarity and Subjectivity
    sentiment_series = df['Result'].tolist()
    columns = ['Polarity_result', 'Positive_result', 'Negative_result']
    df2 = pd.DataFrame(sentiment_series, columns=columns, index=df.index)
    # Combine both DataFrames into 1
    df3 = pd.merge(df, df2, left_index=True, right_index=True)
    # deletes the column Result, so that there's no redundant data
    del df3['Result']
    # save the new Dataset into a csv file
    df3.to_csv('Textblob_Analysed_' + ds, index=False)

apply_analysis(ds1)
# apply_analysis(ds2)
#apply_analysis(ds3)
# apply_analysis(ds4)
#apply_analysis(ds5)
# apply_analysis(ds6)
#apply_analysis(ds7)
# apply_analysis(ds8)
#apply_analysis(ds9)
# apply_analysis(ds10)
apply_analysis(ds11)
apply_analysis(ds12)
import pandas as pd
from textblob import TextBlob

# Initializes a DataFrame out of the csv file
df = pd.read_csv("Uber_Ride_Review_1345.csv")

# Iterates through the Column and applies Textblob.sentiment
def sentiment_calc(ride_review):
    try:
        return TextBlob(ride_review).sentiment
    except:
        return None

df['Result'] = df['ride_review'].apply(sentiment_calc)

# Splits the Result Column into Polarity and Subjectivity
sentiment_series = df['Result'].tolist()
columns = ['Polarity', 'Subjectivity']
df2 = pd.DataFrame(sentiment_series, columns=columns, index=df.index)

# Combine both DataFrames into 1
df3 = pd.merge(df, df2, left_index=True, right_index=True)
# deletes the column Result, so that there's no redundant data
del df3['Result']
# save the new Dataset into a csv file
df3.to_csv('Textblob_Analysed_UberRide_Review.csv', index=False)

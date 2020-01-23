from __future__ import prin_statement
import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint
import pandas as pd

# Initializes a DataFrame out of the csv file
df = pd.read_csv("xxx.csv")

# API key to access DeepAffects API
deepaffects.configuration.api_key['apikey'] = '<dKsguddWi6LYRexyd6SOndI3vKrAyhgU>'

# Create API Class with sentence that needs to be featurized
api_instance = deepaffects.EmotionApi()
var body = {
    "content": "TEXT"
}

try:
    api_response = api_instance.sync_text_recognise_emotion(body)
    pprint(api_response)
except ApiExcpetion as e:
    print("Exception when calling EmotionApi->sync_recognise_emotion: %\n" % e)

"""

# Iterates through the Column and applies Textblob.sentiment
def sentiment_calc(columnname):
    try:
        return TextBlob(columnname).sentiment
    except:
        return None

df['Result'] = df['columnname'].apply(sentiment_calc)

# Splits the Result Column into Polarity and Subjectivity
sentiment_series = df['Result'].tolist()
columns = ['Polarity', 'Subjectivity']
df2 = pd.DataFrame(sentiment_series, columns=columns, index=df.index)

# Combine both DataFrames into 1
df3 = pd.merge(df, df2, left_index=True, right_index=True)
# deletes the column Result, so that there's no redundant data
del df3['Result']
# save the new Dataset into a csv file
df3.to_csv('Textblob_Analysed_Domain_Review.csv', index=False)

"""

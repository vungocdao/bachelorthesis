import pandas as pd

ds1 = "Amazon_Reviews"
ds2 = "IMDB_Reviews"
ds3 = "Restaurant_Reviews"
ds4 = "Uber_Ride_Reviews"
ds5 = "Yelp_Reviews"
ds6 = "Amazon_Reviews_sample"

def splitPolarityResult(file):
    df = pd.read_csv("Vader_Analysed_" + file + ".csv")
    df['Polarity_result'] = df['Polarity_result'].replace(r'[^-\d+"."+","]+', '', regex = True)
    df['Polarity_result'].to_csv("Vader_Result_" + file + ".txt", sep='\n', index = None)

splitPolarityResult(ds1)
splitPolarityResult(ds2)
splitPolarityResult(ds3)
splitPolarityResult(ds4)
splitPolarityResult(ds5)

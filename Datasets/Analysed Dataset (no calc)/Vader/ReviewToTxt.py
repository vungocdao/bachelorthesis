import pandas as pd

ds1 = "Vader_Analysed_Amazon_Reviews"
ds2 = "Vader_Analysed_IMDB_Reviews"
ds3 = "Vader_Analysed_Restaurant_Reviews"
ds4 = "Vader_Analysed_Uber_Ride_Reviews"
ds5 = "Vader_Analysed_Yelp_Reviews"

def transformToTxt(file):
    read_file = pd.read_csv(file + ".csv")
    read_file['Polarity_result'].to_csv(file + ".txt", sep='\n', index = None)

transformToTxt(ds1)
transformToTxt(ds2)
transformToTxt(ds3)
transformToTxt(ds4)
transformToTxt(ds5)

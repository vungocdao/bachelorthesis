import pandas as pd

ds1 = "Amazon_Reviews"
ds2 = "Amazon_Reviews_sample"
ds3 = "IMDB_Reviews"
ds4 = "IMDB_Reviews_sample"
ds5 = "Restaurant_Reviews"
ds6 = "Restaurant_Reviews_sample"
ds7 = "Uber_Ride_Reviews"
ds8 = "Uber_Ride_Reviews_sample"
ds9 = "Yelp_Reviews"
ds10 = "Yelp_Reviews_sample"

def ConvertCsvToJson(file):
    read_file = pd.read_csv(file + ".csv")
    read_file.to_json("JSON_" + file + ".json", orient='split', index=None, indent=1)

ConvertCsvToJson(ds1)
ConvertCsvToJson(ds2)
ConvertCsvToJson(ds3)
ConvertCsvToJson(ds4)
ConvertCsvToJson(ds5)
ConvertCsvToJson(ds6)
ConvertCsvToJson(ds7)
ConvertCsvToJson(ds8)
ConvertCsvToJson(ds9)
ConvertCsvToJson(ds10)

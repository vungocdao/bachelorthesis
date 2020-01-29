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

def ConvertExcelToCsv(file):
    read_file = pd.read_excel("MeaningCloud_" + file + ".xlsx")
    read_file.to_csv("MeaningCloud_Analysed_" + file + ".csv", index = False)

ConvertExcelToCsv(ds2)
ConvertExcelToCsv(ds4)
ConvertExcelToCsv(ds6)
ConvertExcelToCsv(ds8)
ConvertExcelToCsv(ds10)

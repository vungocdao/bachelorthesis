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
ds11 = "Ambiguity_Dataset"
ds12 = "Bias_Dataset"
ds13 = "Negation_Dataset"

def ConvertCsvToExcel(file):
    read_file = pd.read_csv(file + ".csv")
    read_file.to_excel("Excel_" + file + ".xlsx", index = None, header = True)

#ConvertCsvToExcel(ds1)
#ConvertCsvToExcel(ds2)
#ConvertCsvToExcel(ds3)
#ConvertCsvToExcel(ds4)
#ConvertCsvToExcel(ds5)
#ConvertCsvToExcel(ds6)
#ConvertCsvToExcel(ds7)
#ConvertCsvToExcel(ds8)
#ConvertCsvToExcel(ds9)
#ConvertCsvToExcel(ds10)
ConvertCsvToExcel(ds11)
ConvertCsvToExcel(ds12)
ConvertCsvToExcel(ds13)
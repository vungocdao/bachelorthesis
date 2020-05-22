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

def ConvertExcelToCsv(file):
    read_file = pd.read_excel(file + ".xlsx", sheet_name='Sheet1')
    read_file.to_csv(file + ".csv", index = False)

#ConvertExcelToCsv(ds2)
#ConvertExcelToCsv(ds4)
#ConvertExcelToCsv(ds6)
#ConvertExcelToCsv(ds8)
#ConvertExcelToCsv(ds10)
ConvertExcelToCsv(ds11)
ConvertExcelToCsv(ds12)
ConvertExcelToCsv(ds13)

import pandas as pd

ds1 = "Textblob_Analysed_Rounded_Amazon_Reviews"
ds2 = "Textblob_Analysed_Rounded_0.3_Amazon_Reviews"
ds3 = "Calc_IMDB_with_skip"
ds4 = "Calc_IMDB_with_skip_0.3"
ds5 = "Textblob_Analysed_Rounded_Restaurant_Reviews"
ds6 = "Textblob_Analysed_Rounded_0.3_Restaurant_Reviews"
ds7 = "Calc_Uber_with_skip"
ds8 = "Calc_Uber_with_skip_0.3"
ds9 = "Calc_Yelp_with_skip"
ds10 = "Calc_Yelp_with_skip_0.3"

def ConvertCsvToExcel(file):
    read_file = pd.read_csv(file + ".csv")
    read_file.to_excel(file + ".xlsx", index = None, header = True)

ConvertCsvToExcel(ds1)
ConvertCsvToExcel(ds2)
ConvertCsvToExcel(ds3)
ConvertCsvToExcel(ds4)
ConvertCsvToExcel(ds5)
ConvertCsvToExcel(ds6)
ConvertCsvToExcel(ds7)
ConvertCsvToExcel(ds8)
ConvertCsvToExcel(ds9)
ConvertCsvToExcel(ds10)

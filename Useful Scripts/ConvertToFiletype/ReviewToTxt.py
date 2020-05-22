import pandas as pd

ds1 = "Amazon_Reviews"
ds2 = "IMDB_Reviews"
ds3 = "Restaurant_Reviews"
ds4 = "Uber_Ride_Reviews"
ds5 = "Yelp_Reviews"
ds6 = "Negation_Dataset"
ds7 = "Bias_Dataset"
ds8 = "Ambiguity_Dataset"

def ReviewToTxt(file):
    read_file = pd.read_csv(file + ".csv")
    read_file['Review_new'] = read_file['Review'].astype(str)
    read_file2 = read_file['Review_new']
    read_file2.to_csv(file + ".txt", sep='\n', index = None)

#ReviewToTxt(ds1)
#ReviewToTxt(ds2)
#ReviewToTxt(ds3)
#ReviewToTxt(ds4)
#ReviewToTxt(ds5)
ReviewToTxt(ds6)
ReviewToTxt(ds7)
ReviewToTxt(ds8)

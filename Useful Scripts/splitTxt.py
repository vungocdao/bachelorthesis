import pandas as pd

file1 = "Amazon_Reviews"
file2 = "IMDB_Reviews"
file3 = "Restaurant_Reviews"
file4 = "Uber_Ride_Reviews"
file5 = "Yelp_Reviews"

# used to split the txt files in single txt files
# specificially used for IBM Tone Analyzer
def splitTxtFile(file):
    df = pd.read_csv(file + ".csv")

    for i, row in df.iterrows():
        if i > len(df):
            break
        else:
            f = open(file+str(i)+'.txt', 'w')
            f.write(row[1])
            f.close()
            i+=1

splitTxtFile(file1)
splitTxtFile(file2)
splitTxtFile(file3)
splitTxtFile(file4)
splitTxtFile(file5)

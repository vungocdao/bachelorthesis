import pandas as pd

ds1 = "Negation_Dataset_Vader"
ds2 = "Bias_Dataset_Vader"

def splitPolarityResult(file):
    df = pd.read_csv(file + ".csv")
    df['Polarity_result'] = df['Polarity_result'].replace(r'[^-\d+"."+","]+', '', regex = True)
    df['Polarity_result'].to_csv("Vader_Result_" + file + ".txt", sep='\n', index = None)

splitPolarityResult(ds1)
splitPolarityResult(ds2)

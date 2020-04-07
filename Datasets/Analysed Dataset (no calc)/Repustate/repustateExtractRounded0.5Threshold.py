import pandas as pd

ds1 = "Amazon"
ds3 = "IMDB"
ds5 = "Restaurant"
ds7 = "Uber"
ds9 = "Yelp"

def round(ds):
    df = pd.read_csv("Repustate_" + ds + ".csv")
    df.loc[(df['Text'] >= 0.5), 'Polarity_rounded'] = 1
    df.loc[(df['Text'] <= -0.5), 'Polarity_rounded'] = -1
    df.loc[(df['Text'] < 0.5) & (df['Text']> -0.5), 'Polarity_rounded'] = 0
    df['Polarity_rounded'] = df['Polarity_rounded'].astype(int)
    df2 = df['Polarity_rounded']
    df2.to_excel("Repustate_Rounded_0.5_" + ds + ".xlsx", index=False)

round(ds1)
# round(ds2)
# round(ds3)
# round(ds4)
# round(ds5)

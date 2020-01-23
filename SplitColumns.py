import pandas as pd

df = pd.read_csv("Amazon_Review_3000.csv")

df[['Polarity','Review']] = df ['Polarity'].str.split(pat =',', n=1, expand=True)


# df['Review'] = df['Review'].str[1:-1]

df.to_csv("Amazon_Review_3000_new.csv",index = False)

import pandas as pd

data = pd.read_csv('Result_IMDB.txt', sep="\n", header = None)
print(data)
print(data.loc[[1976]])

data2 = data[data.index % 2 == 0]
print(data2)

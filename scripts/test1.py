import json
import pandas as pd

with open('data/output.json', 'r') as file:
    dataset = json.load(file)

# parse x:
df = pd.DataFrame(dataset)

# print(df)
len = len(df.Genre)

filtred_genre = []

print(len)

for i in range(len):
    if "1997" == df.Released_Year[i]:
        filtred_genre.append(i)

print(filtred_genre)

df1 = pd.DataFrame()
for i in filtred_genre:
    df1 = df1._append(dataset[i])

df = dataset.where(dataset.Released_Year == "1997")

len1 = len(filtred_genre)

print(len1)






print(df["year"])

# the result is a Python dictionary:
# print(y["age"])
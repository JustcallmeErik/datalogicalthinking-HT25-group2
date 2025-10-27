import json
import pandas as pd

with open("data/output.json", "r", encoding="utf-8") as f:
    data = json.load(f) 

df = pd.json_normalize(data)

# Example of a query where it looks for any title that has "fight" in it. It is not case sensetive.
#title_query = "fight"
#results = df[df["Series_Title"].str.contains(title_query, case=False, na=False)]
#print(results[["Series_Title", "Released_Year", "IMDB_Rating"]])
#this will however give us a lot of results and it will also cause the text to be shortened in the terminal so below is another example
#of a single movie with the genres Action, Adventure, Mystery. Here we are simply making it so that the individual items in the array results
#gets printed to new rows and then in the print message we have added some filler strings to make it look pretty.

title_query = "Action, Adventure, Mystery"
results = df[df["Genre"].str.contains(title_query, case=False, na=False)]
for _, row in results.iterrows():
    print("I think you would enjoy " f"{row['Series_Title']} by {row['Director']} "
          f"starring {row['Star1']}, {row['Star2']}, {row['Star3']}, {row['Star4']}. "
          f"It's from {row['Released_Year']}, and of the genres {row['Genre']}, "
          f"and its got {row['IMDB_Rating']}, on IMDB! Here is the overview: {row['Overview']}\n")


#{Series_Title} by {Director} starring {Star1, Star2, Star3, Star4}. Its from {Released_Year} and of the genre {Genre} and its got {IMDB_Rating} on IMDB! Here is the overview {Overview}.
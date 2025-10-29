import json
import csv

with open ("imdb_top_1000_cleaned.csv", "r", encoding="utf8") as f:
    read = csv.reader(f)
    next(read)
    
    data = []
    for row in read:
        genres = [g.strip() for g in row[3].split(",")]
        stars = [g.strip() for g in row[7].split(",")]

        data.append({"Series_Title": row[0],
                     "Released_Year": int(row[1]),
                     "Runtime": int(row[2]),
                     "Genre": genres,
                     "IMDB_Rating": float(row[4]),
                     "Overview": row[5],
                     "Director": row[6],
                     "Stars": stars})
        
with open ("structured.json", "w") as f:
 json.dump({"moviedb": {"movies": data}},f, indent=4,)

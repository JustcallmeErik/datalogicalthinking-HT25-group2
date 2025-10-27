import json
import pandas as pd
import numpy as np

with open("data/output.json", "r", encoding="utf-8") as f:
    data = json.load(f) 

df = pd.json_normalize(data)

# x = type(df["Runtime"])
# print(x)

print('''
Welcome to the movie recomender!
My name is Charles and I will help you today.\n''')

y = True
while y == True:
    selection = input('''Please select an option:
        1. If you are looking for recomendations based on your preferences.
        2. If you would like a random movie recomendation.
        3. If to exit.
        \n
        ''')
    try:
        selection = int(selection);

        if selection == 1:
            genre = input('''
        Perfect! What kind of genre are you in the mood for today?
        \n
        ''')
        #     minutes = input('''
        # Exciting! How much time(minutes) do you have to watch the movie?
        # The shortest movie we have is 45 minutes and the longest 321 minutes.
        # \n
        # ''')
            
            decade = str(input('''
        Great! From which year would you like the movie to be from?
        We have movies from the 1950s to the 2020s.
        \n
        '''))
            results = df[df["Genre"].str.contains(genre, case=False, na=False)
                        #  & (int(df["Runtime"].split()[0]) <= minutes )
                         & df["Released_Year"].str.contains(decade, case=False, na=False)]
            print(results)

        if selection == 2:
            results = df.sample(n=2, replace=True)
            print('''
        I think you would enjoy: \n
        ''')
            for _, row in results.iterrows():
                print(f'''
        "{row['Series_Title']}" by {row['Director']},
        starring {row['Star1']}, {row['Star2']}, {row['Star3']}, and {row['Star4']}.
        It's from {row['Released_Year']}, belongs to the genres {row['Genre']},
        and has an IMDB rating of {row['IMDB_Rating']}.
        Here’s the overview: {row['Overview']}
            ''')
        if selection == 3:
            print("See You! \n")
            break
        y = False
    except:
        print("Wrong input, please try again.")

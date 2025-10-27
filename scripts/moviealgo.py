import json
import pandas as pd
import numpy as np

with open("data/output2.json", "r", encoding="utf-8") as f:
    data = json.load(f) 

df = pd.json_normalize(data)


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
        ''').strip().lower()
            matching_rows = []
            for i in range(len(df)):
                g_list = df.loc[i, 'Genre'] 
                g_list = [g.lower() for g in g_list] 

                if genre in g_list: 
                    matching_rows.append(df.loc[i])
            
            genre_df = pd.DataFrame(matching_rows)
            print(genre_df)

            minutes = int(input('''
        Exciting! How much time(minutes) do you have to watch the movie?
        The shortest movie we have is 45 minutes and the longest 321 minutes.
        \n
        '''))

            min_time = minutes - 10
            max_time = minutes + 10

            time_df = genre_df.loc[(genre_df['Runtime'] >= min_time) 
                                 & (genre_df['Runtime'] <= max_time) ]

            year = int(input('''
        Great! From which decade would you like the movie to be from?
        We have movies from the 1950s to the 2020s.
        \n
        '''))
            
            year_df = genre_df.loc[genre_df['Released_Year'] == year]
            
            combined = pd.merge(time_df, year_df, on=['Series_Title', 'Released_Year', 'Runtime'], how='inner').drop_duplicates(subset="Series_Title")

            if combined.empty:
                print("Sorry! No Movie is found \n")
            else:
                print('''
        I think you would enjoy: \n''')
                print(combined)
                print("\n")

        elif selection == 2:
            results = df.sample(n=2, replace=True)
            print('''
        I think you would enjoy: \n''')
            print(results)
            print("\n")

        elif selection == 3:
            print("\nSee You! \n")
            break

        else:
            print("Wrong input, Please select 1, 2, or 3")
        
    except:
        print("Wrong input, please try again.")

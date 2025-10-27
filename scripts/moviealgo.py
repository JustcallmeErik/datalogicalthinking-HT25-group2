import json
import pandas as pd
import numpy as np

with open("data/output2.json", "r", encoding="utf-8") as f:
    data = json.load(f) 

df = pd.json_normalize(data)

# print(df)

# yr = 2000

# filter = df[df['Released_Year'] == 2000]
# print(filter)

# print(type([df['Genre']]))

# filter2 = df[df['Runtime'] == 175]
# print(filter2)




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
        #     genre = input('''
        # Perfect! What kind of genre are you in the mood for today?
        # \n
        # ''').strip()
            minutes = int(input('''
        Exciting! How much time(minutes) do you have to watch the movie?
        The shortest movie we have is 45 minutes and the longest 321 minutes.
        \n
        '''))
            filtered_df = df.loc[df['Runtime'] == minutes]
            
            
            decade = int(input('''
        Great! From which year would you like the movie to be from?
        We have movies from the 1950s to the 2020s.
        \n
        '''))
            filtered_df1 = df.loc[df['Released_Year'] == decade]

            
            # combined =   pd.concat([filtered_df, filtered_df1]).drop_duplicates(subset="Series_Title")

            
            combined = pd.merge(filtered_df, filtered_df1, on=['Series_Title', 'Released_Year', 'Runtime'], how='inner').drop_duplicates(subset="Series_Title")

            if combined.empty:
                print("Sorry! No Movie is found")
            else:
                print(combined)

            # print(combined[["Runtime", "Released_Year"]])
            # print(type(filtered_df))
            # print(filtered_df)
            # print(filtered_df1)

            # print(results)

            # random_result = combine.sample(1).iloc[0]
            # print(combine)

            
        
        #     filter = df[dc]

        #     random_result = filter.sample(1).iloc[0]
        #     print(random_result)


        if selection == 2:
            results = df.sample(n=2, replace=True)
            print(results)
        #     print('''
        # I think you would enjoy: \n
        # ''')
        #     for _, row in results.iterrows():
        #         print(f'''
        # "{row['Series_Title']}" by {row['Director']},
        # starring {row['Star1']}, {row['Star2']}, {row['Star3']}, and {row['Star4']}.
        # It's from {row['Released_Year']}, belongs to the genres {row['Genre']},
        # and has an IMDB rating of {row['IMDB_Rating']}.
        # Here’s the overview: {row['Overview']}
        #     ''')
        if selection == 3:
            print("See You! \n")
            break
        y = False
    except:
        print("Wrong input, please try again.")

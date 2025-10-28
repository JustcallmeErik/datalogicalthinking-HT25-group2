import json
import pandas as pd


with open("datalogicalthinking-HT25-group2\data\output2.json", "r", encoding="utf-8") as f:
    json_data = json.load(f) 

df = pd.json_normalize(json_data)

def main():
    # taking user input
    selection = int(input('''Please select an option:
        1. If you are looking for recomendations based on your preferences.
        2. If you would like a random movie recomendation.
        3. If to exit.
        \n
        '''))
    try:
        # test user input 
        if selection == 1:
            movie_recommender() # call the function movie_recommender()
        
        elif selection == 2: 
            random_movie() # call the random_movie() function

        elif selection == 3:
            print("See You! \n")
        
        else:
            # if the user enter int value other than 1,2,3
            print("Wrong input, Please select 1, 2, or 3")
            main() # run function again
            
    except:
        # handle error
        print("Wrong input, please try again.") 
        main()      

def movie_recommender():
    # we get and store user inputs
    minutes = int(input('''
        Exciting! How much time(minutes) do you have to watch the movie?
        The shortest movie we have is 45 minutes and the longest 321 minutes.
        \n
        ''')) 
    decade = int(input('''
        Great! From which year would you like the movie to be from?
        We have movies from the 1950s to the 2020s.
        \n
        '''))
    genre = input('''
        Which genre are you looking for?
        \n
        ''').strip().lower() # we convert the input to lowercase and remove any extra space 

    get_data(genre, minutes, decade) # call get_data() function

def get_data(genre, minutes, decade):

    matching_rows = [] # define an empty list
    for i in range(len(df)):
        g_list = df.loc[i, 'Genre'] # get the Genre column for each row
        g_list = [g.lower() for g in g_list]  # convert all the values to lowercase in Genre
        if genre in g_list:  # if the given genre is in the list
            matching_rows.append(df.loc[i]) # if matched, we add the row into the empty list

        genre_df = pd.DataFrame(matching_rows) # convert list into a dataframe


    min_time = minutes - 10 # set lower limit for a runtime
    max_time = minutes + 10 # set upper limit for a runtime

    # we filter the genre_df further by time duration and assign into a new dataframe
    time_df = genre_df.loc[(genre_df['Runtime'] >= min_time) 
                                 & (genre_df['Runtime'] <= max_time) ]
    
     # we filter the time_df further by year  and assign into a new dataframe
    year_df = time_df.loc[time_df['Released_Year'] == decade]

    # if the dataframe is empty
    if year_df.empty:
        print("Sorry! No Movie is found \n")
    else:
        # print dataframe
        for _, row in year_df.iterrows():
            print("\n")
            print("I think you would enjoy " f"{row['Series_Title']} by {row['Director']} \n"
            f"Duration {row['Runtime']} \n"
            f"starring {', '.join(row['Stars'])}. \n"
            f"It's from {row['Released_Year']}, and of the genres {', '.join(row['Genre'])}, \n"
            f"and its got {row['IMDB_Rating']}, on IMDB! Here is the overview: {row['Overview']}\n")

def random_movie():
    # if the user select 2 
    results = df.sample(n=2, replace=True) # here we take random two values from dataset and it will not give the same result twice
    print(results)
    main() # call main() function

main()


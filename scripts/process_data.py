# import json

# # with open('data/cleanedData.json', 'r') as file:
# #     dataset = json.load(file)

# print('''
# Welcome to the movie recomender!
# My name is Charles and I will help you today.\n''')

# y = True
# while y == True:
#     selection = input('''Please select an option:
#         1. If you are looking for recomendations based on your preferences.
#         2. If you would like a random movie recomendation.
#         3. If to exit.
#         \n
#         ''')
#     try:
#         selection = int(selection);
#         if selection == 1:
#             genre = input('''
#         Perfect! What kind of genre are you in the mood for today?
#         \n
#         ''')
#             minutes = input('''
#         Exciting! How much time(minutes) do you have to watch the movie?
#         The shortest movie we have is 45 minutes and the longest 321 minutes.
#         \n
#         ''')
#             decade = input('''
#         Great! From which year would you like the movie to be from?
#         We have movies from the 1950s to the 2020s.
#         \n
#         ''')
#             # here we need to code to get the matching movie(s) from dataset
#             print('''
#         Thank you! Here is a''', genre, "movie", minutes, "minutes long", "from year", decade,".\n")
#             # here we print out the movie detais.
#         if selection == 2:
#             # here we need to implement code to retireve to movies
#             print('''I think you would enjoy 
#         {Series_Title} 
#         by {Director} 
#         starring {Star1, Star2, Star3, Star4}. 
#         Its from {Released_Year} 
#         and of the genre {Genre} 
#         and its got {IMDB_Rating} 
#         on IMDB! 
#         Here is the overview {Overview}.''')
#         if selection == 3:
#             print("See You! \n")
#             break
#         y = False
#     except:
#         print("Wrong input, please try again.")

year = int(2011)

startdecade = year - (year%10)
decade_end = startdecade + 9

print(startdecade)
print(decade_end)
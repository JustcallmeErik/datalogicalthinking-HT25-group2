import json

with open('data/cleanedData.json', 'r') as file:
    dataset = json.load(file)

movie_genre = input("What genre do you like watch today? ").str.lower()

movie_duration = input("How much time you wish to spare? ")
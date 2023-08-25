import json
import csv
from collections import defaultdict

def fetch_movie_info() -> None:
    '''Reads 'movie.csv' and maps the data into the format:
    movieId : [movieTitle, movieYear, movieGenre]
    '''
    info = defaultdict(list)
    
    csvFilePath = "archive/movie.csv"
    with open(csvFilePath, 'r') as file:
        csvReader = csv.reader(file)
        next(csvReader) #skip header line
        
        for row in csvReader:
            movieId = row[0]
            for char in row[1]:
                '''split string at '(' for title and year'''
    
if __name__ == "__main__":
    fetch_movie_info()
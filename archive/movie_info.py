import json
import csv
from collections import defaultdict

def fetch_movie_info() -> None:
    '''Reads 'movie.csv' and maps the data into the format:
    movieId : [movieTitle, movieYear, movieGenre]
    '''
    info = defaultdict(list)
    
    csvFilePath = "archive/movie.csv"
    with open(csvFilePath, 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file) #read as a csv file
        next(csvReader) #skip header line
        
        for row in csvReader:
            movieId = row[0]
            
            '''Separate the movie title and year from a single string'''
            movieTitleYear = row[1]
            
            try:
                for i in range(len(movieTitleYear) - 1, -1, -1): #reverse for loop
                    if(movieTitleYear[i] == "("):
                        movieTitle = movieTitleYear[:i].strip()
                        movieYear = movieTitleYear[i+1:-1].strip()
                        break
            except ValueError:
                print(f"Error splitting {movieTitleYear}")
                continue
            
            movieGenre = row[2]
            
            try:
                info[movieId].extend([movieTitle, movieYear, movieGenre])
            except KeyError:
                print(f"Unable to insert ID: {movieId} Title: {movieTitle} Year: {movieYear} into dictionary.")
                continue
            
        try:
            with open('movie_info.json', 'w') as f:
                json.dump(info, f, indent=4)
        except:
            print(f"An error occured when writing to Json file containing movie_info.")
    
if __name__ == "__main__":
    fetch_movie_info()
import json
import csv
from collections import defaultdict

def fetch_movie_ratings() -> None:
    '''Reads rating.csv and creates a hashmap that maps every unique movie id to the average
    rating of the indivudal movie.'''
    ratings = defaultdict(list)
    res = dict()

    csv_file_path = "archive/rating.csv"
    with open(csv_file_path, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        header = next(csvreader) # skips header row
        for row in csvreader:
            rate = row[2]
            try:
                movie_id = row[1]
                rate = float(rate)
                ratings[movie_id].append(rate)
            except:
                print(f"Could not convert rating to a float type. Rating is: {rate}")
    
    for i, j in ratings.items():
        # print(i,j)
        res[i] = sum(j) / len(j)
    
    try:
        j = json.dumps(res, indent=4)
        with open('movie_ratings.json', 'w') as f:
            f.write(j)
    except:
        print(f"An error occured when creating a new JSON file with writing movie ratings.")
    
def fetch_movie_names() -> None:
    '''Reads movie.csv and converts all the data into a JSON file.'''
    res = dict()

    csv_file_path = "archive/movie.csv"

    with open(csv_file_path, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        header = next(csvreader) # skips header row
        for row in csvreader:
            movie_id = row[0]
            movie_title = row[1]
            movie_genre = row[2]
            try:
                res[movie_id] = [movie_title, movie_genre]
            except:
                pass
    
        try:
            j = json.dumps(res, indent=4)
            with open('movie_title.json', 'w') as f:
                f.write(j)
        except:
            print(f"An error occured when creating a new JSON file for writing movie titles.")


if __name__ == "__main__":
    fetch_movie_names()
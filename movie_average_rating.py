import json
import csv
from collections import defaultdict

def main() -> None:
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
    
    j = json.dumps(res, indent=4)
    with open('movie_ratings.json', 'w') as f:
        f.write(j)
    
if __name__ == "__main__":
    main()
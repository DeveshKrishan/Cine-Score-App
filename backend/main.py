from flask import Flask
import pyodbc
from dotenv import dotenv_values

app = Flask(__name__)

config = dotenv_values(".env")

# Configure database connection
server = config.get('DATABASE_CONNECTION_STRING')
database = config.get('DATABASE')
username = config.get('USERNAME')
password = config.get('PASSWORD')
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

#basic route to which you can grab information
#activate virtual environment with source env/bin/activate for mac
# run with python main.py
#explain everything before starting backend to everyone
#exit virtual env with deactivate

#when installing new stuff dependencies: 
#pip freeze > requirements.txt

#https://pip.pypa.io/en/latest/user_guide/#requirements-files

# read this to learn about virtual environemnts for python
@app.route("/")
def home():
    fetched_data = run_query("SELECT * FROM Movies")
    # Convert the fetched data to a string representation
    data = '\n'.join([str(row) for row in fetched_data])
    return data

@app.route("/get-friends")
def get_friends():
    user1 = "Test"
    fetched_data = run_query(f"SELECT User2Username ,FriendshipStarted FROM Friends WHERE User1Username = {user1}")
    data = '\n'.join([str(row) for row in fetched_data])
    return data

@app.route("/get-favorite-movies")
def get_favorite_movies():
    user1 = "Test"
    fetched_data = run_query(f"SELECT f.Username, m.MovieName FROM Movies m INNER JOIN Favorites f ON m.MovieId = f.MovieId WHERE f.Username = {user1} GROUP BY m.MovieName ,f.Username")
    data = '\n'.join([str(row) for row in fetched_data])
    return data

@app.route("/get-all-reviews")
def get_all_reviews():
    user1 = "Test"
    fetched_data = run_query(f"SELECT r.Username, m.MovieName, m.MovieYear, r.Score, r.ReviewDate FROM Reviews r INNER JOIN Movies m ON r.MovieId = m.MovieId INNER JOIN [User] u ON r.Username = u.Username WHERE u.Username = {user1} GROUP BY m.MovieName, m.MovieYear, r.Score, r.ReviewDate, r.Username")
    data = '\n'.join([str(row) for row in fetched_data])
    return data

@app.route("/average-rating-movie")
def get_average_rating_for_movie():
    movie_id = "Test"
    fetched_data = run_query(f"SELECT m.MovieName, AVG(r.Score) AS 'Average Score' FROM Reviews r INNER JOIN Movies m ON m.MovieId = r.MovieId WHERE m.MovieID = {movie_id} GROUP BY m.MovieName")
    data = '\n'.join([str(row) for row in fetched_data])
    return data

@app.route("/average-rating-user")
def get_average_rating_for_user():
    username = "Test"
    fetched_data = run_query(f"SELECT u.Username, AVG(r.Score) AS 'Average Score' FROM Reviews r INNER JOIN [User] u ON r.Username = u.Username WHERE u.Username = {username} GROUP BY u.Username")
    data = '\n'.join([str(row) for row in fetched_data])
    return data

@app.route("/get-movie-info")
def get_movie_info():
    movie_id = "Test"
    fetched_data = run_query(f"SELECT m.MovieId, m.MovieName, m.MovieYear, mg.Genre FROM Movies m INNER JOIN MovieGenre mg ON m.MovieId = mg.MovieGenreId WHERE m.MovieId = {movie_id} GROUP BY m.MovieId, m.MovieName, m.MovieYear, mg.Genre")
    data = '\n'.join([str(row) for row in fetched_data])
    return data

@app.route("/check-user-exists")
def check_user_exists():
    username = "Test"
    fetched_data = run_query(f"SELECT u.Username FROM [User] u WHERE u.Username = {username}")
    data = '\n'.join([str(row) for row in fetched_data])
    return data


def run_query(query: str) -> dict:
    data = ""
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        cursor.execute(query)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

    except Exception as e:
        data = f"Error: {str(e)}"

    return data

if __name__ == '__main__':
    app.run(debug=True)

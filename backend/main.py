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
    data = ""
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = "SELECT * FROM Movies"

        cursor.execute(query)

        fetched_data = cursor.fetchall()

        cursor.close()
        conn.close()

        # Convert the fetched data to a string representation
        data = '\n'.join([str(row) for row in fetched_data])

    except Exception as e:
        data = f"Error: {str(e)}"

    return data

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
import pyodbc


app = Flask(__name__)

# Configure database connection
server = 'your_server_name.database.windows.net'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

#basic route to which you can grab information
#activate virtual environment with source env/bin/activate for mac
# run with python main.py
#explain everything before starting backend to everyone
#exit virtual env with deactivate
@app.route("/")
def home():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = "SELECT * FROM TABLE"

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)
    except:
        pass
    return "hi"

#https://pip.pypa.io/en/latest/user_guide/#requirements-files

# read this to learn about virtual environemnts for python

if __name__ == '__main__':
    app.run(debug=True)
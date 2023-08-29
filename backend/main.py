from flask import Flask

app = Flask(__name__)

#basic route to which you can grab information
#activate virtual environment with source env/bin/activate for mac
# run with python main.py
#explain everything before starting backend to everyone
#exit virtual env with deactivate
@app.route("/")
def home():
    return "hi"

#https://pip.pypa.io/en/latest/user_guide/#requirements-files

# read this to learn about virtual environemnts for python

if __name__ == '__main__':
    app.run(debug=True)
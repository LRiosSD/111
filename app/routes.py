cdc
from flask import Flask


app = Flask(__name__)


@app.route("/")
def about_me():
    me = {
        "first_name":"Leonardo",
        "last_name":"Rios",
        "hobbies": "Camping",
        "active": True
    }

    return me

    @app.route("/greet/<name>/")
    def greet_user(name):
        return "<h1>Hello, %s</h1>" % (fname, lname)


@app.route("/square/<int:num>/")
def square_num(num):
    return "<h1>%s squared is: %s</h1>" %s (num, num*num)
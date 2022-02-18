from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

year = datetime.now().year


@app.route("/")  # Route Decorator
def hello_world():
    number = random.randint(1, 100)
    return render_template("index.html", num=number, cpr=year)


@app.route("/login", methods=["post"])
def login():
    x = (request.form["file_name"])
    y = (request.form["greeting"])
    print(x, y)
    return render_template("basic.html", file_name=x, greeting=y)



if __name__ == "__main__":
    app.run(debug=True)  # FUNCTIONS LIKE NODEMON

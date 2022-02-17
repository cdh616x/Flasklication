from flask import Flask

app = Flask(__name__)  # This is the only REQUIRED input


@app.route("/<username>")  # USE THIS SYNTAX TO PARSE URL INTO VARIABLE, can parse multiple things in one url
def hello_world(username):
    return f"<h1>Hello {username}. How are ya?</h1>" \
           f"<p>Check this out</p>"


if __name__ == "__main__":
    app.run(debug=True)  # FUNCTIONS LIKE NODEMON

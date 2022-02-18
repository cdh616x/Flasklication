from flask import Flask

app = Flask(__name__)  # This is the only REQUIRED input


# def make_bold(function):
#     def wrapper_function():
#         return f"<em>{function()}</em>"
#
#     return wrapper_function()


@app.route("/<username>")  # USE THIS SYNTAX TO PARSE URL INTO VARIABLE, can parse multiple things in one url
# @make_bold
def hello_world(username):
    return f"<h1>Hello {username}. How are ya?</h1>" \
           f"<p>Check this out</p>"


if __name__ == "__main__":
    app.run(debug=True)  # FUNCTIONS LIKE NODEMON

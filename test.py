def print_goodbye(function):
    def wrapper_function():
        print("Printed before function output")
        function()
        print("Printed after function output")
    return wrapper_function


def make_bold(function):
    def wrapper_function():
        return f"<em>{function}</em>"
    return wrapper_function()


@print_goodbye
@make_bold
def say_hello():
    print("Hello")


say_hello()
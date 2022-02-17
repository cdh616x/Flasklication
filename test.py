def print_goodbye(function):
    def wrapper_function():
        print("Printed before function output")
        function()
        print("Printed after function output")
    return wrapper_function


@print_goodbye
def say_hello():
    print("Hello")


say_hello()
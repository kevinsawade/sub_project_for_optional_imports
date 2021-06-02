import getpass

def print_hello_world():
    return "Hello World"

def print_hello_user():
    return f"Hello {getpass.getuser()}"

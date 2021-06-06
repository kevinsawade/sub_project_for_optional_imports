import getpass

def print_hello_user():
    """Returns a string reading "Hello $USER!""

    Returns:
        str: A string saying "Hello $USER!"

    Examples:
        >>> greeting = print_hello_user()
        >>> print(greeting) # doctest: +SKIP
        Hello $USER!
        >>> print(type(greeting))
        <class 'str'>

    """
    return f"Hello {getpass.getuser()}!"

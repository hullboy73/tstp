def square_input():
    """ Prints and returns the square of a user entered number."""
    x = int(input("Please type a number: "))
    print(x**2)
    return(x**2)

def print_string(a_string):
    """ Prints a string passed as argument."""
    print(a_string)
    return

def params_example(x, y, z, a=2, b=3):
    """ Prints the square of first argument, the cube of second argument,
    and the sum of all three required arguments.
    Optional arguments amend the first and second exponents.
    """
    print(x**a)
    print(y**b)
    print(x+y+z)
    return

def divide_by_two(x):
    """ Returns the argument divided by 2."""
    return x / 2

def times_by_4(x):
    """ Returns the argument multiplied by 4."""
    return x * 4

def conv_str_to_float(a_string):
    """ Prints and returns a string converted to a float."""
    try:
        x = float(a_string)
        print(x)
        return x
    except ValueError:
        print("Please ensure you enter a number.")
        
# square_input()
# print_string("lazenby")
# params_example(10, 6, 13)
# y = divide_by_two(28)
# z = times_by_4(y)
# print(z)
# x = conv_str_to_float("14")


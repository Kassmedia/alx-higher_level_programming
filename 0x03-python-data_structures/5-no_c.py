#!/usr/bin/python3
def no_c(my_string):
       new_string = list(my_string)  # Create list of characters
    while "c" in new_string:
        new_string.remove("c")
    while "C" in new_string:
        new_string.remove("C")
    return "".join(new_string)

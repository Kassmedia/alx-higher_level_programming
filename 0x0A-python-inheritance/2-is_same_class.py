#!/usr/bin/python3
"""Documentation for  function that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """Function that return isintance of an object

        Returns:
        True if object is an instance, False otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False

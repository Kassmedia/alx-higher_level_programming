#!/usr/bin/python3
import json
""" Defines a function that convert string to json form"""


def to_json_string(my_obj):
    """
        Args:
            my_obj (str) to convert to json

        Return: (string) JSON rep of my_obj
    """
    return json.dumps(my_obj)

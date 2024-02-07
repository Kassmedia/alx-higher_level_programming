#!/usr/bin/python3
""" Defines a function that returns JSON representation of an object """
import json

def from_json_string(my_str):
    """
        Returns the JSON representation of an object (string)

        Args:
            my_obj (obj): The object to return JSON representation

        Return: (string) JSON representation of my_obj
    """
    return json.loads(my_str)

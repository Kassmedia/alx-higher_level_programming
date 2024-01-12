#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    check = sorted(a_dictionary.keys())
    sorted_dict = {key: a_dictionary[key] for key in check}
    return sorted_dict

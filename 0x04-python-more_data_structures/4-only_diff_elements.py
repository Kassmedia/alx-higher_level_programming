#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    check_1 = set_1.difference(set_2)
    check_2 = set_2.difference(set_1)
    return check_1.union(check_2)

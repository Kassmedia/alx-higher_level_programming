#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    load = 0
    try:
        for a in my_list[:x]:
            print("{}".format(a), end="")
            load = load + 1
    except:
        pass
    print()
    return load

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print_count = 0
        for item in range(x):
            print(my_list[item], end="")
            print_count += 1
        print()
        return(print_count)
    except IndexError:
        print()
        return(print_count)

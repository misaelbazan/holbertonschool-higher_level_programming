#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Prints a list of anything, but only prints the integers
    Return:
        Number of integers printed
    """
    nb_integers = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                nb_integers += 1
    except (ValueError, TypeError):
        return
    else:
        print()
        return(nb_integers)

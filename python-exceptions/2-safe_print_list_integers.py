#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints a list of anything, but only prints the integers
    Return:
        Number of integers printed
    """
    nb_integers = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_integers += 1
        except (ValueError, TypeError):
            continue
    print()
    return(nb_integers)

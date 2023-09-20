#!/usr/bin/python3
import sys


def main():
    # declaring a variable that contains the number of parameters given
    len_argv = len(sys.argv) - 1

    # wtd if there's 0 parametters
    if len_argv == 0:
        print("{} arguments.".format(len_argv))

    # wtd if there's 1 parameter
    elif len_argv == 1:
        print("{} argument:".format(len_argv))
        print("{}: {}".format(len_argv, sys.argv[1]))

    # wtd if there's more than 1 parameter
    elif len_argv > 1:
        print("{} arguments:".format(len_argv))
        arg_counter = 1
        for each_arg in sys.argv[1:]:
            print("{}: {}".format(arg_counter, each_arg))
            arg_counter += 1


if __name__ == "__main__":
    main()

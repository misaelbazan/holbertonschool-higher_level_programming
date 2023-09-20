#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("{} arguments.".format(len(sys.argv) - 1))
if len(sys.argv) == 2:
    print("{} argument:".format(len(sys.argv) - 1))
    print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))

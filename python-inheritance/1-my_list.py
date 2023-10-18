#!/usr/bin/python3
"""
This module contains:
    Classes: 01
        MyList: inherits from list
"""


class MyList(list):
    """
    This class inherits from type(list)
    """
    def print_sorted(self):
        """This method prints a sorted list that is inside an instance"""
        sorted_list = sorted(self)
        print(sorted_list)

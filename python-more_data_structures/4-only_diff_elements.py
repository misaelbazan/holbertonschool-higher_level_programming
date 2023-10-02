#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_union = set_1.union(set_2)
    set_intersection = set_1.intersection(set_2)
    diff_list = {x for x in set_union if x not in set_intersection}
    return(list(diff_list))

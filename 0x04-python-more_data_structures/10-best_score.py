#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary)
        values = [x for i, x in a_dictionary.items()]
        max_value = max(values)
        index = values.index(max_value)
        return keys[index]
    else:
        return None

#!/usr/bin/python3
def best_score(a_dictionary):
    score = -99999999999999999999999999999999
    better = ""
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if value > score:
                score = value
                better = key
        return better
    else:
        return None

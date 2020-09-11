#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        return max(a_dictionary.items())
        # con .items accedo a los it del dic en cualqu orden

# Another way:
# return max(a_dictionary, key=a_dictionary.get)

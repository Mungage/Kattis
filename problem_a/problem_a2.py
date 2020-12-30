# Problem description
"""Kattis has started a new hobby, postcard collection. 
# She strives to collect postcards for as many unique cities as possible every year. 
# She already has a few years’ collection. 
# Can you tell her how many unique cities these postcards come from? 

# Input: The first line of input contains a single positive integer T≤50 indicating the number of years to investigate. 
# Then follows, for each year, a line with a single positive integer n indicating the number postcards from that year. 
# The following n lines describe the city each postcard comes from. The ith such line simply contains the name of the city of the i th postcard.
# The names of the cities are normalized to make processing easier: 
# city names only contain lowercase English letters, have at least one letter, and do not contain spaces.
# The number of postcards is at most 100 and no city name contains more than 20 characters.

# Output: For each year, simply output a single line containing a single integer that is the number of distinct cities that Kattis has gathered postcards from this year. 
# """

# Required variables:
# t: int - number of years to investigate
# n: list of ints - each year's number of postcards
# formatted_list: list

# Given constraints:
# T <= 50
# n <= 100 
# City names have to be lowercase English characters with no spaces - Either as a constraint or formatted by the program
# cities > = 1 and < = 20

import sys

def main():

    # Get the standard inputs and turn them into a list of elements
    inputs = sys.stdin.read().split()

    # Format the list of inputs into a mixed list of strings and ints
    formatted_list = [format_list(n) for n in format_list(inputs)]
    
    # Set the T variable to the first index
    T = formatted_list[0]
    
    # Get a sliced list containing the postcard/cities 

    list_of_postcards = slice_list(formatted_list)

    # Check all the given constraints and assign some variables
   # print(check_constraints(formatted_list, T, list_of_postcards))

    # Print the result, which should be the number of unique postcards for each year 
    #check_unique_cities(list_of_postcards, T)

def format_list(inputs):
    try:
        return int(inputs)
    except (ValueError, TypeError):
        return inputs

def check_constraints(formatted_list, T, list_of_postcards):
    n = 0

    print(list_of_postcards)
    # Get the number n for each actual year in the list of inputs
    for postcard in formatted_list[1:]:
        if isinstance(postcard, int):

            if postcard > 0 and postcard <= 100:
                n += 1
                print(n, postcard)
            else:
                return "One of the given years broke a constraint"
    
        else:
            pass

    # Check whether the number of cities after each n is equal to the n

    # Check whether the T is equal to the number of ints n after range [1:]
    if T == n and T > 0 and T <= 50:
        pass
    else:
        return "The number of years to investigate is not equal to the number of actual years provided"
    return(True)
    
    # Given constraints:
    # T <= 50   Done
    # n <= 100  Done
    # City names have to be lowercase English characters with no spaces - Either as a constraint or formatted by the program
    # cities > = 1 and < = 20
    # the number T must be equal to the number of years     Done
    # the number n of each year must be equal to the number of strings

def get_indexes(temp_list):
    indexes = []

    for item in temp_list:
        try:
            if isinstance(item, int):
                indexes.append(temp_list.index(item))
        except ValueError:
            pass

    return indexes

def slice_list(formatted_list):
    temp_list = formatted_list.copy()
    sliced_list = [] 
    temp_list.pop(0)   # We remove the first index from the list we get
    indexes = get_indexes(temp_list)

    print(indexes)     # 0, 8

    #print(len(temp_list))

    #print(temp_list)
    i = 0
    j = 0
    
    for i in range(len(indexes)):
        new_list = []
        sliced_list.append(new_list)

    for item in temp_list[1:]:

        if isinstance(item, str):
            sliced_list[j].append(item)
        else:
            j += 1

    print(sliced_list)
        
    """
    for index, item in enumerate(temp_list):

        if isinstance(item, int):
            start = temp_list.index(item) + 1
            stop = item + start
            sliced_list.append(temp_list[start:stop])
   # print(temp_list)
   # print(sliced_list)

# om inte det inputtade nummret är samma som mängden 

    for index, item in enumerate(temp_list):
        
        if isinstance(item, int):
            startslice = temp_list.index(item) + 1
            stopslice = item + startslice
            #print(startslice, stopslice, "\n-------")
            sliced_list.append(temp_list[startslice: stopslice])
            print(sliced_list, "\n-------")

    # Return a sliced list containing as many lists as needed
    return sliced_list
    """

def check_unique_cities(sliced_list, T):
    for num in range(T):
        print(len(set(sliced_list[num])))

main()



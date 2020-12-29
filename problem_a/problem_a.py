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
# T: int - number of years to investigate
# n: list of ints - each year's number of postcards
# formatted_list: list

# Given constraints:
# T <= 50
# n <= 100 
# City names have to be lowercase English characters with no spaces - Either as a constraint or formatted by the program
# cities > = 1 and < = 20

import sys

# Define function for formatting the list of inputs to correctly become a mixed list of ints and strings
def convert_inputs(list_of_inputs):
    try:
        return int(list_of_inputs)
    except (ValueError, TypeError):
        return list_of_inputs

def get_number_of_postcards(formatted_list, n):
    for item in formatted_list[1:]:
        try:
            n.append(int(item))
        except ValueError:
            pass

def get_all_cities(formatted_list, list_of_cities):
    for item in formatted_list:
        try:
            if isinstance(item, str):
                list_of_cities.append(item)
        except ValueError:
            pass
                
# Define function for checking the given constraints
def check_constraints(formatted_list, t, n):
    # Check whether the number of years to investigate is less than 50
    if t <= 0 or t >= 50:
        return False

    # Check whether the numbers in the postcards are less than 100
    for num in n:
        if num <= 0 or num >= 100:
            return False

    # check whether the cities in the list follow english characters, are lowercase and contain no spaces
    for line in formatted_list:
        if isinstance(line, str):
            for char in line:
                if not char.islower() or not char.isalpha():
                    return False                
    return True

def get_indexes(formatted_list):   
    list_of_indexes = []
    # For every item in the list
    for item in formatted_list[1:]:
        if isinstance(item, int):
            list_of_indexes.append(formatted_list.index(item))
    return list_of_indexes

def check_unique_cities(n, list_of_cities):
    temp_list = []

    try:
        for item in range(n[0]):    # här loopar den 7 eller 3 gånger
            temp_list.append(list_of_cities[0]) # den tar första indexen från list_of_cities och lägger i en temporär lista.
            list_of_cities.pop(0) 
        n.pop(0)
    except:
        pass

    return temp_list

# Create the required variables with the previously defined helper function
list_of_inputs = sys.stdin.read().rsplit()
formatted_list = [convert_inputs(number) for number in convert_inputs(list_of_inputs)]
t = formatted_list[0]
n = []
list_of_cities = []

get_number_of_postcards(formatted_list, n)
get_all_cities(formatted_list, list_of_cities)

if check_constraints(formatted_list, t, n):

    for x in range(len(n)):
        list_of_cities.append(check_unique_cities(n, list_of_cities))

    print(list_of_cities)

else:
    print("Something went wrong, perhaps one of the given constraints were broken")



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

# Given constraints:
# 0 < T <= 50       
# 0 < n <= 100      
# City names have to be lowercase English characters with no spaces
# City names must shorter than 20 characters
# The number T must be equal to the number of years
# The number n must be equal to the number of actual postcards

import sys

def main():

    # Get the standard inputs and turn them into a list of elements
    inputs = sys.stdin.read().split()

    # Format the list of inputs into a mixed list of strings and ints
    formatted_list = [format_list(n) for n in format_list(inputs)]
    
    # Set the T variable to the first index, and n equal to the number of ints after the first index
    T = formatted_list[0]
    n = []
    get_number_of_postcards(formatted_list, n)
    
    # Get a sliced list containing the actual postcard/cities 
    list_of_postcards = slice_list(formatted_list, n)

    # Check all the given constraints
    if check_constraints(formatted_list, T, n, list_of_postcards):
        # Finally, print our final results
        check_unique_cities(list_of_postcards, T)
    else:
        print("One or more of the constraints were broken")

# Helper function to turn our inputs into a mixed list of ints and strings
def format_list(inputs):
    try:
        return int(inputs)
    except (ValueError, TypeError):
        return inputs

# Helper function to get the ints specifying the number of postcards
def get_number_of_postcards(formatted_list, n):
    for item in formatted_list[1:]:
        try:
            n.append(int(item))
        except ValueError:
            pass

# Function to slice our formatted list of inputs
def slice_list(formatted_list, n):
    temp_list = formatted_list.copy()
    sliced_list = [] 
    temp_list.pop(0)   # We remove the first index from the list we get for easier handling

    j = 0
    for i in range(len(n)):
        new_list = []
        sliced_list.append(new_list)

    for item in temp_list[1:]:
        if isinstance(item, str):
            sliced_list[j].append(item)
        else:
            j += 1
    return(sliced_list)

def check_constraints(formatted_list, T, n, list_of_postcards):

    # Check whether the years to investigate variable is within the given constraints 
    if not T == len(n) and T > 0 and T <= 50:
        return False

    # Check constraints for n, and if n is equal to the actual number of postcards
    i = 0
    for n in n:
        if not n == len(list_of_postcards[i]) or n <= 0 or n >= 100:          
            return False
        else:
            i += 1

    # Check whether the city names are all lowercase and of the english alphabet.
    for line in list_of_postcards:
        for city in line:
            if not city.islower() or not city.isalpha() or not len(city) <= 20:
                return False        
    return True   

def check_unique_cities(sliced_list, T):
    for num in range(T):
        print(len(set(sliced_list[num])))

main()
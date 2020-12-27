"""We’re not going to sugar-coat it: Chicago’s winters can be rough. 
The temperatures sometimes dip to uncomfortable levels and, after last year’s “polar vortex”, 
the University of Chicago Weather Service wants to find out exactly how bad the winter was. 
More specifically, they are interested in knowing the total number of days in which the temperature was below zero degrees Celsius.

Input: The input is composed of two lines. 
The first line contains a single positive integer n (1≤n≤100) that specifies the number of temperatures collected by the University of Chicago Weather Service. 
The second line contains n temperatures, each separated by a single space. Each temperature is represented by an integer t (−1000000≤t≤1000000) 

Output: You must print a single integer: the number of temperatures strictly less than zero."""

import sys

# Define a function to determine the number of negative temperatures in the list, disregarding index 0
def determine_negative_temps(temp_list: list) -> int:
    number_of_temperatures = 0

    for num in temp_list[1:]:
        # Check whether the temperatures are within the given constraints
        if num <= -1000000 or num >= 1000000:
            # If not, return None
            return None
        # Check if the temperatures are below zero, in which case add one to the number_of_temperatures
        elif num < 0:
            number_of_temperatures += 1
            
    return number_of_temperatures

# Define the list holding the temperatures
temp_list = []
# Get inputs from stdin and convert them into a list of ints
temp_list = [int(item) for item in sys.stdin.read().split()]
# Use the created function to give us the number of temperatures below 0 degrees
number_of_temps = determine_negative_temps(temp_list)

# Check whether the function returned a valid number or not and print the result
if number_of_temps is None:
    print("The temperatures were not within the given constraints")
else:
    print(number_of_temps)

"""
In electrical engineering, a resistive touchscreen is a touch-sensitive computer display composed of two flexible sheets coated with a resistive material and separated by an air gap.
Inside such a screen, there are two conductive layer, split into rows and columns. When contact is made with the surface of the touchscreen, the two sheets are pressed together. This conducts electricity between the layers, and by measuring which columns and rows are connected a measurement can be made of which area of the screen was touched, with a resolution limited by the width of the conducting columns and rows.
Unfortunately, when multiple areas are pressed at the same time, it may not be possible to uniquely identify which area was touched. After all, you only know for each column if it was touched or not, not exactly where along the row or column the touch was made.
Kattis trying to develop some software for a new mobile phone and needs some help with the calculations in the microcontroller. The microcontroller will probe the screen, and store the information in an r×c
grid of 0 and 1 values. The value stored in row i and column j of this grid is 1 if at least one area in row i was touched and at least one (possibly different) area in column j
was touched. Otherwise, the value that is stored at this position is 0.

Can you write the software to interpret the result, check for errors and provide as much information as possible from the microcontroller?

input:
Input starts with a single positive integer T≤200 indicating the number of test cases, followed by a new line. Each test case then starts with two integers r and c where 1≤r≤10 and 1≤c≤10. This indicates that the display is an r×c
grid. Then follows another new line. After this follows r lines, describing the state of the display. The ith row contains a string of c consecutive 0 and 1 characters, follwed by a new line. Note that there are no separating spaces.

output:
For each test case, output the following information. If there is no combination of touches on the keypad that would produce this 0/1 grid then output a single line containing the word impossible. Otherwise, output r lines, each containing a string of length c. This should describe a grid where the character at row i and column j
is: 
    N if no touch combination that produces the input grid has the jth area on row i being touched.

    P if all touch combinations that produce the input grid have the jth area on row i being touched.

    I if some, but not all, touch combinations that produce the input grid have the jth area on row i being touched.

Finally, the last line of each test case should be followed by the string ---------- (10 dashes).
"""

# Given constraints
# T <= 200
# T == number of test cases
# Number of test cases 
# Each test case has two integers r and c
# 1 <= r <= 10
# 1 <= c <= 10

import sys

# Get inputs

def main():
    # Take inputs from stdin and format them into a list of ints
    inputs = sys.stdin.read().split() 

    # set T to first index of inputs specifying the number of test cases
    T = int(inputs[0])

    # Split inputs into lists according to T number of test cases
    test_cases = slice_list(T, inputs)

    #print(test_cases)

    # Now that we've got lists of ['4', '3', '110', '000', '110', '000'], ['2', '3', '101', '000'], ['2', '2', '10', '01']
    # We want to split these into 3 2d tuples  

    # 2d array should contain n rows taking first string of next 4 inputs in every list

    # We want to get a 2d_list signifying a grid.
    # The grid should contain r rows, and c numbers 

    # which means the 2d_list for each test case would look like this: [[1, 0, 0], [0, 0, 0], [1, 1, 0], [0, 0, 0]]
    # We get this list by going through each index, i.e. each list in our sliced_list:
    # First index in each t in sliced_list will mean we want to create r lists.
    # We then go through every element after the second index[1:] and split these strings up.

    # So essentially we create t[0] lists for every list in sliced_list

        #for r in range(int(test_case[0])):     # För varje rad i test_caset
        #    grid.append(test_case[2:])
            # ta alla slices från 2: och lägg i en lista
       


        # for n rows
        # split the strings 3 times
        # this will become one list.
    #except:
        #print("Something went wrong")

def format_list(inputs):
    try:
        return int(inputs)
    except (ValueError, TypeError):
        return inputs

def slice_list(T, inputs):
    temp_list = inputs
    sliced_list = []
    test_cases = [] 

    # Remove first index as we don't need it anymore
    try:
        temp_list.pop(0)    
        # We want to slice the temp_list T times and create T amount of separate lists containing the given inputs
        for t in range(T):                           
            n = int(temp_list[0]) + 2                                    
                                                                    
            sliced_list.append(temp_list[0:n])
            del temp_list[0:n]

        for test_case in sliced_list:
            grid = []

            #print(test_case)
            # Creating the 2d grid for each testcase
            for r in test_case[2:]:      # för varje sträng i test case range 2:
                res = []
                res[:] = r
                grid.append(res)
            
            test_cases.append(grid)
            
            print("end of test case")

        print(test_cases)

        return test_cases

    except IndexError:
        print("Error caught when slicing lists")
        
class test_case:
    def __init__(self):
        pass
        


    def define_grid(self, sliced_list):
        pass


main()




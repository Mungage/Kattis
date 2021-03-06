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

def main():
    # Take inputs from stdin and format them into a list of ints
    inputs = sys.stdin.read().split() 

    # set T to first index of inputs specifying the number of test cases
    T = int(inputs[0])

    # split our inputs into a 3dlist of testcases and their respective grids
    test_cases = slice_list(T, inputs)

    # Finally  
    control_grid(test_cases)

def convert_list(inputs):
    try:
        return int(inputs)
    except (ValueError, TypeError):
        return inputs

def slice_list(T, inputs):
    temp_list = inputs
    sliced_list = []
    test_cases = [] 

    try:
        temp_list.pop(0)    
        # We want to slice the temp_list T times and create T amount of separate lists containing the provided inputs
        for t in range(T):                           
            n = int(temp_list[0]) + 2                                    
                                                                    
            sliced_list.append(temp_list[0:n])
            del temp_list[0:n]

        for test_case in sliced_list:
            grid = []

            # Creating the 2d grid for each testcase
            for r in test_case[2:]:  
                res = []
                res[:] = r
                # converting the grid into ints
                res = [convert_list(n) for n in convert_list(res)]
                grid.append(res)
                
            test_cases.append(grid)

        return test_cases
    except IndexError:
        print("Error caught when slicing lists")

def control_grid(test_cases):
    # When we print a test case we get its grid
    # A grid looks like this: [1,1,0], [0,0,0], [1,1,0], [0,0,0]
    
    # For each row in the grid we want to check three things
    # If a position in the grid is i, n, or p

    # To do this we need to check each combination of row and column.
    
    # for each index[j] in a row.
    # Check whether there is another "1" in the same column

    # if index[j] of row i is 1, and if index [j] of every other row in test case are 1, then print index[0] of row 1 as an I. 
    # else if index[1:] contain any 1, print index[j] as a p
    # if index[0] of row 1 is ]

    # if i1, j1 == 1 and i3, j1 == 1, print I
    # elif i1, j1 == 1 and i1, j4 == 1, print p
    # else print N

    for test_case in test_cases:
        print(test_case)

        for i in range(len(test_case)):
            print(i)

main()

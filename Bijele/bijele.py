# The problem can be found at: https://open.kattis.com/problems/bijele

import sys

# Define function to check for the given constraints
def checkconstraints(current_pieces):
    result = all(ele >= 0 and ele <= 10 for ele in current_pieces)
    return result
     
# Set a list of the required pieces to check against
required_pieces = [1, 1, 2, 2, 2, 8]
# Get the standard inputs and turn them into a list of ints
current_pieces = [int(item) for item in sys.stdin.read().split()]
# Check if any of the inputs break the constraints
if checkconstraints(current_pieces):
    i = 0
    # For each piece print the result of that piece minus the number of pieces that Mirko has.
    for piece in required_pieces:
        print(piece - current_pieces[i])
        i += 1
else:
    print("inputs did not adhere to the given constraints")


# The problem can be found here: https://open.kattis.com/problems/tarifa

import sys

# Define a function to check whether the inputs are within the given constraints
def checkconstraints(x, n, p):
    if (1 <= x <= 100) and (1 <= n <= 100) and all(0 <= ele and ele <= 10000 for ele in p):
        return True
    else:
        return False
    
# Get the inputs and split them up into their respective variables
inputs = [int(item) for item in sys.stdin.read().split()]
x = inputs[0]   # Amount of megabytes each month
n = inputs[1]   # The number of months
p = inputs[2:]  # How many megabytes pero has used each month

# Set i = 0 and result = 10 (at the start of every month Pero beings with x amount of megabytes + the previous one)
i = 0
result = x

# Use the checkconstraints function we defined earlier
if checkconstraints(x, n, p):
    for month in range(n):
        result += (x - p[i])
        i += 1
    print(result)
else:
    print("The inputs did not comply with the given constraints")









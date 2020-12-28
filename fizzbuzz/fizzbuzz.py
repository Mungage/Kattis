"""
According to Wikipedia, FizzBuzz is a group word game for children to teach them about division. 
This may or may not be true, but this question is generally used to torture screen young computer science graduates during programming interviews.
Basically, this is how it works: you print the integers from 1 to N,
replacing any of them divisible by X with Fizz or, if they are divisible by Y, with Buzz.
If the number is divisible by both X and Y , you print FizzBuzz instead. Check the samples for further clarification.

Input contains a single test case. Each test case contains three integers on a single line, X
, Y and N (1≤X<Y≤N≤100).

Print integers from 1
to N in order, each on its own line, replacing the ones divisible by X with Fizz, 
the ones divisible by Y with Buzz and ones divisible by both X and Y with FizzBuzz.
"""

import sys

# Define function to check whether the given constraints are adhered to.
def checkconstraints(x, y, N) -> bool:
    if 0 <= x <= 100 and 0 <= y <= 100 and 0 <= N <= 100:
        return True
    else:
        return False

# Get inputs as a list of ints, then turn them into the required variables x, y and N
fizzbuzzlist = [int(item) for item in sys.stdin.read().split()]
x = fizzbuzzlist[0]
y = fizzbuzzlist[1]
N = fizzbuzzlist[2]

# Us the checkconstraints function, which continues if all the variables adhere to the constraints 0 <= x, y, N <= 100
if checkconstraints(x, y, N):
    # For r in range(1, N+1), because otherwise we'll do modulus on 6 instead of last number 7, which is undefined,
    # check if r is divisible by fizz and buzz respectively.
    for r in range(1, N+1):
        if r % x == 0 and r % y == 0:
            print("FizzBuzz")
        elif r % x == 0:
            print("Fizz")
        elif r % y == 0:
            print("Buzz")
        else:
            print(r)
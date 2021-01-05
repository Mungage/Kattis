# Description of the problem can be found here: https://open.kattis.com/problems/hissingmicrophone

# Problem is to find double occurances of s and printing hiss or no hiss dependingly
# This can be solved using either regular expression, collections.Counter class or your own methods

import sys
import timeit

for line in sys.stdin:
    inputs = line.split()

string = inputs[0]

if len(inputs) == 1 and string.count("ss") >= 1 and len(string) >= 1 and len(string) <= 30 and string.islower() == True:
    print("hiss")
elif len(inputs) == 1 and string.count("ss") == 0 and len(string) >= 1 and len(string) <= 30 and string.islower() == True:
    print("no hiss")
else:
    print("Constraints were broken")


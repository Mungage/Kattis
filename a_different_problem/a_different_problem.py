# Read the problem description here: https://open.kattis.com/problems/different

import sys
list_of_pairs = []
# Get standard inputs

for line in sys.stdin:
    list_of_pairs.append(line.split())

# Take the pair of ints in the list of inputs and subtract the lower number from the larger one, then print the results
for pair in list_of_pairs:
    x = int(pair[0])
    y = int(pair[1])
    print(max(x, y) - min(x, y))
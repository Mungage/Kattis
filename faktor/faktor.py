# Problem description can be found here: https://open.kattis.com/problems/faktor

import sys

# Take standard inputs
for line in sys.stdin:
    inputs = line.split()

articles = int(inputs[0])
impact_factor = int(inputs[1])

if articles >= 1 and articles <= 100 and impact_factor >= 1 and impact_factor <= 100:
    # Calculation
    bribed_authors = (articles * impact_factor) - articles + 1
    print(bribed_authors)
else:
    print("Input constraints were broken")
import sys
# Get standard input
for string in sys.stdin:
    dices = string.split()  # split dices into two ints
    N = int(dices[0])
    M = int(dices[1])

    if 4 <= N & N <= 20 and 4 <= M & M <= 20:

        target = (2+M+N)/2 # The most probably number in the middle.
        



#Count up to the provided number, starting at 1, saying "Abracadabra" each time
#Constraints 1 <= N <= 100

#Get standard input N as int
#Check constraints
#For range in N
#Print N + Abracadabra

import sys

for x in sys.stdin:
    N = int(x)
    if 1 <= N & N <= 100:
        for x in range(N):
            print(x + 1, "Abracadabra")
        




    
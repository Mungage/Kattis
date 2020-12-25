import sys

carrotlist = []

for line in sys.stdin:
    carrotlist.append(line.rstrip())

x = carrotlist[0].split()
carrots = int(x[1])
print(carrots)
    



    


   




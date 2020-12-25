#The number S is called the mean of two numbers R1 and R2 if S is equal to (R1+R2)/2. 
#Mirko’s birthday present for Slavko was two integers R1 and R2. 
#Slavko promptly calculated their mean which also happened to be an integer but then lost R2! Help Slavko restore R2.

#The first and only line of input contains two integers R1 and S, both between −1000 and 1000.

#Output R2 on a single line.

# s = (r1+r2)/2
# r2 = s*2-r1 

import sys

#get standard input
for line in sys.stdin:
    #turn inputs into ints
    inputs = line.split()
    r1 = int(inputs[0])  # r1
    s = int(inputs[1])  # mean
    #check constraints -1000 : 1000
    if -1000 <= r1 & r1 <= 1000 and -1000 <= s & s <= 1000:
        #Calculate and print r2
        r2 = ((s*2)-r1)
        print(r2)



    



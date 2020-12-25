import sys

#Take two ints from stdin
for string in sys.stdin:
    answers = string.split()
    #reverse the two numbers
    a = int(str(answers[0][::-1]))
    b = int(str(answers[1][::-1]))    

#compare and print which one is the largest
print(max(a, b))












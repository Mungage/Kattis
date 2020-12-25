import sys

#Take input from stdin
for string in sys.stdin:

    #Check if input string contains any zeroes
    if "0" in string:
        print("Sorry, the inputs contained a zero")
    else:
        #Turn input into two separate string variables
        answers = string.split()
        #Reverse the two foremost strings and turn them into ints
        a = int(str(answers[0][::-1]))
        b = int(str(answers[1][::-1]))
        #Check to see if the two numbers are equal to one another
        if a != b:
            #Compare the two ints and print the larger one
            print(max(a, b))
        else:
            print("Sorry, the inputs cannot be equal")
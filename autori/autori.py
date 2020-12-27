"""
Great scientific discoveries are often named by the last names of scientists that made them. For example, the most popular asymmetric cryptography system, 
RSA was discovered by Rivest, Shamir and Adleman. Another notable example is the Knuth-Morris-Pratt algorithm, named by Knuth, Morris and Pratt.
Scientific papers reference earlier works a lot and it’s not uncommon for one document to use two different naming conventions: 
the short variation (e.g. KMP) using only the first letters of authors last names and the long variation (e.g. Knuth-Morris-Pratt) using complete last names separated by hyphens.
We find mixing two conventions in one paper to be aesthetically unpleasing and would like you to write a program that will transform long variations into short. 

Input: The first and only line of input will contain at most 100 characters, uppercase and lowercase letters of the English alphabet and hyphen (‘-’ ASCII 45). 
The first character will always be an uppercase letter. 
Hyphens will always be followed by an uppercase letter. 
All other characters will be lowercase letters.

Output: The first and only line of output should contain the appropriate short variation.
"""

import sys

# Get standard input
for line in sys.stdin:
    # Turn and format the lines into a list containing each name as separated by the hyphens.
    names = line.rstrip('\n').split('-')
    abbreviation = ""

# Take every name in list and check whether they follow the given constraints
for x in names:
    # If constraints are not broken, add the first uppercase letter to a string
    if x[0].isupper() and x[1:] == "":
        abbreviation += x[0]
    elif x[0].isupper() and x[1:].islower():
        abbreviation += x[0]
    # If constraints were broken, break the loop and set abbreviation to None
    else:
        abbreviation = None
        break

# If abbreviation is none, print an error, otherwise print the correct result
if abbreviation == None:
    print("Constraints were broken")
else:
    print(abbreviation)

        

    
        
            
    
            
    
    

            








#Print a string containing an uppercase abbreviation of the first letters after each hyphen from the input.


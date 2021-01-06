#Read the problem description here: https://open.kattis.com/problems/spavanac
# The problem is the 24 hour notation, how can I go back 45 minutes from 00:00 to 23:15
# By using datetime is probably the easiest, for example timedelta.

import sys
from datetime import timedelta

def main():
    # Take inputs from standard inputs
    for line in sys.stdin:
        inputs = line.split()

    # Check for the inputs constraint
    if len(inputs) == 2:  
        # Prepare the inputs variables
        hours = int(inputs[0])
        minutes = int(inputs[1])

        # Call the function to calculate and print the correct output using timedelta
        calculate_time(hours, minutes)
    else:
        print("The input sample broke the constraints")

def calculate_time(hours, minutes):
    # Create a new timedelta object which has been subtracted by 45 minutes
    new_time = timedelta(hours=hours, minutes=minutes) - timedelta(minutes=45)

    # Using timedelta we calculate backwards from the "seconds" attribute contained within the object.
    # In practice, this is how it is calculated. We have 33900 seconds in our timedelta object, in order to get the hours we need to
    # divide these 33900 seconds by 3600 (amount of seconds in one hour), we use floor division in order to ignore the remainder and just give us the largest number denoting the hour.
    # Once we have the hour we need to get the minutes, which can be done by taking the 33900 seconds, turning them into 565 minutes (the total number of minutes),
    # then we can use modulo %60 to get the correct number of minutes.
    seconds = new_time.seconds  
    hours = seconds//3600       
    minutes = (seconds//60)%60  

    print(hours, minutes)

# Execute the main function
main()






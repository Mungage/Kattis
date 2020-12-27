"""A common problem in mathematics is to determine which quadrant a given point lies in. There
    are four quadrants, numbered from $1$ to $4$, as shown in the diagram below:
 
    For example, the point $A$, which is at coordinates $(12, 5)$ 
    lies in quadrant $1$ since both its $x$ and $y$ values are positive, 
    and point $B$ lies in quadrant 2 since its $x$ value is negative and its $y$ value is positive.

    Your job is to take a point and determine the quadrant it is in. 
    You can assume that neither of the two coordinates will be $0$.
    """
 # Input:The first line of input contains the integer $x$ ($-1000 \le x \le 1000; x \not= 0$). 
 # The second line of input contains the integer $y$ ($-1000 \le y \le 1000; y \not= 0$).

 # Output: Output the quadrant number ($1$, $2$, $3$ or $4$) for the point $(x, y)$.
 # Import stdin

import sys

coordinates = []
# get standard input as two coordinates => list
for line in sys.stdin:
    coordinates.append(int(line.strip()))

# Check to see if any of the coordinates are equal to 0, else check and print which quadrant.
if 0 in coordinates:
    print("The inputted coordinates cannot be equal to 0")
elif coordinates[0] > 0 and coordinates[1] > 0:
    print("1")
elif coordinates[0] < 0 and coordinates[1] > 0:
    print("2")
elif coordinates[0] < 0 and coordinates[1] < 0:
    print("3")
elif coordinates[0] > 0 and coordinates[1] < 0:
    print("4")
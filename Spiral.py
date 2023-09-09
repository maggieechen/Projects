#  File: Spiral.py

#  Description: This program creates a square spiral based upon the size from the input file.
#  It takes numbers from the input file and outputs the sum of all the numbers adjacent to this number, but not including this number.

#  Student Name: Maggie Chen

#  Student UT EID: mc74329

#  Course Name: CS 313E

#  Unique Number: 52020

#  Date Created: January 17th, 2023

#  Date Last Modified: January 21, 2023

# Input: n is an odd integer between 1 and 100
#  File: Spiral.py

#  Description: This program creates a square spiral based upon the size from the input file.
#  It takes numbers from the input file and outputs the sum of all the numbers adjacent to this number, but not including this number.

#  Student Name: Maggie Chen

#  Student UT EID: mc74329

#  Course Name: CS 313E

#  Unique Number: 52020

#  Date Created: January 17th, 2023

#  Date Last Modified: January 21, 2023

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral(n):
    if n % 2 == 0:
        n = n + 1
    top_row = 0
    left_column = 0
    bottom_row = n-1
    right_column = n-1
    arr = [[1 for i in range(n)] for j in range(n)]
    number = n * n
    direction = 'left'
    row = 0
    column = n-1
    while number > 1:
            if direction == 'left':
                while column > left_column:
                    arr[row][column] = number
                    column = column - 1
                    number = number - 1
                direction = 'down'
                if top_row < n:
                    top_row = top_row + 1
                
            elif direction == 'down':
                while row < bottom_row:
                    arr[row][column] = number
                    row = row + 1
                    number = number - 1
                direction = 'right'
                if left_column < n:
                    left_column = left_column + 1
            
            elif direction == 'right':
                while column < right_column:
                    arr[row][column] = number
                    column = column + 1
                    number = number - 1
                direction = 'up'
                if bottom_row > 0:
                    bottom_row = bottom_row - 1
                
            else:
                while row > top_row:
                    arr[row][column] = number
                    row = row - 1
                    number = number - 1
                direction = 'left'
                if right_column > 0:
                    right_column = right_column - 1
 
    return arr
        

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

def sum_adjacent_numbers(spiral, n):
    #find number
    length = len(spiral[0])
    r = 0
    c = 0
    found = False
    #use for loop
    for r in range(length):
        for c in range(length):
            if int(spiral[r][c]) == int(n):
                found = True
                break
        if found:
            break
    #add numbers around it
    sum = 0
    if found:
        for i in range(max(0,r - 1),min(r + 2,length)):
            for j in range(max(0,c - 1),min(c + 2,length)):
                sum += spiral[i][j]
        sum = sum - int(n)
    
    return sum

def main():
    # read the input file
    lines = sys.stdin.readlines()
    dimension = int(lines[0])
    # create the spiral
    s = create_spiral(dimension)
    # add the adjacent numbers
    for k in range(1,len(lines)):
        output = sum_adjacent_numbers(s,lines[k])
        # print the result
        print(output)
            
if __name__ == "__main__":
    main()

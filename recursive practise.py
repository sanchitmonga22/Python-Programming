"""
file: double_add_5.py
language: python3
author: sm3468@rit.edu Sanchit Monga 
description: cs1 Integer Sequences
"""
import math

"""
This function computes and prints the value of the expression double add 5 of a series of the number using recursion technique
start: a local variable that stores the value of starting point
count: a local variable that has the count of the numbers to be printed of the series
the base case is when the count is either less than or equal to 0, which prints the last number in the series
"""
def print_sequence_rec(start,count):
    if count<=0:
        print(start)
    else:
        print(start)
        return(print_sequence_rec(start*2+5,count-1))
    
"""
This function computes and prints the value of the expression double add 5 of a series of the number using the iterations
start: a local variable that stores the value of starting point
count: a local variable that has the count of the numbers to be printed of the series
the function uses a while loop with the condition that count is greater than or equal to 0, it will run till the condition is true
"""
def print_sequence_iter(start,count):
    while count>=0:
        print(start)
        start=start*2+5
        count=count-1

"""
This function returns the value of the last number of the series of expression double add 5 using recursive technique
start: a local variable that stores the value of starting point
count: a local variable that has the count of the numbers and also represents the last number in the series
the base case is when the count is equal to 0, which returns the last number in the series
"""
def find_end_rec(start, count):
    if count==0:
        return(start)
    else:
        return(find_end_rec(start*2+5,count-1))

"""
This function returns the value of the last number of the series of expression double add 5 using the loops
start: a local variable that stores the value of starting point
count: a local variable that has the count of the numbers and also represents the last number in the series
This function uses while loop which has a condition that count is not equal to 0, and executes the code till the condition becomes false
"""        
def find_end_iter(start,count):
    while count!=0:
        start=start*2+5
        count=count-1
    if(count==0):
        return(start)
    
"""
The function invokes the find_end_iter function to calculate the start value that meets the requirements to solve a problem
start: a local variable that stores the value of starting point
count: a local variable that has the count of the numbers and also represents the last number in the series
j: it is a local variable which stores the final answer
"""        
def find_start_iter(goal,count):
    j=0
    while find_end_iter(j,count)<goal:
        j=j+1
    print(j)

"""
This is a helper function and invokes the find_end_rec and calculates the start value to solve the problem
start: a local variable that stores the value of starting point
count: a local variable that has the count of the numbers and also represents the last number in the series
j: it is a local variable which stores the final answer
"""
def find_start(goal,count,j):
    if(find_end_rec(j,count)>=goal):
        return j
    else:
        return find_start(goal,count,j+1)

"""
The function invokes the find_start function to solve a problem using recursive technique
start: a local variable that stores the value of starting point
count: a local variable that has the count of the numbers and also represents the last number in the series
"""
def find_start_rec(goal, count):
    print(find_start(goal,count,0))

print_sequence_rec(0,-1)
print_sequence_rec(0,0)
print_sequence_rec(1,2)
print_sequence_iter(2,5)
print_sequence_rec(1,0)
print_sequence_iter(1,1)
print_sequence_iter(3,19)
find_end_rec(100,3)
find_end_iter(100,3)
find_end_iter(1,10)
find_end_rec(2,40)
find_end_rec(1,1001)
find_end_iter(1,1001)
find_start_rec(7,3)
find_start_iter(8,3)
find_start_rec(9,2)
find_start_iter(100,1)
find_start_rec(100,3)










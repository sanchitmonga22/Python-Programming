import turtle as tt
import math
"""
author:Sanchit Monga
filename:cross.py
language:pyhton
Practical Exam
"""
"""
In the pre and post condition the turtle is at the centre facing north 
This function draws the single course by taking the input of the length of the single cross
"""
def cross1(length):
    tt.forward(length)
    tt.up()
    tt.back(length)
    tt.down()
    tt.back(length)
    tt.forward(length)
    tt.right(90)
    tt.forward(length)
    tt.up()
    tt.back(length)
    tt.down()
    tt.back(length)
    tt.forward(length)
    tt.left(90)
"""
In the pre and post condition the turtle is at the centre facing north 
This function draws the crosses with depth 2 by taking length as the input
"""
def cross2(length):
    cross1(length)
    tt.up()
    tt.right(45)
    tt.forward(length)
    tt.down()
    cross1(length/2)
    tt.up()
    tt.back(length)
    tt.left(90)
    tt.forward(length)
    tt.down()
    cross1(length/2)
    tt.up()
    tt.back(length)
    tt.right(45)
    tt.down()
"""
In the pre and post condition the turtle is at the centre facing north 
This function draws the crosses with depth 3 and takes the length as the input
"""
def cross3(length):
    cross2(length)
    tt.right(45)
    tt.up()
    tt.forward(length)
    tt.right(45)
    tt.forward(length/2)
    tt.down()
    cross1(length/4)
    tt.up()
    tt.back(length/2)
    tt.left(90)
    tt.forward(length/2)
    tt.down()
    cross1(length/4)
    tt.up()
    tt.back(length/2)
    tt.right(45)
    tt.back(length)
    tt.left(45)
    tt.left(45)
    tt.forward(length)
    tt.left(45)
    tt.forward(length/2)
    tt.down()
    cross1(length/4)
    tt.up()
    tt.back(length/2)
    tt.right(90)
    tt.forward(length/2)
    tt.down()
    cross1(length/4)
    tt.up()
    tt.back(length/2)
    tt.left(45)
    tt.back(length)
    tt.right(45)
"""
In the pre and post condition the turtle is at the centre facing north 
This function takes the depth as the input and draws the crosses recursively
"""
def crosses(length,depth):
    if(length<=0 or depth==0):# assuming that the depth will always be >=0
        pass
    elif(length>0 and depth>0):
        cross1(length)
        tt.up()
        tt.right(45)
        tt.forward(length)
        tt.down()
        crosses(length/2,depth-1)
        tt.up()
        tt.back(length)
        tt.left(90)
        tt.forward(length)
        tt.down()
        crosses(length/2,depth-1)
        tt.up()
        tt.back(length)
        tt.right(45)
        tt.down()

"""
This function takes the user input and calls the crosses function
"""  
def main():
    d=int(input("Enter the depth of the crosses: "))
    tt.left(90)
    crosses(100,d)
    tt.done()
    
main()

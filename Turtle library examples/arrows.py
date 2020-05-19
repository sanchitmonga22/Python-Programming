import math
import turtle
import random
"""
This program draws arrows randomly in a box.
Author: Sanchit Monga
language: python
"""
"""
declaring global variables that will be used throughout the program
"""
MAX_SIZE=30
MAX_DISTANCE=30
MAX_ANGLE=30
BOUNDING_BOX=100
MAX_FIGURES=500

"""
This function calculates and returns the value of area of an equilateral triangle.
"""
def area_of_triangle(length):
    area=(math.sqrt(3)*length**2)/4
    return(area)

"""
This function checks whether the turtle draws arrows in the designated area or not and moves the turtle by 180 degrees if the turtle tries to go out of the box
"""
def boundary_check():
    if(turtle.xcor()+MAX_SIZE>BOUNDING_BOX):
        turtle.setheading(180)
    elif(turtle.ycor()+MAX_SIZE>BOUNDING_BOX):
        turtle.setheading(270)
    elif(turtle.xcor()-MAX_SIZE<-BOUNDING_BOX):
        turtle.setheading(0)
    elif(turtle.ycor()-MAX_SIZE<-BOUNDING_BOX):
        turtle.setheading(90)

"""
This function draws an equilateral triangle using turtle
This function uses the RGB values to randomly print the colors of the figures
"""
def triangle(length):
    boundary_check()
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.colormode(255)
    turtle.pencolor((r,g,b))
    turtle.fillcolor((r,g,b))
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.end_fill()

"""
This function calls the triangle function and draws the number of traingles as they are input by the user. This function uses recursive technique and prints the arrows randomly throughout the board
This function also computes the total area of the triangle that is shaded and returns the value
"""
def draw_figures_rec(depth,length,ar1):
    if(depth>0 and length>0):
        triangle(length)
        turtle.up()
        turtle.forward(random.randint(1,MAX_DISTANCE))
        turtle.left(random.randint(-MAX_ANGLE,MAX_ANGLE))
        turtle.down()
        ar1=ar1+area_of_triangle(length)
        return(draw_figures_rec(depth-1,random.randint(1,MAX_SIZE),ar1))
    else:
        return ar1

"""
This function is same as the draw_figures_rec function, It also calls the triangle function and prints the arrows randomly throughout the board
This function also prints the total shaded area of the triangle.
"""
def draw_figures_iter(depth,length):
    ar2=0
    while(depth>0 and length>0):
        triangle(length)
        turtle.up()
        turtle.forward(random.randint(1,MAX_DISTANCE))
        turtle.left(random.randint(-MAX_ANGLE,MAX_ANGLE))
        turtle.down()
        ar2=ar2+area_of_triangle(length)
        length=random.randint(1,MAX_SIZE)
        depth=depth-1
    if(depth==0 or length==0):
        return ar2

"""
This function draws the board of 200 by 200 pixels and moves the turtle to the center of the figure after drawing it
"""
def boundary():
    turtle.up()
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.down()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.up()
    turtle.forward(200)
    turtle.right(90)
    turtle.down() 

"""
So the main function takes the input from the user for the total number of the arrows and calls the draw_figures_rec function and draw_figures_iter.
It prints the value of the total shaded area in the figure.
"""
def main():
    a=int(input("arrows (0-500) "))
    turtle.speed(0)
    if(a<=MAX_FIGURES):
        boundary()
        sum=draw_figures_rec(a,random.randint(1,30),0)
        print("The total area is ",sum,"units")
        v=input("Hit enter to continue...")
        turtle.reset()
        turtle.speed(0)
        boundary()
        sum1=draw_figures_iter(a,random.randint(1,30))
        print("The total area is ",sum1,"units")
        print("CLose the canvas window to quit.")
    else:
        print("Arrows must be between 0 and 500 inclusive")
    turtle.done()

        
main()

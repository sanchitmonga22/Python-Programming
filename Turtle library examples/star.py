"""
drawing a star
author:sanchit monga
"""
import turtle

"""
defining the initial position of the turtle
"""
def initialize():
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.left(203)

"""
This function draws an equilateral triangle of side 100 pixels each 
the function starts drawing a straight line of 100 pixels and then changes its angle and then again draws the line and repeats the process thrice
the final state of the turtle after drawing the triangle is the initial state for drawing the next triangle
"""
def draw_triangle():
    turtle.down()
    turtle.forward(100)
    turtle.left(240)
    turtle.forward(100)
    turtle.left(240)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(348)

"""
the main function calls the rest of the functions and draws the complete star
It first calls the initialize function which assigns a position to the turtle
then it calls the triangle function for 5 times to make a complete star consisting of 5 equilateral triangles.
"""
def main():
    initialize()
    draw_triangle()   
    draw_triangle()
    draw_triangle()
    draw_triangle()
    draw_triangle()
    turtle.done()

main()

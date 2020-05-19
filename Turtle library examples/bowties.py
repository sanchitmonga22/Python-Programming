import turtle
"""
This program uses recursive technique to draw bowties
author:Sanchit Monga
"""
"""
This function draws a single equilateral triangle or half the bowtie
Pre: The turtle in the initial state is facing east
post: It is same as the precondition
s is a local variable and is the size of the side of the triangle
"""
def draw_triangle(s):
    turtle.pencolor("purple")
    turtle.left(30)
    turtle.forward(s)
    turtle.right(120)
    turtle.forward(s)
    turtle.right(120)
    turtle.forward(s)
    turtle.right(150)
    
"""
This function calls the draw_triangle function twice and draws 2 equilateral triangle in the form of a bowtie. After drawing 2 triangles it draws a circle in the middle of about a 1/4 of the size of the side
Pre: The turtle in the initial state is facing east
post: It is same as the precondition
siz is a local variable and is the size of the side of the triangle 
"""
def draw_one_bowtie(siz):
    draw_triangle(siz)
    turtle.left(180)
    draw_triangle(siz)
    turtle.left(180)
    turtle.right(90)
    turtle.forward(siz/4)
    turtle.left(90)
    turtle.pencolor("blue")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(siz/4)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(siz/4)
    turtle.right(90)
    turtle.down()

"""
This is a recursive function and calls itself again and again along with draw_one_bowtie function. This function takes 2 arguments depth and size.
The function has a base case which stops the function from crashing. The function calls the bow_tie function and navigates the turtle to all the other positions to draw the bowtie.
Pre: The turtle in the initial state is facing east
post: It is same as the precondition
size is a local variable and is the size of the side of the triangle
depth is a local variable and it is the number of times the recursive function will call itself
"""
def draw_bowties(depth,size):
    if depth==0 or size==0:
        pass
    else:
        draw_one_bowtie(size)
        turtle.left(30)
        turtle.up()
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.left(120)
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.right(150)
        turtle.right(30)
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.right(120)
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.left(150)
        turtle.down()

"""
The main function takes the input of the depth from the user and calls the draw_bowties function and prints the figure and stops the program after drawing the figure.
Pre: The turtle in the initial state is facing east
post: It is same as the precondition
size is a local variable and is the size of the side of the triangle
"""      
def main():
    turtle.setup(600,600)
    turtle.speed(0)
    d=int(input("enter the recursive depth: "))
    draw_bowties(d,100)
    turtle.done()
    
main()

import turtle as tt
"""
This program draws the circles using recursive technique
author: Sanchit Monga
"""
"""
This function draws a single circle and the intial and final position of the turtle is the centre of the circle
Initially the turtle is up and then it is down.
rad is the local variable which has the value of the radius of the circle to be drawn
"""
def draw_one_circle(rad):
    tt.up()
    tt.right(90)
    tt.forward(rad)
    tt.left(90)
    tt.down()
    tt.circle(rad)
    tt.up()
    tt.left(90)
    tt.forward(rad)
    tt.right(90)
    tt.down()

"""
This is the recursive function which calls itself according to the value of n
This function has a base case which does nothing when the value of n is 0.
n and r are local variables where n represents the number of recursions and r represents the radius of the circle
This function calls the draw_one_circle function and uses it for drawing one single circle
"""
def draw_circle(n,r):
    if(n==0):
        pass
    elif(n>0):
        draw_one_circle(r)
        tt.up()
        tt.forward(r)
        tt.left(90)
        tt.forward(r/2)
        tt.right(90)
        tt.down()
        draw_circle(n-1,r/2)
        tt.up()
        tt.right(90)
        tt.forward(r/2)
        tt.left(90)
        tt.back(2*r)
        tt.left(90)
        tt.forward(r/2)
        tt.right(90)
        tt.down()
        draw_circle(n-1,r/2)
        tt.up()
        tt.right(90)
        tt.forward(r/2)
        tt.left(90)
        tt.forward(r)
        tt.down()
"""
This function takes the input from the user for the value of n.
This function calls the draw_circle functions and passes the value of n entered by the user
"""
def main():
    tt.speed(0)
    n=int(input("enter the value of n:  "))
    draw_circle(n,100)
    turtle.done()

main()

     

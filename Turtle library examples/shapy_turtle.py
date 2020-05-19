import turtle
import math
"""
Author: Sanchit Monga
Language: Python
This program takes the shorthand language commands and perform the given task
"""
def front(st):
    """
    This function inputs a string and checks whether the characters are numbers or not and returns a string without number in the front
"""
    num=""
    for char in st:
        if (char.isdigit()):
            num=num+char
        else:
            break
    return num

def left(st):
    """
    This function inputs a string and it extracts the number from front
    then this program uses the number to turn the turtle left by the given angle
"""
    d=front(st)
    turtle.left(int(d))
    return(st[len(d):])

def right(st):
    """
    This function inputs a string and it extracts the number from front
    then this program uses the number to turn the turtle right by the given angle
"""
    d=front(st)
    turtle.right(int(d))
    return(st[len(d):])

def square(st):
    """
    This function inputs a string and it extracts the number from front
    The function draws a square with the side of the length of the number that was extracted from front function
"""
    a=front(st)
    s=int(a)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.right(90)
    return(st[len(a):])

def equitri(st):
    """
    This function inputs a string and it extracts the number from front
    The function draws an equilateral triangle with the side of the length of the number that was extracted from front function
"""
    a=front(st)
    s=int(a)
    turtle.forward(s)
    turtle.left(120)
    turtle.forward(s)
    turtle.left(120)
    turtle.forward(s)
    turtle.left(120)
    return(st[len(a):])

def cir(st): 
    """
    This function inputs a string and it extracts the number from front
    The function draws a cricle of the radius of the number that was extracted from front function
"""
    r=front(st)
    turtle.circle(int(r))
    return(st[len(r):])
        
def forw(st):
    """
    This function inputs a string and it extracts the number from front
    The function moves the turtle forward with the length of the number that was extracted from front function
"""
    r=front(st)
    turtle.forward(int(r))
    return(st[len(r):])

def back(st):
    """
    This function inputs a string and it extracts the number from front
    The function moves the turtle back with the length of the number that was extracted from front function
"""
    r=front(st)
    turtle.back(int(r))
    return(st[len(r):])

def up():
    """
    This function moves the turtle pen up so that the turtle does not draw
"""
    turtle.up()    
    
def down():
    """
    This function moves the turtle pen down so that the turtle can draw as it moves
"""
    turtle.down()   

def rect(st):
    """
    This function inputs a string and it extracts the number from front
    The function draws the triangle with the length and breadth of the number that will be extracted from front function
""" 
    l=front(st)
    b=front(st[len(l)+1:])
    if(b!=""):#Checking whether the second command entered for the rectangle is a number or not
        l1=int(l)
        b1=int(b)
        turtle.forward(b1)
        turtle.left(90)
        turtle.forward(l1)
        turtle.left(90)
        turtle.forward(b1)
        turtle.left(90)
        turtle.forward(l1)
        turtle.left(90)
        return (st[len(l)+len(b)+1:])
    else:
        return 'a'#Returning a variable other than the commands

def polygon(st):
    """
    This function inputs a string and it extracts the number from front
    The function draws a regualar polygon by taking length and the number of sides as the input which was extracted from front function
""" 
    s=front(st)
    l=front(st[len(s)+1:])
    if(l!=""):#Checking whether the second command entered for the polygon is a number or not
        s1=int(s)
        l1=int(l)
        for i in range(s1):
            turtle.forward(l1)
            turtle.left(360/s1)
        return (st[len(s)+len(l)+1:])
    else:
        return 'a'#Returning a variable other than the commands

def goto(st):
    """
    This function inputs a string and it extracts the number from front
    The function moves the turtle to the X and Y numbers that were extracted from front function
"""
    x=front(st)
    y=front(st[len(x)+1:])
    if(y!=""):#Checking whether the second command entered for the Goto is a number or not
        x1=int(x)
        y1=int(y)
        turtle.goto(x1,y1)
        return (st[len(x)+len(y)+1:])
    else:
        return 'a'#Returning a variable other than the commands

def penc(st):
    """
    This function inputs a string and it extracts the number from front
    The function changes the pencolor according to the pencolor code given in the question by extracting the number by using front function
""" 
    z=front(st)
    z1=int(z)
    if(z1==0):
        turtle.pencolor("red")
    elif(z1==1):
        turtle.pencolor("blue")
    elif(z1==2):
        turtle.pencolor("green")
    elif(z1==3):
        turtle.pencolor("yellow")
    elif(z1==4):
        turtle.pencolor("brown")
    else:
        turtle.pencolor("black")
    return(st[len(z):])

def processC(s):
    """
    This function takes the string as input from the user and uses a while loop to go through all the characters of the string.
    This function uses if else statements to check whether the front of the string is a shorthand language command or not and calls the functions accordingly
"""
    while(s!=""):
        if(s[0]=='S' and s[1].isdigit()):
            s=square(s[1:])
        elif(s[0]=='<' and s[1].isdigit()):
            s=left(s[1:])
        elif(s[0]=='>' and s[1].isdigit()):
            s=right(s[1:])
        elif(s[0]=='G' and s[1].isdigit()):
            s=goto(s[1:])
        elif(s[0]=='R' and s[1].isdigit()):
            s=rect(s[1:])
        elif(s[0]=='P' and s[1].isdigit()):
            s=polygon(s[1:])
        elif(s[0]=='Z' and s[1].isdigit()):
            s=penc(s[1:])
        elif(s[0]=='F' and s[1].isdigit()):
            s=forw(s[1:])
        elif(s[0]=='B' and s[1].isdigit()):
            s=back(s[1:])
        elif(s[0]=='T' and s[1].isdigit()):
            s=equitri(s[1:])
        elif(s[0]=='C' and s[1].isdigit()):
            s=cir(s[1:])
        elif(s[0]=='U'):
            up()
            s=s[1:]
        elif(s[0]=='D'):
            down()
            s=s[1:]
        else:
            return 0
            break
        
def main():
    """
    This function takes the input from the user and passes the value to the processC function which further performs all the required tasks
"""
    st=input("Enter the Command: ")
    turtle.speed(0)
    a=processC(st)
    if(a==0):
        print("Error")
        print("The command entered is wrong")
        print("Command entered: ",st)
        return None
    turtle.done()  

main()




    
    

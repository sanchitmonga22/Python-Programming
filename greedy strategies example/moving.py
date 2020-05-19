"""
author: Sanchit monga
lang: Python
This program arranges the items in a box according to the given strategies
"""
from dataclasses import dataclass#importing dataclass

@dataclass
class box():
    """
capacity stores the total capacity remaining of the box after an item is put in it
weight stores the weight of the box after the items are put in
items stores the list of the items that are put in the box
"""
    capacity: int
    weight: int
    items: list

@dataclass
class item():
    """
Weight1 stores the weight of the items
names stores the names of the items
"""
    weight1: int
    names: str

def build(f):
    """
This function takes the filename as the input and opens it
After opening it calls the box and item object and stores the values in the list
The function returns the list of the class box and class item
"""
    file=open(f)
    box1=file.readline().split()
    boxes=[]
    for i in box1:
        boxes.append(box(int(i),0,[]))
    l=[]
    for line in file:
        temp=line.split()
        l.append(item(int(temp[1]),temp[0]))
        l.sort(key=lambda g:g.weight1, reverse=True)
    return boxes,l

def str1(b,i):
    """
This function takes the boxes and item as the input and returns the output according to the strategy 1
"""
    for j in i: # itering through the items
        w=j.weight1# weight of the item
        b.sort(key=lambda g:g.capacity, reverse=True)# Arranging the capacity of boxes according to the ascending order
        w1=b[0].capacity# Capacity of the box
        if(w1>=w):# Capacity of the box
            b[0].capacity=w1-w  #
            b[0].weight+=w
            b[0].items+=[(j.names+" "+str(w))]
            j.weight1=0
    return b,i
    

def str2(b,i):
    """
This function takes the boxes and item as the input and returns the output according to the strategy 2
"""
    h=0
    for j in i: # iterating through the items
        w=j.weight1# weight of the item        
        b.sort(key=lambda g:g.capacity)#sorting the boxes
        while(True):
            if(h<len(b)):
                w1=b[h].capacity # Capacity of the box
                if(w1>=w):
                    b[h].capacity=w1-w
                    b[h].weight+=w
                    b[h].items+=[(j.names+" "+str(w))]
                    j.weight1=0
                    h=0
                    break
                else:
                    h+=1
            else:
                break
    return b,i

def str3(b,i):
    """
This function takes the boxes and item as the input and returns the output according to the strategy 3
"""
    h=0
    for j in i: # itering through the items
        w=j.weight1 #weight of the item
        while(True):
            if(h<len(b)):
                w1=b[h].capacity # Capacity of the box
                if(w1>=w):
                    b[h].capacity=w1-w
                    b[h].weight+=w
                    b[h].items+=[(j.names+" "+str(w))]
                    j.weight1=0
                    h=0
                    break
                else:
                    h+=1
            else:
                break
    return b,i
    
def main():
    """
This function takes the name of the file as the input and invokes the functions str1, str2 and str3 to apply the required strategies and gives the output 
"""
    name=input("Enter data filename: ")
    box1,item1=build(name)
    box_,item_=str1(box1,item1)
    """
Strategy 1
"""
    print()
    print("Result from strategy 1")
    c=0
    for j in item_: 
        if(j.weight1>0):
            c=1
            break 
    if(c==0):
        print("All items successfully packed into boxes!")
        y=0
        for k in box_:
            print("Box",(y+1),"of weight capacity", box1[y].weight, "contains: ")
            for i in k.items:
                w=i.split()
                print("     ",w[0], "of weight", int(w[1]))
            y+=1
    else:
        print("Unable to pack all items")
        y=0
        for k in box_:
            print("Box",(y+1),"of weight capacity", (box1[y].weight+box1[y].capacity), "contains: ")
            for i in k.items:
                w=i.split()
                print("     ",w[0], "of weight", int(w[1]))
            y+=1
        for item in item_:
            if(item.weight1!=0):
                print("     ",item.names+" of weight",item.weight1," got left behind.")
    """
Strategy 2
"""
    print()
    print("Result from greedy strategy 2")
    box3,item3=build(name)
    box2,item2=str2(box3,item3)
    c2=0
    for j in item2: 
        if(j.weight1>0):
            c2=1
            break
    if(c2==0):
        print("All items successfully packed into boxes!")
        y=0
        for k in box2:
            print("Box",(y+1),"of weight capacity", box2[y].weight, "contains: ")
            for i in k.items:
                w=i.split()
                print("     ",w[0], "of weight", int(w[1]))
            y+=1
    else:
        print("Unable to pack all items")
        y=0
        for k in box2:
            print("Box",(y+1),"of weight capacity", (box2[y].weight+box2[y].capacity), "contains: ")
            for i in k.items:
                w=i.split()
                print("     ",w[0], "of weight", int(w[1]))
            y+=1
        for item in item2:
            if(item.weight1!=0):
                print("     ",item.names+" of weight",item.weight1," got left behind.")

    """
Strategy 3
"""
    print()
    print("Result from greedy strategy 3")
    box4,item4=build(name)
    box5,item5=str3(box4,item4)
    c2=0
    for j in item5: 
        if(j.weight1>0):
            c2=1
            break
    if(c2==0):
        print("All items successfully packed into boxes!")
        y=0
        for k in box5:
            print("Box",(y+1),"of weight capacity", box5[y].weight, "contains: ")
            for i in k.items:
                w=i.split()
                print("     ",w[0], "of weight", int(w[1]))
            y+=1
    else:
        print("Unable to pack all items")
        y=0
        for k in box5:
            print("Box",(y+1),"of weight capacity", (box5[y].weight+box5[y].capacity), "contains: ")
            for i in k.items:
                w=i.split()
                print("     ",w[0], "of weight", int(w[1]))
            y+=1
        for item in item5:
            if(item.weight1!=0):
                print("     ",item.names+" of weight",item.weight1," got left behind.")

    
main()
        
            


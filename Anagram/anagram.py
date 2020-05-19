"""
@author: Sanchit Monga
"""
def arrange(s):
    """
This function accepts a string and returns a string arranged in ascending order
"""
    a=[]
    for c in s:
        a.append(c)
    b=sorted(a)
    a1=''
    for d in b:
        a1=a1+d
    return a1# returning the string arranged in the ascending order

def read_file(filename):
    """
This function accepts the name of the file
and opens and reads the file. While reading it it extract all the words and add them to the dictionary with the appropriate key
"""
    l={}
    with open(filename, "r", encoding="utf-8") as fd:
        for line in fd:
            word=line.strip()
            arr=arrange(word)# arranging the characters in the ascending order by invoking the arrange function
            if arr in l:
                l[arr].append(word)
            else:
                l[arr]=[word]
    fd.close()
    return l# returning a dictionary

def task3(w,l):
    """
This function completes the task 3.
It takes the dictionary and the length of the word as the parameters
This function first checks all the word of the required length

"""
    li=[]# list of the words
    limax=0# the maximum number of lexigraphical words in a list
    j=[]# storing the elements of list with maximum words
    for i in w:
        if(len(i)==l):
            li=w[i][:]# All the elements of the list with key i are assigned to li
            if(len(li)>limax):# checking whether the limax has the maximum number of the elements
                limax= len(li)
                j=li
    return j  # Returning the list with the maximum words              

def task4(w,l):
    """
This function computes the task 4 in which it returns the number of words which are unique and do not have a lexigraphical word
This function takes the length of the word and dictionary as the parameters
"""
    li=[]
    j=[]
    count=0
    for i in w:# accesing the words in the dictionary with the key
        if(len(i)==l):# if the length of the key matches the length of the word
            li=w[i][:]
            if(len(li)==1):
                count+=1# counting the number of unique words
    return count# returning the maximum number of non lexographical characters

def main():
    """
This function takes the input from the user and invokes the other functions and computes the value of all the tasks
"""
    file="american-english.txt"
    a=read_file(file)# calling the readfile function
    """
Task 2
"""
    while True:
        search=input("Enter input string (hit enter key to go to task 3): ")# Taking the input of theword to be searched in the dictionary
        if(search!=""):
            e=arrange(search)# calling the arrange function to arrange the characters of the word in the ascending order
            if e in a:
                print(a[e])
            else:
                print("No words can be formed from:", search)
        else:
            break
    """
Task 3
"""
    while True:
        integer=input("Enter word length (hit enter key to go to task 4): ")# taking the input of the length of the word for task4
        if(integer!=""):
            k=task3(a,int(integer))
            print(k)
        else:
            break
    """
Task 4
"""
    while True:
        i=input("Enter word length (hit enter key to quit): ")# taking the input of the length of the word
        if(i!=""):
            o=task4(a,int(i))
            print(o)
        else:
            break
        
main()
                    
        

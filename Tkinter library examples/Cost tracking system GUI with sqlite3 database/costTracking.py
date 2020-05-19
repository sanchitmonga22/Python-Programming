from tkinter import *
from tkinter import ttk
import math
import sqlite3
import pathlib

"""
@Author: Sanchit Monga
@Author Arpit Mehta
A program created to help keep track of costs and hours for a manufacturing
company
"""

#dbFile= pathlib.Path("D:\downloads\p3\Project3.sqlite3")
#conn.close()

root = Tk()
root.title("Project 3")
root.geometry("400x400")

sales = 0
materialcost = 0
laborcost = 0
totalquantity = 0
profit = 0
finalassembly = 0
machinehrs = 0
finishhrs = 0
assemblyhrs = 0
ono = 0

"""
if dbFile.exists() == False:
    # The database file does NOT exists
    raise Exception("Database file:"+dbFile+" does not exist")
else:
    try:
        # Open the connection to the file
        connection = sqlite3.connect(dbFile)
        command = connection.cursor()
        command.execute("CREATE TABLE p3Orders (id INTEGER PRIMARY KEY AUTOINCREMENT, qty INT, finalassembly INT, hours INT)")
    except Exception as ex:
        print("Database Error:", ex)
"""

connection= sqlite3.connect("costTracking.sqlite3")
command= connection.cursor()

"""
Calculates the finishweek provided the number of total hours
"""
def calculateFinishWeek(totalhours):
    if totalhours%40==0:
        finishweek = int(totalhours/40)
    else:
        finishweek = math.floor(((totalhours)/40)+1)
    return finishweek

"""
Initializes the GUI with all the values from the sql database
"""
def fnDisplayValues():
    #lb.delete(0,END)

    #contains the sql command which takes out all the orders from the database file
    sql = "SELECT * FROM p3Orders"
    
    #going over all the records
    for record in command.execute(sql):
        #Calculating the finish week for the entered query
        
        totalhours=int(record[2])
        finishweek=calculateFinishWeek(totalhours)

        #message to be displayed in the ListBox
        msgInlistBox= "Order "+ str(record[0]) + "||Qty " + str(record[1]) + "||Final Assembly:" +str(record[3]) +"||Hours " +str(totalhours) + "||Finish Week " +str(finishweek)

        #inserts the message at the end of the listBox
        lb.insert(END, msgInlistBox)

"""
This function is called when a user selects to delete an item from the list box
"""
def deleteOrder():
    sql = "DELETE FROM p3Orders WHERE id ="
    selectionIndex= lb.curselection()
    if selectionIndex:
        print("Value was selected to be removed.")
        sql+=str(selectionIndex)
        fnDisplayValues()
        command.execute(sql)
    else:
        raise Exception("Please select a value to remove")



"""
This function is called when the user prints clicks a button in the GUI to add the orders into it
"""
def button_click():
    
    global ono, sales,materialcost, laborcost, totalquantity, profit,finalassembly, machinehrs, finishhrs, assemblyhrs

    ono = ono + 1
    sql="INSERT INTO p3Orders (qty, finalassembly, hours) VALUES ("+str(ono)+ ","
    orderquantity = float(inputValue.get())
    msgInLstBx = "Order " + str(ono) +  "||Qty " + str(orderquantity) + "||Final Assembly:" 
    if applyFinalAssemblyVar.get () == 1:
        finalassembly = finalassembly + 10
        applyFinalAssemblytext.config(text=str(finalassembly))
        assemblyhrs = assemblyhrs + (1*orderquantity)
        laborcost = laborcost + 15 * 1 * orderquantity
        msgInLstBx = msgInLstBx + "1"
        sql+="1,"
    else:
        messageInLstBx = "0"
        sql+="0,"
    
    # Formulas to calculate the variables
    sales = (150 * 1 * (orderquantity)) + (sales) + finalassembly
    materialcost = (20 * (orderquantity)) + (materialcost)
    laborcost = (20 * 3 * (orderquantity)) + (30 * 1 * (orderquantity)) + (laborcost)
    totalquantity = (orderquantity) + (totalquantity)
    profit= sales - laborcost- materialcost
    machinehrs = (3 * (orderquantity)) + (machinehrs)
    finishhrs =  (1 * (orderquantity)) + (finishhrs)
    
    # Formulas to calculate finish week
    totalhours = (assemblyhrs + machinehrs + finishhrs)

    # Use conditions to remain at correct week when total hours is divisible by 40. Using math.floor to round down finish week values
    if totalhours%40==0:
        finishweek = int(totalhours/40)
    else:
        finishweek = math.floor(((totalhours)/40)+1)
    
    #updating the message to be printed in the listBox
    msgInLstBx = msgInLstBx + "||Hours " + str(totalhours) + "||Finish Week " + str(finishweek)

    #updating the database sql command
    sql+=str(totalhours)+")"

    # Converting all variables to string and updating the texts in the Labels
    Salestext.config(text=str(sales))
    MaterialText.config(text=str(materialcost))
    Labortext.config(text=str(laborcost))
    totalquantText.config(text=str(totalquantity))
    Profittext.config(text=str(profit))
    MachinistText.config(text=str(machinehrs))
    FinishingText.config(text=str(finishhrs))
    AssemblyText.config(text=str(assemblyhrs))

    # adding data in the database
    command.execute(sql)
    # Adding data to the list
    lb.insert ( END,     msgInLstBx  )

"""
Creates a label with the provided labelName and places it in the desired row and column of the GUI
"""
def createLabel(labelName, row, column):
    label=Label(root,text=labelName)
    label.grid(row=row, column=column, sticky=W)
    return label

# Main Program
label1 = createLabel("Order Quantity:",0,0)
inputValue = Entry(root)
inputValue.grid(row=0, column=1, sticky=W)
button = Button(root, text="Order", command=button_click)
button.grid(row=0, column=2, sticky=W)

applyFinalAssemblyVar = IntVar()
applyFinalAssembly = Checkbutton(root, text="Final Assembly: $", variable=applyFinalAssemblyVar)
applyFinalAssembly.grid(row=1, column=0, sticky=W)
applyFinalAssemblytext = createLabel("",1,1)

label2= createLabel("Material Costs: $",3,0)
MaterialText=createLabel("0",3,1)

label3 = createLabel("Labor Costs: $",4,0)
Labortext = createLabel("0",4,1)

label4 = createLabel("Sales: $",5,0)
Salestext = createLabel("0",5,1)

label5 = createLabel("Profit: $",6,0)
Profittext = createLabel("0",6,1)

label6 = createLabel("Total Quantity:",7,0)
totalquantText =createLabel("0",7,1)

label7 = createLabel("Machinist Hours:",3,2)
MachinistText = createLabel("0",3,3)

label8 = createLabel("Finishing Hours:",4,2)
FinishingText = createLabel("0",4,3)

label9 = createLabel("Assembly Hours:",5,2)
AssemblyText = createLabel("0",5,3)

createLabel("Production Planning:",11,0)
planningFrame = Frame(root)
planningFrame.grid(row=12, rowspan=40, column=0, columnspan=50, sticky=W)

# Creating listbox and scrollbar
lb = Listbox(planningFrame, width=60, height=5)
lb.pack(side = 'left',fill = 'y' )
scrollbar = Scrollbar(planningFrame, orient="vertical",command=lb.yview)
scrollbar.pack(side="right", fill="y")
lb.config(yscrollcommand=scrollbar.set)

button = Button(root, text="Delete Selected Order", command=deleteOrder)
button.grid(row=60, column=0, sticky=W)

root.mainloop()

from tkinter import *
import math

"""
@author: Sanchit Monga
Project 2
"""

root = Tk()
root.title("Sanchit Monga Project 2")
root.geometry("400x300")

materialCosts=0
laborCosts=0
sales=0
profit=0
totalQty=0
machineHours=0
finishHours=0
assemblyHours=0
final_assembly=0
final_hrs=0
outputCollection=[]
finalAssembly="No"
orderNumberCounter=1
quantity_number=0
finishWeek=0
"""
Final Assembly Price(optional) $10
Material Costs Per Unit $20
Machining Hours Per unit 3 hrs
Finishing Hours per unit 1 hr
Assembly hours per unit(optional) 1 hr
Machining Labor hourly wage $20/hr
Finishing Labor Hourly Wage $30/hr
Assembly Labor hourly wage $15/hr
"""
def button_click():
    #print("button_click called")
    global materialCosts,laborCosts,sales,profit,totalQty,machineHours,assemblyHours, finishHours, final_assembly, final_hrs, finishWeek, orderNumberCounter, finalAssembly, outputCollection
    orders= float(inputValue.get())
    """
    If the button was clicked
    """
    if Final_Assembly_Var.get()==1:
        final_assembly=final_assembly+orders*10
        FinalAssemblyText.config(text=str(final_assembly))
        laborCosts=laborCosts+orders*15*1
        assemblyHours=assemblyHours+1*orders
        finalAssembly="Yes"
    
    """
    Calculating all the values
    """
    materialCosts= materialCosts+orders*20
    laborCosts=laborCosts+(20*3*orders+30*1*orders)
    sales=sales+orders*150+final_assembly
    profit=sales-laborCosts-materialCosts
    totalQty=totalQty+orders
    machineHours= machineHours+orders*3
    finishHours= finishHours+orders
    final_hrs = machineHours+finishHours+assemblyHours
    finishWeek=finishWeek+ math.floor(final_hrs/40)+1
    if final_hrs%40==0:
        finishWeek=finishWeek-1
        
    """
    Updating the values in all the text boxes
    """
    MaterialText.config(text=str(materialCosts))
    Labourtext.config(text=str(laborCosts))
    Salestext.config(text=str(sales))
    Profittext.config(text=str(profit))
    totalquantText.config(text=str(totalQty))
    MachinistText.config(text=str(machineHours))
    FinishingText.config(text=str(finishHours))
    AssemblyText.config(text=str(assemblyHours))
    output="Order "+str(orderNumberCounter)+" || Qty "+str(orders)+" || Final Assembly "+str(finalAssembly)+" || Hours "+str(final_hrs)+" || Finish Week "+str(finishWeek)
    ListBox.insert( END, output)
    orderNumberCounter+=1
    finalAssembly="No"



Quantity_Label = Label(root, text="Quantity ")
Quantity_Label.grid(row=0, column=0, sticky=W)

inputValue = Entry(root,)
inputValue.grid(row=0, column=1, sticky=W)

button = Button(root, text="Order", command=button_click)
button.grid(row=0, column=2, sticky=W)

Final_Assembly_Var = IntVar()
FinalAssembly = Checkbutton(root, text="Final Assembly: ", variable=Final_Assembly_Var)
FinalAssembly.grid(row=2, column=2, sticky=W)
FinalAssemblyText = Label(root, text="")
FinalAssemblyText.grid(row=2,column=3,sticky=W)

Machinist_label = Label(root, text="Machinist Hours:")
Machinist_label.grid(row=3, column=2, sticky=W)
MachinistText = Label(root, text="0")
MachinistText.grid(row=3, column=3, sticky=W)

Finishing_hours_label = Label(root, text="Finishing Hours:")
Finishing_hours_label.grid(row=4, column=2, sticky=W)
FinishingText = Label(root, text="0")
FinishingText.grid(row=4, column=3, sticky=W)

Assembly_hours_label = Label(root, text="Assembly Hours:")
Assembly_hours_label.grid(row=5, column=2, sticky=W)
AssemblyText = Label(root, text="0")
AssemblyText.grid(row=5, column=3, sticky=W)

Material_Costs_Label = Label(root, text="Material Costs:   $")
Material_Costs_Label.grid(row=2, column=0, sticky=W)
MaterialText = Label(root, text="0")
MaterialText.grid(row=2, column=1, sticky=W)

Labour_Costs_label = Label(root, text="Labour Costs:     $")
Labour_Costs_label.grid(row=3, column=0, sticky=W)
Labourtext = Label(root, text="0")
Labourtext.grid(row=3, column=1, sticky=W)

Sales_Label = Label(root, text="Sales:                   $")
Sales_Label.grid(row=4, column=0, sticky=W)
Salestext = Label(root, text="0")
Salestext.grid(row=4, column=1, sticky=W)

Profit_label = Label(root, text="Profit:                  $")
Profit_label.grid(row=5, column=0, sticky=W)
Profittext = Label(root, text="0")
Profittext.grid(row=5, column=1, sticky=W)

Total_Qty_label = Label(root, text="Total Qty:")
Total_Qty_label.grid(row=6, column=0, sticky=W)
totalquantText = Label(root, text="0")
totalquantText.grid(row=6, column=1, sticky=W)

Label(root, text="Production Planning:").grid(row=11, column=0, sticky=W)
pFrame = Frame(root)
pFrame.grid(row=12, rowspan=80, column=0, columnspan=150, sticky=W)

ListBox = Listbox(pFrame, width=60, height=5)
ListBox.pack(side = 'left',fill = 'y' )
scrollbar = Scrollbar(pFrame, orient="vertical",command=ListBox.yview)
scrollbar.pack(side="right", fill="y")
ListBox.config(yscrollcommand=scrollbar.set)

root.mainloop()
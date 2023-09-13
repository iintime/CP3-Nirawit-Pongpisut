from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    labelBMI.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if bmi >= 30:
        labelResult.configure(text="Very Fat",fg="red")
    elif bmi >= 25.0 and bmi <= 29.9:
        labelResult.configure(text="Fat",fg="orange")
    elif bmi >= 23.0 and bmi <= 24.9:
        labelResult.configure(text="Over Weight",fg="yellow")
    elif bmi >= 18.6 and bmi <= 22.9:
        labelResult.configure(text="Normal Weight",fg="green")
    elif bmi <= 18.5:
        labelResult.configure(text="Too Thin",fg="blue")


MainWindow = Tk()
labelHeight = Label(MainWindow, text = "Height (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=2)
labelWeight = Label(MainWindow, text = "Weight (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=2)
calculateButton = Button(MainWindow, text = "Calculation")
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row=2,column=0)
labelBMI = Label(MainWindow, text="BMI")
labelBMI.grid(row=2,column=2)
labelResult = Label(MainWindow)
labelResult.grid(row=3,column=1)
MainWindow.mainloop()
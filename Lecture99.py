from tkinter import *
import math
def leftClickButton(event):
    # labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    height = float(textBoxHeight.get())
    weight = float(textBoxWeight.get())
    BMI = round((weight / (math.pow(height / 100, 2))), 2)
    print(BMI)
    if BMI < 18.5:
        labelResult.configure(text=[BMI, 'Very Skinny'])
    elif BMI < 22.9:
        labelResult.configure(text=[BMI, "Normal"])
    elif BMI < 24.9:
        labelResult.configure(text=[BMI, "Overweight"])
    elif BMI < 29.9:
        labelResult.configure(text=[BMI, "Fat"])
    else:
        labelResult.configure(text=[BMI, "Very Fat"])


MainWindow = Tk()
labelHeight = Label(MainWindow,text="Height (cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="Weight (kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="Result")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="Result")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()
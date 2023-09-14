from tkinter import *


#ฟังก์ชันคำนวนโบนัส
def leftClickButton(event):
    labelResult.configure(text=float(textBoxMonth.get())*(float(textBoxSalary.get())))

#ฟังก์ชั่นปุ่มรีเซ็ท
def reset():
    salary.delete(0,END)
    bonus.delete(0,END)
    labelResult.configure(text="")

MainWindow = Tk()
MainWindow.geometry("300x250")
MainWindow.title("Bonus Calculator")
Label(text="Please Enter Your Information").grid(row=0, column=1)

Label(text="").grid(row=1, column=1)

#รับค่าเงินเดือนมา
salary = Label(MainWindow, text="Salary (THB)")
salary.grid(row=2,column=0)
Label(MainWindow,text="THB").grid(row=2, column=2)
textBoxSalary = Entry(MainWindow)
textBoxSalary.grid(row=2,column=1)

Label(text="").grid(row=3, column=1)

#รับค่าจำนวนโบนัสที่ได้
bonus = Label(MainWindow, text="Bonus (Month)")
bonus.grid(row=4,column=0)
Label(MainWindow,text="Month").grid(row=4, column=2)
textBoxMonth = Entry(MainWindow)
textBoxMonth.grid(row=4,column=1)

Label(text="").grid(row=5, column=1)


calculateButton = Button(MainWindow,text = "Calculate")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=6,column=0)
labelResult = Label(MainWindow,text="Total")
Label(MainWindow,text="THB").grid(row=6, column=2)
labelResult.grid(row=6,column=1)

clearButton = Button(MainWindow, text="Reset", command=reset).grid(row=7, column=0,sticky=E)

MainWindow.mainloop()


import tkinter as tk
import calendar

# The name of the main application is root
root = tk.Tk()

#declaring variables
HEIGHT = 1000
WIDTH = 1200
year = 2020
month = 3

# The Header for the application will say expense tracker
root.title("Expense Tracker")

# Temporary background dimensions
background = tk.Canvas(root, height=HEIGHT, width=WIDTH)
background.pack()

# Created a frame to the left for the Categories and the expenses
leftFrame = tk.Frame(root, bg='blue')
leftFrame.place(relx=0, rely=0, relheight=1, relwidth=0.30)

# A frame for the calendar part of the application
calFrame = tk.Frame(root, bg='green')
calFrame.place(relx=0.30, rely=0, relheight=1, relwidth=0.7)

# Inserting the calendar into the gui
testList = calendar.monthcalendar(year, month)
for i, j in enumerate(testList):
    for index, listNums in enumerate(j):
        myCal = tk.Label(calFrame, bg='yellow', text=listNums)
        myCal.grid(row=i, column=index, ipady=10, ipadx=10)
# This runs the application
root.mainloop()

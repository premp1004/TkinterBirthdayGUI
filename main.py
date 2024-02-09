import tkinter as tk
import math
import datetime
from datetime import datetime, timedelta, date


# from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import *
# from tkcalendar import Calendar, DateEntry
window = tk.Tk()
window.title("Age Calculator")
window.geometry("750x750")
window.configure(bg='lightgray')


month = StringVar(window)
choices = ['Jan','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
month.set('Jan') # set the default option

###########DEF#############
def clearEntry() :
  birthDateInput.delete(0, END)
  birthDateInput.insert(0, "")
  birthMonthInput.delete(0, END)
  birthMonthInput.insert(0, "")
  birthYearInput.delete(0, END)
  birthYearInput.insert(0, "")

def getUserBirthMonth():
    global birthMonth
    selection = month.get()
    if selection == "Jan" or selection == "Jan":
      birthMonth = 1
      print(birthMonth)
    elif selection == "Feb":
      birthMonth = 2
      print(birthMonth)
    elif selection == "Mar":
      birthMonth = 3
      print(birthMonth)
    elif selection == "Apr":
      birthMonth = 4
      print(birthMonth)
    elif selection == "May":
      birthMonth = 5
      print(birthMonth)
    elif selection == "Jun":
      birthMonth = 6
      print(birthMonth)
    elif selection == "July":
      birthMonth = 7
      print(birthMonth)
    elif selection == "Aug":
      birthMonth = 8
      print(birthMonth)
    elif selection == "Sept":
      birthMonth = 9
      print(birthMonth)
    elif selection == "Oct":
      birthMonth = 10
      print(birthMonth)
    elif selection == "Nov":
      birthMonth = 11
      print(birthMonth)
    elif selection == "Dec":
      birthMonth = 12
      print(birthMonth)
    else:
      print("Choose a month")

def dates():
    global birthDate, birthMonth, birthYear, dayToday, monthToday, yearToday, hourToday, minuteToday, secondToday

#https://www.programiz.com/python-programming/datetime/strftime
    yearToday = int(date.today().strftime('%Y'))
    monthToday = int(date.today().strftime('%m'))
    dayToday = int(date.today().strftime('%d'))
    hourToday = int(datetime.now().strftime('%H'))
    minuteToday = int(datetime.now().strftime('%M'))
    secondToday = int(datetime.now().strftime('%S'))

    birthDate = int(birthDateInput.get())
    birthMonth = int(birthMonthInput.get())
    birthYear = int(birthYearInput.get())



    try :
      # The get() could throw an exception if the user
      # enters a non-numerical answer, so handle it!
        int(float(birthDate))
        int(birthMonth)
        int(birthYear)
    except ValueError :
        output_label.configure(text="Error! Enter a valid number.Please try again.")
        # clear the entry box
        clearEntry()
    else :
        pass

    finally :
        ageYears()
        ageMonths()
        ageDays()
        ageHours()
        ageMinutes()
        ageSeconds()



def test():
    global birthDate, birthMonth, birthYear, dayToday, monthToday, yearToday


def Calc():
    print("hi")

def ageYears() :
    global birthDate, birthMonth, birthYear, dayToday, monthToday, yearToday, ageYears

    ageYears = yearToday - birthYear - ((monthToday, dayToday) < (birthMonth, birthDate))
    print(ageYears)

def ageMonths():
    global birthDate, birthMonth, birthYear, dayToday, monthToday, yearToday, ageYears

    ageMonths = ((ageYears*12) + abs((monthToday - birthMonth)))
    ageMonthsRounded = math.floor(ageMonths)
    print(ageMonthsRounded)

def ageDays():
    global birthDate, birthMonth, birthYear, dayToday, monthToday, yearToday, daysAlive

    birthdayDate = datetime(birthYear, birthMonth, birthDate)
    new_date = datetime.today() - birthdayDate
    daysAlive = new_date.days
    print(daysAlive)


def ageHours():
    global dayToday, monthToday, yearToday, daysAlive, hourToday, minuteToday, hoursAlive
    hoursAlive = ((daysAlive*24) + hourToday)
    print(hoursAlive)

def ageMinutes():
    global hourToday, minuteToday, hoursAlive, secondToday, minutesAlive
    minutesAlive = ((hoursAlive*60) + minuteToday)
    print(minutesAlive)

def ageSeconds():
    global hourToday, minuteToday, hoursAlive, secondToday, minutesAlive
    secondsAlive = ((minutesAlive*60) + secondToday)
    print("You have lived", secondsAlive)

###########DEF-END#########
txtTitle = tk.Label(text="Age Calculator", font=('Helvetica', 32, 'underline'))
txtTitle.configure(bg='lightgray')
txtTitle.pack()
subText = tk.Label(text="For Calculating your exact age in years and months, minutes and seconds!", font=('Helvetica', 16))
subText.configure(pady=5, bg='lightgray')
subText.pack()

birthDateInput = tk.Entry(bd=2)
birthDateInput.insert(0, "DD")
birthDateInput.pack(pady=10)

# label = tk.Label(text="Enter your birth month")
# label.pack()
# option_menu = OptionMenu(window, month, *choices)
# option_menu.config(width=16)
# option_menu.pack()

birthMonthInput = tk.Entry(bd=2)
birthMonthInput.insert(0, "MM")
birthMonthInput.pack(pady=10)


birthYearInput = tk.Entry(bd=2)
birthYearInput.insert(0, "YYYY")
birthYearInput.pack(pady=10)

button = tk.Button(text="Click me!", command=dates)
button.pack()

output_label = tk.Label(text="Enter numbers, then click either button", font=('Helvetica', 16))
output_label.pack(pady=15)


# start the GUI
window.mainloop()

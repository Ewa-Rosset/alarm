from tkinter import *
import datetime
import time
from playsound import playsound
import webbrowser


# Alarm clock function

def alarm(setAlarm):
    while True:

        # need a time now so we can compare
        current_time = datetime.datetime.now()
        time = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%y")
        print(time)
        print(date)
        
        if time == setAlarm:
            print("Time to wake up!")
            #If song is on a computer
            #playsound(r"C:\Users\ewaro\Desktop\Random\Bittersweet.mp3")
            open()
            break
        
def open():
    return webbrowser.open('https://www.youtube.com/watch?v=argdA1u9CFw&ab_channel=Emigrate-Topic', new = 2)

def alarm_time():
    setAlarm = f"{hour.get()}:{minute.get()}"
    print(setAlarm)
    alarm(setAlarm)
    
    

#Initialising tkinter

clock = Tk()
clock.title("Alarm Clock by Ewa Rosset ")
clock.geometry("400x200")

time_format = Label(clock, text= "Enter time in 24 hour format!", fg="coral",bg="black",font="Verdana").place(x=80,y=5)
add_time = Label(clock,text = "Hour         Min",font=60).place(x=120,y=80)
set_alarm = Label(clock,text = "When to wake you up",fg="coral",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=50)

hour = StringVar()
minute = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "coral",width = 15).place(x = 120, y=50)
minTime= Entry(clock,textvariable = minute,bg = "coral",width = 10).place(x=180,y=50)

submit = Button(clock,text = "Set Alarm",fg="coral",width = 10,command = alarm_time).place(x =120,y=120)


clock.mainloop()




#Nathan Attoh - University of Ghana

from tkinter import *
from PIL import Image, ImageTk
import os
import datetime
import time
import winsound
import webbrowser

#current path of the code
currentpath = os.path.dirname(__file__)

#joins resource folder path to the current path
resourcefolder = os.path.join(currentpath, 'resources')

#relativepath of the github image we will need
#githubimage_path = "github.png"

#joins relative path to the resource folder
#gitimagefolder = os.path.join(currentpath, githubimage_path)


#alarm clock function that accepts parameter to be used to determine if its time yet
def alarmclock(alarm_set):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        
        if now == alarm_set:
            print("WAKE UP!!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

#takes input from the User interface and assigns it to a variable that gets passed on to the alarm clock function above
def actual_time():
    alarm_set = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarmclock(alarm_set)


#creates the user interface
clockui = Tk()

clockui.title("Plutus Alarm Clock V.2")
clockui.geometry("800x400")
clockui.configure(background="white")
clockui.resizable(0,0)

#function to exit the app
def closeclockui():
    clockui.destroy()

#variables to be used in the userinterface
hour = StringVar()
min = StringVar()
sec = StringVar()

#external git hub stuff
giturl = "https://www.github.com/attohx"

#github image logo for icon
#gitimage = Image.open("github.png")
#gitimage_resized = gitimage.resize((250,250))
#gitimage2 = ImageTk.PhotoImage(gitimage_resized)

#function to open a tab in the web browser towards github link
def openweb():
    webbrowser.open(giturl)

#labels to be printed out on the User Interface
time_format=Label(clockui, text = "Please Insert Your Time In The 24 Hour Format", fg="darkorchid1", font = "Arial").place(x = 250,y = 270)
addhr = Label(clockui, text=" Hour", font = 60 ).place(x = 266, y = 160)
addmin = Label(clockui, text=" Minutes", font = 60 ).place(x = 376, y = 160)
addsecs = Label(clockui, text=" Seconds", font = 60 ).place(x = 486, y = 160)

setTheAlarm = Label(clockui, text = "Input Time Below", fg = "darkorchid1", relief = "ridge", font = ("Arial", 16, "bold")).place(x = 320,y = 80)

#accepts user input on the user interface
hourTime = Entry(clockui, textvariable = hour, bg = "white", bd = 2 , width = 10,).place(x = 270,y = 200)
minTime = Entry(clockui, textvariable = min, bg = "white", bd = 2,  width = 10).place(x = 380, y = 200)
secTime = Entry(clockui, textvariable = sec, bg ="white",  bd = 2, width = 10).place(x = 490, y = 200)

#buttons of the user interface
submit = Button(clockui, text = "Activate Alarm", fg = "black", width = 20, pady = 5, font = ("Helvetica", "10", "bold"), command = actual_time).place(x = 330, y = 350)

githublink = Button(clockui, text = "Github", font = ("Helvetica", "10", "bold"), fg = "black", width = 10, pady = 5, command = openweb ).place(x = 650, y = 350)

closealarm = Button(clockui, text = "Exit App", fg = "black", width = 10, pady = 5, font = ("Helvetica", "10", "bold"), command = closeclockui ).place(x = 50, y = 350)


clockui.mainloop()
#Nathan Attoh - University of Ghana

from tkinter import *
from PIL import Image, ImageTk
import datetime
import time
import winsound
import webbrowser

terminator = ""
switch = ""
confirm_exit = ""

#alarm clock function that accepts parameter to be used to determine if its time yet
def alarmclock(alarm_set, confirm_exit):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        
        if now == alarm_set:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

        elif confirm_exit == "Yes":
            break

#function that takes input from the User interface and assigns it to a variable that gets passed on to the alarm clock function above
def actual_time():
    alarm_set = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarmclock(alarm_set)

#function to exit the app
def closeclockui():
    clockui.destroy()


#function to open a tab in the web browser towards github link
def openweb():
    webbrowser.open(giturl)


#creates the user interface
clockui = Tk()

clockui.title("Plutus Alarm Clock V.2")
clockui.geometry("800x400")
#clockui.iconbitmap(image="github.png")
clockui.resizable(0,0)

#external git hub stuff
giturl = "https://www.github.com/attohx"

#loads and resize github image logo for icon
gitimage = Image.open("github.png")
gitimage_resized = gitimage.resize((60,60))
gitimage2 = ImageTk.PhotoImage(gitimage_resized)

#canvas for the alarm clock
clockcanvas = Canvas(clockui, width = 800, height = 400, border = 0, highlightthickness = 0)
clockcanvas.pack(fill = "both", expand = True)

#loads background image
bgimage = PhotoImage(file= "bgimage.png")

#sets the background image for the clock
clockcanvas.create_image(0,0, image = bgimage, anchor = 'nw')

#creates labels or text in canvas, made this more optimized than placing them directly in the ui
clockcanvas.create_text(420,80, text="Insert Time Below In the 24 Hour Format", fill = "darkorchid1", font=("Arial", 16, "bold"))
clockcanvas.create_text(300,160, text="HOUR", fill = "white", font = ("Arial", 15,"bold"))
clockcanvas.create_text(420,160, text="MINUTES", fill = "white", font = ("Arial", 15,"bold"))
clockcanvas.create_text(550,160, text="SECONDS",fill = "white", font = ("Arial", 15,"bold"))

#define buttons for the canvas
submit = Button(clockui, text = "SET ALARM", fg = "black", width = 20, pady = 5, font = ("Helvetica", "10", "bold"), command = actual_time)
githublink = Button(clockui, text = "GITHUB", fg = "black", width = 10, pady = 5, font = ("Helvetica", "10", "bold"), command = openweb )
closealarm = Button(clockui, text = "EXIT", fg = "black", width = 10, pady = 5, font = ("Helvetica", "10", "bold"), command = closeclockui )
stopalarm = Button(clockui, text = "STOP", fg = "black", width = 10, pady = 5, font = ("Helvetica", "10", "bold"), command = terminator == "On" )

#creates visual or windows for buttons above... better than before imho
submit_window = clockcanvas.create_window(400,350, window = submit, anchor ="center")
githublink_window = clockcanvas.create_window(750,350, window = githublink)
closealarm_window = clockcanvas.create_window(50,350, window = closealarm)
stopalarm_window = clockcanvas.create_window(750, 300, window = stopalarm)

#variables to be used in the userinterface
hour = StringVar()
min = StringVar()
sec = StringVar()
placeholder = "00"

#defines the entry boxes for input on the user interface
hourTime = Entry(clockui, textvariable = hour, bg = "white", bd = 0, width = 15)
minTime = Entry(clockui, textvariable = min, bg = "white", bd = 0,  width = 15)
secTime = Entry(clockui, textvariable = sec, bg ="white",  bd = 0, width = 15)

#creates the windows for the entry boxes
hourtime_window = clockcanvas.create_window(300,200, window = hourTime )
minTime_window = clockcanvas.create_window(420,200, window = minTime)
secTime_window = clockcanvas.create_window(550,200, window = secTime)

#creates the placeholder text for the entry boxes
hourTime.insert(0, placeholder)
minTime.insert(0, placeholder)
secTime.insert(0, placeholder)

clockui.mainloop()
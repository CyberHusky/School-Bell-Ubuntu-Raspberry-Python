import sys

if sys.version_info[0] == 3:
    # for Python3
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import *  ## notice lowercase 't' in tkinter here
	# from filedialog import askopenfilename
else:
    # for Python2
    import Tkinter as tk
    from Tkinter import *  ## notice capitalized T in Tkinter
    from tkFileDialog import askopenfilename

# import Tkinter as tk
import time
import os

# from Tkinter 	  import *
from playsound import playsound
from PIL import Image
from time import gmtime, strftime, localtime, strptime
# from tkFileDialog import askopenfilename

# ApiKey
import csv
import codecs
import requests
import urllib.request
import urllib.error



import requests
import pprint
from requests.structures import CaseInsensitiveDict

url = "https://api.ukrainealarm.com/api/v3/alerts"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["Authorization"] = "086c31f0:fab40d26ccec9c6deaa47265b753fdc5"

resp = requests.get(url, headers=headers)
data = resp.json()

#print(data["regionId"])

for i in data:
    print(i.items())
    if i.keys() == 'regionId':
        print(i.values())

#print(resp.json())


'''

# ================ WELCOME ====================

begin_ms = "Welcome to School bell app. This app will help you to automatizate your school bell. \n What you need?\n-PC with Ubuntu;\n-Installed Python 3.\nAuthor of app: Gordieiev Artem (gordieiev.artem@gmail.com). V1.2. \n\n"
print(begin_ms)

# ================ SETUP ====================

fields = ['Lesson 1:', 'Lesson 2:', 'Lesson 3:', 'Lesson 4:', 'Lesson 5:', 'Lesson 6:', 'Lesson 7:', 'Lesson 8:',
          'Lesson 9:', 'Lesson 10:', 'Lesson 11:']
len(fields)

global times_bell, times_bell_sec

# === Times for bell ===
times_bell = ['08:30:00', '09:05:00', '09:15:00', '10:00:00', '10:10:00', '10:55:00', '11:10:00', '11:55:00',
              '12:15:00', '13:00:00',
              '13:45:00', '14:30:00', '14:40:00', '15:25:00', '15:35:00', '16:20:00', '16:40:00', '17:25:00',
              '17:35:00', '18:20:00', '18:30:00', '19:00:00']



# Make array with bell times in seconds
times_bell_sec = []
for i in range(0, len(times_bell)):
    bell_time = time.strptime(times_bell[i], '%H:%M:%S')
    times_bell_sec.append(bell_time.tm_hour * 3600 + bell_time.tm_min * 60 + bell_time.tm_sec)

# === Music setup ===
global default_music
default_music = os.getcwd() + "/sound.mp3"


# === for RaspberryPi ==
# --- Add full music file way. Make comment on default_music value before!
# default_music = "/home/pi/Desktop/School-Bell-master/sound.mp3" 
# --- RaspberryPi work only with preinstalled player, like VLC. Make comment on playsound() func value above and add this thing to 'MUSIC PLAY' block!
# os.system("vlc --play-and-exit "+"/home/pi/Desktop/School-Bell-master/sound.mp3")
# --- Sleeptimer. It need for start a GUI of OS and only after that we could make Tkinker stuff to start GUI of our programm. 
# time.sleep(40)

# YOU SHOULD CHOOSE FILE WITHOUT SPACES IN NAME!!!
# playsound("/home/artem/PycharmProjects/SchoolBell/sound.mp3") # Play sound

# ====================================


# === BUTTON FUNCTIONS ===

# Button play music again
def playagain():
    playsound(default_music)


# === FUNCTIONS ===

def time2sec(time_arg):
    timeis = time.strptime(time_arg, '%H:%M:%S')
    timeinsec = timeis.tm_hour * 3600 + timeis.tm_min * 60 + timeis.tm_sec
    return timeinsec


# === Clock function + play music
def tick():
    global time1
    global default_music
    global times_bell, times_bell_sec
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        lable_clock.config(text=time2)
        # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    lable_clock.after(200, tick)

    # === Timer
    localtime = time.localtime()
    localtime_sec = time2sec("{0}:{1}:{2}".format(localtime.tm_hour, localtime.tm_min, localtime.tm_sec))

    if (localtime_sec < times_bell_sec[0]) or (localtime_sec > times_bell_sec[-1]):
        lable_belltime.config(text="END OF LESSONS!!!")
    else:
        for i in range(0, len(times_bell_sec) - 1):
            if (localtime_sec >= times_bell_sec[i]) and (localtime_sec <= times_bell_sec[i + 1]):
                sec = times_bell_sec[i + 1] - localtime_sec
                s = sec % 60
                m = int(sec / 60)
                lable_belltime.config(text="{0}:{1}".format(m, s))

    # === MUSIC PLAY
    for i in range(0, len(times_bell)):
        if (time2 == times_bell[i]) or (time2 == times_bell[i]):
            playsound(default_music)


# === END of Clock function


# Open file 
def file_open():
    global default_music
    default_music = askopenfilename()
    entry_file.insert(END, default_music)
    print(default_music)


if __name__ == '__main__':

    # global default_music # directory of music file

    # === Window ===
    window = tk.Tk()
    window.title('SchoolBell. V1.0a')
    window.resizable(0, 0)
    # window.geometry('500x200')

    time1 = ''

    # === Labels ===
    # Make labels with lesson numbers
    for i in range(0, len(fields)):
        Label(window, text=fields[i], font=("Ubuntu", 8)).grid(row=i + 1)

    # Make lessons time labels
    count = 0
    for i in range(0, len(times_bell), 2):
        Label(window, text=times_bell[i][0:5], background="lightblue", width=10, font=("Ubuntu", 8)).grid(row=count + 1,
                                                                                                          column=1)
        Label(window, text=times_bell[i + 1][0:5], background="lightblue", width=10, font=("Ubuntu", 8)).grid(
            row=count + 1, column=2)
        count += 1

    # Make lables with Begin and End word
    Label(window, text="Begin:", font=("Ubuntu", 8)).grid(row=0, column=1)
    Label(window, text="End:", font=("Ubuntu", 8)).grid(row=0, column=2)

    # Make label for Time now
    Label(window, text="TIME NOW:", font=("Ubuntu", 14)).grid(row=2, column=3)
    lable_clock = Label(window, background="#F23A3A", font=("Ubuntu", 14))
    lable_clock.grid(row=3, column=3)

    Label(window, text="TIME TO BELL:", font=("Ubuntu", 14)).grid(row=4, column=3)
    lable_belltime = Label(window, background="#F23A3A")
    lable_belltime.grid(row=5, column=3)
    lable_belltime.config(text="???")

    tick()

    # === FILE buttons + entry + play again
    button_file = Button(window, font=("Ubuntu", 8),
                         text="FILE...",
                         command=file_open)
    button_file.grid(row=count + 1, column=0)

    entry_file = Entry(window)
    entry_file.grid(row=count + 1, column=1, columnspan=2)
    entry_file.insert(END, default_music)

    tk.Button(window,
              text="Play again...", font=("Ubuntu", 8),
              command=playagain).grid(row=count + 1, column=3)

    # === Bell LOGO ===

    bell_photo = PhotoImage(file="Photo_logo.png")

    label_logo = Label(image=bell_photo)
    label_logo.image = bell_photo
    label_logo.grid(row=1, column=5, columnspan=2, rowspan=7)

    window.mainloop()

'''


# === TRASH ===

'''
times_bell = ['08:30:00','09:05:00','09:15:00', '10:00:00', '10:20:00', '11:05:00', '11:25:00', '12:10:00', '12:30:00', '13:15:00',
			  '14:15:00', '15:00:00', '15:15:00', '16:00:00', '16:30:00', '17:15:00', '17:30:00', '18:15:00', '18:30:00', '19:00:00']
'''
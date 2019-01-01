import Tkinter as tk
import time
import os
# Tkinter import Separator, Style
#from Tkinter import *
from Tkinter 	  import *
from playsound    import playsound
from PIL 		  import Image
from time 		  import gmtime, strftime
from tkFileDialog import askopenfilename 

# ====================================

begin_ms = "Welcome to School bell app. This app will help you to automatizate your school bell. \n What you need?\n-PC with Ubuntu;\n-Installed Python 3.\nAuthor of app: Gordieiev Artem (gordieiev.artem@gmail.com). V1.0. \n\n"
print(begin_ms)

# ====================================

fields = ['Lesson 1:' , 'Lesson 2:', 'Lesson 3:', 'Lesson 4:' , 'Lesson 5:' , 'Lesson 6:']
len(fields)

global mute_logo_visible
times_from  = ['09:15:00' , '10:10:00' , '11:20:00' , '12:15:00' , '14:00:00' , '15:00:00']
times_to	= ['10:10:00' , '10:55:00' , '12:05:00' , '13:00:00' , '14:45:00' , '15:45:00']


global default_music 
default_music = os.getcwd() + "/sound.mp3"
#print os.getcwd()
#print default_music
# playsound("/home/artem/PycharmProjects/SchoolBell/sound.mp3") # Play sound


def buttonMute():
	global mute_logo_visible

	if mute_logo_visible == True:
		mute_logo.grid_forget()
		mute_logo_visible = False
	else:
		mute_logo.grid(row=8, column=1, columnspan=1, rowspan=1, sticky="W")
		mute_logo_visible = True

def tick():
    global time1
    global default_music
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)
    #print time2
    for i in xrange(0, len(times_from)):
    	if (time2 == times_from[i]) or (time2 == times_to[i]):
    		playsound(default_music)

def file_open():
	global default_music
	default_music = askopenfilename()
	file_entry.insert(END, default_music)
	print default_music

if __name__ == '__main__':

	global default_music

	# === Window ===
	window = tk.Tk()
	window.title('SchoolBell. V1.0a')
	#window.geometry('500x200')

	time1 = ''
	time_bell1 = ''
	# === Labels ===
	for i in xrange(1, len(fields)):
		Label(window, text=fields[i-1]	  			  , font=("Ubuntu", 8)).grid(row=i)
		Label(window, text=times_from[i-1][0:5], background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=i, column=1)
		Label(window, text=times_to[i-1][0:5]  , background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=i, column=2)
		

	Label(window, text="From:", font=("Ubuntu", 8)).grid(row=0, column=1)
	Label(window, text="To:"  , font=("Ubuntu", 8)).grid(row=0, column=2)

	button_mute = tk.Button(window,
								text = "Mute", font=("Ubuntu", 8),
								command = buttonMute).grid(row=8, column=0)

	#tk.Separator(window,orient="vertical").grid(column=3, rowspan=7)

	#column = 3
	
	#localtime = time.asctime( time.localtime(time.time()) )
	#print "Local time is:", localtime.tm_year
	print "Local time is:", strftime("%X")

	file_entry = Entry(window)
	file_entry.grid(row=1, column=3)
	file_entry.insert(END, default_music)
	
	Label(window, text="TIME NOW:", font=("Ubuntu", 14)).grid(row=2, column=3)
	#time_now.configure(text = strftime("%X"))
	clock = Label(window, background="#F23A3A", font=("Ubuntu", 14))
	clock.grid(row=3, column=3)
	tick()
	


	
	Label(window, text = "TIME TO BELL:", font=("Ubuntu", 14)).grid(row=4, column=3)
	time_to_bell = Label(window, background="#F23A3A")
	time_to_bell.grid(row=5, column=3)
	time_to_bell.configure(text = "???")
	

	mute_photo = PhotoImage(file="volume-off-indicator.png")
	mute_logo = Label(image = mute_photo)
	mute_logo.image = mute_photo
	mute_logo.grid(row=8, column=1, columnspan=1, rowspan=1, sticky="W")
	mute_logo.grid_forget()
	mute_logo_visible = False
	
	#

	#column = 4
	button_file = Button(window, font=("Ubuntu", 8),
								 text = "FILE...",
								 command = file_open)
	button_file.grid(row=1, column=4)


	#column=5   BELL LOGO

	#bell_img = Image.open("bell-outline.png")
	bell_photo = PhotoImage(file="bell-outline.png")

	bell_logo = Label(image = bell_photo)
	bell_logo.image = bell_photo
	bell_logo.grid(row=1, column=5, columnspan=2, rowspan=3)


	window.mainloop()




	
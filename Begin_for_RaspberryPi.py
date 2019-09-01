import sys

if sys.version_info[0] == 3:
    # for Python3
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import *   ## notice lowercase 't' in tkinter here
    #from filedialog import askopenfilename 
else:
    # for Python2
    import Tkinter as tk
    from Tkinter import *   ## notice capitalized T in Tkinter
    from tkFileDialog import askopenfilename 

#import Tkinter as tk
import time
import os

#from Tkinter 	  import *
#from playsound    import playsound
from PIL 		  import Image
from time 		  import gmtime, strftime, localtime, strptime
#from tkFileDialog import askopenfilename 

time.sleep(40)

# ================ WELCOME ====================

begin_ms = "Welcome to School bell app. This app will help you to automatizate your school bell. \n What you need?\n-PC with Ubuntu;\n-Installed Python 3.\nAuthor of app: Gordieiev Artem (gordieiev.artem@gmail.com). V1.0. \n\n"
print(begin_ms)

# ================ SETUP ====================

fields = ['Lesson 1:' , 'Lesson 2:', 'Lesson 3:', 'Lesson 4:' , 'Lesson 5:' , 'Lesson 6:']
len(fields)

global times_bell, times_bell_sec

# === Times for bell ===
times_bell = ['09:15:00', '10:00:00', '10:10:00', '10:55:00', '11:20:00', '12:05:00',
			  '12:15:00', '13:00:00', '14:00:00', '14:45:00', '15:00:00', '15:45:00']
	# Make array with bell times in seconds
times_bell_sec=[]
for i in range(0, len(times_bell)):
	bell_time = time.strptime(times_bell[i],'%H:%M:%S')
	times_bell_sec.append(bell_time.tm_hour * 3600 + bell_time.tm_min * 60 + bell_time.tm_sec)

# === Music setup ===
global default_music 
default_music = "/home/pi/Desktop/School-Bell-master/sound.mp3"
# os.getcwd() + "/sound.mp3"
# YOU SHOULD CHOOSE FILE WITHOUT SPACES IN NAME!!!

#playsound("/home/pi/Desktop/School-Bell-master/sound.mp3") # Play sound
os.system("vlc --play-and-exit "+"/home/pi/Desktop/School-Bell-master/sound.mp3")

# ====================================


# === BUTTON FUNCTIONS ===

# Button play music again
def playagain():
#	playsound(default_music)
	os.system("vlc --play-and-exit "+"/home/pi/Desktop/School-Bell-master/sound.mp3")



# === FUNCTIONS ===

def time2sec(time_arg):
	timeis = time.strptime(time_arg,'%H:%M:%S')
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
    	lable_belltime.config(text = "END OF LESSONS!!!")
    else:
    	for i in range(0, len(times_bell_sec)-1):
    		if (localtime_sec >= times_bell_sec[i]) and (localtime_sec <= times_bell_sec[i+1]):
    			sec = times_bell_sec[i+1] - localtime_sec
    			s = sec % 60
    			m = int(sec / 60)
    			lable_belltime.config(text = "{0}:{1}".format(m, s) )

    # === MUSIC PLAY
    for i in range(0, len(times_bell)):
    	if (time2 == times_bell[i]) or (time2 == times_bell[i]):
    		#playsound(default_music)
		os.system("vlc --play-and-exit "+"/home/pi/Desktop/School-Bell-master/sound.mp3")
# === END of Clock function


# Open file 
def file_open():
	global default_music
	default_music = askopenfilename()
	entry_file.insert(END, default_music)
	print (default_music)

if __name__ == '__main__':

	#global default_music # directory of music file

	# === Window ===
	window = tk.Tk()
	window.title('SchoolBell. V1.0a')
	window.resizable(0, 0)
	#window.geometry('500x200')

	time1 = ''
	
	# === Labels ===
		# Make labels with lesson numbers
	for i in range(0, len(fields)):
		Label(window, text=fields[i], font=("Ubuntu", 8)).grid(row=i+1)
	
		# Make lessons time labels
	count = 0	
	for i in range(0, len(times_bell), 2):
		Label(window, text=times_bell[i][0:5]    , background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=count+1, column=1)
		Label(window, text=times_bell[i+1][0:5]  , background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=count+1, column=2)
		count += 1
		
		# Make lables with Begin and End word
	Label(window, text="Begin:", font=("Ubuntu", 8)).grid(row=0, column=1)
	Label(window, text="End:"  , font=("Ubuntu", 8)).grid(row=0, column=2)



		# Make label for Time now	
	Label(window, text="TIME NOW:", font=("Ubuntu", 14)).grid(row=2, column=3)
	lable_clock = Label(window, background="#F23A3A", font=("Ubuntu", 14))
	lable_clock.grid(row=3, column=3)
	
	

	
	Label(window, text = "TIME TO BELL:", font=("Ubuntu", 14)).grid(row=4, column=3)
	lable_belltime = Label(window, background="#F23A3A")
	lable_belltime.grid(row=5, column=3)
	lable_belltime.config(text = "???")

	tick()
	


	# === FILE buttons + entry + play again
	button_file = Button(window, font=("Ubuntu", 8),
								 text = "FILE...",
								 command = file_open)
	button_file.grid(row=7, column=0)

	entry_file = Entry(window)
	entry_file.grid(row=7, column=1, columnspan=2)
	entry_file.insert(END, default_music)

	tk.Button(window,
					text = "Play again...", font=("Ubuntu", 8),
					command = playagain).grid(row=7, column=3)


	# === Bell LOGO ===

	bell_photo = PhotoImage(file="/home/pi/Desktop/School-Bell-master/Photo_logo.png")

	label_logo = Label(image = bell_photo)
	label_logo.image = bell_photo
	label_logo.grid(row=1, column=5, columnspan=2, rowspan=7)






	window.mainloop()


# === TRASH ===

'''



	#from threading 	  import Timer
	


	mute_photo = PhotoImage(file="volume-off-indicator.png")
	mute_logo = Label(image = mute_photo)
	mute_logo.image = mute_photo
	mute_logo.grid(row=8, column=1, columnspan=1, rowspan=1, sticky="W")
	mute_logo.grid_forget()
	mute_logo_visible = False









    localtime = time.localtime()
    #time_bell_tick_t = time.strptime(times_bell[num_bell],'%H:%M:%S')
    print("num_bell: {0}".format(str(num_bell)))
    #m = time_bell_tick_t.tm_min - localtime.tm_min -1
    #h = time_bell_tick_t.tm_hour - localtime.tm_hour - 1
    #print("h: "+str(h) + ", m: " + str(m))
    begin_les = time.strptime(times_bell[0],'%H:%M:%S')
    #begin_les = begin_les.tm_hour
    end_les   = time.strptime(times_bell[-1],'%H:%M:%S')
    #end_les   = end_les.tm_hour

    #print("begin: {0}, end_les: {1}".format(begin_les, end_les))
    #print("local hour: {0}, local minutes: {1}, begin_les.tm_hour: {2}, end_les.tm_hour")
    #print("h: "+str(localtime.tm_hour) + ", m: " + str(begin_les))

    #print(str(begin_les) + " " + str(end_les))
    #print(localtime.tm_hour >= begin_les.tm_hour)
    #print(localtime.tm_hour <= end_les.tm_hour)
    #print(localtime.tm_min >= begin_les.tm_min)
    #print(localtime.tm_min <= end_les.tm_min)



#print(localtime.tm_hour >= begin_les.tm_hour)
    #print(localtime.tm_hour <= end_les.tm_hour)
    #print(localtime.tm_min >= begin_les.tm_min)
    #print(localtime.tm_min <= end_les.tm_min)

    if (( localtime.tm_hour >= begin_les.tm_hour ) and ( localtime.tm_hour <= end_les.tm_hour )):
    	print("we are in!")
    	try:
    		time_bell_tick_t = time.strptime(times_bell[num_lesson],'%H:%M:%S')
    		h = time_bell_tick_t.tm_hour - localtime.tm_hour
    		m = time_bell_tick_t.tm_min  - localtime.tm_min  - 1
    		s = 59 - localtime.tm_sec #- time_bell_tick_t.tm_sec
    	except:
    		print("except")

    	if num_lesson < len(times_bell):
    		time_to_bell.config(text = str(m) + ":" + str(s) )
    	else:
    		num_lesson = len(times_bell) # making stop to adding lessons
    		time_to_bell.config(text = "END OF LESSONS!!!")

    	#print("time to bell: {0}:{1}, h:{2}, m:{3}, s:{4} ".format(time_bell_tick_t.tm_hour, time_bell_tick_t.tm_min, h ,m, s))
    	#except:
    	#	h = -1
    	#	m = -1
    	#	num_lesson = 0
    	#	time_to_bell.config(text = "END OF LESSONS!!!")
    	if (h <= 0) or (m < 0):
    		num_lesson += 1

    else:
    	num_lesson = 0
    	time_to_bell.config(text = "END OF LESSONS!!!")







	
		Label(window, text=times_to[i][0:5]    , background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=i+1, column=1)
		Label(window, text=times_from[i][0:5]  , background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=i+1, column=2)

	global mute_logo_visible
	if mute_logo_visible == True:
		mute_logo.grid_forget()
		mute_logo_visible = False
	else:
		mute_logo.grid(row=8, column=1, columnspan=1, rowspan=1, sticky="W")
		mute_logo_visible = True
'''

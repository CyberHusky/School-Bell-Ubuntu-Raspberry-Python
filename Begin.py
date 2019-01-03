import Tkinter as tk
import time
import os
# Tkinter import Separator, Style
#from Tkinter import *
from Tkinter 	  import *
from playsound    import playsound
from PIL 		  import Image
from time 		  import gmtime, strftime, localtime, strptime
from tkFileDialog import askopenfilename 
from threading 	  import Timer

# ====================================

begin_ms = "Welcome to School bell app. This app will help you to automatizate your school bell. \n What you need?\n-PC with Ubuntu;\n-Installed Python 3.\nAuthor of app: Gordieiev Artem (gordieiev.artem@gmail.com). V1.0. \n\n"
print(begin_ms)

# ====================================

fields = ['Lesson 1:' , 'Lesson 2:', 'Lesson 3:', 'Lesson 4:' , 'Lesson 5:' , 'Lesson 6:']
len(fields)

global mute_logo_visible

global time_of_lesson, num_lesson, times_bell
global time_bell_tick, time_of_break, times_to, times_from, h, m
num_lesson = 0
h = -1
m = -1
#times_to   = ['09:15:00' , '10:10:00' , '11:20:00' , '12:15:00' , '14:00:00' , '15:00:00']
#times_from = ['10:00:00' , '10:55:00' , '12:05:00' , '13:00:00' , '14:45:00' , '19:35:00']
#times_bell = times_to + times_from
times_bell = ['09:15:00', '10:00:00', '10:10:00', '10:55:00', '11:20:00', '12:05:00',
			  '12:15:00', '13:00:00', '14:00:00', '14:45:00', '15:00:00', '15:45:00']

#print(times_bell)
time_of_lesson = 45 * 60 #seconds of lesson
time_of_break  = 10 * 60 #seconds of break
time_bell_tick = time_of_lesson

global default_music 
default_music = os.getcwd() + "/sound.mp3"
#print os.getcwd()
#print default_music
# playsound("/home/artem/PycharmProjects/SchoolBell/sound.mp3") # Play sound

# Button for mute sound - NOT WORKING NOW!!!
def playagain():
	playsound(default_music)


# Clock and start music function
def tick():
    global time1
    global time_bell_tick, time_of_break
    global default_music
    global time_of_lesson
    #global times_to, times_from
    global num_lesson, times_bell, h, m
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
	
	# === Timer
    localtime = time.localtime()
    #time_bell_tick_t = time.strptime(times_bell[num_lesson],'%H:%M:%S')
    print("num_lesson: {0}".format(str(num_lesson)))
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
    print(localtime.tm_hour >= begin_les.tm_hour)
    print(localtime.tm_hour <= end_les.tm_hour)
    print(localtime.tm_min >= begin_les.tm_min)
    print(localtime.tm_min <= end_les.tm_min)

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
    	if (h < 0) or (m < 0):
    		num_lesson += 1

    else:
    	num_lesson = 0
    	time_to_bell.config(text = "END OF LESSONS!!!")

    # === MUSIC PLAY
    for i in xrange(0, len(times_bell)):
    	if (time2 == times_bell[i]) or (time2 == times_bell[i]):
    		playsound(default_music)

'''
    if (num_lesson > len(times_bell)):
    	time_to_bell.config(text = "END OF LESSONS!!!")
    	num_lesson = 0
    elif (h < 0):
    	num_lesson += 1
    	localtime = time.localtime()
    	time_bell_tick_t = time.strptime(times_bell[num_lesson],'%H:%M:%S')
    	m = time_bell_tick_t.tm_min - localtime.tm_min - 1
    	h = time_bell_tick_t.tm_hour - localtime.tm_hour 
    	s = 59 - localtime.tm_sec #- time_bell_tick_t.tm_sec
    	#time_to_bell.config(text = str(m) + ":" + str(s) )
    	if (m < 0):
    		num_lesson += 1
    		localtime = time.localtime()
    		time_bell_tick_t = time.strptime(times_bell[num_lesson],'%H:%M:%S')
    		m = time_bell_tick_t.tm_min - localtime.tm_min - 1
    		h = time_bell_tick_t.tm_hour - localtime.tm_hour - 1
    		s = 59 - localtime.tm_sec #- time_bell_tick_t.tm_sec
    	else:
    		time_to_bell.config(text = str(m) + ":" + str(s) )
'''    
    	


    		

def bell():
	time_to_bell.after(1000, bell)
	global time_bell_tick
	#time_bell_tick -= 1
	#m = time_bell_tick // 60
	#s = time_bell_tick-m*60
	#time_to_bell.config(text = str(m) + ":" + str(s) )
    


def timeout():
	print("BELLING")
	time_to_bell.config(text = "???")

# Open file 
def file_open():
	global default_music
	default_music = askopenfilename()
	file_entry.insert(END, default_music)
	print default_music

if __name__ == '__main__':

	global default_music # directory of file
	global time_bell_tick

	# === Window ===
	window = tk.Tk()
	window.title('SchoolBell. V1.0a')
	window.resizable(0, 0)
	#window.geometry('500x200')

	time1 = ''
	time_bell_tick = time_of_lesson
	
	# === Labels ===
	for i in xrange(0, len(fields)):
		Label(window, text=fields[i]	  	   , font=("Ubuntu", 8)).grid(row=i+1)
	
	count = 0	
	for i in range(0, len(times_bell), 2):
		Label(window, text=times_bell[i][0:5]    , background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=count+1, column=1)
		Label(window, text=times_bell[i+1][0:5]  , background="lightblue", width = 10, font=("Ubuntu", 8)).grid(row=count+1, column=2)
		count += 1
		#print(times_bell[i][0:5], count)

	Label(window, text="Begin:", font=("Ubuntu", 8)).grid(row=0, column=1)
	Label(window, text="End:"  , font=("Ubuntu", 8)).grid(row=0, column=2)

	button_mute = tk.Button(window,
								text = "Play again...", font=("Ubuntu", 8),
								command = playagain).grid(row=8, column=3)

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
	
	

	
	Label(window, text = "TIME TO BELL:", font=("Ubuntu", 14)).grid(row=4, column=3)
	time_to_bell = Label(window, background="#F23A3A")
	time_to_bell.grid(row=5, column=3)
	time_to_bell.config(text = "???")

	tick()
	bell()

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
	bell_photo = PhotoImage(file="Photo_logo.png")

	bell_logo = Label(image = bell_photo)
	bell_logo.image = bell_photo
	bell_logo.grid(row=1, column=5, columnspan=2, rowspan=7)






	window.mainloop()


# === TRASH ===

'''

	
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

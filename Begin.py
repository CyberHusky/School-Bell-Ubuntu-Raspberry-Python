import Tkinter as tk
#from Tkinter import *
from playsound import playsound

# ====================================

begin_ms = "Welcome to School bell app. This app will help you to automatizate your school bell. \n What you need?\n-PC with Ubuntu;\n-Installed Python 3.\nAuthor of app: Gordieiev Artem (gordieiev.artem@gmail.com). V1.0. \n\n"
print(begin_ms)

# ====================================

fields = ['Lesson 1:' , 'Lesson 2:', 'Lesson 3:', 'Lesson 4:' , 'Lesson 5:' , 'Lesson 6:']
len(fields)
#times_from  = [9:15]
#times_to	 = []

# playsound("/home/artem/PycharmProjects/SchoolBell/sound.mp3") # Play sound



if __name__ == '__main__':

	window = tk.Tk()
	window.title('SchoolBell. V1.0')

	# === Labels ===
	for i in range(1, len(fields)):
		tk.Label(window, text=fields[i-1]).grid(row=i)
		tk.Entry(window, state='readonly').grid(row=i, column=1)
		tk.Entry(window, state='readonly').grid(row=i, column=2)

	tk.Label(window, text="From:").grid(row=0, column=1)
	tk.Label(window, text="To:").grid(row=0, column=2)

	button1 = tk.Button(window,
								text = "Mute").grid(row=8)

	#column = 3
	tk.Entry(window, state='readonly').grid(row=1, column=3)
	tk.Label(window, text="TIME NOW:").grid(row=2, column=3)
	tk.Entry(window, state='readonly').grid(row=3, column=3)
	tk.Label(window, text="TIME TO BELL:").grid(row=4, column=3)

	#column = 4
	button2 = tk.Button(window,
								text = "FILE...").grid(row=1, column=4)

	#column=5    LOGO
	logo = tk.PhotoImage(file="bell-outline.png")
	tk.Label(window, 
					image = logo).grid(row=1, column=5, columnspan=2, rowspan=3, sticky="W"+"E"+"N"+"S")
	#

	window.mainloop()
'''
	

	

	tk.Label(window, 
					text = "Hello2!",
					fg 	 = "red").pack(side="left")
	
	button1 = tk.Button(window,
					text = "Button1").pack()

'''

	
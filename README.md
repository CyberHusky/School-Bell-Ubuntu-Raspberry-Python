# SchoolBell

School bell in Python (with GUI - Tkinter) that can play mp3 music at the time and have GUI with timer. Also in program added air alert signal detecting in Ukraine. The program was tested in Ubuntu and IOS. 
If you make Windows installer (or EXE) it would be helpful for me!

Tested on Python version: 3.10.7

## Features

What Schoolbell program can do:
- Show current time;
- Show time for nearest bell;
- Play music on the chosen time (you could change time only in .py file, not in executable file);
- Play music when you need – tap on button (default: sound.mp3);
- Detecting air alert region in Ukraine and show it in GUI.
- Play music when air alert is in your region (default: Air_alert.mp3, default region: Kyiv)

Setup in source file:
- You could set up time for bell in your school. Program automatically should to adapts to your setup;
- You could set up logo of your school;
- You could set up a number of lessons;
- You could set up your region for air alert.

![GitHub Logo](/program_gif2.gif)

## Getting Started

Preinstall next stuff (most of this libraries are installed in Python 3.10):
```
sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
```

For develop, use next libraries (I recommended install with pip3 on Python 3.6 or above):
```
sudo apt-get install python3-tk tk-dev
pip3 install --user pillow
pip3 install --user Image
pip3 install --user playsound
```

For make an executable file use:
```
pip3 install pyinstaller
```
make executible file with next command:
```
python3 -m PyInstaller --onefile <your_script_name>.py
```

If you need to change num of lesson you should change "time_bell" value block in source file.

## Air alert and API

If you need working air alert signal in Ukraine you need to visite next site and ask creators for API key:
https://api.ukrainealarm.com/

After you take an API you need to copy it into next section of code:

```
headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["Authorization"] = "YOUR API"
```

...where "YOUR API" is given key to you before. 

Also you need to enter your region of Ukraine into next variable:

```
my_region = '31'  # Kyiv is 31
```

Read tutorial for details from your email, when you recieve the API key from creators.

## RaspberryPi 

In RaspberryPi I was use pure python execution with script in "launcher.sh" file. For auto launch I was use "crontab -e" command in terminal with next code in the end of the file:
```
@reboot DISPLAY=:0 sh /home/pi/Desktop/School-Bell-master/launcher.sh >/home/pi/Desktop/School-Bell-master/logs/cronlog  2>&1
```

Note that you should uncomment block "for RaspberryPi" in source code and comment other part of code (read source code for details). Furthermore, I added sleep timer before start the program, so if you want to try program (not in autostart of OS) you should wait 40 sec or just comment that code for a while.

## RTC to RaspberryPi

* install first:
```
sudo apt-get install i2c-tools
```
* Add device to the system:
```
sudo nano /boot/config.txt
```
Add line:
```
dtoverlay=i2c-rtc,ds1307
```
* Add module:
```
sudo nano /etc/modules
```
Add line: 
```
snd-bcm2835
i2c-bcm2835
i2c-dev
rtc-ds3231
```
* Then make detect the device:
```
sudo i2cdetect -y 0  # (if using v1 Raspberry Pi or)
sudo i2cdetect -y 1  # (if using v2 Raspberry Pi) - it was usefull for me
```
* Synchronize device. Open:
```
sudo nano /etc/rc.local
```
Add the following two lines before the "exit 0" line :
```
echo ds3231 0x68 > /sys/class/i2c-adapter/i2c-1/new_device 
hwclock -s
```

* Time Zones. Maybe you need to change timezone. You can do it with next command:
```
sudo raspi-config
```
and then select “Internationalization Options” followed by “Change Timezone”.


Troubleshooting.

Sometimes RaspberryPi doesn't on I2C interface. So open file /boot/config.txt and add or uncomment next line:
```
dtparam=i2c1=on (or dtparam=i2c0=on on old models)
dtparam=i2c_arm=on
```

Main sites that you could use for help:

https://www.raspberrypi-spy.co.uk/2015/05/adding-a-ds3231-real-time-clock-to-the-raspberry-pi/
https://www.raspberrypi.org/forums/viewtopic.php?t=115080
https://www.raspberrypi.org/documentation/configuration/device-tree.md
https://raspberrypi.ru/blog/598.html
https://www.abelectronics.co.uk/kb/article/30/rtc-pi-on-a-raspberry-pi-raspbian-stretch





## Authors
Gordieiev Artem. For questions, you could write me on email: gordieiev.artem@gmail.com

It would be awesome if you help me to make this program better (make a different language, make a setup function in GUI).

For donation, you can use next channel:

PayPal: https://www.paypal.com/donate/?hosted_button_id=GYP25ZFAUWCTW 

Monobank: https://send.monobank.ua/jar/AdWGndoK6k



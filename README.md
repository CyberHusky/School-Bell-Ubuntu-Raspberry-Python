# SchoolBell

School bell in Python (with GUI - Tkinter + .grid) that can play mp3 music at the time and have GUI with timer. Execution file for Linux_x64 version is avaliable (tested only on Ubuntu 16.04). If you make Windows installer (or EXE) it would be helpful for me!

Tested on Python version: 2.7.12
On Pythond 3 sould work too. 

## Features

What Schoolbell program can do:
- Show current time;
- Show time for nearest bell;
- Play music on the chosen time (you could change time only in .py file, not in executable file);
- Play music when you need;
- You could choose music for play (default: sound.mp3).

Setup in source file:
- You could choose time for bell in your school. Program automatically should to adapts to your setup;
- You could choose logo of your school;
- You could choose number of lessons.

![GitHub Logo](/program_gif.gif)

## Getting Started

Preinstall next stuff:
```
apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
```

For develop use next libraries:
```
apt-get install python-tk python3-tk tk-dev
pip install --user pillow
pip3 install --user Image

```

For make an exe file use:
```
pip install pyinstaller
```
with command:
```
pyinstaller --onefile <your_script_name>.py
```

If you need to change num of lesson you should change "time_bell" value and "row" value in "FILE button + entry + play again" block in source file.

## RaspberryPi 

In RaspberryPi I was use pure python execution with script in "launcher.sh" file. For auto launch I was use "crontab -e" command in terminal with next code in the end of the file:
```
@reboot DISPLAY=:0 sh /home/pi/Desktop/School-Bell-master/launcher.sh >/home/pi/Desktop/School-Bell-master/logs/cronlog  2>&1
```

Note that you should uncomment block "for RaspberryPi" in source code and comment other part of code (read source code for details). Furthermore, I added sleep timer before start the program, so if you want try program (not in autostart of OS) you should wait 40 sec or just comment that code for awhile.

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
* Then make detect the divice:
```
sudo i2cdetect -y 0  # (if using v1 Raspberry Pi or)
sudo i2cdetect -y 1  # (if using v2 Raspberry Pi) - it was usefull for me
```
* Synchronise device. Open:
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
and then select “Internationalisation Options” followed by “Change Timezone”.


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
Gordieiev Artem. For questions you could write me on email: gordieiev.artem@gmail.com

It would be awesome if you help me to make this program better (make a different language, make a setup function in GUI).


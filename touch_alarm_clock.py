#By the grace of G-D
from tkinter  import *
import tkinter.font  as font
import time
#import datetime
import pygame
import os
import vlc

#   SET Customazations Here
FS = "False"     # Make App Fullscreen
FG = "green"   # Font Color
BG = "black"   # Background Color
HLBG = FG        # Button Border Color
STREAM1 = 'https://xxx'  #First Radio Stream URL
STREAM2 = 'http://xxx'       #Second Radio Stream URL
CAM1 = 'rtsp://xxx'  #First Camera URL
CAM2 = 'http://xxx'        #Second Camera URL
ALARM1SOUND = 'sound1.wav'
ALARM2SOUND = 'sound2.wav'
#ALARM1SOUND = 'ChiribimChiribom.wav'
#ALARM2SOUND = 'TimmyTime1.wav'
# End Customazations

time1 = ''
alarm1Armed = "no"
alarm2Armed = "no"
alarm1Init = 0
alarm2Init = 0

root = Tk()
root.configure(width = 480,  height=300, bg=BG)
root.title("Alarm Clock")
root.attributes("-fullscreen", FS)
buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

Grid.rowconfigure(root,  0, weight=1)
Grid.rowconfigure(root,  1,  weight=1)
Grid.rowconfigure(root,  2,  weight=1)
Grid.rowconfigure(root,  3,  weight=1)
Grid.columnconfigure(root,  0,  weight=1)
Grid.columnconfigure(root,  1,  weight=1)
Grid.columnconfigure(root,  2,  weight=1)
Grid.columnconfigure(root, 3 ,  weight=1)

clock = Label(root, width=7,  font=('LCDMono', 120), fg=FG,  bg=BG)
strDate = Label(root, width=20,  font=('LCDMono', 40, 'bold'), fg=FG,  bg=BG)
clock.grid(row=0,  column=0,  columnspan=4)
strDate.grid(row=1,  column=0,  columnspan=4)
alarm1ButtonToggle ="true"
alarm2ButtonToggle ="true"
radioButton1Toggle =""
radioButton2Toggle =""
enterAlarm1PMToggle =""
enterAlarm2PMToggle =""

pygame.mixer.init()


def setAlarm1():
    top = Toplevel()
    top.configure(width = 480,  height=300, bg=BG)
    top.attributes("-fullscreen", FS) 
    Grid.rowconfigure(top,  0, weight=1)
    Grid.rowconfigure(top,  1,  weight=1)
    Grid.rowconfigure(top,  2,  weight=1)
    Grid.rowconfigure(top,  3,  weight=1)
    Grid.columnconfigure(top,  0,  weight=1)
    Grid.columnconfigure(top,  1,  weight=1)
    Grid.columnconfigure(top,  2,  weight=1)
    Grid.columnconfigure(top, 3 ,  weight=1)
    Grid.columnconfigure(top, 4 ,  weight=1)
    
    def button_click(number):
        
        current = timeEntry.get()
        timeEntry.delete(0,  END)
        timeEntry.insert(0,  str(current) + str(number))
        
    
    def enterAlarm1():
        global enterAlarm1PMToggle
        a = str(timeEntry.get())
        if len(a) < 5:
            print ('a ' + a)
            if int(a) < 1200:
                if enterAlarm1PMToggle:
                    a = int(a) + 1200
                    print('alarm set ' +  str(a))
            if int(a) < 2400:
                b =(str(a).zfill(4))
                print ('b ' + b)
                if  int(b[2] )< 6:
                    print("c " + b[2])
                    button_3['text'] = b
                    enterAlarm1PMToggle =""
                    button_PM1.configure (bg = BG,  fg = FG)
                    top.destroy()
                else:
                    enterAlarm1PMToggle =""
                    button_PM1.configure (bg = BG,  fg = FG)
                    timeEntry.delete(0,  END)
            else:
                enterAlarm1PMToggle =""
                button_PM1.configure (bg = BG,  fg = FG)
                timeEntry.delete(0,  END)
        else:
            enterAlarm1PMToggle =""
            button_PM1.configure (bg = BG,  fg = FG)
            timeEntry.delete(0,  END)       
                
    def enterAlarm1PM():
        global enterAlarm1PMToggle
        enterAlarm1PMToggle = not enterAlarm1PMToggle  
        if enterAlarm1PMToggle:
            button_PM1.configure (bg = FG,  fg = BG)
        else:
            button_PM1.configure (bg = BG,  fg = FG)
    
    
            
   
    timeEntry = Entry(top, width=20, font=buttonFont, fg=FG,  bg=BG)
    #timeEntry.insert(0,  "Set Alrm time")
    timeEntry.grid(row=0,  column=0,  columnspan=3,  sticky = "nsew")
    #Set Alarm buttons
    button_enter1 = Button(top, borderwidth=3, font=buttonFont, padx=10,  pady=10, fg =FG,  bg = BG, text="Enter",  command=enterAlarm1)
    button_PM1 = Button(top, borderwidth=3, font=buttonFont, padx=10,  pady=10, fg =FG,  bg = BG, text="PM",  command=enterAlarm1PM)
    button_01 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="1",  command= lambda: button_click(1))
    button_02 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="2",  command= lambda: button_click(2))
    button_03 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="3",  command= lambda: button_click(3))
    button_04 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="4",  command= lambda: button_click(4))
    button_05 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="5",  command= lambda: button_click(5))
    button_06 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="6",  command= lambda: button_click(6))
    button_07 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="7",  command= lambda: button_click(7))
    button_08 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="8",  command= lambda: button_click(8))
    button_09 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="9",  command= lambda: button_click(9))
    button_00 = Button(top, borderwidth=3, font=buttonFont, padx=20,  pady=20, fg =FG,  bg = BG, text="0",  command= lambda: button_click(0))
    
    button_PM1.grid(row=0,  column=3,  sticky = "nsew")
    button_enter1.grid(row=0,  column=4,  sticky = "nsew")
    button_01.grid(row=2,  column=0,  sticky = "nsew")
    button_02.grid(row=2,   column=1,  sticky = "nsew")
    button_03.grid(row=2,  column=2,  sticky = "nsew")
    button_04.grid(row=2,  column=3,  sticky = "nsew")
    button_05.grid(row=2,  column=4,  sticky = "nsew")
    button_06.grid(row=3,  column=0,  sticky = "nsew")
    button_07.grid(row=3,  column=1,  sticky = "nsew")
    button_08.grid(row=3,  column=2,  sticky = "nsew")
    button_09.grid(row=3,  column=3,  sticky = "nsew")
    button_00.grid(row=3,  column=4,  sticky = "nsew")

    
def setAlarm2():
    top = Toplevel()
    top.configure(width = 480,  height=300, bg=BG)
    top.attributes("-fullscreen", FS) 
    Grid.rowconfigure(top,  0, weight=1)
    Grid.rowconfigure(top,  1,  weight=1)
    Grid.rowconfigure(top,  2,  weight=1)
    Grid.rowconfigure(top,  3,  weight=1)
    Grid.columnconfigure(top,  0,  weight=1)
    Grid.columnconfigure(top,  1,  weight=1)
    Grid.columnconfigure(top,  2,  weight=1)
    Grid.columnconfigure(top, 3 ,  weight=1)
    Grid.columnconfigure(top, 4 ,  weight=1)
    
    def button_click(number):
        
        current = timeEntry.get()
        timeEntry.delete(0,  END)
        timeEntry.insert(0,  str(current) + str(number))
        
    def enterAlarm2():
        global enterAlarm2PMToggle
        a = str(timeEntry.get())
        if len(a) < 5:
            print ('a ' + a)
            if int(a) < 1200:
                if enterAlarm2PMToggle:
                    a = int(a) + 1200
                    print('alarm set ' +  str(a))
            if int(a) < 2400:
                b =(str(a).zfill(4))
                print ('b ' + b)
                if  int(b[2] )< 6:
                    print("c " + b[2])
                    button_4['text'] = b
                    enterAlarm2PMToggle =""
                    button_PM2.configure (bg = BG,  fg = FG)
                    top.destroy()
                else:
                    enterAlarm2PMToggle =""
                    button_PM2.configure (bg = BG,  fg = FG)
                    timeEntry.delete(0,  END)
            else:
                enterAlarm2PMToggle =""
                button_PM2.configure (bg = BG,  fg = FG)
                timeEntry.delete(0,  END)
        else:
            enterAlarm2PMToggle =""
            button_PM2.configure (bg = BG,  fg = FG)
            timeEntry.delete(0,  END)       
                
    def enterAlarm2PM():
        global enterAlarm2PMToggle
        enterAlarm2PMToggle = not enterAlarm2PMToggle  
        if enterAlarm2PMToggle:
            button_PM2.configure (bg = FG,  fg = BG)
        else:
            button_PM2.configure (bg = BG,  fg = FG)
   
        
   
    timeEntry = Entry(top, width=20, font=buttonFont, fg=FG,  bg=BG)
    timeEntry.grid(row=0,  column=0,  columnspan=3,  sticky = "nsew")
    #Set Alarm buttons
    button_enter2 = Button(top, borderwidth=3, font=buttonFont, padx=10, fg =FG,  bg = BG, pady=10,  text="Enter",  command=enterAlarm2)
    button_PM2 = Button(top, borderwidth=3, font=buttonFont,  padx=10, fg =FG,  bg = BG, pady=10,  text="PM",  command= enterAlarm2PM)
    button_01 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="1",  command= lambda: button_click(1))
    button_02 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="2",  command= lambda: button_click(2))
    button_03 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="3",  command= lambda: button_click(3))
    button_04 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="4",  command= lambda: button_click(4))
    button_05 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="5",  command= lambda: button_click(5))
    button_06 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="6",  command= lambda: button_click(6))
    button_07 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="7",  command= lambda: button_click(7))
    button_08 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="8",  command= lambda: button_click(8))
    button_09 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="9",  command= lambda: button_click(9))
    button_00 = Button(top, borderwidth=3, font=buttonFont, padx=20, fg =FG,  bg = BG, pady=20,  text="0",  command= lambda: button_click(0))
    
    button_PM2.grid(row=0,  column=3,  sticky = "nsew")
    button_enter2.grid(row=0,  column=4,  sticky = "nsew")
    button_01.grid(row=2,  column=0,  sticky = "nsew")
    button_02.grid(row=2,   column=1,  sticky = "nsew")
    button_03.grid(row=2,  column=2,  sticky = "nsew")
    button_04.grid(row=2,  column=3,  sticky = "nsew")
    button_05.grid(row=2,  column=4,  sticky = "nsew")
    button_06.grid(row=3,  column=0,  sticky = "nsew")
    button_07.grid(row=3,  column=1,  sticky = "nsew")
    button_08.grid(row=3,  column=2,  sticky = "nsew")
    button_09.grid(row=3,  column=3,  sticky = "nsew")
    button_00.grid(row=3,  column=4,  sticky = "nsew")

def armAlarm1():
    global alarm1ButtonToggle
    global alarm1Armed
    global alarm1Init
    
    if alarm1ButtonToggle:
        button_3.configure (bg = FG,  fg = BG)
        alarm1Armed = "yes"
    else:
        button_3.configure (bg = BG,  fg = FG)
        alarm1Armed = "no"
        pygame.mixer.music.stop()
    alarm1Init = 0  
    alarm1ButtonToggle = not alarm1ButtonToggle   
    
def armAlarm2():
    global alarm2ButtonToggle
    global alarm2Armed
    global alarm2Init
     
    if alarm2ButtonToggle:
        button_4.configure (bg = FG,  fg = BG)
        alarm2Armed = "yes"
    else:
        button_4.configure (bg = BG,  fg = FG)
        alarm2Armed = "no"
        pygame.mixer.music.stop()
    alarm2Init = 0  
    alarm2ButtonToggle = not alarm2ButtonToggle  

def playRadio1():  
    from subprocess import Popen
    global radioButton1Toggle
    radioButton1Toggle = not radioButton1Toggle 
    if radioButton1Toggle:
        button_7.configure (bg = FG,  fg = BG)
       # proc = Popen(['mplayer', ' -volume 20 ',  '%s', '1>/dev/null', '2>&1', STREAM1 ])
        proc = Popen('mplayer -volume 70 ' +  STREAM1 ,  shell=True)
    else:
        button_7.configure (bg = BG,  fg = FG)
        os.system("killall -9 mplayer")
        proc.kill()
     
    
def playRadio2():  
    from subprocess import Popen
    global radioButton2Toggle
    radioButton2Toggle = not radioButton2Toggle    
    if radioButton2Toggle:
        button_8.configure (bg = FG,  fg = BG)
        #proc = Popen(['mplayer', '%s', '1>/dev/null', '2>&1',SOUND])
        proc = Popen('mplayer -volume 70 ' +  STREAM2 ,  shell=True)
    else:
        button_8.configure (bg = BG,  fg = FG)
        os.system("killall -9 mplayer")
        proc.kill()
    
     
def cam1():
    player=vlc.MediaPlayer(CAM1)
    player.toggle_fullscreen() 
    player.play()
    time.sleep(15)
    player.stop()
       
def cam2():
 
    player=vlc.MediaPlayer(CAM2)
    player.toggle_fullscreen() 
    player.play()
    time.sleep(15)
    player.stop()
       

button_1 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,   fg =FG,  bg = BG,   padx=20,  pady=20,  text="Set Alarm 1",  command=setAlarm1)
button_2 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,  fg =FG,  bg = BG,  padx=20,  pady=20,  text="Set Alarm 2",  command=setAlarm2)
button_3 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,  fg =FG,  bg = BG,  padx=20,  pady=20,  text="Alarm 1 not set",  command=armAlarm1)
button_4 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,  fg =FG,  bg = BG,  padx=20,  pady=20,  text="Alarm 2 not set",  command=armAlarm2)
button_5 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,  fg =FG,  bg = BG,  padx=20,  pady=20,  text="Camera 1",  command=cam1)
button_6 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,  fg =FG,  bg = BG,  padx=20,  pady=20,  text="Camera 2",  command=cam2)
button_7 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,  fg =FG,  bg = BG,  padx=20,  pady=20,  text="Radio 1",  command=playRadio1)
button_8 = Button(root, borderwidth=3, font=buttonFont, highlightbackground = HLBG,  fg =FG,  bg = BG,  padx=20,  pady=20,  text="Radio 2",  command=playRadio2)

button_1.grid(row=2,  column=0,  sticky = "nsew")
button_2.grid(row=3,  column=0,  sticky = "nsew")
button_3.grid(row=2,  column=1,  sticky = "nsew")
button_4.grid(row=3,  column=1,  sticky = "nsew")
button_5.grid(row=2,  column=2,  sticky = "nsew")
button_6.grid(row=3,  column=2,  sticky = "nsew")
button_7.grid(row=2,  column=3,  sticky = "nsew")
button_8.grid(row=3,  column=3,  sticky = "nsew")


def playAlarm1():
    global alarm1Armed
    global alarm1Init
    print (alarm1Armed )
    alarm1Init=alarm1Init+1
    print("outer" + str(alarm1Init))
    if alarm1Init > 200:
       alarm1Init = 0
            
    if alarm1Armed == 'yes':
        if alarm1Init == 1:
           print("iiner" + str(alarm1Init))
           pygame.mixer.music.load(ALARM1SOUND)
           pygame.mixer.music.play(loops=0)
           pygame.mixer.music.set_volume(0.7)
    else:
        pygame.mixer.music.stop()
        alarm1Init = 0
        
def playAlarm2():
    global alarm2Armed
    global alarm2Init
    print (alarm2Armed )
    alarm2Init=alarm2Init+1
    print("outer" + str(alarm2Init))
    if alarm2Init > 200:
       alarm2Init = 0
            
    if alarm2Armed == 'yes':
        if alarm2Init == 1:
           print("iiner" + str(alarm2Init))
           pygame.mixer.music.load(ALARM2SOUND)
           pygame.mixer.music.play(loops=0)
           #pygame.mixer.music.set_volume(0.4)
    else:
        pygame.mixer.music.stop()
        alarm2Init = 0
        
    
def tick():
    global time1
    global strDate
    global days
    global dayNum
        
    # get the current local time from the PC
    time2 = time.strftime('%I:%M')
    time3 = time.strftime('%H%M')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        strDate.config(text=time.strftime("%A %m/%d/%Y"))        
        clock.config(text=time2)
    #strDate.config(text=time3)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
    #strDate.after(200, tick)
    aSET1 = button_3['text'] 
    aSET2 = button_4['text'] 
#    print(str(aSET1) + time3 )
   
    if str(aSET1) == time3:
        playAlarm1()
    if str(aSET2) == time3:
        playAlarm2()
       
tick()


root.mainloop()

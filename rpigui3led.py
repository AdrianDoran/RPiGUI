from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

redled = LED(17)
blueled = LED(27)
greenled = LED(22)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Event Process ##
def redLedToggle():
    if redled.is_lit:
        redled.off()
        redButton["text"] = "Turn Red LED on"
    else:
        redled.on()
        redButton["text"] = "Turn Red LED off"

def blueLedToggle():
    if blueled.is_lit:
        blueled.off()
        blueButton["text"] = "Turn Blue LED on"
    else:
        blueled.on()
        blueButton["text"] = "Turn Blue LED off"

def greenLedToggle():
    if greenled.is_lit:
        greenled.off()
        greenButton["text"] = "Turn Green LED on"
    else:
        greenled.on()
        greenButton["text"] = "Turn Green LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## Buttons ##
redButton = Button(win, text = 'Turn Red LED on', font = myFont, command = redLedToggle, bg = 'bisque2', height = 1, width = 24)
redButton.grid(row=0,column=1)
blueButton = Button(win, text = 'Turn Blue LED on', font = myFont, command = blueLedToggle, bg = 'bisque2', height = 1, width = 24)
blueButton.grid(row=1,column=1)
greenButton = Button(win, text = 'Turn Green LED on', font = myFont, command = greenLedToggle, bg = 'bisque2', height = 1, width = 24)
greenButton.grid(row=2,column=1)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close, bg = 'red', height = 1, width = 12)
exitButton.grid(row=4,column=1)

win.protocol("WM_DELETE_WINDOW", close) #clean Exit

win.mainloop() #Looper

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:46:35 2019

@author: joutras
"""

from Flag import Flag

from tkinter import *
import time
import datetime
from infi.systray import SysTrayIcon

running = False
programContinue = 1
popUpCount = 30

class PopUpWindow (object):
    windowCount = 0
    counter = -1
        
    def counterLabel(self, label):
        self.resetBtn['state'] = 'normal'
        self.stopBtn['state'] = 'normal'
        def count():
            if running:  
                # To manager the intial delay
                if PopUpWindow.counter == -1:
                    display="Starting..."
                else:
                    display=str(datetime.timedelta(seconds = PopUpWindow.counter))
                
                label.config(text=display)
                label.after(1000, count)
                PopUpWindow.counter += 1
        
        # Triggering the start of the counter.
        count()
        
    # Start the function of the stopwatch
    def Start(self):
        global running
        running = True
        self.counterLabel(self.timerLbl)
        self.breakBtn['state'] = 'disabled'
        self.stopBtn['state'] = 'normal'
        self.resetBtn['state'] = 'normal'
            
    # Stop function of the stopwatch
    def Stop(self):
        global running
        running = False
        self.breakBtn['state'] = 'normal'
        self.stopBtn['state'] = 'disabled'
        self.resetBtn['state'] = 'normal'
        
    # Reset function of the stopwatch
    def Reset(self):
        PopUpWindow.counter = -1
        
        # If reset is pressed after pressing stop
        if running == False:
            self.resetBtn['state'] = 'disabled'
            self.timerLbl['text'] = 'Welcome!'
            
        # If reset is pressed while hte stopwatch is running
        else:
            self.timerLbl['text'] = 'Starting ...'
            
    def getStatus():
        return programContinue
    
    def exitApp(self):
        Flag.setFlag(1)
        self.systray.shutdown()
        self.window.destroy()
        
    def closeWindow(self):
        PopUpWindow.windowCount = PopUpWindow.windowCount + 1
        self.window.destroy()
        
    def increasePopUpCount(self):
        global popUpCount
        popUpCount = popUpCount + 1
        self.popUpTimer.config(text = str(popUpCount) + " Minutes")
        
    def decreasePopUpCount(self):
        global popUpCount
        popUpCount = popUpCount - 1
        self.popUpTimer.config(text = str(popUpCount) + " Minutes")
        
    def getPopUpCount():
        global popUpCount
        return popUpCount
    
    def say_hello(systray):
        print ("Hello")
        
    def __init__ (self, time):
    
        # Create a blank window
        self.window = Tk()
        self.window.title("Break Timer")
        
        # Create a label widget
        lbl = Label(self.window, text = "The time is", font = ("Arial Bold", 20))
        lbl.grid(column = 0, row = 0)
        
        # Create a label to display the current time
        self.timeLbl = Label(self.window, text = time, font = ("Arial Bold", 20))
        self.timeLbl.grid(column = 0, row = 1)
        
        # Create a timer label
        if (PopUpWindow.counter == -1):
            self.timerLbl = Label(self.window, text = "00:00", font = ("Arial Bold", 20))
        else:
            self.timerLbl = Label(self.window, text = str(datetime.timedelta(seconds = PopUpWindow.counter)), font = ("Arial Bold", 20))
        self.timerLbl.grid(column = 1, row = 1)
        
        # Create a button to take a break
        self.breakBtn = Button(self.window, text = "Take a break", bg = "grey80", fg = "black", command = lambda:self.Start(), font = ("Arial",20))
        self.breakBtn.grid(column = 0, row = 2)
        
        # Create a reset timer button
        self.resetBtn = Button(self.window, text = "Reset timer", bg = "grey80", fg = "black", state = "disabled", command = lambda:self.Reset(), font = ("Arial",20))
        self.resetBtn.grid(column = 1, row=2)
        
        # Create a stop timer button
        self.stopBtn = Button(self.window, text = "Stop timer", bg = "grey80", fg = "black", state = "disabled", command = lambda:self.Stop(), font = ("Arial",20))
        self.stopBtn.grid(column = 2, row = 2)
        
        separator = Frame(height=30, bd=1, relief=SUNKEN)
        separator.grid(column = 0, row = 3)
        
        # Create a close button
        closeBtn = Button(self.window, text = "Close Window", bg = "grey80", fg = "black", command = lambda:self.closeWindow(), font = ("Arial",20))
        closeBtn.grid(column = 0, row = 4)
        
        separator2 = Frame(height=30, bd=1, relief=SUNKEN)
        separator2.grid(column = 0, row = 5)
        
        # Create a exit button
        exitBtn = Button(self.window, text = "Exit App", bg = "grey80", fg = "black", command = lambda:self.exitApp(), font = ("Arial", 20))
        exitBtn.grid(column = 0, row = 6)
        
        # Create a window count label
        counterLbl = Label(self.window, text = "Pop up count: " + str(PopUpWindow.windowCount), font = ("Arial Bold", 20))
        counterLbl.grid(column = 1, row = 0)
        
        # Create a label to display the amount of time until the pop-up indow pop ups
        self.popUpTimer = Label(self.window, text = str(popUpCount) + " Minutes", font = ("Arial Bold", 20))
        self.popUpTimer.grid(column = 2, row = 5)
        
        self.popUpTimerUpButton = Button(self.window, text = "+1", bg = "grey80", fg = "black", command = lambda:self.increasePopUpCount(), font = ("Arial Bold", 20), width = 3)
        self.popUpTimerUpButton.grid(column = 2, row = 4)
        
        self.popUpTimerDownButton = Button(self.window, text = "-1", bg = "grey80", fg = "black", command = lambda:self.decreasePopUpCount(), font = ("Arial Bold", 20), width = 3)
        self.popUpTimerDownButton.grid(column = 2, row = 6)

        # set the window size
        self.window.geometry('600x350')
        
        # Create a message box to display the current time
        #messagebox.showinfo("Current Time", time)
        
        # Bring the Window in front of every other window
        self.window.attributes("-topmost", True)
        
        # Create a system tray icon
        menu_options = (("Reset Timer", None, self.Reset),)
        self.systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
        self.systray.start()
                
        # Start the window
        self.window.mainloop()
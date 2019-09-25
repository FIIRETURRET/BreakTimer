# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:40:35 2019

@author: joutras
"""

from PopUpWindow import PopUpWindow
from Flag import Flag

import datetime
from tkinter import *
import time

from infi.systray import SysTrayIcon

@staticmethod
def createWindow():
    # Get current time
    currentDT = datetime.datetime.now()
    currentDT = currentDT.strftime("%H:%M")
    # Convert from military time
    hours, minutes = currentDT.split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours = hours - 12
    currentDT = str(hours) + ":" + str(minutes) + " " + setting
    window = PopUpWindow(currentDT) 
    
if __name__ == "__main__":
    menu_options = (("Pop Up Window", None, createWindow()),)
    systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
    systray.start()
    Flag.setFlag(0)
    while 0 == Flag.getFlag():
        createWindow()
        if Flag.getFlag() == 1:
            break
        print("See you in " + str(PopUpWindow.getPopUpCount()) + " minutes")
        time.sleep(PopUpWindow.getPopUpCount() * 60)
    print("GoodBye")
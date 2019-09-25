# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:34:38 2019

@author: joutras
"""

class Flag():
    flag = 0
    
    def __init__(self):
        Flag.flag = 0
        
    def setFlag(inputFlag):
        Flag.flag = inputFlag
        
    def getFlag():
        return Flag.flag
    
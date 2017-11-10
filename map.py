# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:07:15 2017

@author: e
"""
#there is a difference between an action and an order
#a unit can be taking an action
#an order just tells it what action to take
wmap = [] #the worldmap
units = [] #all the units
items = [] #all the items
cursx = 0
cursy = 0

def createmap(wmap, x, y, cell, mapscale = 1):
    for i in range(x):
        wmap.append([])
        for j in range(y):
            wmap[i].append(cell)
            
            
createmap(wmap, 10, 20, {"terraincost":0, "items":[], "terrainsymbol":"M"})

def printmap(map):
    printstring = ""
    for item in map:
        for jtem in item:
            printstring = printstring +jtem["terrainsymbol"]
        printstring = printstring + "\n"
    print(printstring)
    
class unit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.action = 1
        self.order = []
        self.actiondelay = 0
        
printmap(wmap)

def processorder(unit, order, a1, a2):
    if order == 0: #move
        unit.action= 0
        unit.actiondelay = int(.5*wmap[unit.x][unit.y]["terraincost"] + .5*wmap[a1][a2]["terraincost"])

def processaction(unit):
    if unit.order == []:
        unit.order.append([1])
    if not unit.actiondelay == 0:
        unit.actiondelay = unit.actiondelay -1
    else:
        if unit.action == 0:
            unit.x = unit.order[0][1]
            unit.y = unit.order[0][2]
            del unit.order[0]
            processorder(unit, unit.order[0][0], unit.order[0][1], unit.order[0][2])
        elif unit.action == 1:
            del unit.order[0]
            processorder(unit, unit.order[0][0], unit.order[0][1], unit.order[0][2])
        
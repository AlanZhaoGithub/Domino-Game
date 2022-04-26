# Author: Adrian Lam, Alan Zhao
# Date: 31 May 2017
# Purpose: simulate a domino game

# [Imports] ====================================================================

import random
from tkinter import *
import time
import os

# [Global variables] ===========================================================

window = Tk()
rectangle = ""
chosenDomino = -1
move = ""
playButton = Button (window, bg = "white", text = "Play", font = ("Arial",12,"bold"), command=lambda:dominoGame.play(canvas, 380, 295))
exitButton = Button (window, bg = "white", text = "exit", font = ("Arial",12,"bold"), command=lambda:os._exit(0))

# [Classes] ====================================================================

# [Domino] ---------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: a class for a domino
# Fields:
#   value: the value of the domino 
#   size: size of the domino 
#   radius: radius of the dots 
#   gap: gap of the dots
#   orientation: orientation of the domino
#   faceup: if the domino is facing up
#   colour: colour of the domino
#   borderColour: colour of the border of the domino
# Methods:
#   setFaceUp: sets whether the domino is drawn fac up or face down
#   getValue: gets the value of the domino from the user
#   setValue: sets the value of the domino to a valid value
#   flip: changes the value of the domino from XY to YX
#   setOrientation: sets the value of the domino's orientation
#   setSize: sets the value of the domino's size to a valid value
#   randomize: randomly sets the value of the domino to a new valid value
#   draw: draws the domino on a given canvas
#   setColour: sets the color of the domino
#   setBorderColour: sets the color of the border of the domino
# ------------------------------------------------------------------------------
class Domino:
    def __init__ (self, value = 0, size = 30, faceUp = True, colour = "white", borderColour = "black"):
        self.value = value
        self.size = size
        self.radius = self.size / 5
        self.gap = self.radius / 2
        self.orientation = "horizontal"
        self.faceUp = faceUp
        self.colour = colour
        self.borderColour = borderColour

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: returns the value of the domino as a string
# Input: /
# Ouput: the value of the domino as a string
# ------------------------------------------------------------------------------
    def __str__ (self):
        return str(self.value)

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 26 2017
# Purpose: adds the values of two dominoes
# Input: /
# Ouput: total value of the two dominoes
# ------------------------------------------------------------------------------
    def __add__ (self, domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        totalValue = domino1Value + domino2Value
        return totalValue

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: subtracts the values of two dominoes
# Input: /
# Ouput: difference between the two dominoes
# ------------------------------------------------------------------------------
    def __sub__ (self, domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        difference = abs(domino1Value - domino2Value)
        return difference

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: multiplies the values of two dominoes
# Input: /
# Ouput: product of the two dominoes
# ------------------------------------------------------------------------------
    def __mul__ (self,domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        product = domino1Value * domino2Value
        return product

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: returns true if the domino is greater than domino2
# Input: /
# Ouput: True or False
# ------------------------------------------------------------------------------
    def __gt__ (self,domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        if domino1Value > domino2Value:
            greaterThan = True
        else:
            greaterThan = False
        return greaterThan

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: returns true if the domino is greater than or equal to domino2
# Input: /
# Ouput: True or False
# ------------------------------------------------------------------------------
    def __ge__ (self,domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        if domino1Value > domino2Value or domino1Value == domino2Value:
            greaterOrEqual = True
        else:
            greaterOrEqual = False
        return greaterOrEqual

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: returns true if the domino is less than domino2
# Input: /
# Ouput: True or False
# ------------------------------------------------------------------------------
    def __lt__ (self,domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        if domino1Value < domino2Value:
            lessThan = True
        else:
            lessThan = False
        return lessThan

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: returns true if the domino is less than or equal to domino2
# Input: /
# Ouput: True or False
# ------------------------------------------------------------------------------
    def __le__ (self,domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        if domino1Value < domino2Value or domino1Value == domino2Value:
            lessOrEqual = True
        else:
            lessOrEqual = False
        return lessOrEqual

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: returns true if the domino is equal to domino2
# Input: /
# Ouput: True or False
# ------------------------------------------------------------------------------
    def __eq__ (self,domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        if domino1Value == domino2Value:
            equal = True
        else:
            equal = False
        return equal

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: returns true if the domino is not equal to domino2
# Input: /
# Ouput: True or False
# ------------------------------------------------------------------------------
    def __ne__ (self,domino2):
        domino1Value = calcAscendingValue (self)
        domino2Value = calcAscendingValue (domino2)
        if domino1Value != domino2Value:
            notEqual = True
        else:
            notEqual = False
        return notEqual

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: gets the value of the domino from the user
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------
    def getValue (self):
        blnOk = False
        while blnOk == False:
            value = input ("Please enter a valid value for you domino: ")
            if value.isdigit ():
                value = int (value)
                if value // 10 > 6 or value % 10 > 6:
                    print ("Neither digit can be greater than 6.")
                else:
                    self.value = value
                    blnOk = True

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: sets the value of the domino to a valid value
# Input: a value to set the domino to 
# Ouput: /
# ------------------------------------------------------------------------------
    def setValue (self, value = 0):
        if value // 10 <= 6 and value % 10 <= 6:
            self.value = value
        else:
            self.value = 0

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: changes the value of the domino from XY to YX
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------
    def flip (self):
        valueX = self.value // 10
        valueY = self.value % 10
        self.value = valueY * 10 + valueX
        
# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: sets the value of the domino's orientation
# Input: orientation
# Ouput: /
# ------------------------------------------------------------------------------
    def setOrientation (self, orientation):
        if orientation == 0:
            self.orientation = "horizontal"
        elif orientation == 1:
            self.orientation = "vertical"

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 31 May 2017
# Purpose: sets whether the domino is drawn fac up or face down
# Input: True or False
# Ouput: /
# ------------------------------------------------------------------------------
    def setFaceUp (self, blnFaceUp):
        if blnFaceUp == True:
            self.faceUp = True
        elif blnFaceUp == False:
            self.faceUp = False

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: sets the value of the domino's size
# Input: the size of the domino to set it to
# Ouput: /
# ------------------------------------------------------------------------------
    def setSize (self, size = 30):
        if size <= 50 and size >= 30:
            self.size = size

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: June 6 2017
# Purpose: sets the border colour of the domino
# Input: the border colour of the domino
# Ouput: /
# ------------------------------------------------------------------------------
    def setBorderColour (self, colour):
        self.borderColour = colour

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: June 6 2017
# Purpose: sets the colour of the domino
# Input: the colour of the domino
# Ouput: /
# ------------------------------------------------------------------------------
    def setColour (self, colour):
        self.colour = colour

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 4 2017
# Purpose: randomly sets the value of the domino to a new valid value
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------
    def randomize (self):
        value = 1000
        while value // 10 > 6 or value % 10 > 6:
            value = random.randint (0, 66)
        self.value = value

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 5 2017
# Purpose: draws the dots
# Input: value, x, y, colour
# Ouput: /
# ------------------------------------------------------------------------------
    def drawDots (self, canvas, value, x, y):
        if value == 1:
            canvas.create_oval (x + self.size / 5 * 2, y + self.size / 5 * 2, x + self.size / 5 * 3, y + self.size / 5 * 3, fill = self.borderColour)
        elif value == 2:
            if self.orientation == "horizontal":
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 1, x + self.size / 10 * 3, y + self.size / 10 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 7, x + self.size / 10 * 9, y + self.size / 10 * 9, fill = self.borderColour)
            else:
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 7, x + self.size / 10 * 3, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 1, x + self.size / 10 * 9, y + self.size / 10 * 3, fill = self.borderColour)
        elif value == 3:
            if self.orientation == "horizontal":
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 1, x + self.size / 10 * 3, y + self.size / 10 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 7, x + self.size / 10 * 9, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 5 * 2, y + self.size / 5 * 2, x + self.size / 5 * 3, y + self.size / 5 * 3, fill = self.borderColour)
            else:
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 7, x + self.size / 10 * 3, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 1, x + self.size / 10 * 9, y + self.size / 10 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 5 * 2, y + self.size / 5 * 2, x + self.size / 5 * 3, y + self.size / 5 * 3, fill = self.borderColour)
        elif value == 4:
            canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 1, x + self.size / 10 * 3, y + self.size / 10 * 3, fill = self.borderColour)
            canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 7, x + self.size / 10 * 3, y + self.size / 10 * 9, fill = self.borderColour)
            canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 7, x + self.size / 10 * 9, y + self.size / 10 * 9, fill = self.borderColour)
            canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 1, x + self.size / 10 * 9, y + self.size / 10 * 3, fill = self.borderColour)
        elif value == 5:
            canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 1, x + self.size / 10 * 3, y + self.size / 10 * 3, fill = self.borderColour)
            canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 7, x + self.size / 10 * 3, y + self.size / 10 * 9, fill = self.borderColour)
            canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 7, x + self.size / 10 * 9, y + self.size / 10 * 9, fill = self.borderColour)
            canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 1, x + self.size / 10 * 9, y + self.size / 10 * 3, fill = self.borderColour)
            canvas.create_oval (x + self.size / 5 * 2, y + self.size / 5 * 2, x + self.size / 5 * 3, y + self.size / 5 * 3, fill = self.borderColour)
        elif value == 6:
            if self.orientation == "horizontal":
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 1, x + self.size / 10 * 3, y + self.size / 10 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 7, x + self.size / 10 * 3, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 5 * 2, y + self.size / 10 * 7, x + self.size / 5 * 3, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 7, x + self.size / 10 * 9, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 1, x + self.size / 10 * 9, y + self.size / 10 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 5 * 2, y + self.size / 10 * 1, x + self.size / 5 * 3, y + self.size / 10 * 3, fill = self.borderColour)
            else:
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 1, x + self.size / 10 * 3, y + self.size / 10 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 10 * 7, x + self.size / 10 * 3, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 1, y + self.size / 5 * 2, x + self.size / 10 * 3, y + self.size / 5 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 7, x + self.size / 10 * 9, y + self.size / 10 * 9, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 10 * 1, x + self.size / 10 * 9, y + self.size / 10 * 3, fill = self.borderColour)
                canvas.create_oval (x + self.size / 10 * 7, y + self.size / 5 * 2, x + self.size / 10 * 9, y + self.size / 5 * 3, fill = self.borderColour)
                
# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: April 5 2017
# Purpose: draws the domino
# Input: canvas, x, y coordinates of the top left corner, size, colour
# Ouput: /
# ------------------------------------------------------------------------------
    def draw (self, canvas, x, y):
        value1 = self.value // 10
        value2 = self.value % 10
        if self.orientation == "horizontal":
            canvas.create_rectangle (x, y, x + 2 * self.size, y + self.size, outline = self.borderColour, fill = self.colour)
            if self.faceUp == True:
                canvas.create_line (x + self.size, y, x + self.size, y + self.size, fill = self.borderColour)
                self.drawDots (canvas, value1, x, y) 
                self.drawDots (canvas, value2, x + self.size, y)
        else:
            canvas.create_rectangle (x, y, x + self.size, y + 2 * self.size, outline = self.borderColour, fill = self.colour)
            if self.faceUp == True:
                canvas.create_line (x , y + self.size, x + self.size, y + self.size, fill = self.borderColour)
                self.drawDots (canvas, value1, x, y) 
                self.drawDots (canvas, value2, x, y + self.size)

# [DominoGroup] -----------------------------------------------------------------

# Author: Adrian Lam
# Date: 10 May 2017
# Purpose: a class for a DominoGroup
# Fields:
#   dominoList: a list of domino objects
#   size: size of the list
#   orientation: if the dominos are to be displayed horizontally or vertically
#   faceUp: if the dominos are to be displayed face up or face down
# Methods:
#   __str__: return the domino list followed by the size
#   valueOfDomino: returns the value of the ith Tile in the list
#   sizeOfHand: returns the size of the hand
#   addDomino: adds a domino to the end of the list
#   setOrientation: changes the orientation of the hand
#   setFaceUp: changes whether the hand is to be drawn face up or face down
#   sortHand: sorts the list
#   initDeal: randomizes the DominoGroup 
#   findValue: returns the location of a given parameter value element
#   drawList: displays itself starting at x,y on a given canvas
#   removeAt: remove a domino object at a given position within the list
# ------------------------------------------------------------------------------
class DominoGroup:
    def __init__ (self, size = 0, orientation = "H"):
        domino = Domino()
        if size >= 0 and size <= 28:
            self.dominoList = []
            for i in range (size):
                domino = Domino()
                domino.randomize ()
                self.dominoList.append(domino)
            self.size = size
        else:
            self.dominoList = []
            self.size = 0
        if orientation == "H":
            for i in range (self.size):
                self.dominoList[i].setOrientation (0)
            self.orientation = "H"
        elif orientation == "V":
            for i in range (self.size):
                self.dominoList[i].setOrientation (1)
            self.orientation = "V"
        else:
            self.orientation = "H"
        self.faceUp = True
 
# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 10 May 2017
# Purpose: returns the list followed by the size
# Input: /
# Ouput: string of the list followed by the size
# ------------------------------------------------------------------------------
    def __str__ (self):
        strReturn = ""
        for i in range (self.size):
            strReturn = strReturn + str(self.dominoList[i].value//10) + "|" + str(self.dominoList[i].value % 10) + "  "
        strReturn = strReturn + "size: " + str(self.size)
        return strReturn

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 31 May 2017
# Purpose: returns the value of the ith Tile in the list
# Input: /
# Ouput: the ith tile
# ------------------------------------------------------------------------------
    def valueOfDomino (self, tile):
        tileValue = -1
        tile = tile - 1
        if tile < self.size:
            tileValue = self.dominoList [tile].value
        return tileValue

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 31 May 2017
# Purpose: returns the size of the hand
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------
    def sizeOfHand (self):
        size = self.size
        return size

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 31 May 2017
# Purpose: adds a domino to the end of the list
# Input: value
# Ouput: /
# ------------------------------------------------------------------------------
    def addDomino (self, value = 0):
        if self.size < 28:
            dominoValue1 = value // 10
            dominoValue2 = value % 10
            if dominoValue1 > 6 or dominoValue2 > 6 or value < 0:
                value = 0
            self.dominoList.append (Domino(value = value))
            self.size = self.size + 1

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 31 May 2017
# Purpose: changes the orientation of the hand
# Input: "H" or "V"
# Ouput: /
# ------------------------------------------------------------------------------
    def setOrientation (self, orientation):
        if orientation == "H":
            for i in range (self.size):
                self.dominoList[i].setOrientation (0)
            self.orientation = "H"
        elif orientation == "V":
            for i in range (self.size):
                self.dominoList[i].setOrientation (1)
            self.orientation = "V"

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 5 June 2017
# Purpose: changes the colour of the hand
# Input: colour and borderColour
# Ouput: /
# ------------------------------------------------------------------------------
    def setColour (self, colour, borderColour):
        for i in range (self.size):
            self.dominoList[i].setColour (colour)
            self.dominoList[i].setBorderColour (borderColour)

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 31 May 2017
# Purpose: changes whether the hand is drawn face up or face down
# Input: True or False
# Ouput: /
# ------------------------------------------------------------------------------
    def setFaceUp (self, blnFaceUp):
        if blnFaceUp == True:
            for i in range (self.size):
                self.dominoList[i].setFaceUp (True)
        elif blnFaceUp == False:
            for i in range (self.size):
                self.dominoList[i].setFaceUp (False)

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 12 May 2017
# Purpose: returns the location of a given parameter value element
# Input: value of domino
# Ouput: the location of a given parameter value element
# ------------------------------------------------------------------------------
    def findValue (self, value = 0):
        dominoValue1 = value // 10
        dominoValue2 = value % 10
        location = -1
        if dominoValue1 > 6 or dominoValue2 > 6 or value < 0:
            value = 0
        if dominoValue1 > dominoValue2:
            value = dominoValue2 * 10 + dominoValue1
        for i in range (self.size):
            dominoValue = calcAscendingValue (self.dominoList[i])
            if dominoValue == value and location == -1:
                location = i
        return location

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 12 May 2017
# Purpose: draws the domino list
# Input: canvas, x, y
# Ouput: /
# ------------------------------------------------------------------------------
    def displayHand (self, canvas, x, y, face = False):
        if face == True:
            if self.orientation == "H":
                for i in range (self.size):
                    if i < 4:
                        self.dominoList[i].draw (canvas, x + i * ( 2 * self.dominoList[i].size + 10), y)
                    else:
                        self.dominoList[i].draw (canvas, x + (i - 4) * ( 2 * self.dominoList[i].size + 10) + 35, y + 30 + 10)
            else:
                for i in range (self.size):
                    if i < 4:
                        self.dominoList[i].draw (canvas, x, y + i * ( 2 * self.dominoList[i].size + 10))
                    else:
                        self.dominoList[i].draw (canvas, x + 30 + 10, y + (i - 4)* ( 2 * self.dominoList[i].size + 10) + 35)
        else:
            if self.orientation == "H":
                for i in range (self.size):
                    self.dominoList[i].setFaceUp(False)
                    if i < 4:
                        self.dominoList[i].draw (canvas, x + i * ( 2 * self.dominoList[i].size + 10), y)
                    else:
                        self.dominoList[i].draw (canvas, x + (i - 4) * ( 2 * self.dominoList[i].size + 10) + 35, y + 30 + 10)
            else:
                for i in range (self.size):
                    self.dominoList[i].setFaceUp(False)
                    if i < 4:
                        self.dominoList[i].draw (canvas, x, y + i * ( 2 * self.dominoList[i].size + 10))
                    else:
                        self.dominoList[i].draw (canvas, x + 30 + 10, y + (i - 4)* ( 2 * self.dominoList[i].size + 10) + 35)

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 1 June 2017
# Purpose: sorts the domino list
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------
    def sortHand (self):
        self.dominoList.sort ()
        
# ------------------------------------------------------------------------------
 
# Author: Alan Zhao
# Date: 8 June 2017
# Purpose: remove a domino from the domino list at a certain position
# Input: position
# Ouput: /
# ------------------------------------------------------------------------------
    def removeAt (self, position):
        if not(position >= self.size):
            del self.dominoList[position]
            self.size = self.size - 1

# [Table] ----------------------------------------------------------------------

# Author: Alan Zhao, Adrian Lam
# Date: 1 June 2017
# Purpose: a class for the table
# Fields:
#   table: a list of dominos on the table
#   size: size of the list
# Methods:
#   leftTable: returns the left side value of the first domino tile on the left side of the table
#   rightTable: returns the right side value of the first domino tile on the right side of the table
#   drawTable: draws the table of played dominos
#   addToTable: adds a domino to the table
# ------------------------------------------------------------------------------
class Table():
    def __init__(self,size = 0):
        self.table = DominoGroup()
        self.size = size

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 10 May 2017
# Purpose: returns the list followed by the size
# Input: /
# Ouput: string of the list followed by the size
# ------------------------------------------------------------------------------
    def __str__ (self):
        strReturn = ""
        for i in range (self.size):
            strReturn = strReturn + str(self.table.dominoList[i].value//10) + "|" + str(self.table.dominoList[i].value % 10) + "  "
        strReturn = strReturn + "size: " + str(self.size)
        return strReturn

# ------------------------------------------------------------------------------

# Author: Alan Zhao
# Date: 1 June 2017
# Purpose: returns the left side value of the first domino tile on the left side of the table
# Input: /
# Ouput: left side value of the domino on the left side
# ------------------------------------------------------------------------------
    def leftTable(self):
        firstDominoValue = self.table.dominoList[0].value 
        leftSideValue = firstDominoValue // 10
        return leftSideValue

# ------------------------------------------------------------------------------

# Author: Alan Zhao
# Date: 1 June 2017
# Purpose: returns the right side value of the first domino tile on the right side of the table
# Input: /
# Ouput: right side value of the domino on the right side
# ------------------------------------------------------------------------------
    def rightTable(self):
        lastDominoValue = self.table.dominoList[-1].value
        rightSideValue = lastDominoValue % 10
        return rightSideValue 

# ------------------------------------------------------------------------------

# Author: Alan Zhao, Adrian Lam
# Date: 2 June 2017
# Purpose: draws the table of played dominos
# Input: canvas, x and y coordinates
# Ouput: /
# ------------------------------------------------------------------------------
    def drawTable(self,canvas,x,y):
        leftList = self.table.dominoList[0:self.table.findValue(66)]
        leftList.reverse()
        rightList = self.table.dominoList[self.table.findValue(66):]
        multiplier = 1
        placeX = x
        placeY = y
        for i in range (len(rightList)):
            if i % 16 == 5:
                x = x - 30
            elif i % 16 == 12:
                x = x + 30
            if (i + 4) % 8 == 0:
                rightList[i].setOrientation(1)
                rightList[i].draw(canvas,x,y)
                rightList[i].setOrientation(0)
                y = y + 60
                multiplier *= -1
            else:
                if i > 4 and i < 12:
                    rightList[i].flip()
                    rightList[i].draw(canvas,x,y)
                    rightList[i].flip()
                    x = x + (60 * multiplier)
                else:
                    rightList[i].draw(canvas,x,y)
                    x = x + (60 * multiplier)
        x = placeX
        y = placeY
        multiplier = 1
        x = x - 60
        for i in range (len(leftList)):
            if i % 16 == 3:
                x = x + 30
            elif i % 16 == 12:
                x = x - 30
            if (i + 5) % 8 == 0:
                y = y - 30
                leftList[i].setOrientation(1)
                leftList[i].draw(canvas,x,y)
                leftList[i].setOrientation(0)
                y = y - 30
                multiplier *= -1
            else:
                if i > 3 and i < 12:
                    leftList[i].flip()
                    leftList[i].draw(canvas,x,y)
                    leftList[i].flip()
                    x = x - (60 * multiplier)
                else:
                    leftList[i].draw(canvas,x,y)
                    x = x - (60 * multiplier)

# ------------------------------------------------------------------------------

# Author: Alan Zhao, Adrian Lam
# Date: 1 June 2017
# Purpose: adds a domino to the table
# Input: value and location
# Ouput: /
# ------------------------------------------------------------------------------
    def addToTable(self,value=0,location="l", colour = "white", borderColour = "black"):
        if value // 10 <= 6 and value % 10 <= 6:
            domino = Domino(value = value, colour = colour, borderColour = borderColour)
            if location == "r": #appends the value to the right/back of the array "table"
                self.table.dominoList.append(domino)
                self.table.size = self.table.size + 1
                self.size = self.size + 1
            elif location == "l": #inserts the value to the left/front of the array "table"
                self.table.dominoList.insert(0,domino)
                self.table.size = self.table.size + 1
                self.size = self.size + 1

# [DominoGame] -----------------------------------------------------------------

# Author: Adrian Lam, Alan Zhao
# Date: 5 June 2017
# Purpose: a class for the Domino game
# Fields:
#   available: array of 66 booleans
#   handN: north domino hand
#   handE: east domino hand
#   handS: south domino hand
#   handW: west domino hand
#   table: table class for the played dominos
#   namesList: list of 4 names
# Methods:
#   setup: sets up the game
#   getNames: gets the names of the players
#   initAvailable: set values with the first digit >= second digit to true
#   deal: deal the players' hand
#   putHand: puts the ith hand
#   canMove: returns true if the player can move
#   firstmove: returns the player with the 6|6
#   getUsersMove: gets the value of the domino the user wants to play and which end of the line to put it
#   getComputersMove: gets the value of the domino the computer is going to pay and which end of the line to put it
#   play: plays the domino game
# ------------------------------------------------------------------------------
class DominoGame():
    def __init__(self):
        self.available = []
        self.table = Table()
        self.handN = DominoGroup()
        self.handE = DominoGroup()
        self.handS = DominoGroup()
        self.handW = DominoGroup()
        self.namesList = []
        self.dragItem = None
        self.itemX = 0
        self.itemY = 0

# ------------------------------------------------------------------------------

# Author: Alan Zhao
# Date: 6 June 2017
# Purpose: prepares the game to be played
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------    
    def setUp(self):
        self.handN = DominoGroup()
        self.handE = DominoGroup()
        self.handS = DominoGroup()
        self.handW = DominoGroup()
        self.table = Table ()
        self.getNames()
        self.initAvailable()
        self.deal()
        
# ------------------------------------------------------------------------------

# Author: Alan Zhao, Adrian Lam
# Date: 6 June 2017
# Purpose: Initializes the array of 66 booleans to be used in dealing
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------   
    def initAvailable(self):
        for i in range(67):
            self.available.append(False)
            if i // 10 >= i % 10:
                self.available[i] = True
        
# ------------------------------------------------------------------------------

# Author: Alan Zhao
# Date: 6 June 2017
# Purpose: Gets the list of names 
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------            
    def getNames(self):
        namesList = ["Player","Computer 1","Computer 2","Computer 3"]
        return namesList

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 6 June 2017
# Purpose: deals the hand
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------   
    def deal(self):
        for i in range(7):
            value = random.randint (0,66)
            while (value // 10 > 6 and value % 10 < 6) or self.available[value] == False:
                value = random.randint (0,66)
            self.handN.addDomino(value)
            self.available[value] = False
            value = random.randint (0,66)
            while (value // 10 > 6 and value % 10 < 6) or self.available[value] == False:
                value = random.randint (0,66)
            self.handE.addDomino(value)
            self.available[value] = False
            value = random.randint (0,66)
            while (value // 10 > 6 and value % 10 < 6) or self.available[value] == False:
                value = random.randint (0,66)
            self.handS.addDomino(value)
            self.available[value] = False
            value = random.randint (0,66)
            while (value // 10 > 6 and value % 10 < 6) or self.available[value] == False:
                value = random.randint (0,66)
            self.handW.addDomino(value)
            self.available[value] = False
        self.handE.setOrientation ("V")
        self.handW.setOrientation ("V")
        self.handN.setColour ("black", "lime")
        self.handE.setColour ("black", "magenta")
        self.handS.setColour ("black", "cyan")
        self.handW.setColour ("black", "yellow")
        self.handN.displayHand (canvas, dominoHandX (800, self.handN), 10)
        self.handE.displayHand (canvas, 720, dominoHandY (620, self.handE))
        self.handS.displayHand (canvas, dominoHandX (800, self.handS), 540,True)
        self.handW.displayHand (canvas, 10, dominoHandY (620, self.handW))


# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 7 June 2017
# Purpose: returns true if the ith player can move
# Input: /
# Ouput: True or False
# ------------------------------------------------------------------------------ 
    def canMove (self, dominoGroup):
        canMove = False
        for i in range(dominoGroup.size):
            if dominoGroup.dominoList[i].value // 10 == self.table.leftTable() or dominoGroup.dominoList[i].value // 10 == self.table.rightTable() \
            or dominoGroup.dominoList[i].value % 10 == self.table.leftTable() or dominoGroup.dominoList[i].value % 10 == self.table.rightTable():
                canMove = True
        return canMove

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 7 June 2017
# Purpose: returns the player with the 6|6
# Input: /
# Ouput: "N", "E", "S" or "W"
# ------------------------------------------------------------------------------
    def firstMove (self):
        if self.handN.findValue (66) != -1:
            firstMove = "N"
        elif self.handE.findValue (66) != -1:
            firstMove = "E"
        elif self.handS.findValue (66) != -1:
            firstMove = "S"
        elif self.handW.findValue (66) != -1:
            firstMove = "W"
        return firstMove

# ------------------------------------------------------------------------------

# Author: Alan Zhao and Adrian Lam
# Date: 7 June 2017
# Purpose: gets the computer's move
# Input: dominoHand, colour, borderColour
# Ouput: /
# ------------------------------------------------------------------------------
    def getComputersMove(self,dominoHand, colour = "white", borderColour = "black"):
        position = "x"
        value = -1
        if self.canMove(dominoHand) == True:
            for i in range(dominoHand.size):
                if position == "x" and dominoHand.dominoList[i].value // 10 == self.table.leftTable():
                    value = (dominoHand.dominoList[i].value % 10) * 10 + (dominoHand.dominoList[i].value // 10)
                    position = "l"
                    dominoHand.removeAt(i)
                elif position == "x" and dominoHand.dominoList[i].value % 10 == self.table.leftTable():
                    value = dominoHand.dominoList[i].value
                    position = "l"
                    dominoHand.removeAt(i)
                elif position =="x" and dominoHand.dominoList[i].value // 10 == self.table.rightTable():
                    value = dominoHand.dominoList[i].value
                    position = "r"
                    dominoHand.removeAt(i)
                elif position == "x" and dominoHand.dominoList[i].value % 10 == self.table.rightTable():
                    value = (dominoHand.dominoList[i].value % 10) * 10 + (dominoHand.dominoList[i].value // 10)
                    position = "r"
                    dominoHand.removeAt(i)
        if position != "x" and value != -1:
            self.table.addToTable(value,position, colour = colour, borderColour = borderColour)

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 14 June 2017
# Purpose: makes the user's move
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------
    def makeUsersMove (self, position = "l"):
        global move
        global chosenDomino
        value = -1
        if self.canMove(self.handS) == True or self.handS.dominoList[chosenDomino].value == 66:
            if self.handS.dominoList[chosenDomino].value == 66:
                value = 66
            elif position == "l":
                if self.handS.dominoList[chosenDomino].value // 10 == self.table.leftTable():
                    value = (self.handS.dominoList[chosenDomino].value % 10) * 10 + (self.handS.dominoList[chosenDomino].value // 10)
                    self.handS.removeAt(chosenDomino)
                    move = "W"
                elif self.handS.dominoList[chosenDomino].value % 10 == self.table.leftTable():
                    value = self.handS.dominoList[chosenDomino].value
                    self.handS.removeAt(chosenDomino)
                    move = "W"
                else:
                    messagebox.showinfo ("Error", "That is not a valid move.")
            elif position == "r":
                if self.handS.dominoList[chosenDomino].value // 10 == self.table.rightTable():
                    value = self.handS.dominoList[chosenDomino].value
                    self.handS.removeAt(chosenDomino)
                    move = "W"
                elif self.handS.dominoList[chosenDomino].value % 10 == self.table.rightTable():
                    value = (self.handS.dominoList[chosenDomino].value % 10) * 10 + (self.handS.dominoList[chosenDomino].value // 10)
                    self.handS.removeAt(chosenDomino)
                    move = "W"
                else:
                    messagebox.showinfo ("Error", "That is not a valid move.")
            self.table.addToTable(value,position, colour = "black", borderColour = "cyan")
            self.handS.displayHand (canvas, dominoHandX (800, self.handS), 540,True)
            self.table.drawTable(canvas,370,295)

# ------------------------------------------------------------------------------

# Author: Alan Zhao and Adrian Lam
# Date: 14 June 2017
# Purpose: plays the game
# Input: canvas object, x coordinate and y coordinate
# Ouput: /
# ------------------------------------------------------------------------------
    def play(self,canvas,x,y):
        global playButton
        global exitButton
        leftButton = Button (window, bg = "cyan", text = "Left", font = ("Arial",12,"bold"), command=lambda:dominoGame.makeUsersMove("l"))
        rightButton = Button (window, bg = "cyan", text = "Right", font = ("Arial",12,"bold"), command=lambda:dominoGame.makeUsersMove("r"))
        leftButton.place (x = "245", y = "652", width = "60", height = "30")
        rightButton.place (x = "595", y = "652", width = "60", height = "30")
        canvas.delete (dominoLogo)
        playButton.place_forget ()
        exitButton.place_forget ()
        global move
        blnPass = False
        if self.firstMove() == "N":
            canvas.create_oval (390, 90, 410, 110, fill = "lime")
            self.handN.removeAt(self.handN.findValue(66))
            move = "E"
            self.table.addToTable(66,"r", "black", "lime")
        elif self.firstMove() == "E":
            canvas.create_oval (690, 300, 710, 320, fill = "magenta")
            self.handE.removeAt(self.handE.findValue(66))
            move = "S"
            self.table.addToTable(66,"r", "black", "magenta")
        elif self.firstMove() == "S":
            canvas.create_oval (390, 510, 410, 530, fill = "cyan")
            self.handS.removeAt(self.handS.findValue(66))
            move = "W"
            self.table.addToTable(66,"r", "black", "cyan")
        elif self.firstMove() == "W":
            canvas.create_oval (90, 300, 110, 320, fill = "yellow")
            self.handW.removeAt(self.handW.findValue(66))
            move = "N"
            self.table.addToTable(66,"r", "black", "yellow")
        canvas.delete("all")
        while (self.canMove(self.handS) == True or self.canMove(self.handN) == True or self.canMove(self.handE) == True or self.canMove(self.handW) == True) and \
        self.handN.size > 0 and self.handE.size > 0 and self.handS.size > 0 and self.handW.size > 0:
            if move == "S":
                canvas.create_oval (390, 510, 410, 530, fill = "cyan")
            if self.canMove(self.handS) == False and move == "S" and blnPass == True:
                    messagebox.showinfo ("Pass", "You do not have a valid move. You must pass this turn.")
                    move = "W"
            while move != "S" and self.handN.size > 0 and self.handE.size > 0 and self.handS.size > 0 and self.handW.size > 0:
                canvas.delete("all")
                self.handN.displayHand (canvas, dominoHandX (800, self.handN), 10)
                self.handE.displayHand (canvas, 720, dominoHandY (620, self.handE))
                self.handS.displayHand (canvas, dominoHandX (800, self.handS), 540,True)
                self.handW.displayHand (canvas, 10, dominoHandY (620, self.handW))
                self.table.drawTable(canvas,x,y)
                window.update()
                if move == "N":
                    canvas.create_oval (390, 90, 410, 110, fill = "lime")
                    window.update()
                    self.getComputersMove(self.handN, "black", "lime")
                    time.sleep(0.5)
                    move = "E"
                elif move == "E":
                    canvas.create_oval (690, 300, 710, 320, fill = "magenta")
                    window.update()
                    self.getComputersMove(self.handE, "black", "magenta")
                    time.sleep(0.5)
                    move = "S"
                elif move == "W":
                    canvas.create_oval (90, 300, 110, 320, fill = "yellow")
                    window.update()
                    self.getComputersMove(self.handW, "black", "yellow")
                    time.sleep(0.5)
                    move = "N"
                canvas.delete("all")
            self.handN.displayHand (canvas, dominoHandX (800, self.handN), 10)
            self.handE.displayHand (canvas, 720, dominoHandY (620, self.handE))
            self.handS.displayHand (canvas, dominoHandX (800, self.handS), 540,True)
            self.handW.displayHand (canvas, 10, dominoHandY (620, self.handW))
            self.table.drawTable(canvas,x,y)
            window.update()
            blnPass = True
        if self.handS.size == 0:
            messagebox.showinfo ("You Win", "Player Wins.")
        elif self.handE.size == 0:
            messagebox.showinfo ("You Lose", "Magenta Wins.")
        elif self.handN.size == 0:
            messagebox.showinfo ("You Lose", "Lime Wins.")
        elif self.handW.size == 0:
            messagebox.showinfo ("You Lose", "Yellow Wins.")
        if (self.canMove(self.handS) == False and self.canMove(self.handN) == False and self.canMove(self.handE) == False and self.canMove(self.handW) == False) and \
        self.handN.size > 0 and self.handE.size > 0 and self.handS.size > 0 and self.handW.size > 0:
            messagebox.showinfo ("Tie!", "It's a tie! No one has played all their dominos and there are no more valid moves.")
        rightButton.place_forget()
        leftButton.place_forget()
        self.showMenu ()

# ------------------------------------------------------------------------------

# Author: Adrian Lam
# Date: 16 June 2017
# Purpose: shows the menu
# Input: /
# Ouput: /
# ------------------------------------------------------------------------------
    def showMenu (self):
        global playButton
        global exitButton
        canvas.delete("all")
        dominoGame.setUp()
        dominoLogo = canvas.create_image(400, 310, image=photo)
        playButton = Button (window, bg = "white", text = "Play", font = ("Arial",12,"bold"), command=lambda:dominoGame.play(canvas, 370, 295))
        exitButton = Button (window, bg = "white", text = "exit", font = ("Arial",12,"bold"), command=lambda:os._exit(0))
        playButton.place (x = "400", y = "490", width = "100", height = "50")
        exitButton.place (x = "400", y = "550", width = "100", height = "50")

# [Subprograms] ================================================================ 

# Author: Adrian Lam
# Date: April 27 2017
# Purpose: calculates the ascending value of a domino
# Input: /
# Output: /
# ------------------------------------------------------------------------------
def calcAscendingValue (domino):
    dominoValue = domino.value
    dominoValue1 = domino.value // 10
    dominoValue2 = domino.value % 10
    if dominoValue1 > dominoValue2:
        dominoValue = dominoValue2 * 10 + dominoValue1
    return dominoValue

# ------------------------------------------------------------------------------
 
# Author: Adrian Lam
# Date: April 17 2017
# Purpose: calculates the x coordinate of the domino hand 
# Input: /
# Output: /
# ------------------------------------------------------------------------------
def dominoHandX (canvasX, dominoGroup):
    if dominoGroup.orientation == "V":
        x = (canvasX - (30  + 10) * 4 + 50) / 2
    else:
        x = (canvasX - (30  + 10) * 8 + 50) / 2
    return x
 
# ------------------------------------------------------------------------------
 
# Author: Adrian Lam
# Date: April 17 2017
# Purpose: calculates the y coordinate of the domino hand 
# Input: /
# Output: /
# ------------------------------------------------------------------------------
def dominoHandY (canvasY, dominoGroup):
    if dominoGroup.orientation == "V":
        y = (canvasY - (30 + 10) * 8 + 50) / 2
    else:
        y = (canvasY - (30 + 10) * 4 + 50)/ 2
    return y

# ------------------------------------------------------------------------------

# Author: Adrian Lam and Alan Zhao
# Date: June 13 2017
# Purpose: Chooses the domino
# Input: /
# Output: /
# ------------------------------------------------------------------------------
def chooseDomino (event):
    global rectangle
    global chosenDomino
    canvas.delete(rectangle)
    if event == None:
        chosenDomino = -1
    elif (event.x >= 265 and event.x <= 325) and (event.y >= 540 and event.y <= 570):
        chosenDomino = 0
        rectangle = canvas.create_rectangle(263, 538, 328, 573, width = 4,outline = "cyan")
    elif (event.x >= 335 and event.x <= 395) and (event.y >= 540 and event.y <= 570):
        chosenDomino = 1
        rectangle = canvas.create_rectangle(333, 538, 398, 573, width = 4,outline = "cyan")
    elif (event.x >= 405 and event.x <= 465) and (event.y >= 540 and event.y <= 570):
        chosenDomino = 2
        rectangle = canvas.create_rectangle(403, 538, 468, 573, width = 4,outline = "cyan")
    elif (event.x >= 475 and event.x <= 535) and (event.y >= 540 and event.y <= 570):
        chosenDomino = 3
        rectangle = canvas.create_rectangle(473, 538, 538, 573, width = 4,outline = "cyan")
    elif (event.x >= 300 and event.x <= 360) and (event.y >= 580 and event.y <= 610):
        chosenDomino = 4
        rectangle = canvas.create_rectangle(298, 578, 363, 613, width = 4,outline = "cyan")
    elif (event.x >= 370 and event.x <= 430) and (event.y >= 580 and event.y <= 610):
        chosenDomino = 5
        rectangle = canvas.create_rectangle(368, 578, 433, 613, width = 4,outline = "cyan")
    elif (event.x >= 440 and event.x <= 500) and (event.y >= 580 and event.y <= 610):
        chosenDomino = 6
        rectangle = canvas.create_rectangle(438, 578, 503, 613, width = 4,outline = "cyan")
    else:
        chosenDomino = -1
    if dominoGame.handS.size < chosenDomino:
        canvas.delete(rectangle)

# ------------------------------------------------------------------------------
 
# Author: Adrian Lam and Alan Zhao
# Date: June 13 2017
# Purpose: Chooses the domino
# Input: /
# Output: /
# ------------------------------------------------------------------------------
def aboutClient():
    helpWindow = Tk()
    helpWindow.title ("About")
    helpWindow.minsize(800, 400)
    textbox = Canvas(helpWindow,height = 300, width = 700, bg = '#def1ff')
    textbox.place( x = 50,y =50)
    textbox.create_text(300,15,text = "The player first must select a domino tile they wish to play by left clicking on it.")
    textbox.create_text(300,30,text = "It will then be selected, and it is indicated by a cyan border around it.")
    textbox.create_text(300,45,text = "The player must then choose to place it on the right or the left side of the")
    textbox.create_text(300,60,text = "“line of play” by clicking on the “left” or “right” buttons in their")
    textbox.create_text(300,75,text = " respective place of the domino hand.")


                   
#[Menu] ========================================================================
    
menubar = Menu(window)

#[File Menubar] ================================================================

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Exit", command = lambda:os._exit(0))
menubar.add_cascade(label = "File",menu = filemenu)

# [Help Menu] ==================================================================

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About",command = lambda:aboutClient())
menubar.add_cascade(label = "Help", menu = helpmenu)
window.config(menu = menubar)

# [Create] =====================================================================

background = PhotoImage(file = "DominoGameBackground.gif")
backgroundLabel = Label (window, image = background)
photo = PhotoImage(file = 'DominoLogo.gif')
window.title ("Domino Game")
window.geometry ("900x770")
window.resizable(width=False, height=False)
canvas = Canvas (window, bg = "white", width = 800, height = 620)
canvas.bind("<Button-1>", chooseDomino)
playButton = Button (window, bg = "white", text = "Play", font = ("Arial",12,"bold"), command=lambda:dominoGame.play(canvas, 380, 295))
exitButton = Button (window, bg = "white", text = "Exit", font = ("Arial",12,"bold"), command=lambda:os._exit(0))

# [Position] ===================================================================

backgroundLabel.place (x = "-2", y = "-2")
backgroundLabel.pack ()
canvas.place (x = "48", y = "113")
rectangle = canvas.create_rectangle(0, 0, 0, 0)

# [Main] =======================================================================

table = Table ()
dominoGame = DominoGame()
dominoGame.setUp()
dominoGame.showMenu()
dominoLogo = canvas.create_image(400, 310, image=photo)

mainloop ()

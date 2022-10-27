# CMPT 120 Yet Another Image Processer
# Author(s): Alex Cai
# Date: November 30

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Current Image",
         ]

# list of basic operation options
basic = [
          "1: Apply Red Filter",
          "2: Apply Green Filter",
          "3: Apply Blue Filter",
          "4: Apply Sepia Filter",
          "5: Apply Warm Filter",
          "6: Apply Cold Filter",
          "7: Switch to Advanced Functions"
         ]

# list of advanced operation options
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Double Size",
                "4: Half Size",
                "5: Locate Fish",
                "6: Switch to Basic Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
  """
  Input:  state - a dictionary containing the state values of the application
  Returns: a list of strings, each element represets a line in the interface
  """
  menuString = ["Welcome to CMPT 120 Image Processer!"]
  menuString.append("") # an empty line
  menuString.append("Choose the following options:")
  menuString.append("") # an empty line
  menuString += system
  menuString.append("") # an empty line

  # build the list differently depending on the mode attribute
  if state["mode"] == "basic":
    menuString.append("--Basic Mode--")
    menuString += basic
    menuString.append("")
    menuString.append("Enter your choice: (Q/O/S/R OR 1-7)...")
  elif state["mode"] == "advanced":
    menuString.append("--Advanced Mode--")
    menuString += advanced
    menuString.append("")
    menuString.append("Enter your choice: (Q/O/S/R OR 1-7)...")
  else:
    menuString.append("Error: Unknown mode!")

  return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
  """
  Input:  state - a dictionary containing the state values of the application
          img - the 2d array of RGB values to be operated on
  Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
  """
  userInput = state["lastUserInput"].upper()
  # handle the system functionalities
  if userInput.isalpha(): # check if the input is an alphabet
    print("Log: Doing system functionalities " + userInput)
    if userInput == "Q": 
      print("Log: Quitting...")
    if userInput == "O":
      print("Opening image...")
      tkinter.Tk().withdraw()
      openFilename = tkinter.filedialog.askopenfilename()
      if openFilename == (): # if user clicks cancel
        print("No filename was inputted.")
        cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(state))
      else:
        img = cmpt120imageProjHelper.getImage(openFilename)
        state["lastOpenFilename"] = openFilename # updates appStateValues
        title = openFilename.split("/")[-1] # gets the file name by splitting filepath into a list
        cmpt120imageProjHelper.showInterface(img, f"Open Image {title}", generateMenu(state))
    if userInput == "S":
      print("Saving image...")
      tkinter.Tk().withdraw()
      saveFilename = tkinter.filedialog.asksaveasfilename()
      title = saveFilename.split("/")[-1] # gets the file name by splitting filepath into a list
      if saveFilename == "": # if user clicks cancel
        print("No filename was inputted.")
        cmpt120imageProjHelper.showInterface(img, f"Save Image {title}", generateMenu(state))
      else:
        cmpt120imageProjHelper.saveImage(img, f"{saveFilename}")
        state["lastSaveFilename"] = saveFilename # updates appStateValues
        cmpt120imageProjHelper.showInterface(img, f"Save Image {title}", generateMenu(state))
    if userInput == "R":
      if state["lastOpenFilename"] == "": # if user tries to reload before opening an image
        print("No image to reload")
      else:
        print("Reloading image...")
        img = cmpt120imageProjHelper.getImage(state["lastOpenFilename"]) 
        title = state["lastOpenFilename"].split("/")[-1] # gets the file name by splitting filepath into a list
        cmpt120imageProjHelper.showInterface(img, f"Reload Image {title}", generateMenu(state))

  # or handle the manipulation functionalities based on which mode the application is in
  elif userInput.isdigit(): # has to be a digit for manipulation options
    print("Log: Doing manipulation functionalities " + userInput)
    if state["mode"] == "basic":
      if userInput == "1":
          print("Log: Performing " + basic[int(userInput)-1])
          img = cmpt120imageManip.redFilter(img)
          cmpt120imageProjHelper.showInterface(img, "Apply Red Filter", generateMenu(state))
      elif userInput == "2":
        print("Log: Performing " + basic[int(userInput)-1])
        img = cmpt120imageManip.greenFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Green Filter", generateMenu(state))
      elif userInput == "3":
        print("Log: Performing " + basic[int(userInput)-1])
        img = cmpt120imageManip.blueFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Blue Filter", generateMenu(state))
      elif userInput == "4":
        print("Log: Performing " + basic[int(userInput)-1])
        img = cmpt120imageManip.sepiaFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Sepia Filter", generateMenu(state))
      elif userInput == "5":
        print("Log: Performing " + basic[int(userInput)-1])
        img = cmpt120imageManip.warmFilterRed(img)
        img = cmpt120imageManip.warmFilterBlue(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Warm Filter", generateMenu(state))
      elif userInput == "6":
        print("Log: Performing " + basic[int(userInput)-1])
        img = cmpt120imageManip.coldFilterRed(img)
        img = cmpt120imageManip.coldFilterBlue(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Cold Filter", generateMenu(state))
      elif userInput == "7":
        print("Log: Performing " + basic[int(userInput)-1])
        state["mode"] = "advanced"
        cmpt120imageProjHelper.showInterface(img, "Switch to Advanced Functions", generateMenu(state))
    elif state["mode"] == "advanced":
      if userInput == "1": 
        print("Log: Performing " + advanced[int(userInput)-1])
        img = cmpt120imageManip.rotateLeft(img)
        cmpt120imageProjHelper.showInterface(img, "Rotate Left", generateMenu(state))
      elif userInput == "2":
        print("Log: Performing " + advanced[int(userInput)-1])
        img = cmpt120imageManip.rotateRight(img)
        cmpt120imageProjHelper.showInterface(img, "Rotate Right", generateMenu(state))
      elif userInput == "3":
        print("Log: Performing " + advanced[int(userInput)-1])
        img = cmpt120imageManip.doubleSize(img)
        cmpt120imageProjHelper.showInterface(img, "Double Size", generateMenu(state))
      elif userInput == "4":
        print("Log: Performing " + advanced[int(userInput)-1])
        img = cmpt120imageManip.halfSize(img)
        cmpt120imageProjHelper.showInterface(img, "Half Size", generateMenu(state))
      elif userInput == "5":
        if appStateValues["lastOpenFilename"] == "/home/runner/FinalProject/fish.jpg":
          print("Log: Performing " + advanced[int(userInput)-1])
          rows_and_columns = cmpt120imageManip.findYellow(img) # extracts rows and columns with yellow
          row_list = rows_and_columns[0]
          row_list = list(dict.fromkeys(row_list)) # removes duplicates from list 
          col_list = rows_and_columns[1]
          col_list = list(dict.fromkeys(col_list)) # removes duplicates from list
          img = cmpt120imageManip.boxDraw(img, row_list, col_list) # draw box from input lists
          cmpt120imageProjHelper.showInterface(img, "Locate Fish", generateMenu(state))
        else: # if currently opened image is not the fish
          print("Fish image not opened.")
      elif userInput == "6":
        print("Log: Performing " + advanced[int(userInput)-1])
        state["mode"] = "basic"
        cmpt120imageProjHelper.showInterface(img, "Switch to Basic Functions", generateMenu(state))
            
  else: # unrecognized user input
      print("Log: Unrecognized user input: " + userInput)
  return img

# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
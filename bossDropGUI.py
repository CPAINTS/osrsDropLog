import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import json
from typing import Type

#Open the JSON file and load into our info 
with open("bossDropGUI.json", 'r') as f:
        Info = json.load(f)

def readMe():
    messagebox.showinfo("Read Me", Info["ReadMe"])

def default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def writeJSON():
    dropInfo = {
    'Boss': bossVar,
    'Drops' : [
        {
            'Drop': dropChoice,
            'KC': killCount
        }
    ]
} 

    with open("BossDrops.json", "w") as drops:
        res = json.dumps(dropInfo, default=default)
        json.dump(res, drops)

#mainframe of the application 300x300 pixels w/ title
root = tk.Tk()
root.title("OSRS Boss Drop Log")
root.geometry("300x300")

#Button for the readMe which uses the JSON readMe information to pop up in a message box
readMeButton = ttk.Button(root, text ="Read Me",command = readMe).place(x = 100, y = 70)

#Label for menu choices
bossVar = StringVar(root)
menuLabel = Label(root, textvariable=bossVar).place(x = 90, y = 110)
bossVar.set("Boss Choice Menu\n______________________")

#Create Boss Option Menu for specific boss type
bossChoice = StringVar(root)
checkChoice = bossChoice
bossmenu = ttk.OptionMenu(root, bossChoice, *Info["BossOption"]).place(x = 100, y = 150)

#create a menu for drops based off the boss they're killing
dropChoice = StringVar(root)

dropmenu = ttk.OptionMenu(root, dropChoice, *Info[bossChoice.get()]).place(x = 100, y = 180)

#Create a input textbox for killcount
killCount = IntVar(root)
KCLabel = Label(root, text="Kill Count:").place(x = 35, y = 210)
killCountBox = ttk.Entry(root,textvariable=killCount).place(x = 100, y = 210)

#Button to add the drop once the user has inputted their latest boss drop
addDropButton = ttk.Button(root, text="Add Drop", command = writeJSON).place(x = 100, y = 240)


root.mainloop()

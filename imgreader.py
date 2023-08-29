import PIL.Image, PIL.ImageTk
import time
import math
from random import randint
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sys

def gethex():
	return "#%02x%02x%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))

# stylesheet
buttonStylesheet = {
	"bg" : "#c9c9c9",
	"relief" : "flat",
	"activebackground" : "#b0b0b0",
	"font" : ("Calibri", 15)
}

# gui setup
root = Tk()
root.geometry("400x300+100+100")
root.state("zoomed")
root.title("MapDesigner v0.0.1")

# map designer thingy
canv = Canvas(root, width=800, height=600)
toolFrame = Frame(root)
canv.create_rectangle(5, 5, 795, 595)
toolLabel = Label(root, text="Select a tool to begin.", font=("Calibri", 20))
currentTool = ["none"]
prevclick = [False, False]
rects = []
data = []
colors = {}

def startEditor():
	designButton.destroy()
	toolLabel.pack()
	canv.pack()
	toolFrame.pack()
	setButton.grid(row=0, column=0, padx=5)
	delButton.grid(row=0, column=1, padx=5)
	configMenu[0].grid(row=1, column=0, padx=2)
	configMenu[1].grid(row=1, column=1)
	helpButton.grid(row=0, column=2, padx=5)

def placeWall():
	currentTool[0] = "placewall"
	toolLabel.config(text="Current Tool: Place Wall Tool")
def deleteWallTool():
	currentTool[0] = "deletewall"
	toolLabel.config(text="Current Tool: Delete Wall Tool")
def helpTool():
	messagebox.showinfo("Help", """
Select a tool to get started.
To use wall tool: click somewhere, then click somewhere else and a wall will appear.
Delete wall tool: click on a wall to remove it.
Press right click or z to undo.
Press Ctrl-P to print out wall data to console.""")
def removeElement(e):
	if len(rects) == 0:
		return
	canv.delete(rects.pop())
	data.pop()

def onclick(event):
	if currentTool[0] == "placewall":
		if prevclick[0] is False:
			prevclick[0] = event.x
			prevclick[1] = event.y
		else:
			name = configMenu[1].get(1.0, "end-1c")
			col = "#000000"
			if name in colors:
				col = colors[name]
			else:
				col = gethex()
				colors[name] = col
			rects.append(canv.create_rectangle(prevclick[0], prevclick[1], event.x, event.y, fill=col))
			data.append([min(prevclick[0], event.x), min(prevclick[1], event.y),
				max(prevclick[0], event.x) - min(prevclick[0], event.x), max(prevclick[1], event.y) - min(prevclick[1], event.y),
				configMenu[1].get(1.0, "end-1c")])
			prevclick[0] = False
	elif currentTool[0] == "deletewall":
		for i in range(0, len(data)):
			if 0 < event.x - data[i][0] < data[i][2] and 0 < event.y - data[i][1] < data[i][3]:
				canv.delete(rects[i])
				data.pop(i)
				rects.pop(i)
				break


designButton = Button(root, text = "Use In-App Editor", width = 50, height = 10, command = startEditor,
	**buttonStylesheet)
setButton = Button(toolFrame, text = "Wall Tool", command = placeWall, **buttonStylesheet)
delButton = Button(toolFrame, text = "Delete Wall Tool", command = deleteWallTool, **buttonStylesheet)
helpButton = Button(toolFrame, text="Help", command = helpTool, **buttonStylesheet)
configMenu = (Label(toolFrame, text="Wall Type:"), Text(toolFrame, height=1, width=20))
designButton.pack(padx = 10, pady = 10)
canv.bind("<Button-1>", onclick)
root.bind("<z>", removeElement)
root.bind("<Control-p>", lambda _: print(data))

root.mainloop()

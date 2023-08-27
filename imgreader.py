import PIL.Image, PIL.ImageTk
import time
import math
from tkinter import *
from tkinter import filedialog
import sys

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
root.title("MapDesigner v0.0.1")

def openFile():
	root.fileName = filedialog.askopenfilename(initialdir = "C:/Users/wangh/Documents/Jerry/python/flask", title = "Open Image",
		filetypes = ((
		"JPG Files", "*.jpg"), ("PNG Files", "*.png"), ("BMP Files", "*.bmp"), ("All Files", "*")))
	if root.fileName: # chose a file
		uploadButtonBig.destroy()
		previewImg = PIL.Image.open(root.fileName)
		previewImg = previewImg.resize((root.winfo_width() - 30, root.winfo_height() - 50), PIL.Image.ANTIALIAS)

		previewImgTk = PIL.ImageTk.PhotoImage(previewImg)

		previewLabel.config(image = previewImgTk)
		previewLabel.image = previewImgTk

		# pack frames
		root.geometry("400x600+100+100")
		imgPreviewFrame.pack(padx = 5, pady = 5)
		imgOptionsFrame.pack(padx = 5, pady = 5)

def goBack():
	pass

# bohhh why cant like keys() just return a list already
def getKeys(d):
	res = []
	for key in d.keys():
		res.append(key)
	return tuple(res)

def processImg(img):
	im = PIL.Image.open(img) # Can be many different formats.
	pixs = im.load()
	width = im.size[0]
	height = im.size[1]
	numOfPixs = width * height
	logs = []
	advancedLogs = []

	colorsIncomplete = {}
	pixColors = {}
	finalList = ""


	for x in range(width):
		for y in range(height):
			currentPos = [x, y]
			currentColor = pixs[x, y]

			if (len(currentColor) == 4 and currentColor[3] != 0) or currentColor[0] != 255 and currentColor[1] != 255 and currentColor[2] != 255: # so it's not transparent
				advancedLogs.append(
					f"[ADVANCEDLOGS]: non-transparent pixel found. coords: {currentPos}, color: {currentColor}\n")

				if currentColor in getKeys(colorsIncomplete): # so the color has already occured
					colorsIncomplete[currentColor].append(currentPos)
					advancedLogs.append(
						f"[ADVANCEDLOGS]: non-transparent pixel of the same color {currentColor} has already occured\n")

					if len(colorsIncomplete[currentColor]) == 4: # 4 of the same color occured, ready to spit out a wall
						poses = colorsIncomplete[currentColor]
						print("wall ready. poses=" + repr(poses))
						wallX = min(poses[0][0], poses[1][0], poses[2][0], poses[3][0])
						wallY = min(poses[0][1], poses[1][1], poses[2][1], poses[3][1])
						wallWidth = max(poses[0][0], poses[1][0], poses[2][0], poses[3][0])
						wallHeight = max(poses[0][1], poses[1][1], poses[2][1], poses[3][1])
						advancedLogs.append(
							f"[ADVANCEDLOGS]: wall ready. wallX = {wallX}, wallY = {wallY}, wall\
							Width = {wallWidth}, wallHeight = {wallHeight}\n")
						finalList += "Wall({}, {}, {}, {}),\n".format(
							wallX, wallY, wallWidth, wallHeight)

						del colorsIncomplete[currentColor]

				else: # so the color is new
					colorsIncomplete[currentColor] = [currentPos]
					advancedLogs.append("[ADVANCEDLOGS]: non-transparent pixel color was new\n")
	root.finalList = finalList
	if True:
		root.advancedLogs = advancedLogs
		logsText.insert(1.0, root.advancedLogs)
	logsText.configure(state = "disabled")
	root.logs = logs
	resFrame.pack()
	print(finalList)
	

# Buttons and other w's

# Upload File
uploadButtonBig = Button(root, text = "Scan Image (very broken, don't use)", width = 50, height = 3, command = openFile,
	**buttonStylesheet)
uploadButtonBig.pack(padx = 10, pady = 10)

# After Image Selected
imgPreviewFrame = LabelFrame(root, text = "Preview", padx = 10, pady = 10)
previewLabel = Label(imgPreviewFrame)
previewLabel.grid(row = 0, column = 0, rowspan = 5, columnspan = 5)
okButton = Button(imgPreviewFrame, text = "Ok", command = lambda: processImg(root.fileName), **buttonStylesheet)
okButton.grid(row = 6, column = 1)
cancelButton = Button(imgPreviewFrame, text = "Cancel", command = goBack, **buttonStylesheet)
cancelButton.grid(row = 6, column = 4)

imgOptionsFrame = LabelFrame(root, text = "Options", padx = 10, pady = 10)

# after processed
resFrame = LabelFrame(root, text = "Results", padx = 10, pady = 10)
logsLabel = Label(resFrame, text = "Logs")
logsLabel.pack(padx = 10, pady = 5)
logsText = Text(resFrame, height = 10, font = ("Calibri", 11))
logsText.pack()

# section 2: designer thingy

# map designer thingy
canv = Canvas(root, width=800, height=600)
canv.create_rectangle(5, 5, 795, 595)
currentTool = ["none"]
prevclick = [False, False]
rects = []
data = []

def startEditor():
	uploadButtonBig.destroy()
	designButton.destroy()
	canv.pack()
	setButton.pack()
	delButton.pack()

def placeWall():
	currentTool[0] = "placewall"
def deleteWallTool():
	currentTool[0] = "deletewall"
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
			rects.append(canv.create_rectangle(prevclick[0], prevclick[1], event.x, event.y))
			data.append([min(prevclick[0], event.x), min(prevclick[1], event.y),
				max(prevclick[0], event.x) - min(prevclick[0], event.x), max(prevclick[1], event.y) - min(prevclick[1], event.y)])
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
setButton = Button(root, text = "Wall Tool", command = placeWall, **buttonStylesheet)
delButton = Button(root, text = "Delete Wall Tool", command = deleteWallTool, **buttonStylesheet)
designButton.pack(padx = 10, pady = 10)
canv.bind("<Button-1>", onclick)
root.bind("<z>", removeElement)
root.bind("<Control-p>", lambda _: print(data))

root.mainloop()

'''
A random line generator by Hayden Walker - 27 July 2019 @ 2:29 AM
'''
from tkinter import *
import tkinter.messagebox
import random
import datetime


class MainWindow:
	'''
	A graphical pattern generator
	'''
	def __init__(self, master):
		'''
		Initialize the window
		'''
		master.resizable(False, False)
		master.title("Pattern Generator")
		self.lines = 0
		self.rectangles = 0

		# Menu bar
		self.menubar = Menu(master)
		master.config(menu = self.menubar)
		self.filemenu = Menu(self.menubar)
		self.menubar.add_cascade(label = "File", menu = self.filemenu)
		self.filemenu.add_command(label = "Quit", command = self.quitprog)
		self.menubar.add_command(label = "About", command = self.about)

		# Toolbar
		self.toolbar = Frame(master, relief = RAISED)
		# Label
		numlabel = Label(self.toolbar, text = "Quantity: ")
		numlabel.pack(side = LEFT)
		# Entry field
		self.enternum = Entry(self.toolbar, width = 7)
		self.enternum.pack(side = LEFT)
		# Clear button
		self.clearbutton = Button(self.toolbar, text = "Clear", command = self.cls)
		self.clearbutton.pack(side = RIGHT)
		# Submit button
		self.submit = Button(self.toolbar, text = "Generate Lines", command = self.genlines)
		self.submit.pack(side = RIGHT)
		# Squares button
		self.squares = Button(self.toolbar, text = "Generate rectangles", command = self.genrect)
		self.squares.pack(side = RIGHT)
		# Packing the toolbar
		self.toolbar.pack(side = TOP, fill = X)

		# Canvas
		self.canv = Canvas(width = 500, height = 300, bg = "white")
		self.canv.pack()
		# Status
		self.status = tkinter.StringVar()
		self.status.set("[Status bar]")
		status = Label(master, relief = SUNKEN, bd = 1, textvariable = self.status, anchor = W)
		status.pack(side = BOTTOM, fill = X)

	def genlines(self):
		'''
		Generate a certain number of lines.
		'''
		# Get the input from the entry field and convert to integer
		try:
			lines = int(self.enternum.get())
		except:
			self.status.set(f"{datetime.datetime.now().time()}: Invalid input")
			return 0

		# Generate the specified number of lines
		for i in range(lines):
			# Pick a random start point
			sx = random.randint(0, 500)
			sy = random.randint(0, 300)
			# Pick a random endpoint
			fx = random.randint(0, 500)
			fy = random.randint(0, 300)
			# Pick the line's colour
			colournum = random.randint(0, 3)
			if colournum == 0:
				colour = "red"
			elif colournum == 1:
				colour = "green"
			elif colournum == 2:
				colour = "blue"
			else:
				colour = "yellow"
			# Draw the line
			self.line = self.canv.create_line(sx, sy, fx, fy, fill = colour)
			# Add one to the total number of lines
			self.lines += 1

		# Update the status bar
		self.status.set(f"{datetime.datetime.now().time()}: Drew {lines} lines. Lines: {self.lines} Rectangles: {self.rectangles}")

	def genrect(self):
		# Get input from the entry field
		try:
			runs = int(self.enternum.get())
		except:
			self.status.set(f"{datetime.datetime.now().time()}: Invalid input")	
			return 0

		# Generate a certain number of rectangles
		for i in range(runs):
			# Pick a random start point
			sx = random.randint(0, 500)
			sy = random.randint(0, 300)
			# Pick a random size
			w = random.randint(50, 150)
			h = random.randint(50, 150)
			# Pick a random colour
			colournum = random.randint(0, 3)
			if colournum == 0:
				colour = "red"
			elif colournum == 1:
				colour = "green"
			elif colournum == 2:
				colour = "blue"
			else:
				colour = "yellow"
			# Draw the rectangle
			self.square = self.canv.create_rectangle(sx, sy, h, w, fill = colour)
			self.rectangles += 1
		# Update the status bar
		self.status.set(f"{datetime.datetime.now().time()}: Drew {runs} rectangles. Lines: {self.lines} Rectangles: {self.rectangles}")


	def cls(self):
		'''
		Clear the canvas
		'''
		# Clear the canvas
		self.canv.delete(ALL)
		# Set total lines to 0
		self.lines = 0
		# Update the status bar
		self.status.set(f"{datetime.datetime.now().time()}: Cleared the screen.")

	def about(self):
		tkinter.messagebox.showinfo("About", "A random line generator by Hayden Walker\n27 July 2019 @ 2:37 AM\nBeta 1.0")

	def quitprog(self):
		ans = tkinter.messagebox.askquestion("Quit?", "Do you really wish to exit the program?")
		if ans == "yes":
			quit()
		else:
			return 0

root = Tk()
wind = MainWindow(root)
root.mainloop()

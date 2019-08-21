import os
from tkinter import *


class MainWin:
	def __init__(self, master):
		# Window title/resizability
		master.title("Monty Python Soundboard")
		master.resizable(False, False)

		# Menu bar
		menubar = Menu(master)
		master.config(menu = menubar, bg = "yellow", bd = 5)
		menubar.add_command(label = "Quit", command = lambda: quit())

		# Buttons
		naughtyboy = Button(master, text = "Naughty", command = lambda: os.system("aplay naughty.wav&"))
		naughtyboy.grid(row = 0, column = 0)

		bigus = Button(master, text = "Bigus", command = lambda: os.system("aplay bigus.wav&"))
		bigus.grid(row = 0, column = 1)

		weirdo = Button(master, text = "Weirdo", command = lambda: os.system("aplay weirdo.wav&"))
		weirdo.grid(row = 0, column = 2)

		discuss = Button(master, text = "Discuss", command = lambda: os.system("aplay discuss.wav&"))
		discuss.grid(row = 1, column = 0)

		oddball = Button(master, text = "Oddball", command = lambda: os.system("aplay oddball.wav&"))
		oddball.grid(row = 1, column = 1)

		woger = Button(master, text = "Woger", command = lambda: os.system("aplay woger.wav&"))
		woger.grid(row = 1, column = 2)

		hide = Button(master, text = "Hide", command = lambda: os.system("aplay hide.wav&"))
		hide.grid(row = 2, column = 0)

		nasty = Button(master, text = "Nasty", command = lambda: os.system("aplay nasty.wav"))
		nasty.grid(row = 2, column = 1)

		waste = Button(master, text = "Waste", command = lambda: os.system("aplay waste.wav&"))
		waste.grid(row = 2, column = 2)

root = Tk()
mw = MainWin(root)
root.mainloop()

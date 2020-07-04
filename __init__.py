"""
PyFiles 1.0
Angus Goody
04/07/2020
"""

#=================IMPORTS================
from shed.colourTools import *
from shed.storageTools import *
from shed.tkinterTools import *

#=================WINDOW SETUP================

class window(Tk):
	"""
	The window class is the main
	class for the whole program
	"""
	def __init__(self):
		Tk.__init__(self)
		#Setup
		self.geometry("400x300")
		self.title("PyFiles")


#Run window
if __name__ == "__main__":
	window=window()
	window.mainloop()
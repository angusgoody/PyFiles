"""
PyFiles 1.0
Angus Goody
04/07/2020
"""

#=================IMPORTS================
from shed.colourTools import *
from shed.storageTools import *
from shed.tkinterTools import *


# =========SCREENS==========
class homeScreen(screen):
    """
    Screen where user selects
    which diary file to open
    """
    def __init__(self,controller):
        screen.__init__(self,controller,"Open")
        #Configure rows
        self.grid_rowconfigure(2,weight=1)
        self.grid_columnconfigure(0,weight=1)
        #Create frames
        self.topBar=mainFrame(self)
        self.filterFrame=mainFrame(self)
        self.middle=mainFrame(self)
        self.bottomBar=mainFrame(self)
        #Position Frames
        self.topBar.grid(row=0,column=0,sticky="EW",padx=20,pady=20)
        self.filterFrame.grid(row=1,column=0,sticky="EW")
        self.middle.grid(row=2,column=0,sticky="NSEW")
        self.bottomBar.grid(row=3,column=0,sticky="EW")
        #Configire Frames
        #---Top---
        self.topBar.grid_rowconfigure(0,weight=1)
        self.topBar.grid_columnconfigure(0,weight=1)
        #---Middle---
        self.middle.grid_rowconfigure(0,weight=1)
        self.middle.grid_columnconfigure(0,weight=1)


        #-----Top Bar-------
        self.pathEntry=Entry(self.topBar,state=DISABLED)
        self.pathEntry.grid(row=0,column=0,sticky="EW")
        self.pathButton=Button(self.topBar,text="Browse")
        self.pathButton.grid(row=0,column=1,padx=(10,0))

        #-----Middle-------
        self.mainListbox=advancedListbox(self.middle)
        self.mainListbox.grid(row=0,column=0,sticky="NSEW")

        #-----Bottom-------
        self.myButton=Button(self.bottomBar,text="Hello")
        self.myButton.grid(row=0,column=0)



# =========MAIN PROGRAM==========
class PyFiles(Tk):
	"""
	This class is the main
	program class and controls
	how the whole program will work
	"""
	def __init__(self):
		Tk.__init__(self)
		#Setup
		self.title("PyFiles")
		self.geometry("600x500")
		self.grid_rowconfigure(0,weight=1)
		self.grid_columnconfigure(0,weight=1)
		#Create a screenmaster
		self.screenMaster=screenController(self)
		self.screenMaster.grid(row=0,column=0,sticky="NSEW")
		#Project Manager setup
		self.projectManager=projectManager(getWorkingDirectory(),"PyFiles")
		self.projectManager.fileExtension=".pf"

		#Screens
		self.homeScreen=homeScreen(self.screenMaster)
		self.homeScreen.show()

		#Last calls

#Final Call
if __name__ == '__main__':
	window=PyFiles()
	window.mainloop()


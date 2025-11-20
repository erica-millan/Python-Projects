#import tkinter module, choosing all the widgits with *
import tkinter
from tkinter import *

#region
#frame is the parent class from tkinter that we will be inheriting from
#we pass in master so we can start referencing our frame as master
#endregion

class ParentWindoww(Frame):
      #region         
      # __init__ --> when Python first initialses your class the first thing it will do is find the 
      #__init function__ if it's there then run what ever is underneath it.
      #giving self it's like the key so it has access to all the info
      #within the class, we put in master so we can start referecning 
      #our frame as master, and our class as self.
      #endregion}
    def __init__ (self, master):
       Frame.__init__ (self)
       #region
       #you have to use "self" when you're referncing class items.
       #putting master into self.master, so whenevr we need to use it we will use self.master
       #self.master is primary window that pops up on screen
       #endregion
       self.master = master
       #region
      #window can not be resized setting it to false
       #endregion
       self.master.resizable(width=False, height=False)
       #region
       #700 pixels wide by 400 pixels height
       #endregion
       self.master.geometry('{}x{}'.format(700, 400))
       self.master.title('Learning Tkinter!')
       self.master.config(bg='lightgray')
       #region
       #StringVar() is a tkinter class that allows us to create text boxes
       #it allows us to create a variable that can be used to store and retrieve text
       #we create an instance of it and assign it to a variable
       #this variable can then be used to get or set the text in the text box
       #by writing StringVar() we are creating an instance of the class
       #Then we assign it to a variable so we can use it later. in this case 
       #self.varFName and self.varLName are variables that will hold the text entered into the text boxes
       #once you have the name you can use the get() and set() methods to retrieve or update the text. 
       #endregion
       self.varFName = StringVar()
       self.varLName = StringVar()

       self.lblFName = Label(self.master, text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
       #region
       #in padx we are saying put 10 pixels of padding on the left side and 0 on the right side
       #in pady we are saying put 10 pixels of padding on the top side and 0 on the bottom side
       #same for all the other labels and entry boxes
       #endregion       
       self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

       self.lblLName = Label(self.master, text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
       self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

       self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightgray')
       self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
        #region
        #by doing entry(self.master...) we basically saying place this entry box onto the master window- self.master is the plain window
        #text will always = what is being stored in varFName, 
        #font is a tuple that contains the font family and size
        #fg is foreground color of the text
        #bg is background color of the text box
        #everything in the () is instantiating the entry class and giving blueprints for how we want the entry box to look
        #then we put it in self.txtFName so we can reference it later
        #endregion       
       self.txtFName = Entry(self.master, text=self.varFName, font = ("Helvetica", 16), fg='black', bg='lightblue')
       #command to paint onto the window
       self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

       self.txtLName = Entry(self.master, text=self.varLName, font = ("Helvetica", 16), fg='black', bg='lightblue')
       #command to paint onto the window
       self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))
       #region
       #when button is clicked it will call the submit method which is why we have command=self.submit
       #same for the cancel button
       #endregion
       self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
       self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

       
       self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
       #region
       #the grid is the command to paint onto the window
       # everythig is the same but padx is (0,90) so 0 pixels 
       # on left side and 90 pixels on right side so that it's side by side with submit button  
       # endregion    
       self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

       #region
       #inside submit is going to be self because it's a part of the class so it's required 
       # to be referred to as self. You have to pass the key 
       #self is the class instance so it has access to all the info within the class
       #submit is the name of the method
       #in the submit method we will be getting the value of the text from the entry boxes with the get() method
       #you're getting value from vriable name not the text box itself, since the variable name is what
       #variable the value is stored in
       #endregion
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        #region
        #to get somethign to change dynamically in the middle of the program you have to use the config() method
        #endregion
        self.lblDisplay.config(text="Hello {} {}!".format(fn, ln))
    def cancel(self):
        self.master.destroy()
      #region
      # tk() is tkinters main class and we named it root
      # we are attaching it to our parent window
      # once it's instantiated were passing it to app
      # the room.mainloop() line allows window to continuously run.
      #endregion
if __name__ == "__main__":
    #region
    #first line instantiates tkinter
    #instantiating tkinter will be calling on the class
    # now called on the class object (Tk). So we have an instance of it and we name it root.
    #endregion
    root = Tk()
    #region
    #next line is basically passing it over to our class program
    #next syntax when you're dealing with tkinter is doing App = ParentWindow and attatching it to root
    #we put our root object inside the parenthesis so now parent window (frame). the Tk() is thde frame. we named
    # it root and are now attaching to our parent window.
    #once that's instantiated our class is, our class is instantiated with the tkinter class instantiated
    #and we're passing it to app.
    #endregion
    App = ParentWindoww(root)
    #region
    #last line creates a main loop for that to run so the window constantly stays open
    #mainloop() keeps the window staying open and alive until we close the main loop
    #endregion
    root.mainloop()
    

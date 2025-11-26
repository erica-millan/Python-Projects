import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Default HTML button
        self.btn= Button(self.master, text="Default HTML Page", width=25, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10, 5), pady=(0, 15))

        #  User instructions
        self.label = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 5))

        # Custom text box
        self.txtBox = Entry(self.master, width=60)
        self.txtBox.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))

        # Custom HTML button
        self.btnCustom = Button(self.master, text="Submit Custom Text", width=25, height=2, command=self.customHTML)
        self.btnCustom.grid(row=2, column=1, padx=(5, 10), pady=(0, 15))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        #generate custom HTML 
    def customHTML(self):
        #retrieve text from entry widgit self.txtbox
        htmlText = self.txtBox.get()
        #open or create file names index.html
        htmlFile = open("index.html", "w")
        #build content as a string
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #write html content to file
        htmlFile.write(htmlContent)
        #close html file
        htmlFile.close()
        #open html file in default browser
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

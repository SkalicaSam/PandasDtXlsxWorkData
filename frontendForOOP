from tkinter import *
from backend import Datas, file_finder



class Window(object):
    
    def __init__(self, window):        
        self.window = window
        self.window.title("Extracting program from .xlsx  1.0")
        
        global file_text
        
        # Label = label with text
        l2 = Label(window, text = "Exceptation file for disposibility: ")
        l2.grid(row = 0, column = 1)
        # Button
        b1 = Button(window, text = "Extract", width = 12, command = self.uprav)
        b1.grid(row= 0, column= 4)
        
        b2 = Button(window, text = "About", width = 12, command = self.create_secondwindow )
        b2.grid(row= 1, column= 3)

        b3 = Button( window ,text = "Exit", width = 12, command = window.destroy)
        b3.grid(row= 1, column= 4)
        # entry 
        self.file_text = StringVar()
        self.e1=Entry(window,textvariable = self.file_text, width = 15)
        self.e1.grid(row = 0, column = 3 )
        window.mainloop()
        
    def uprav(self):
        global nameExpect
        self.file = str(self.file_text.get())
        file_finder(self.file)
        nameExpect = self.file

    def create_secondwindow(self):
        create_secondwindow1 = Tk()
        create_secondwindow1.title("About")
        label1 = Label(create_secondwindow1, text = " Program na hromadnu upravu tabuliek")
        label1.grid(row = 1, column = 1)
        label3 = Label(create_secondwindow1, text = " Support: samcostehlik@gmail.com   ")
        label3.grid(row = 3, column = 1)
        create_secondwindow1.mainloop()
        

window = Tk()
Window(window)















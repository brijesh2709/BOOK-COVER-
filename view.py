# imports controller, tkinter, PIL
import controller as c
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk


# main class for tkinter GUI
class Main_GUI(Frame):

    # initializes the class
    def __init__(self):
        pass

    # main tkinter window
    def main_screen(self, master=None):
        # we create the window
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry('300x120')
        
        # we create a label
        self.label = Label(master, text='Please Input the name of the book')
        self.label.pack()

        self.e = Entry(master, width=20)
        self.e.pack()
        self.e.focus_set()

        self.label = Label(master, text='Try: Little Women')
        self.label.pack()
        
        # we create a button
        self.close_button = Button(master, text='I think it is time to Quit', 
                                   command=master.destroy)
        self.close_button.pack(side='bottom')
        
        self.ISBN_data = Button(master, text='View Cover', 
                                command=self.get_det)
        self.ISBN_data.pack(side='bottom')

    # getting book details
    def get_det(self):
        # gets the details
        global e
        string = self.e.get()
        string = string.replace(" ", "+")
        # opens controller to access model
        t = c.opensourcecontroller()
        img = Image.open(t.photo(string))
        # creates a new window for the book cover
        window = Toplevel()
        window.title('Book Cover')
        window.geometry('700x700')
        window.configure(background='grey')
        path = 'picture.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(window, image=img)
        panel.pack(side='bottom', fill='both', expand='yes')
        window.mainloop()

    # main functionality for the tkinter screen
    def run(self):
        root = Tk()
        my_gui = Main_GUI()
        my_gui.main_screen(root)
        root.wm_title('Book Covers')
        root.mainloop()

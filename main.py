from tkinter import *
from matplotlib.figure import Figure
import os
import glob
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def opening_window():
    root = Tk()
    root.title("Opening Window")
    root.attributes("-fullscreen",True)
    root.configure(background = "grey34")
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()
    x_size = win_width * 0.3
    y_size = win_height * 0.1
    #Opening text
    title = Label(
        text = "Molecule Application",
        font = ("Times",40), fg = "purple",
        bg = "grey70", width = 20,
        borderwidth = 3, relief = "solid")
    title.place(anchor = CENTER, rely = 0.1, relx = 0.5)
    # Button to go to app section
    app_button = Button(text="Enter Application",bg = "grey70", command=lambda: application_window(root))
    app_button.place(anchor = CENTER, relx = 0.5, rely = 0.45, width = x_size, height = y_size)    
    # Button to quit
    quit_button = Button(text="Quit",bg = "grey70",command=root.destroy)
    quit_button.place(anchor = CENTER, relx = 0.5, rely = 0.65, width = x_size, height = y_size)
    root.mainloop() 

def application_window(root):
    global application_window
    root.destroy()
    application_window = Tk()
    application_window.title("molecular properties")
    application_window.attributes("-fullscreen", True)
    win_width = application_window.winfo_screenwidth()
    win_height = application_window.winfo_screenheight()
    back_button = Button(text="Back to menu",command=lambda: go_to_opening_window(application_window))
    back_button.place(anchor = NW, width=100, height=100)
    ##creating the canvas for which the molecule will be drawn onto
    molecule_canvas = Canvas(application_window, bg = "white",
                             width = win_width*0.6,highlightbackground="black",
                             height = win_height*0.8)
    molecule_canvas.place(anchor = N, relx = 0.45)


def go_to_opening_window(root):
    root.destroy()  # Close the opening window
    opening_window()
opening_window()

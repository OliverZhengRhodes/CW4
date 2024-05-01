from tkinter import *
global molecules
import tkinter as tk
from PIL import Image, ImageTk
from rdkit import Chem
from rdkit.Chem import Draw
molecules = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
             "16","17","18","19","20"]
molecule_information = {
    "melting point":"",
    "boiling point":"",
    "hazards":"",
    "uses":""}
def on_mousewheel(event):
    y_offset = int(-1 * (event.delta / 120))
    canvas_height = molecule_button_canvas.winfo_height()
    frame_height = molecule_button_canvas.bbox("all")[3] - molecule_button_canvas.bbox("all")[1]
    bottom_boundary = 0
    top_boundary = canvas_height
    current_y = molecule_button_canvas.canvasy(0)
    
    if y_offset < 0:  # Check if scrolling downwards
        if current_y + y_offset >= bottom_boundary:
            molecule_button_canvas.yview_scroll(y_offset, "units")
    else:  # Check if scrolling upwards
        if current_y + y_offset <= top_boundary:
            molecule_button_canvas.yview_scroll(y_offset, "units")



def create_scrollable_buttons(frame):
    global molecules
    buttons = []
    for i in range(20):
        command_func = globals().get(f"button_{i + 1}_command")
        button = Button(frame, text=f"{molecules[i]}", width=40, height=5, command=command_func)
        button.grid(row=i, column=0, pady=5)
        buttons.append(button)
    return buttons

def button_1_command():
    display_molecule_image("[Co-2](Cl)(Cl)(Cl)Cl")
    display_molecule_information(1)

def button_2_command():
    print("Button 2 clicked!")

def display_molecule_image(mol_text):
    global molecule_canvas
    
    # Create an RDKit molecule (you can replace this with your own molecule)
    mol = Chem.MolFromSmiles(mol_text)

    # Render the molecule
    img = Draw.MolToImage(mol)

    # Resize the image to fit the canvas
    img = img.resize((molecule_canvas.winfo_width(), molecule_canvas.winfo_height()))

    # Convert the PIL image to a Tkinter-compatible format
    photo = ImageTk.PhotoImage(img)

    # Display the molecule image on the molecule_canvas
    molecule_canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Keep a reference to the photo object to prevent it from being garbage collected
    molecule_canvas.photo = photo



def opening_window():
    root = Tk()
    root.title("Opening Window")
    root.attributes("-fullscreen", True)
    root.configure(background="grey34")
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()
    x_size = win_width * 0.3
    y_size = win_height * 0.1
    # Opening text
    title = Label(
        text="Molecule Application",
        font=("Times", 50), fg="purple",
        bg="grey70", width=20,
        borderwidth=3, relief="solid")
    title.place(anchor=CENTER, rely=0.1, relx=0.5)
    # Button to go to app section
    app_button = Button(text="Enter Application", bg="grey70", font=("Arial", 40),
                        command=lambda: application_window(root))
    app_button.place(anchor=CENTER, relx=0.5, rely=0.45, width=x_size, height=y_size)
    # Button to quit
    quit_button = Button(text="Quit", bg="grey70", font=("Arial", 40), command=root.destroy)
    quit_button.place(anchor=CENTER, relx=0.5, rely=0.65, width=x_size, height=y_size)
    root.mainloop()

def application_window(root):
    global molecule_canvas
    root.destroy()
    application_window = Tk()
    application_window.title("molecular properties")
    application_window.attributes("-fullscreen", True)
    win_width = application_window.winfo_screenwidth()
    win_height = application_window.winfo_screenheight()
    # creating the back button
    back_button = Button(text="Back to menu", command=lambda: go_to_opening_window(application_window),
                         font=("Helvetica", 31))
    back_button.place(x=0, y=win_height * 0.925)
    # creating the label above where you choose which molecule to create
    molecule_title = Label(
        text="Molecules", font=("Arial", 31), fg="purple",
        bg="grey70", width=12,
        borderwidth=2, relief="solid")
    molecule_title.place(x=0, y=0)
    # creating the canvas for which the molecule will be drawn onto
    molecule_canvas = Canvas(application_window, bg="white",
                             width=round(win_width * 0.6), highlightbackground="black",
                             height=round(win_height))
    molecule_canvas.place(anchor=N, relx=0.45)
    # creating the canvas which will hold the scrollable buttons, which
    # will produce the image of the selected molecule
    global molecule_button_canvas
    molecule_button_canvas = Canvas(application_window, bg="blue",
                                    width=round(win_width * 0.145), highlightbackground="black",
                                    height=round(win_height * 0.875))
    molecule_button_canvas.place(anchor=N, relx=0.075, rely=0.045)
    # Create a frame to hold the buttons
    buttons_frame = Frame(molecule_button_canvas, bg="blue")
    molecule_button_canvas.create_window((0, 0), window=buttons_frame, anchor='nw')
    # Create scrollable buttons inside the frame
    global buttons
    buttons = create_scrollable_buttons(buttons_frame)
    # Add a scrollbar to the canvas
    scrollbar = Scrollbar(application_window, orient=VERTICAL, command=molecule_button_canvas.yview)
    scrollbar.place(in_=molecule_button_canvas, relx=1, rely=0, relheight=1)
    molecule_button_canvas.configure(yscrollcommand=scrollbar.set)
    # Bind mousewheel event to the canvas
    molecule_button_canvas.bind_all("<MouseWheel>", on_mousewheel)


def go_to_opening_window(root):
    root.destroy()  # Close the opening window
    opening_window()

opening_window()

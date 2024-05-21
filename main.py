import tkinter as tk
from PIL import Image, ImageTk
from rdkit import Chem
from rdkit.Chem import Draw
from lib.molecules import *
from lib.orca import * 

global molecules, data_label
def on_mousewheel(event):
    y_offset = int(-1 * (event.delta / 120))
    canvas_height = molecule_button_canvas.winfo_height()
    frame_height = molecule_button_canvas.bbox("all")[3] - molecule_button_canvas.bbox("all")[1]
    bottom_boundary = 0
    top_boundary = canvas_height
#gets the current height of the button selection, so that
#it can detect whether the user can scroll up or whether not
    current_y = molecule_button_canvas.canvasy(0)   
    if y_offset < 0:  # Check if scrolling downwards
        if current_y + y_offset >= bottom_boundary:
            molecule_button_canvas.yview_scroll(y_offset, "units")
    else:  # Check if scrolling upwards
        if current_y + y_offset <= top_boundary:
            molecule_button_canvas.yview_scroll(y_offset, "units")



def create_scrollable_buttons(frame):
    global molecules
#creates an empty list called buttons
    for i in range(20):
        command_func = globals().get(f"button_{i + 1}_command")
#defines the function for each of the buttons as button_no._command
#all of the buttons through i in range 20 will recieve their own
#function
        button = Button(frame, text=f"{molecules[i]}",font=("Times", 10),  width=40, height=5, command=command_func)
        button.grid(row=i, column=0, pady=5)
#places the buttons on the same column, so that they are all in line
#but then places them on different rows with a padding
#so that the buttons have some spacing between them

#ammonia
def button_1_command():
    display_molecule_image("[NH3]")
    display_molecule_information(0)
    name.configure(text = molecules[0])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#aspirin
def button_2_command():
    display_molecule_image("O=C(C)Oc1ccccc1C(=O)O")
    display_molecule_information(1)
    name.configure(text = molecules[1])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#calcium oxide
def button_3_command():
    display_molecule_image("[Ca+2].[O-2]")
    display_molecule_information(2)
    name.configure(text = molecules[2])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#carbon dioxide
def button_4_command():
    display_molecule_image("O=C=O")
    display_molecule_information(3)
    name.configure(text = molecules[3])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#cobalt tetrachloride
def button_5_command():
    display_molecule_image("[Co-2](Cl)(Cl)(Cl)Cl")
    display_molecule_information(4)
    name.configure(text = molecules[4])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#DDT
#close Clc1cc(Cl)cc(c1Cl)C(c2cc(Cl)cc(Cl)c2)Cl
    #still figuring this one 
def button_6_command():
    display_molecule_image("ClC1=CC=C(C=C1)C(Cl)(Cl)C(Cl)(Cl)Cl")
    display_molecule_information(5)
    name.configure(text = molecules[5])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#ethanol
def button_7_command():
    display_molecule_image("CCO")
    display_molecule_information(6)
    name.configure(text = molecules[6])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#ethylene
def button_8_command():
    display_molecule_image("C=C")
    display_molecule_information(7)
    name.configure(text = molecules[7])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#morhpine CN1CCC23C4C1CC5=C2C(=C(C=C5)O)OC3C(C=C4)O looks goofy
def button_9_command():
    display_molecule_image("CN1CCC23C4C1CC5=C2C(=C(C=C5)O)OC3C(C=C4)O")
    display_molecule_information(8)
    name.configure(text = molecules[8])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#penicilin
def button_10_command():
    display_molecule_image("CC1([C@@H](N2[C@@H](S1)[C@@H](C2=O)NC(=O)Cc3ccccc3)C(=O)O)C")
    display_molecule_information(9)
    name.configure(text = molecules[9])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#phosphoric acid
def button_11_command():
    display_molecule_image("OP(=O)(O)O")
    display_molecule_information(10)
    name.configure(text = molecules[10])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#potassium nitrate
def button_12_command():
    display_molecule_image("[K+].[N+](=O)([O-])[O-]")
    display_molecule_information(11)
    name.configure(text = molecules[11])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#progestin
def button_13_command():
    display_molecule_image("CC(C)CCC1C2CCC3C(CCC4=CC(=O)CCC34C)C2CCC1=O")
    display_molecule_information(12)
    name.configure(text = molecules[12])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#sodium chloride
def button_14_command():
    display_molecule_image("[Cl][Na]")
    display_molecule_information(13)
    name.configure(text = molecules[13])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#sodium hydroxide
def button_15_command():
    display_molecule_image("[Na][OH]")
    display_molecule_information(14)
    name.configure(text = molecules[14])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#sodium stearate
def button_16_command():
    display_molecule_image("CCCCCCCCCCCCCCCC(=O)[O-].[Na+]")
    display_molecule_information(15)
    name.configure(text = molecules[15])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#silicon dioxide
def button_17_command():
    display_molecule_image("O=[Si]=O")
    display_molecule_information(16)
    name.configure(text = molecules[16])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#sulfuric acid
def button_18_command():
    display_molecule_image("OS(=O)(=O)O")
    display_molecule_information(17)
    name.configure(text = molecules[17])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#toluene
def button_19_command():
    display_molecule_image("Cc1ccccc1")
    display_molecule_information(18)
    name.configure(text = molecules[18])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
#urea
def button_20_command():
    display_molecule_image("NC(N)=O")
    display_molecule_information(19)
    name.configure(text = molecules[19])
    name.place(anchor=CENTER, rely=0.05, relx=0.45)
    
def display_molecule_information(x):
    global data_label
    #this is the label which will display all of the information for
    #the currently selected moleule
    #using the ascii to make certain words underlined and to include
    #the degree symbol
    #molecule_information is a dictionary which is in molecules.py
    data_label.configure(text = ("\u0332".join("Introduction")+"\n"+molecule_information["introduction"][x]+"\n"+"\u0332".join("Melting Point")+"\n"+
                                 molecule_information["melting point"][x]+u"\u2103"+"\n"+"\u0332".join("Boiling Point")+"\n"+
                                 molecule_information["boiling point"][x]+u"\u2103"+"\n"+"\u0332".join("Hazards")+"\n"+
                                 molecule_information["hazards"][x]+"\n"+"\u0332".join("Uses")+"\n"+
                                 molecule_information["uses"][x]))
def display_molecule_image(mol_text):
    global molecule_canvas
    
    # Create an RDKit molecule (you can replace this with your own molecule)
    mol = Chem.MolFromSmiles(mol_text)

    # Render the molecule
    img = Draw.MolToImage(mol)

    # Calculate the desired width and height for the molecule canvas
    canvas_width = 0.6 * molecule_canvas.winfo_screenwidth()  # Adjust as needed
    canvas_height = 0.8 * molecule_canvas.winfo_screenheight()  # Adjust as needed
    
    # Resize the image to fit the canvas
    img = img.resize((int(canvas_width), int(canvas_height)))
    
    # Convert the PIL image to a Tkinter-compatible format
    photo = ImageTk.PhotoImage(img)

    # Display the molecule image on the molecule_canvas
    molecule_canvas.create_image(0, 250, anchor=tk.NW, image=photo)

    # Keep a reference to the photo object to prevent it from being garbage collected
    molecule_canvas.photo = photo

def read_file(x):
    with open(x,"r") as file:
        text1 = file.read()
        spe_label.configure(text = text1)
        spe_label.place(x=800, y=win_height * 0.925)
    
def opening_window():
    global win_height
    root = Tk()
    root.title("Opening Window")
    root.attributes("-fullscreen", True)
    root.configure(background="grey34")
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()
    #these sizes will be used as a reference when determining
    #the size of other labels
    x_size = win_width * 0.3
    y_size = win_height * 0.1
    # Opening text
    title = Label(
        text="Molecule Application",
        font=("Times", 50), fg="purple",
        bg="grey70", width=20,
        borderwidth=3, relief="solid")
    title.place(anchor=CENTER, rely=0.1, relx=0.5)
    #subtext title
    subtext = Label(
        text="20 Important Chemicals in Science",
        font=("Times", 20), fg="purple",
        bg="grey70", width=40,
        borderwidth=3, relief="solid")
    subtext.place(anchor=S, rely=0.2, relx=0.5)
    # Button to go to app section
    app_button = Button(text="Enter Application", bg="grey70", font=("Arial", 40),
                        command=lambda: application_window(root))
    app_button.place(anchor=CENTER, relx=0.5, rely=0.45, width=x_size, height=y_size)
    # Button to quit
    quit_button = Button(text="Quit", bg="grey70", font=("Arial", 40), command=root.destroy)
    quit_button.place(anchor=CENTER, relx=0.5, rely=0.65, width=x_size, height=y_size)
    root.mainloop()

def application_window(root):
    global molecule_canvas, name, data_label, spe_label
    root.destroy()
    #destroys the opening window
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
    molecule_canvas.place(anchor=N, relx=0.45, rely = -0.16)
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
    #creating a label that will say the name of the molecule
    name = Label(
        text="",
        font=("Times", 40), fg="purple",
        bg="grey70", width=30,
        borderwidth=3, relief="solid")
    #creating a label that will say the data of the molecule
    data_label = Label(
        text="", fg="purple",
        bg="grey70", width=60,height = 70,
        borderwidth=3, relief="solid", anchor = NW, justify ="left")
    data_label.place(anchor=CENTER, rely=0.50, relx=0.875)
    #spe
    #
    orca_read_button = Button(text="Read Orca", command=lambda: read_file("orca_calc_results.txt"),
                         font=("Helvetica", 31))
    orca_read_button.place(x=300, y=win_height * 0.85)
    #spe display
    spe_label = Label(
        text="", fg="purple",
        bg="grey70", width=55,height = 1,
        font = ("Arial", 15),
        borderwidth=3, relief="solid", anchor = CENTER, justify ="left")
    #button that runs the orca
    orca_button = Button(text="Run Orca Calculations", command=lambda: run_orca_thread(name["text"]),
                         font=("Helvetica", 31))
    orca_button.place(x=300, y=win_height * 0.925)
    
def go_to_opening_window(root):
    root.destroy()  # Close the opening window
    opening_window()

opening_window()
#add orca generate an input file and dropdown to generate and run calculations eg. coordinates, energies

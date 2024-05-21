import os
import subprocess
import threading
#this is so that when the run orca calculation button is clicked
#the program does not freeze as the calculations will be runing
#on a separate thread
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from rdkit import Chem
from rdkit.Chem import Draw
def write_to_text_file(name, data, filename):
    print(data)
    with open(filename, 'w') as file:
        file.write(name+" has single point energy: "+data+"(Eh)")

# ORCA calculation functions
def write_orca_input(molecule, filename):
    with open(filename, 'w') as f:
        f.write(f"""! SP B3LYP def2-SVP 
{molecule}
*
""")

def run_orca(input_file, output_file):
    try:
        command = f'orca {input_file} > {output_file}'
        #this is what you would type in command line to produce the
        #output file from running orca
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result.check_returncode()
        print("ORCA execution successful.")
        #this was useful in testing 
        if result.stderr:
            print("ORCA standard error output:")
            #this was useful in testing
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"ORCA failed with error: {e.stderr}")
        #this was useful in testing
        raise

def extract_energy(output_file):
    energy = None
    try:
        with open(output_file, 'r') as f:
            for line in f:
            #reads through every line in the output file
                if 'FINAL SINGLE POINT ENERGY' in line:
                    #if it finds "FINAL SINGLE POINT ENERGY" in the output
                    #file, it takes the float value as energy
                    energy = float(line.split()[4])
                    break
    except FileNotFoundError:
        print(f"Output file {output_file} not found.")
    return energy

def orca_calculation(molecule_choice):
    molecules_data = {
#these are parts of the input files
    'Ammonia': """\
* xyz 0 1
N    0.000000    0.000000    0.000000
H    0.000000    0.942341    0.333333
H    0.816497   -0.471170    0.333333
H   -0.816497   -0.471170    0.333333
""",
    'Aspirin': """\
* xyz 0 2
C    1.399334    0.000000    0.000000
C    0.000000    0.000000    0.000000
C   -0.699667    1.209163    0.000000
C    0.000000    2.418327    0.000000
C    1.399334    2.418327    0.000000
C    2.098668    1.209163    0.000000
O    2.098668   -1.209163    0.000000
O    3.497501    1.209163    0.000000
H   -1.768800    1.209163    0.000000
H   -0.349834    3.355986    0.000000
H    1.749167    3.355986    0.000000
""",
    'Calcium Oxide': """\
* xyz 0 1
Ca    0.000000    0.000000    0.000000
O     1.000000    0.000000    0.000000
""",
    'Carbon Dioxide': """\
* xyz 0 1
O    0.000000    0.000000    1.160000
C    0.000000    0.000000    0.000000
O    0.000000    0.000000   -1.160000
""",
    'Cobalt Tetrachloride': """\
* xyz 0 2
Cl   -1.443454    1.024827    0.000000
Cl    1.443454    1.024827    0.000000
Cl   -1.443454   -1.024827    0.000000
Cl    1.443454   -1.024827    0.000000
Co    0.000000    0.000000    0.000000
""",
    'DDT': """\
* xyz 0 2
C    2.64362   -0.11156   -0.11632
C    1.29221    0.33320   -0.10704
C    0.48522   -0.72222    0.18789
C   -0.73329   -0.40765    0.12672
C   -1.31372    0.86980    0.07337
C   -0.52780    1.93357   -0.01024
C    0.70892    1.61355   -0.00664
C    2.12235    2.01789   -0.07923
Cl   -2.98023   -0.13510    0.16114
Cl    3.73912    0.23395   -0.18441
Cl    0.20298   -2.05453    0.42618
Cl   -0.87717    3.31632   -0.04887
C    1.37311    3.37478   -0.11766
C    2.15736    4.33059   -0.19159
C    3.53679    3.96469   -0.19841
H    2.63316   -0.16431   -1.20213
H    1.37069    0.38045   -1.18177
H    0.64897   -0.82151    1.26426
H    1.40679    5.21070   -0.25982
H    4.17539    4.74011   -0.24956
H    3.58838    2.98224   -0.18067
H   -2.29193    1.52425    0.01834
H    0.99898    0.54879   -0.05514
H   -0.95222   -1.29348    0.24793
""",
    'Ethanol': """\
* xyz 0 1
C    0.000000    0.000000    0.000000
C    1.529000    0.000000    0.000000
O    2.145000    1.165000    0.000000
H   -0.553000    0.553000    0.000000
H   -0.553000   -0.553000    0.000000
H    1.865000   -0.616000   -0.889000
H    1.865000   -0.616000    0.889000
H    1.865000    0.616000    0.889000
H    1.865000    0.616000   -0.889000
""",
    'Ethylene': """\
* xyz 0 1
C    0.000000    0.000000    0.000000
C    1.339000    0.000000    0.000000
H    0.000000    1.093000    0.000000
H    0.000000   -1.093000    0.000000
H    1.339000    1.093000    0.000000
H    1.339000   -1.093000    0.000000
""",
    'Morphine': """\
* xyz 0 2
C    1.265600    0.000000    0.000000
C    0.000000    0.000000    0.000000
C   -0.677200    1.175330    0.000000
C    0.000000    2.350660    0.000000
C    1.265600    2.350660    0.000000
C    1.943200    1.175330    0.000000
O    2.580000    0.000000    0.000000
N   -1.353300    1.175330    0.000000
H    0.000000   -1.043530    0.000000
H    1.943200   -1.175330    0.000000
H   -0.339100    3.394190    0.000000
H    1.606300    3.394190    0.000000
H   -1.353300    2.130660    0.000000
H   -1.353300    0.220000    0.000000
H    2.580000    1.175330    0.000000
H    2.580000   -1.175330    0.000000
""",
    'Penicillin G': """\
* xyz 0 1
C   -1.209200    1.429460    0.000000
C    0.000000    0.714730    0.000000
C    1.209200    1.429460    0.000000
N   -0.704600   -0.617270    0.000000
C    0.000000   -1.429460    0.000000
C    1.209200   -0.714730    0.000000
O    2.418400    1.429460    0.000000
O   -1.418300    2.763600    0.000000
O    0.704600    2.143200    0.000000
H   -2.143600    1.000000    0.000000
H    2.143600    1.000000    0.000000
H   -0.704600   -2.377600    0.000000
H    1.418300   -1.418300    0.000000
H    2.763600    1.000000    0.000000
""",
    'Phosphoric Acid': """\
* xyz 0 1
O   -1.229300   -0.456500    0.000000
P    0.000000    0.000000    0.000000
O    1.229300   -0.456500    0.000000
O    0.000000    1.347600    0.000000
O    0.000000   -1.347600    0.000000
H    0.000000    1.793700    0.000000
H    0.000000   -1.793700    0.000000
H   -1.793700   -0.456500    0.000000
""",
    'Potassium Nitrate': """\
* xyz 0 1
K    0.000000    0.000000    0.000000
N    0.000000    1.500000    0.000000
O    1.200000    2.100000    0.000000
O   -1.200000    2.100000    0.000000
O    0.000000    3.300000    0.000000
""",
    'Progestin': """\
* xyz 0 2
C   -1.197100   -0.368700    0.000000
C    0.000000   0.000000    0.000000
C    0.000000   0.368700    0.000000
C    0.000000   0.737400    0.000000
C    0.000000   1.106100    0.000000
C    0.000000   1.474800    0.000000
H   -1.292800   -1.157600    0.000000
H   -1.155600    0.000000    0.000000
H    0.155600   0.000000    0.000000
H    0.000000    0.737400    1.155600
H    0.000000   -0.737400    1.155600
H    0.000000    0.737400   -1.155600
H    0.000000   -0.737400   -1.155600
""",
    'Sodium Chloride': """\
* xyz 0 1
Na   0.000000    0.000000    0.000000
Cl   2.000000    0.000000    0.000000
""",
    'Sodium Hydroxide': """\
* xyz 0 1
Na    0.000000    0.000000    0.000000
O     1.000000    0.000000    0.000000
H     2.000000    0.000000    0.000000
""",
    'Sodium Stearate': """\
* xyz 0 2
Na   0.000000    0.000000    0.000000
C    1.000000    0.000000    0.000000
C    2.000000    0.000000    0.000000
C    3.000000    0.000000    0.000000
C    4.000000    0.000000    0.000000
C    5.000000    0.000000    0.000000
C    6.000000    0.000000    0.000000
C    7.000000    0.000000    0.000000
C    8.000000    0.000000    0.000000
C    9.000000    0.000000    0.000000
C   10.000000    0.000000    0.000000
C   11.000000    0.000000    0.000000
C   12.000000    0.000000    0.000000
C   13.000000    0.000000    0.000000
C   14.000000    0.000000    0.000000
C   15.000000    0.000000    0.000000
C   16.000000    0.000000    0.000000
C   17.000000    0.000000    0.000000
C   18.000000    0.000000    0.000000
O   19.000000    0.000000    0.000000
""",
    'Silicon Dioxide': """\
* xyz 0 1
Si    0.000000    0.000000    0.000000
O     1.000000    0.000000    0.000000
O    -1.000000    0.000000    0.000000
""",
    'Sulfuric Acid': """\
* xyz 0 1
S    0.000000    0.000000    0.000000
O    1.437500    0.000000    0.000000
O   -1.437500    0.000000    0.000000
O    0.000000    1.437500    0.000000
O    0.000000   -1.437500    0.000000
H    2.187500    0.000000    0.000000
H   -2.187500    0.000000    0.000000
""",
    'Toluene': """\
* xyz 0 1
C    0.000000    0.000000    0.000000
C    1.399334    0.000000    0.000000
C    2.098668    1.209163    0.000000
C    1.399334    2.418327    0.000000
C    0.000000    2.418327    0.000000
C   -0.699667    1.209163    0.000000
H    1.987700   -0.835800    0.000000
H    3.076200    1.209163    0.000000
H    1.987700    3.254127    0.000000
H    0.000000    3.254127    0.000000
H   -0.699667    2.630327    0.000000
H   -1.987700    1.209163    0.000000
""",
    'Urea': """\
* xyz 0 1
C    0.000000    0.000000    0.000000
O    1.207000    0.000000    0.000000
N   -1.207000    0.000000    0.000000
H   -1.571000    0.781000    0.000000
H   -1.571000   -0.781000    0.000000
N    0.000000    1.207000    0.000000
H   -0.781000    1.571000    0.000000
H    0.781000    1.571000    0.000000
"""
}

    if molecule_choice not in molecules_data:
        #this was useful in testing, checking whether the molecule inputted
        #for the calculations had a inp file ready
        print(f"Invalid molecule choice: {molecule_choice}")
        print(f"Available choices are: {', '.join(molecules_data.keys())}")
        #this was useful in testing
        return

    molecule = molecules_data[molecule_choice]
    input_file = 'molecule.inp'
    output_file = 'molecule.out'
    #defining what the input and output files were to be called

    for file in [input_file, output_file, 'molecule.gbw', 'molecule.opt', 'molecule.hess', 'molecule.prop']:
        if os.path.exists(file):
            os.remove(file)

    write_orca_input(molecule, input_file)
    #I had issues displaying the energy variable onto the tkinter window
    #the workaround I came up with were to write a statment into another
    #text file which were to be read in and displayed
    try:
        run_orca(input_file, output_file)
        if os.path.exists(output_file):
            energy = extract_energy(output_file)
            if energy is not None:
                energy = float(energy)
                energy = round(energy,4)
                #rounds the single point energy to 4dp
                file_name = "orca_calc_results.txt"
                #this is the name of the text file which contains the statement
                write_to_text_file(molecule_choice,str(energy),file_name)
                print(f'The single point energy is: {energy} Eh')
                #this was useful in testing
            else:
                print('Failed to extract energy from ORCA output.')
                #this was useful in testing
        else:
            print(f"ORCA output file {output_file} was not created.")
            #this was useful in testing
    except Exception as e:
        print(f"An error occurred: {e}")
        #this was useful in testing

def run_orca_thread(molecule_choice):
    thread = threading.Thread(target=orca_calculation, args=(molecule_choice,))
    thread.start()
    #this is what makes the orca calculation run on a separate thread, 

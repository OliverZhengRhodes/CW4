import os
import subprocess
import threading
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from rdkit import Chem
from rdkit.Chem import Draw
def write_to_text_file(name, data, filename):
    print(data)
    with open(filename, 'w') as file:
        file.write(name+" has single point energy: "+data+"J")
# Define the molecules and their data
#molecule_information = {
#    "introduction": ["Ammonia is a compound composed of nitrogen and hydrogen atoms, commonly used in household cleaning products and industrial processes.", "Intro for aspirin", "Intro for calcium oxide", "Intro for carbon dioxide", "Intro for cobalt tetrachloride", "Intro for DDT", "Intro for ethanol", "Intro for ethylene", "Intro for morphine", "Intro for penicillin", "Intro for phosphoric acid", "Intro for potassium nitrate", "Intro for progestin", "Intro for sodium chloride", "Intro for sodium hydroxide", "Intro for sodium stearate", "Intro for silicon dioxide", "Intro for sulfuric acid", "Intro for toluene", "Intro for urea"],
#    "melting point": ["Melting point for ammonia", "Melting point for aspirin", "Melting point for calcium oxide", "Melting point for carbon dioxide", "Melting point for cobalt tetrachloride", "Melting point for DDT", "Melting point for ethanol", "Melting point for ethylene", "Melting point for morphine", "Melting point for penicillin", "Melting point for phosphoric acid", "Melting point for potassium nitrate", "Melting point for progestin", "Melting point for sodium chloride", "Melting point for sodium hydroxide", "Melting point for sodium stearate", "Melting point for silicon dioxide", "Melting point for sulfuric acid", "Melting point for toluene", "Melting point for urea"],
#    "boiling point": ["Boiling point for ammonia", "Boiling point for aspirin", "Boiling point for calcium oxide", "Boiling point for carbon dioxide", "Boiling point for cobalt tetrachloride", "Boiling point for DDT", "Boiling point for ethanol", "Boiling point for ethylene", "Boiling point for morphine", "Boiling point for penicillin", "Boiling point for phosphoric acid", "Boiling point for potassium nitrate", "Boiling point for progestin", "Boiling point for sodium chloride", "Boiling point for sodium hydroxide", "Boiling point for sodium stearate", "Boiling point for silicon dioxide", "Boiling point for sulfuric acid", "Boiling point for toluene", "Boiling point for urea"],
#    "hazards": ["Hazards for ammonia", "Hazards for aspirin", "Hazards for calcium oxide", "Hazards for carbon dioxide", "Hazards for cobalt tetrachloride", "Hazards for DDT", "Hazards for ethanol", "Hazards for ethylene", "Hazards for morphine", "Hazards for penicillin", "Hazards for phosphoric acid", "Hazards for potassium nitrate", "Hazards for progestin", "Hazards for sodium chloride", "Hazards for sodium hydroxide", "Hazards for sodium stearate", "Hazards for silicon dioxide", "Hazards for sulfuric acid", "Hazards for toluene", "Hazards for urea"],
#    "uses": ["Uses for ammonia", "Uses for aspirin", "Uses for calcium oxide", "Uses for carbon dioxide", "Uses for cobalt tetrachloride", "Uses for DDT", "Uses for ethanol", "Uses for ethylene", "Uses for morphine", "Uses for penicillin", "Uses for phosphoric acid", "Uses for potassium nitrate", "Uses for progestin", "Uses for sodium chloride", "Uses for sodium hydroxide", "Uses for sodium stearate", "Uses for silicon dioxide", "Uses for sulfuric acid", "Uses for toluene", "Uses for urea"]
#}
#molecules = ["Ammonia", "Aspirin", "Calcium Oxide", "Carbon Dioxide", "Cobalt Tetrachloride", "DDT", "Ethanol", "Ethylene", "Morphine", "Penicillin G", "Phosphoric Acid", "Potassium Nitrate", "Progestin", "Sodium Chloride", "Sodium Hydroxide", "Sodium Stearate", "Silicon Dioxide", "Sulfuric Acid", "Toluene", "Urea"]

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
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result.check_returncode()
        print("ORCA execution successful.")
        if result.stderr:
            print("ORCA standard error output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"ORCA failed with error: {e.stderr}")
        raise

def extract_energy(output_file):
    energy = None
    try:
        with open(output_file, 'r') as f:
            for line in f:
                if 'FINAL SINGLE POINT ENERGY' in line:
                    energy = float(line.split()[4])
                    break
    except FileNotFoundError:
        print(f"Output file {output_file} not found.")
    return energy

def orca_calculation(molecule_choice):
    molecules_data = {
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
        print(f"Invalid molecule choice: {molecule_choice}")
        print(f"Available choices are: {', '.join(molecules_data.keys())}")
        return

    molecule = molecules_data[molecule_choice]
    input_file = 'molecule.inp'
    output_file = 'molecule.out'

    for file in [input_file, output_file, 'molecule.gbw', 'molecule.opt', 'molecule.hess', 'molecule.prop']:
        if os.path.exists(file):
            os.remove(file)

    write_orca_input(molecule, input_file)
    
    try:
        run_orca(input_file, output_file)
        if os.path.exists(output_file):
            energy = extract_energy(output_file)
            if energy is not None:
                file_name = "orca_calc_results.txt"
                write_to_text_file(molecule_choice,str(energy),file_name)
                print(f'The single point energy is: {energy} Eh')
            else:
                print('Failed to extract energy from ORCA output.')
        else:
            print(f"ORCA output file {output_file} was not created.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_orca_thread(molecule_choice):
    thread = threading.Thread(target=orca_calculation, args=(molecule_choice,))
    thread.start()

def on_calculate_click():
    selected_molecule = molecule_label.cget("text").lower()
    run_orca_thread(selected_molecule)

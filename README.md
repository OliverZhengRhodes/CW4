# CW4 - Molecule Application

An application that which displays 20 of Chemistry's most important molecules along with information and ORCA calculation functionality. The application uses a GUI where the user can select molecules from the options to observe the structure, read information on the chemical and run ORCA calculations to determine the single point energy.

## Table of Contents

- Installation
- Usage
- Features
- Contact

### Installation
The user will require to install ORCA, this can be done by following the link below:

https://orcaforum.kofo.mpg.de/index.php

The user will need to install the latest version of Python on their computer. The python download links can be found at:

https://www.python.org/downloads/

The user will also be required to install the following python modules:
- rdkit (https://rdkit.org/docs/Install.html)
- pillow (https://reduced.to/zh06u)

In order to run the Unit Converter, the user should clone this repository to their local machine using Git CMD,
download available from the following link:

https://git-scm.com/downloads

Once this has downloaded, open Git CMD, navigate to the directory within which the user would like to clone 
the repository then run:

`git clone https://github.com/OliverZhengRhodes/CW4`

To run the GUI, navigate (on the command line) to the CW4 directory that has just been cloned in and type:

`python main.py`

### Usage

Upon opening the application the user will be greeted with an opening screen with 2 buttons. The options being to "Enter Application" and to "Quit". Clicking the "Enter Application" button will lead the user to the main window. The main window will be fairly empty to begin with. The user must click on a button to display information. On this window there are the following features:
- Scrollable list of molecules on the left
- Image in the center which is of the molecule currently chosen
- Information label on the right, which after clicking a molecule will show information
- Run orca calculation button, this will allow the user to generate an input file for the currently selected molecule. This molecule will then be optimised and produce an output to generate a single point energy value. **This calculation may take a couple minutes**
- Read Orca - this will display on screen the single point energy of the last completed orca calculation. **as the calculation may take a few minutes, you will have to wait before pressing this to see the most recent molecule's value**
- Back to menu button - this will take the user back to the opening window
### Features

- View the molecular structure of 20 molecules.
- Read information on melting point, boiling point, hazards and uses of these molecules
- Run orca calculations on the molecules to determine single point energies

### Contact
If you have any questions, suggestions, or issues, please feel free to reach out:

- **Email**: [oliverzhengrhodes@outlook.com](mailto:oliverzhengrhodes@outlook.com)
- **Phone**: +44 7818 394559


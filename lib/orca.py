import os
import subprocess

def write_orca_input(molecule, filename):
    with open(filename, 'w') as f:
        f.write(f"""! SP B3LYP def2-SVP
* xyz 0 1
{molecule}
*
""")

def run_orca(input_file, output_file):
    try:
        # Construct the command to run ORCA and redirect output
        command = f'orca {input_file} > {output_file}'
        # Run ORCA
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

def main():
    global output_file
    # Example molecule: Water (H2O)
    molecule = """\
H   1.000000   0.000000   0.000000
O   0.000000   0.000000   0.957200
H   0.000000   0.926627   0.239987
"""
    input_file = 'molecule.inp'
    output_file = 'molecule.out'

    write_orca_input(molecule, input_file)
    
    try:
        run_orca(input_file, output_file)
        # Ensure the ORCA output file exists before attempting to read it
        if os.path.exists(output_file):
            energy = extract_energy(output_file)
            if energy is not None:
                print(f'The single point energy is: {energy} Eh')
            else:
                print('Failed to extract energy from ORCA output.')
        else:
            print(f"ORCA output file {output_file} was not created.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

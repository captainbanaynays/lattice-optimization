import yaml
import pymatgen
import argparse
import sys

parser = argparse.ArgumentParser(
        prog="Config Generator",
        description="Given user-inputted parameters, generates VASP POSCAR\
                files for Cu2AgBiI6 in a 3x3 crystal of a given space group\
                from 143-161."
        )

parser.add_argument("-i", "--index", help="Filepath to the index file\
        containing all possible positions for each of the elemental\
        sublattices", required=True)

# Check if positive later
parser.add_argument("-n", "--number", type=int, help="Number of configurations\
        that will be generated by the script of the specified spacegroup.",
                    required=True)

parser.add_argument("-s", "--spacegroup", type=int, choices=range(143, 162),
                    help="The spacegroup that we will be generating\
                            configurations to fall into", required=True)

parser.add_argument("-y", "--symmetries", help="Filepath to the YAML file\
        containing the symmetry operations for each of the spacegroups that\
        in the specified range.", required=True)

args = parser.parse_args()

if args.number <= 0:
    print("Please input a positiv number of configurations to generate.")
    sys.exit(1)
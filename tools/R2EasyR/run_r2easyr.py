##################################
#
##################################

import argparse 
import os 

# Create an argument parser
parser = argparse.ArgumentParser(description='A simple Python script with command-line arguments')

# Add an argument for the name
parser.add_argument('--in', dest='input', help='Specify a name')

# Add an argument for the name
parser.add_argument('--name', help='Specify a name')

# Parse the command-line arguments
args = parser.parse_args()

# Run the scipt
os.system(f"Rscript run_r2easyr.R {args.input} {args.name}")

os.system(f"r2r --disable-usage-warning {args.name}.r2r_meta {args.name}.png")
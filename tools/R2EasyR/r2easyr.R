###################################################################
# A wrapper for the R2EasyR tool
#
##################################################################

#!/usr/bin/Rscript
args <- commandArgs(trailingOnly = TRUE)

# Load the R2EasyR library
library(R2easyR)

# Read in the CSV file
df <- read.csv(args[1])

# Write the output 
r2easyR.write(args[2], df, colors = "circles")
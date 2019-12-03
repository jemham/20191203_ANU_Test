import pandas as pd
import os
import sys
#os and sys are for interacting with files

#--------
#data from blahblahblah

data = pd.read_excel('20191130_ANU/data/sample_data.xlsx', sheet_name = 'Table S20', skiprows = 2, header = 0, index_col="gene_id")

#--------

#get gene name from command line

gene = sys.argv[1]

#an exception if they type bullshit in
try:
	data.loc[gene]
except: "Please provide a valid gene name."

#find all the expressions
for x in data.columns:
	print(f"Expression at {x}:{data.loc[gene][x]}")

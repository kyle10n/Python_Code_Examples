import pandas as pd
import sys
import os

#ensure this python file is inside your file with your xlsx files

#names of your xlsx files

my_directory = sys.argv[1]

file_names = os.listdir(my_directory)

excel_names = [file for file in file_names if file[-4:] == 'xlsx']

excels = [pd.ExcelFile(name) for name in excel_names]


#gotta read that files
frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]


frames = [df for df in frames]

combined = pd.concat(frames, axis=1)

#gotta combine thattttt :D
combined.to_excel("Greatest Matrix File.xlsx", header=True, index=False)


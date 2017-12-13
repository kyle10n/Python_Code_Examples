import pandas as pd

#ensure this python file is inside your file with your xlsx files

#names of your xlsx files

excel_names = ['1.xlsx', '10_11_12_13.xlsx', '14_15_16.xlsx', '17_18_19_20.xlsx', 
               '21_22_23.xlsx', '25a.xlsx', '26_27.xlsx', '28_29_30.xlsx', '2_3.xlsx',
               '31.xlsx', '32.xlsx', '33_34.xlsx', '35_36.xlsx', '4_5_6_7.xlsx', '8_9.xlsx']

excels = [pd.ExcelFile(name) for name in excel_names]


#gotta read that files
frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]


frames = [df for df in frames]

combined = pd.concat(frames, axis=1)

#gotta combine thattttt :D
combined.to_excel("Greatest Matrix File.xlsx", header=True, index=False)

print("Check your directory. It should be done! :)")

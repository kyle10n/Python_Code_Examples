import pandas as pd
import os
import numpy as np



list_of_rows = []

files = os.listdir() #get files in the directory
excel_files = [] #file list
for i in files:  #strip files that are not ending in xlsx names
    if i[-3:] == 'lsx':
        excel_files.append(i)
        print("yes")
    else:
        print("")

print("Got File Names")
print(excel_files)

row_input = input("What rows would you like? Enter the digit(s) that must be seperated by commas")

row_input_numbers = list(map(int, row_input.split(",")))

for file_names in excel_files: #take row index that user inputted and append to the list_of_rows
    df_excel = pd.read_excel(file_names)
    for numbers in row_input_numbers:
        to_append = list(df_excel.iloc[numbers])
        list_of_rows.append(to_append)

new_df = pd.DataFrame(list_of_rows, columns = ["Index",
"Label",
"Pinned",
"Occurence(% of all documents)",
"Document Count",
"Terms",
"Sentiment: positivity%",
"Sentiment: skepticism%",
"Sentiment: negativity%",
"Association1",
"Association1 Document Count",
"Association2",
"Association2 Document Count",
"Association3",
"Association3 Document Count",
"Association4",
"Association4 Document Count",
"Association5",
"Association5 Document Count",
"Association6",
"Association6 Document Count",
"Association7",
"Association7 Document Count",
"Association8",
"Association8 Document Count",
"Association9",
"Association9 Document Count",
"Association10",
"Association10 Document Count"])

writer = pd.ExcelWriter("__Read_ME.xlsx")

new_df.to_excel(writer,'Sheet1')

writer.save()

print("Done")


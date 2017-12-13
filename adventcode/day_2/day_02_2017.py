import pandas as pd
import numpy


df = pd.read_excel("checksum.xlsx")

checksum = []

for index, row in df.iterrows():
    a = list(row)

    for i in a:
        if i%2 == 0:
            

    b = max(a) - min(a)
    checksum.append(b)
print(sum(checksum))


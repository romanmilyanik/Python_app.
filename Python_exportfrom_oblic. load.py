import os
import numpy as np
import pandas as pd
os.chdir("D:/USERS/ROMAN/WORK/Python/Перебір обліків циклом")

flnm = "base_xxx.csv"
df = pd.read_csv(flnm, header=None, sep=";")
df.columns = ["ky", "day", "date_start", "date_end", "P011", "kod", "ugoda", "date_oblic"]

df.dtypes










#csv
df.to_csv("swiss_bank_notes_3.csv", sep=";", index=False)

#xlsx
writer = pd.ExcelWriter("towrite.xlsx", engine='xlsxwriter')
df.to_excel(writer, index=False)
writer.save()



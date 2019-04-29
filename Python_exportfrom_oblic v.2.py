import os
import datetime
from datetime import datetime
import numpy as np
import pandas as pd
os.chdir("D:/USERS/ROMAN/WORK/Python/Перебір обліків циклом")

file_names = pd.DataFrame(os.listdir("D:/USERS/ROMAN/WORK/Python/Перебір обліків циклом/oblic"), columns = ["column"])
t = datetime.strptime("1970-01-01", '%Y-%m-%d')
k = range(len(file_names))

for i in k:
    y = "".join(["D:/USERS/ROMAN/WORK/Python/Перебір обліків циклом/oblic/", file_names["column"].values[i]])
    a = pd.read_excel(y, skiprows=1)
    z3 = file_names["column"].values[i][10:20]
    oblic = "-".join([z3[-4:], z3[3:5], z3[:2]])
    b = a[["КОД УГОДИ",
           "К-сть днів",
           "ДАТА ВИДАЧІ",
           "ДАТА ПОГАШЕННЯ",
           "Р011",
           "ІДЕНТИФІКАЦІЙНИЙ КОД",
           "№ УГОДИ"]]
    b["oblic"] = oblic
    b = b.dropna(subset=["КОД УГОДИ"])
    b = b.fillna(0)
    
    b["ДАТА ВИДАЧІ"].replace(0, t, inplace=True)
    b["ДАТА ПОГАШЕННЯ"].replace(0, t, inplace=True)
    
    b["ДАТА ВИДАЧІ"] = pd.to_datetime(b["ДАТА ВИДАЧІ"])
    b["ДАТА ПОГАШЕННЯ"] = pd.to_datetime(b["ДАТА ПОГАШЕННЯ"])
    b["oblic"] = pd.to_datetime(b["oblic"])
    
    b["ДАТА ВИДАЧІ"] = b["ДАТА ВИДАЧІ"].dt.date
    b["ДАТА ПОГАШЕННЯ"] = b["ДАТА ПОГАШЕННЯ"].dt.date
    b["oblic"] = b["oblic"].dt.date
    
    b[["КОД УГОДИ", "К-сть днів", "Р011", "ІДЕНТИФІКАЦІЙНИЙ КОД"]] = b[["КОД УГОДИ", "К-сть днів", "Р011", "ІДЕНТИФІКАЦІЙНИЙ КОД"]].astype(np.int)
    b.to_csv("base_xxx.csv", index=False, mode='a', header=False, sep=";", encoding="utf-8")

    if i % 1 == 0:
        print(".. processed " + str(1) + " files at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))







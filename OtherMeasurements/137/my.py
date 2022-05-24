# importing pandas
import pandas as pd
import os
 
for x in os.listdir('.'):
    if x.endswith("_all.txt"):
        # Prints only text file present in My Folder
        name_txt = x
        name_xlsx = name_txt.replace("txt", "xlsx")
#        print(name_txt)
#        print(name_xlsx)


# read text file into pandas DataFrame
df = pd.read_csv(name_txt, sep='\t', names=["P_onset", "P", "P_offset", "Q", "R_onset", "R", "R_offset", "S", "T_onset", "T", "T_offset", "P_amp", "Q_amp", "R_amp", "S_amp", "T_amp"])
  
# display DataFrame
#print(df)

# save to excel
df.to_excel(name_xlsx, index=False)

print("File "+name_xlsx+" Done!")

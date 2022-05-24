# Script to list all the directories and files
# From subdirectories, search for "_all.xlsx" files, substitutes the negative values with empty cells 
# for a new version of the file (v2) and saves to excel (*_all_v2.xlsx)
# Calculates the average per column and stores in new excel file (*_all_stats.xlsx)
# by Paulo Coelho 2022/04/10
################################################################################################################3
import pandas as pd
import numpy as np
import os
from pathlib import Path

# Get working folder
rootdir = os.getcwd()

for rootdir, dirs, files in os.walk(rootdir):
    for subdir in dirs: # All the folders in the dataset
        path_dir = os.path.join(rootdir, subdir)
        #print(path_dir)
        for _, _, sub_folder_files in os.walk(path_dir): # For each subfolders in the dataset
            #print(sub_folder_files)
            for file in sub_folder_files:
                if file.endswith("_all.xlsx"):
                    name_xlsx = os.path.join(path_dir, file)
                    name_xlsx_v2 = name_xlsx.replace("_all.xlsx", "_all_v2.xlsx")
                    name_xlsx_stats = name_xlsx.replace("_all.xlsx", "_all_stats.xlsx")
                    #print(name_xlsx)
                    #print(name_xlsx_v2)
                    #print(name_xlsx_stats)

                    # read excel file into pandas DataFrame
                    df = pd.read_excel(name_xlsx, names=["P_onset", "P", "P_offset", "Q", "R_onset", "R", "R_offset", "S", "T_onset", "T", "T_offset", "P_amp", "Q_amp", "R_amp", "S_amp", "T_amp",
                    "RR interval", "PP interval", "P Duration", "PR interval", "PR segment", "QRS duration", "ST segment",
                    "ST-T segment", "QT duration", "TP interval", "R amplitude", "T amplitude", "P amplitude"])
												
                    # Copies and calculates the average 
                    # (must have NaN in either empty or negative cells to calculate the average)
                    df_avg = df.copy()
                    df_avg[df_avg < 0] = np.nan
                    
                    # Replaces negative numbers as empty cells
                    df[df < 0] = ""
                    
                    # display DataFrame, debug only
                    # print(df)
                    # df_avg.loc['avg'] = df_avg.mean()

                    # New dataframe to store the average statistics
                    df_avg_stats = pd.DataFrame({"RR interval AVG": [df_avg['RR interval'].mean()], "PP interval AVG": [df_avg['PP interval'].mean()], "P Duration AVG": [df_avg['P Duration'].mean()],
                    "PR interval AVG": [df_avg['PR interval'].mean()], "PR segment AVG": [df_avg['PR segment'].mean()], "QRS duration AVG": [df_avg['QRS duration'].mean()], "ST segment AVG": [df_avg['ST segment'].mean()],
                    "ST-T segment AVG": [df_avg['ST-T segment'].mean()], "QT duration AVG": [df_avg['QT duration'].mean()], "TP interval AVG": [df_avg['TP interval'].mean()], "R amplitude AVG": [df_avg['R amplitude'].mean()],
                    "T amplitude AVG": [df_avg['T amplitude'].mean()], "P amplitude AVG": [df_avg['P amplitude'].mean()]})#, index=['avg'])

                    # display DataFrame, debug only
                    # print(df_avg_stats)

                    # Saves to excel with empty cells in the negatives location 
                    # Saves new file with stats
                    # Removes the index from pandas Dataframe
                    df.to_excel(name_xlsx_v2, index=False)
                    df_avg_stats.to_excel(name_xlsx_stats, index=False)

                    print("File "+name_xlsx_v2+" Done!")


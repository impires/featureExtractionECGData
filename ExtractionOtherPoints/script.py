# Script to list all the directories and files
# From subdirectories, search for "_all.txt" files, removes NaN values and saves to excel
# by Paulo Coelho 2022/04/03

import pandas as pd
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
                if file.endswith("_all.txt"):
                    name_txt = os.path.join(path_dir, file)
                    name_xlsx = name_txt.replace("txt", "xlsx")
                    #print(name_txt)
                    #print(name_xlsx)

                    # read text file into pandas DataFrame
                    df = pd.read_csv(name_txt, sep='\t', names=["P_onset", "P", "P_offset", "Q", "R_onset", "R", "R_offset", "S", "T_onset", "T", "T_offset", "P_amp", "Q_amp", "R_amp", "S_amp", "T_amp"])

                    # Drop rows where Dataframe is NaN
                    df.dropna(inplace=True)

                    # display DataFrame
                    #print(df)

                    # save to excel, removes the index from pandas Dataframe
                    df.to_excel(name_xlsx, index=False)

                    print("File "+name_xlsx+" Done!")


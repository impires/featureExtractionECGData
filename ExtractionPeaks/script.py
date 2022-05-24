# Import packages
import neurokit2 as nk
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# Plotting preferences
#matplotlib inline
matplotlib.rcParams['figure.figsize'] = [14.0, 10.0]  # Bigger figures
sns.set_style("whitegrid")  # White background
sns.set_palette(sns.color_palette("colorblind"))  # Better colours

for item in range(219):

 if(item+1 != 20 and item+1 != 25 and item+1 != 35 and item+1 != 38 and item+1 != 54 and item+1 != 153 and item+1 != 195):

  print(str(item+1))

# Download resting-state data
  ecg_signal = pd.read_csv("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+".csv")["ecg"]

# Plot it
#ecg_signal.plot()

# Extract R-peaks locations
  _, rpeaks = nk.ecg_peaks(ecg_signal, sampling_rate=1000)

  ecg_signal_r = ecg_signal.filter(items = rpeaks['ECG_R_Peaks'], axis=0)

# Visualize R-peaks in ECG signal
# plot = nk.events_plot(rpeaks['ECG_R_Peaks'], ecg_signal)

# Delineate the ECG signal
  _, waves_peak = nk.ecg_delineate(ecg_signal, rpeaks, sampling_rate=1000, method="dwt", show=False, show_type='all')

  ecg_signal_t = ecg_signal.filter(items = waves_peak['ECG_T_Peaks'], axis=0)
  ecg_signal_p = ecg_signal.filter(items = waves_peak['ECG_P_Peaks'], axis=0)
  ecg_signal_q = ecg_signal.filter(items = waves_peak['ECG_Q_Peaks'], axis=0)
  ecg_signal_s = ecg_signal.filter(items = waves_peak['ECG_S_Peaks'], axis=0)

# Visualize the T-peaks, P-peaks, Q-peaks and S-peaks
  plt = nk.events_plot([rpeaks['ECG_R_Peaks'],
                       waves_peak['ECG_T_Peaks'],
                       waves_peak['ECG_P_Peaks'],
                       waves_peak['ECG_Q_Peaks'],
                       waves_peak['ECG_S_Peaks']], ecg_signal)
  
  plt.savefig("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+".png")

  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_r.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], rpeaks['ECG_R_Peaks']))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_p.txt", 'w') as f:
     csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_P_Peaks']))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_q.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_Q_Peaks']))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_t.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_T_Peaks']))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_s.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_S_Peaks']))

  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_r_amp.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], ecg_signal_r))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_p_amp.txt", 'w') as f:
     csv.writer(f).writerows(map(lambda x: [x], ecg_signal_p))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_q_amp.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], ecg_signal_q))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_t_amp.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], ecg_signal_t))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_s_amp.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], ecg_signal_s))

  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_p_onsets.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_P_Onsets']))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_p_offsets.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_P_Offsets']))     
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_t_onsets.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_T_Onsets']))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_t_offsets.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_T_Offsets']))  
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_r_onsets.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_R_Onsets']))
  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_r_offsets.txt", 'w') as f:
    csv.writer(f).writerows(map(lambda x: [x], waves_peak['ECG_R_Offsets'])) 

  with open("Capturas_Neurokit/"+str(item+1)+"/"+str(item+1)+"_all.txt", 'w') as f:
    csv.writer(f, delimiter='\t').writerows(zip(waves_peak['ECG_P_Onsets'], waves_peak['ECG_P_Peaks'], waves_peak['ECG_P_Offsets'], waves_peak['ECG_Q_Peaks'], waves_peak['ECG_R_Onsets'], rpeaks['ECG_R_Peaks'], waves_peak['ECG_R_Offsets'], waves_peak['ECG_S_Peaks'], waves_peak['ECG_T_Onsets'], waves_peak['ECG_T_Peaks'], waves_peak['ECG_T_Offsets'], ecg_signal_p, ecg_signal_q, ecg_signal_r, ecg_signal_s, ecg_signal_t))


                       # Zooming into the first 3 R-peaks, with focus on T_peaks, P-peaks, Q-peaks and S-peaks
#plot = nk.events_plot([rpeaks['ECG_R_Peaks'][:3],
#                       waves_peak['ECG_T_Peaks'][:3],
#                       waves_peak['ECG_P_Peaks'][:3],
#                       waves_peak['ECG_Q_Peaks'][:3],
#                       waves_peak['ECG_S_Peaks'][:3]], ecg_signal[:3000])
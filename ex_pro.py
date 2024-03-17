# IMPORT ALL THE PACKAGES
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import json
import os
import sys
from sklearn.preprocessing import MinMaxScaler

# HERE WE DEFINE THE FUNCTION copia_file TO COPY EVENTUALLY COPY THE FILE WITH ANOTHER NAME
def copia_file(nome_file_input, nome_file_output):
    shutil.copy(nome_file_input, nome_file_output)

if __name__ == "__main__":
    nome_file_input = sys.argv[1]
    nome_file_output = sys.argv[2]
    if nome_file_input == nome_file_output:
    	print('ok')
    else:
    	copia_file(nome_file_input, nome_file_output)



# INTRODUCE THE FILE NAME AND WE PRINT THE HEADER TO CHECK OUT IF THE FILE IS CORRECTLY READ
# IF WE SEE ALL THE NAMES OF THE COLUMNS, EVERYTHING IS OKAY
filename = nome_file_output
with open(filename, 'r') as ppf:
    header = ppf.readline()
    print(header)

# WE TRANSFORM HERE THE FILE IN A OBJECT THAT NUMPY IS ABLE TO WORK WITH
data_filename = filename
print(filename)
data = np.loadtxt(data_filename, unpack=True)
print(type(data))
print(data.shape)
print(type(data.shape))



# WE DEFINE ALL THE COLUMNS JUST TO HAVE A COMPLITELY LOOK (IT IS NOT NECESSARY IS JUST FOR WHO WANT CHANGE THE AXIS OF OUR FUTURE GRAPHICS)
col_1 = np.asarray(data[0])  # M/H
col_2 = np.asarray(data[1])  # m_ini
col_3 = np.asarray(data[2])  # logL
col_4 = np.asarray(data[3])  # logTe
col_5 = np.asarray(data[4])  # M_ass
col_6 = np.asarray(data[5])  # b_ass
col_7 = np.asarray(data[6])  # y_ass
col_8 = np.asarray(data[7])  # m_app
col_9 = np.asarray(data[8])  # b-y
col_10 = np.asarray(data[9])  # dist
col_11 = np.asarray(data[10])  # abs_dist
col_12 = np.asarray(data[11])  # ID_parent
col_13 = np.asarray(data[12])  # age_parent

# WE RENAME OUR COLUMN FOR OUR CONVINIENCE (NOT NECESSARY)
b_y = np.asarray(col_9)  # asse x
M_ass = np.asarray(col_5)  # asse y
age_parent = np.asarray(col_13)  # asse colore
MH = np.asarray(col_1)
M_ini = np.asarray(col_2)



# WE SET THE COLOUR FOR OUR POPULATION, IN ORDER TO EASY DISTINGUISH THEM
colors = []
transparency = []
for value in age_parent:
  if value < 1.0:
    colors.append('#4B0082')
    transparency.append(0.3)
  elif 1.0 < value < 2.0:
    colors.append('#000080')
    transparency.append(0.3)
  elif 2.0 < value < 3.0:
    colors.append('#00BFFF')
    transparency.append(0.3)
  elif 3.0 < value < 4.0:
    colors.append('#AFEEEE')
    transparency.append(0.3)
  elif 4.0 < value < 5.0:
    colors.append('#00FFFF')
    transparency.append(0.6)
  elif 5.0 < value < 6.0:
    colors.append('#66CDAA')
    transparency.append(0.6)
  elif 6.0 < value < 7.0:
    colors.append('#90EE90')
    transparency.append(0.6)
  elif 7.0 < value < 8.0:
    colors.append('#ADFF2F')
    transparency.append(0.6)
  elif 8.0 < value < 9.0:
    colors.append('#FFFF00')
    transparency.append(0.9)
  elif 9.0 < value < 10.0:
    colors.append('#B8860B')
    transparency.append(0.9)
  elif 10.0 < value < 11.0:
    colors.append('#FA8072')
    transparency.append(0.9)
  elif 11.0 < value < 12.0:
    colors.append('#FF0000')
    transparency.append(0.9)
  elif 12.0 < value < 13.0:
    colors.append('#800000')
    transparency.append(1)
    
# HERE WE SET THE TRANSPARENCY'S CRITERIA
scaler = MinMaxScaler()
trans_array = np.asarray(transparency)

# WE PLOT THE FIRST GRAPHIC b-y ON Mag-Abs
fig, ax = plt.subplots()
print(type(ax))
print(type(fig))

legend_elements = [
    mpatches.Patch(color='#4B0082', label='< 1.0'),
    mpatches.Patch(color='#000080', label='1.0 - 2.0 Gyr'),
    mpatches.Patch(color='#00BFFF', label='2.0 - 3.0 Gyr'),
    mpatches.Patch(color='#AFEEEE', label='3.0 - 4.0 Gyr'),
    mpatches.Patch(color='#00FFFF', label='4.0 - 5.0 Gyr'),
    mpatches.Patch(color='#66CDAA', label='5.0 - 6.0 Gyr'),
    mpatches.Patch(color='#90EE90', label='6.0 - 7.0 Gyr'),
    mpatches.Patch(color='#ADFF2F', label='7.0 - 8.0 Gyr'),
    mpatches.Patch(color='#FFFF00', label='8.0 - 9.0 Gyr'),
    mpatches.Patch(color='#B8860B', label='9.0 - 10.0 Gyr'),
    mpatches.Patch(color='#FA8072', label='10.0 - 11.0 Gyr'),
    mpatches.Patch(color='#FF0000', label='11.0 - 12.0 Gyr'),
    mpatches.Patch(color='#800000', label='12.0 - 13.0 Gyr')
]

plt.legend(handles=legend_elements, loc='upper right')
plt.scatter(b_y, M_ass, c=colors, s=1, alpha=trans_array, marker='.')
ax.invert_yaxis()
plt.xlabel("b-y")
plt.ylabel("Mag-Abs")
plt.savefig('Mag_Col.png')
plt.show()



# WE SET THE OBJECT FOR OUR HISTOGRAM
c = len(age_parent)
hist_MH_1 = []
hist_age_1 = []
hist_mini_1 = []
hist_MH_2 = []
hist_age_2 = []
hist_mini_2 = []
hist_MH_3 = []
hist_age_3 = []
hist_mini_3 = []
for i in range(0, c - 1):
  if age_parent[i] < 1.0:
    hist_MH_1.append(MH[i])
    hist_age_1.append(age_parent[i])
    hist_mini_1.append(M_ini[i])
  elif 1.0 < age_parent[i] < 5.0:
    hist_MH_2.append(MH[i])
    hist_age_2.append(age_parent[i])
    hist_mini_2.append(M_ini[i])
  elif 5.0 < age_parent[i] < 13.0:
    hist_MH_3.append(MH[i])
    hist_age_3.append(age_parent[i])
    hist_mini_3.append(M_ini[i])
    
# WE DEFINE OUR MEAN AND MEDIAN FOR EVERY POPULATION
x = np.array(hist_MH_1)
y = np.array(hist_MH_2)
z = np.array(hist_MH_3)
mean_1 = np.mean(x)
median_1 = np.median(x)
mean_2 = np.mean(y)
median_2 = np.median(y)
mean_3 = np.mean(z)
median_3 = np.median(z)

# WE PLOT THE HISTOGRAM WITH M/H ON COUNTS
plt.hist(x, alpha=0.3, color='r', label='Pop t < 1.0 Gyr')
plt.hist(y, alpha=0.3, color='b', label='Pop 1.0 Gyr < t < 5.0 Gyr')
plt.hist(z, alpha=0.3, color='g', label='Pop 5.0 Gyr < t < 13.0 Gyr')
plt.axvline(mean_1,
            color='blue',
            linestyle='dashed',
            linewidth=1,
            label=f'Media Pop t < 1.0 Gyr: {mean_1:.2f} M/H')
plt.axvline(median_1,
            color='black',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana t < 1.0 Gyr: {median_1:.2f} M/H')
plt.axvline(mean_2,
            color='red',
            linestyle='dashed',
            linewidth=1,
            label=f'Media Pop 1.0 Gyr < t < 5.0 Gyr: {mean_2:.2f} M/H')
plt.axvline(median_2,
            color='yellow',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana Pop 2.0 Gyr < t < 5.0 Gyr: {median_2:.2f} M/H')
plt.axvline(mean_3,
            color='orange',
            linestyle='dashed',
            linewidth=1,
            label=f'Media Pop 5.0 Gyr < t < 13.0 Gyr: {mean_3:.2f} M/H')
plt.axvline(median_3,
            color='pink',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana Pop 5.0 Gyr < t < 13.0 Gyr: {median_3:.2f} M/H')
plt.legend()
plt.xlabel("M/H")
plt.ylabel("Counts")
plt.savefig('Hist.png')
plt.show()



# WE DEFINE THE TRANSPARENCY LIKE WE DID BEFORE FOR THE NEXT GRAPHIC
colors_2 = []
transparency_2 = []
for value in age_parent:
  if value < 1.0:
    colors_2.append('red')
    transparency_2.append(0.9)
  elif 1.0 < value < 5.0:
    colors_2.append('green')    
    transparency_2.append(0.5)
  elif 5.0 < value < 13.0:
    colors_2.append('blue')
    transparency_2.append(0.3)
    
trans_2_array = np.asarray(transparency_2)



# AND HERE WE PLOT OUR GRAPHIC WITH M/H FOR X-AXIS ON M_ini FOR Y-AXIS
fig, ax = plt.subplots()
print(type(ax))
print(type(fig))

legend_elements = [
    mpatches.Patch(color='red', label='< 1.0 Gyr'),
    mpatches.Patch(color='green', label='1.0 - 5.0 Gyr'),
    mpatches.Patch(color='blue', label='5.0 - 13.0 Gyr')
]

plt.legend(handles=legend_elements, loc='upper right')
plt.scatter(M_ini, MH, s=2, c=colors_2, alpha=trans_2_array, marker='.')
#ax.invert_xaxis()

plt.ylabel("M/H")
plt.xlabel("M_ini")
plt.savefig('Pop.png')
plt.show()



# WE SET THE BINS FOR OUR 2D-HISTOGRAM
bin_MH_max = max(MH)
bin_Mini_max= max(M_ini)
bin_MH_min = min(MH)
bin_Mini_min= min(M_ini)
maxmin_MH = np.array([bin_MH_min,bin_MH_max])
maxmin_Mini = np.array([bin_Mini_min,bin_Mini_max])


# WE PLOT OUR 2D-HISTOGRAM
H, xedges, yedges = np.histogram2d(M_ini, MH, bins=20, range=[maxmin_Mini, maxmin_MH])

plt.imshow(H.T, origin='lower', cmap='viridis')
plt.colorbar(label='Counts')
plt.xlabel('M_ini')
plt.ylabel('M/H')
plt.savefig('Hist-2D.png')
plt.show()


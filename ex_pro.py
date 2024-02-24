import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import json
import os

with open('mio_file_output.txt', 'r') as dat_file:
  # Leggi il contenuto del file
  data = dat_file.read()

# Apri il file .txt in modalità scrittura
with open('mio_file_output.txt', 'w') as txt_file:
  # Scrivi il contenuto nel file .txt
  txt_file.write(data)

with open('mio_file_output.txt', 'r') as f:
  data = f.readlines()  # read raw lines into an array
  cleaned_matrix = []
  for raw_line in data:
    split_line = raw_line.strip().split(",")  # ["1", "0" ... ]
    nums_ls = [x.replace('"', '') for x in split_line
               ]  # get rid of the quotation marks and convert to integer
  cleaned_matrix.append(nums_ls)
#print(cleaned_matrix)
#print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

with open('cleaned_matrix.txt', 'w') as f:
  for item in cleaned_matrix:
    f.write(json.dumps(item))
    f.write("\n")


def sostituisci_virgole(file_name):
  with open(file_name, 'r') as file:
    contenuto = file.read()
    contenuto_modificato = contenuto.replace(',', '\n')

  with open(file_name, 'w') as file:
    file.write(contenuto_modificato)


def sostituisci_apice(file_name):
  with open(file_name, 'r') as file:
    contenuto = file.read()
    contenuto_modificato = contenuto.replace("'", "")


def sostituisci_parentesi(file_name):
  with open(file_name, 'r') as file:
    contenuto = file.read()
    contenuto_modificato = contenuto.replace("]", '')

  with open(file_name, 'w') as file:
    file.write(contenuto_modificato)


def sostituisci_dopvirgole(file_name):
  with open(file_name, 'r') as file:
    contenuto = file.read()
    contenuto_modificato = contenuto.replace('"', '')

  with open(file_name, 'w') as file:
    file.write(contenuto_modificato)


sostituisci_virgole('cleaned_matrix.txt')
sostituisci_apice('cleaned_matrix.txt')
sostituisci_parentesi('cleaned_matrix.txt')
sostituisci_dopvirgole('cleaned_matrix.txt')


def rimuovi_righe(file_name):
  with open(file_name, 'r') as file:
    righe = file.readlines()

    # Rimuovi le prime 47 righe e le righe dalla 6718 in poi
    righe_modificate = righe[47:6717]

  with open(file_name, 'w') as file:
    file.writelines(righe_modificate)


rimuovi_righe('cleaned_matrix.txt')


def rinomina_file(nome_vecchio, nome_nuovo):
  os.rename(nome_vecchio, nome_nuovo)


rinomina_file('cleaned_matrix.txt', 'a_2.txt')

filename = 'a_2.txt'
data_filename = filename
print(filename)
data = np.loadtxt(data_filename, unpack=True)
print(type(data))
print(data.shape)
print(type(data.shape))

i = 0
dim = data.shape[1]
print(dim)
col_1 = []
col_2 = []
col_3 = []
col_4 = []
col_5 = []
col_6 = []
col_7 = []
col_8 = []
col_9 = []
col_10 = []
col_11 = []
col_12 = []
col_13 = []

for i in range(0, dim):
  #print(i)
  col_1.append(data[0, i])
  col_2.append(data[1, i])
  col_3.append(data[2, i])
  col_4.append(data[3, i])
  col_5.append(data[4, i])
  col_6.append(data[5, i])
  col_7.append(data[6, i])
  col_8.append(data[7, i])
  col_9.append(data[8, i])
  col_10.append(data[9, i])
  col_11.append(data[10, i])
  col_12.append(data[11, i])
  col_13.append(data[12, i])

col_1 = np.asarray(col_1)  # M/H
col_2 = np.asarray(col_2)  # m_ini
col_3 = np.asarray(col_3)  # logL
col_4 = np.asarray(col_4)  # logTe
col_5 = np.asarray(col_5)  # M_ass
col_6 = np.asarray(col_6)  # b_ass
col_7 = np.asarray(col_7)  # y_ass
col_8 = np.asarray(col_8)  # m_app
col_9 = np.asarray(col_9)  # b-y
col_10 = np.asarray(col_10)  # dist
col_11 = np.asarray(col_11)  # abs_dist
col_12 = np.asarray(col_12)  # ID_parent
col_13 = np.asarray(col_13)  # age_parent

b_y = np.asarray(col_9)  # asse x
M_ass = np.asarray(col_5)  # asse y
age_parent = np.asarray(col_13)  # asse colore
MH = np.asarray(col_1)
M_ini = np.asarray(col_2)

max_age = age_parent.max()
print(len(age_parent))
print(max_age)

colors = []
for value in age_parent:
  if value < 1.0:
    colors.append('#4B0082')
  elif 1.0 < value < 2.0:
    colors.append('#000080')
  elif 2.0 < value < 3.0:
    colors.append('#00BFFF')
  elif 3.0 < value < 4.0:
    colors.append('#AFEEEE')
  elif 4.0 < value < 5.0:
    colors.append('#00FFFF')
  elif 5.0 < value < 6.0:
    colors.append('#66CDAA')
  elif 6.0 < value < 7.0:
    colors.append('#90EE90')
  elif 7.0 < value < 8.0:
    colors.append('#ADFF2F')
  elif 8.0 < value < 9.0:
    colors.append('#FFFF00')
  elif 9.0 < value < 10.0:
    colors.append('#B8860B')
  elif 10.0 < value < 11.0:
    colors.append('#FA8072')
  elif 11.0 < value < 12.0:
    colors.append('#FF0000')
  elif 12.0 < value < 13.0:
    colors.append('#800000')

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
plt.scatter(b_y, M_ass, c=colors, marker='.')
ax.invert_yaxis()
plt.xlabel("b-y")
plt.ylabel("Mag-Abs")
plt.savefig('Mag_Col.png')
plt.show()

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

x = np.array(hist_MH_1)
y = np.array(hist_MH_2)
z = np.array(hist_MH_3)
mean_1 = np.mean(x)
median_1 = np.median(x)
mean_2 = np.mean(y)
median_2 = np.median(y)
mean_3 = np.mean(z)
median_3 = np.median(z)

plt.hist(x, alpha=0.3, color='r', label='Pop t < 1.0 Gyr')
plt.hist(y, alpha=0.3, color='b', label='Pop 1.0 Gyr < t < 5.0 Gyr')
plt.hist(z, alpha=0.3, color='g', label='Pop 5.0 Gyr < t < 13.0 Gyr')
plt.axvline(mean_1,
            color='blue',
            linestyle='dashed',
            linewidth=1,
            label=f'Media Pop t < 1.0 Gyr: {mean_1:.2f}')
plt.axvline(median_1,
            color='black',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana t < 1.0 Gyr: {median_1:.2f}')
plt.axvline(mean_2,
            color='red',
            linestyle='dashed',
            linewidth=1,
            label=f'Media Pop 1.0 Gyr < t < 5.0 Gyr: {mean_2:.2f}')
plt.axvline(median_2,
            color='yellow',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana Pop 2.0 Gyr < t < 5.0 Gyr: {median_2:.2f}')
plt.axvline(mean_3,
            color='orange',
            linestyle='dashed',
            linewidth=1,
            label=f'Media Pop 5.0 Gyr < t < 13.0 Gyr: {mean_3:.2f}')
plt.axvline(median_3,
            color='pink',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana Pop 5.0 Gyr < t < 13.0 Gyr: {median_3:.2f}')
plt.legend()
plt.savefig('Hist.png')
plt.show()

colors_2 = []
for value in age_parent:
  if value < 1.0:
    colors_2.append('red')
  elif 1.0 < value < 5.0:
    colors_2.append('blue')
  elif 5.0 < value < 13.0:
    colors_2.append('green')

fig, ax = plt.subplots()
print(type(ax))
print(type(fig))

legend_elements = [
    mpatches.Patch(color='red', label='< 1.0 Gyr'),
    mpatches.Patch(color='blue', label='1.0 - 5.0 Gyr'),
    mpatches.Patch(color='green', label='5.0 - 13.0 Gyr')
]

plt.legend(handles=legend_elements, loc='upper right')
plt.scatter(MH, M_ini, c=colors_2, marker='.')
ax.invert_yaxis()

plt.xlabel("M/H")
plt.ylabel("M_ini")
plt.savefig('Pop.png')
plt.show()

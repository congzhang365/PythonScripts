import parselmouth
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os
import os.path
import re
import numpy as np

directory = "./training_data/"

filenames = []
for wav in glob.glob(directory + "*.wav"):
    f_wav = wav.split("/")[-1]
    f_wav = f_wav.split("\\")[-1]
    f_wav = f_wav.split(".")[0]
    filenames.append(f_wav)
# print('the file names are: ', wave_files)

tgfile_list = []
for i in range(len(filenames)):
    tg_file = filenames[i] + ".TextGrid"
    tgfile_list.append(tg_file)
# print('the textgrid file list is: ', tgfile_list)

textgrid_files = []
for txt in glob.glob("./training_data/*.TextGrid"):
    f_txt = txt.split("/")[-1]
    f_txt = f_txt.split("\\")[-1]
    t_txt = f_txt.split(".")[0]
    textgrid_files.append(f_txt)
# print('the textgrid files are: ', textgrid_files)

no_file = []
for j in range(len(tgfile_list)):
    if not os.path.isfile(directory + tgfile_list[j]):
        no_file.append(tgfile_list[j])
        with open(directory+"record.txt", 'a') as record_file:
            record_file.write(tgfile_list[j] + "\n")

print("These %i files do not exist: " %len(no_file), no_file)
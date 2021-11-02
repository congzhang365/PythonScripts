# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:01:27 2021

@author: kmarcoux

#This script was created to move files for KJ and KM to annotate toBI to be able to - to compare KJ, KM, and CZ's annotations
#It randomly takes 4 files per speaker per task and moves them into the destination file
#The ones that KJ and KM annotated - are a subset of the dataset - a list is provided: 
    SPRINT Dropbox\Academic Research\Production_Pilots\AM_annotation_information\KJ_all_files.txt
"""

import os
import os.path
import shutil
import random
import math
import csv
import io

text_source_folder ="C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/ToBI/Blank_all/"
wav_source_folder ="C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/utterances/"

output="C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/Prag_CZ/prag_cz_annotate_file.txt"
CZ_folder="C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/Prag_CZ/"
#KM_folder= "C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/ToBI/KM/"
#KJ_folder= "C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/ToBI/KJ/"
list_source = os.listdir(text_source_folder)


textgrids=[]
for item in list_source:
    if item.endswith(".TextGrid"):
        textgrids.append(item)

random.shuffle(textgrids)

LP01=[]
LP02=[]
LP03=[]
LP04=[]
LP05=[]
LP06=[]
LP08=[]
LP09=[]

for item in textgrids:
    if item[5:9]=="LP01":
        LP01.append(item)
    if item[5:9]=="LP02":
        LP02.append(item)
    if item[5:9]=="LP03":
        LP03.append(item)
    if item[5:9]=="LP04":
        LP04.append(item)
    if item[5:9]=="LP05":
        LP05.append(item)
    if item[5:9]=="LP06":
        LP06.append(item)
    if item[5:9]=="LP08":
        LP08.append(item)
    if item[5:9]=="LP09":
        LP09.append(item)


super_list=[LP01, LP02,LP03, LP04, LP05, LP06, LP08, LP09]
 #we want to move four files from each speaker
not_enough_files=[]
copied_files=[]
j=0
for item in super_list:
    i=0
    if len(item)<4:
        print("too few of", item)
        not_enough_files.append(item[0][5:9])
    for thing in item:
        if i<=3:
            #print(i, "moving", thing,text_source_folder+thing, CZ_folder)
            shutil.copy2(text_source_folder+thing, CZ_folder)
            wav_file=thing[:-9]+".wav"
            #print(i, "moving", wav_file,wav_source_folder+wav_file, CZ_folder)
            shutil.copy2(wav_source_folder+wav_file, CZ_folder)
            copied_files.append([thing]+[wav_file])
            i+=1
            j+=1

list_copied_files = os.listdir(CZ_folder)
list_copied=[]
for item in list_copied_files:
    if item.endswith(".wav"):
        list_copied.append(item[:-4])

with io.open(output, 'w', newline= '\n',encoding='utf8' ) as csvout:
    writer_out = csv.writer(csvout)
    for item in list_copied:
         writer_out.writerow([item])

# i=0
# len_text=math.ceil(len(textgrids)*0.2)
# for item in textgrids:
#     if i<=len_text:
#         print(i, "moving", item,source_folder+item, KM_folder)
#         shutil.copy2(source_folder+item, KM_folder)
#         i+=1


# i=0
# len_text=ceil(len(textgrids)*0.2)
# for item in textgrids:
#     num=i%3
#     if num ==0:
#         print(i, "moving", item,source_folder+item, CZ_folder)
#         #shutil.copy2(source_folder+item, CZ_folder)
#         i+=1
#     if num ==1:
#         print(i, "moving", item,source_folder+item, KJ_folder)
#         #shutil.copy2(source_folder+item, KJ_folder)
#         i+=1
#     if num ==2:
#         print(i, "moving", item,source_folder+item, KM_folder)
#         #shutil.copy2(source_folder+item, KM_folder)
#         i+=1

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:28:51 2021

@author: kmarcoux
"""

import shutil
import csv
import os

# all you need to change is the in_dir and out_file
# this script will loop through all tasks
# make sure the path keeps the %s and the % task part since it represents the task name

path="C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Perception_Studies/H_LH_emphasis/Stimuli/Matches/" 
group="only_LH_non_final"
list_files=path+group+".txt" 

tasks = ["DIAL", "MAPS", "OBJE", "TFLK", "TNEW", "SCUB"]

lists=[]
with open (list_files) as files:
    reader = csv.reader(files)
    for line in reader:
        wav=line[0]+".wav"
        textgrid=line[0]+".TextGrid"
        lists.append(wav)
        lists.append(textgrid)
#some of these have multiple words from the same file - so delete duplicates
lists_2=set(lists)
i=0
for task in tasks:
    in_dir = "C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/"% task
    
    for item in lists_2:
        output_dir=path+group+"/"
        if os.path.isfile(in_dir+item):
            print(i, "moving", item,in_dir+item, output_dir)
            shutil.copy2(in_dir+item, output_dir)
        i+=1
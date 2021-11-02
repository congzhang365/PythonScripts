import re
import pandas as pd
import os


task_name = "OBJE"
participant_name = ["LP01", "LP02", "LP03", "LP04", "LP05", "LP06", "LP08", "LP09"]

# input = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/%s_index_text.xlsx" % (task_name, task_name)
# output = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/txt/" % (task_name)


input = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Externally_Shared/Vicky Ioannidou_Dafni Bagioka/training_data/GRTR_index_text.xlsx"
output = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Externally_Shared/Vicky Ioannidou_Dafni Bagioka/training_data/txt/"

df = pd.read_excel(input, "Sheet1")
index_list = df.iloc[:, 0].to_list() # the column containing all index numbers
text_list = df.iloc[:, 1].to_list() # the column containing all texts


for i in range(0, len(index_list)):
    index = index_list[i]
    text = text_list[i]
    for participant in participant_name:
        with open(output + '%s.txt' % (index),  'w', encoding='UTF-8') as f:
                    f.write(text)
        # with open(output + 'all.csv', 'a', encoding='utf-8') as f:
        #         #    f.write(map_text + "\n")
        #         #    print("Done!")

    # # if different participants have different lines
    # with open(output + '%s.txt' % (index),  'w', encoding='UTF-8') as f:
    #                 f.write(text)


'''
This script reads creates text transcriptions for every small sound file in preparation for forced alignment.
    task name: specify task name for paths and final file names
    participant name: specify all participants to create files for all participants in one go
    input file: an excel file containing the index number (file names in the output), 
                and text transcription (main text in the txt files). 
    output folder: where you would like to save your result txt files

This script can also write all lines to one single csv file (uncomment last section).

Dr Cong Zhang 19/01/2020 @SPRINT
Last commit: 03/02/2020 
'''

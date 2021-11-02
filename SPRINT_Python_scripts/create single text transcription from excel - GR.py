import re
import pandas as pd
import os


task_name = "SRET"
participant_name = ["AP01", "AP02", "AP03", "AP04", "AP05", "AP06", "AP07", "AP08", "AP09"]

input = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/Greek/Athens/Audio/%s/%s_index_text.xlsx" % (task_name, task_name)
output = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/Greek/Athens/Audio/%s/txt/" % (task_name)


df = pd.read_excel(input, "Sheet1", encoding = 'utf-8')
# df = pd.read_csv(input, encoding = "ISO-8859-1")
index_list = df.iloc[:, 2].to_list() # the column containing all index numbers
text_list = df.iloc[:, 3].to_list() # the column containing all texts


# for i in range(0, len(index_list)):
#     index = index_list[i]
#     text = text_list[i].lower()
#
#     for participant in participant_name:
#         with open(output + '%s_%s_%s.txt' % (task_name, participant, index),  'w', encoding='UTF-8') as f:
#                     f.write(text)
#         # with open(output + 'all.csv', 'a', encoding='utf-8') as f:
#                 #    f.write(map_text + "\n")
#                 #    print("Done!")
#
#     # # if different participants have different lines
#     # with open(output + '%s.txt' % (index),  'w', encoding='UTF-8') as f:
#     #                 f.write(text)

for i in range(0, len(index_list)):
    index = index_list[i]
    text = text_list[i].lower()
    for participant in participant_name:
        with open(output + '%s.txt' % (index),  'w', encoding='UTF-8') as f:
                    f.write(text)
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

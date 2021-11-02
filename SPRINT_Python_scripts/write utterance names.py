import pandas as pd

task_name = "SCUB"
participant_name = ["LP01", "LP02", "LP03", "LP04", "LP05", "LP06", "LP08", "LP09"]

input = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/%s_index_text.xlsx" % (task_name, task_name)
output = "C:/Users/sprin/Desktop/test/new/"


df = pd.read_excel(input, "Sheet1")
sub = df.iloc[:,0:2]
for i in range(len(sub["filename"])):
    with open(output + '%s.txt' % (sub["filename"][i]),  'a', encoding='UTF-8') as f:
                    f.write(str(sub["utterance"][i] + '\n'))



'''
This script reads creates text files of utterance numbers in preparation for saving small sound files from long audio files (in prep for using "Save small sounds from long sound.praat")


    task name: specify task name for paths and final file names
    input file: an excel file containing the index number (file names in the output), 
                and the utterance numbers. 
    output folder: where you would like to save your result txt files


Dr Cong Zhang 19/01/2020 @SPRINT
Last commit: 03/02/2020 
'''

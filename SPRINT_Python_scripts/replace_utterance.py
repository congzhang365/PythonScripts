from praatio import textgrid        # you need python > 3.7 to install praatio 5.x
import os
import pandas as pd

# configure input, output, and excel
input_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/UPDATE/"
output_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/UPDATE/NEW/"
excel_file = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TNEW/TNEW_index_text.xlsx"
task = "TNEW"
speaker = "LP01"
#


df = pd.read_excel(excel_file, "Sheet1")
index_list = df.iloc[:, 0].to_list() # the column containing all index numbers
# text_list = df.iloc[:, 1].to_list() # the column containing all texts
bracket_text_list = df.iloc[:, 2].to_list() # the column containing bracket texts

for f in os.listdir(input_dir):
    # print(f)
    if f.endswith('.TextGrid'):
        tg_file = input_dir + f
        # print(tg_file)

        tg = textgrid.openTextgrid(tg_file, includeEmptyIntervals = False)
        # print(tg)

        sourceTier = tg.tierDict["utterance"]

        for i in range(len(index_list)):
            # print(index)

            # this line checks whether the name of the textgrid is the same as task+speaker+index
            # you can also use a column that contains all the file names instead of joining task, speaker, and index
            # e.g. column C in "MAPS_index_text.xlsx"
            # if f[:-9] == df.iloc[:, 2].to_list()
            if f[:-9] == '_'.join([task, speaker, index_list[i]]):
                print('_'.join([task, speaker, index_list[i]]))


                new_labels = []
                new_start = []
                new_end = []

                for i in range(len(sourceTier.entryList)):
                    start = sourceTier.entryList[0][0]
                    end = sourceTier.entryList[len(sourceTier.entryList)-1][1]
                    new_labels = bracket_text_list[i]
                # print(new_start,new_end,new_labels)
                # wordTier = tg.tierDict['word']
                # newWordTier = wordTier.new()

                new_entry = start, end, new_labels
                # new_entry = new_start, new_end, new_labels

                sourceTier.insertEntry(new_entry, collisionMode='replace', collisionReportingMode= 'silence')
                # print(sourceTier.entryList)
                tg.save(output_dir + f, format="short_textgrid", includeBlankSpaces=True)

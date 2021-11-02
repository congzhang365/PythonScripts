from praatio import textgrid        # you need python > 3.7 to install praatio 5.x
import os


input_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/OBJE/UPDATE/"
output_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/OBJE/UPDATE/"

for f in os.listdir(input_dir):
    print(f)
    if f.endswith('.TextGrid'):
        tg_file = input_dir + f
        print(tg_file)

        tg = textgrid.openTextgrid(tg_file, includeEmptyIntervals = False)
        # print(tg)
        sourceTier = tg.tierDict["utterance"]
        new_labels = []
        new_start = []
        new_end = []
        for i in range(len(sourceTier.entryList)):
            start = sourceTier.entryList[0][0]
            new_start = start
            end = sourceTier.entryList[len(sourceTier.entryList)-1][1]
            new_end = end
            label = sourceTier.entryList[i][2]
            new_labels.append(label)
        # print(new_start,new_end,new_labels)
        # wordTier = tg.tierDict['word']
        # newWordTier = wordTier.new()

        new_entry = new_start, new_end, ' '.join(new_labels)
        # new_entry = new_start, new_end, new_labels

        sourceTier.insertEntry(new_entry, collisionMode='replace', collisionReportingMode= 'silence')
        # print(sourceTier.entryList)
        tg.save(output_dir + f, format="short_textgrid", includeBlankSpaces=True)

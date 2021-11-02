from praatio import tgio # you need python 3.7 to install praatio 4.x (https://github.com/timmahrt/praatIO#version-4-to-5-migration)
import parselmouth
import re
import pandas as pd
import os
import more_itertools as mit
from itertools import groupby



def mark_accent(index_list, text_list, task, participant, pragmatics_list, brackets, sourceTier_name, targetTier_name,
                new_text):
    for i in range(0, len(index_list)):
        # a list of index, text, and text with pragmatics labels
        index = index_list[i]
        text = text_list[i]
        pragmatics = pragmatics_list[i]

        # searching for texts in brackets (or anything. Update the "brackets" variable using re)
        if brackets.search(pragmatics):
            keywordList = brackets.findall(pragmatics)
            keywordList = [''.join(tups) for tups in keywordList]
            # print(keywordList)
            tg = tgio.openTextgrid("%s/%s_%s_%s.TextGrid" % (in_tg, task, participant, index))
            keywordIntervals = []
            sourceTier = tg.tierDict[sourceTier_name]
            targetTier = tg.tierDict[targetTier_name]

            for keywords in keywordList:
                keyword = keywords.split(" ")

                # if there's only one word in the brackets
                if len(keyword) == 1:
                    print(index, keyword)

                    findMatches = sourceTier.find(str(keyword[0]))

                    for i in findMatches:
                        keywordIntervals.append(sourceTier.entryList[i])
                    for j in range(len(keywordIntervals)):
                        new_entry = [(start, stop, new_text) for start, stop, label in keywordIntervals]
                        targetTier.insertEntry(new_entry[j], collisionCode='replace')


                # if there's only one word in the brackets
                elif len(keyword) == 2:
                    print(index, keyword)

                    findMatches_1 = sourceTier.find(str(keyword[0]))
                    findMatches_2 = sourceTier.find(str(keyword[1]))


                    for ind in findMatches_1:
                        if ind + 1 in findMatches_2:
                            findMatches = [ind, ind + 1]
                            # print(findMatches)

                            new_entries = []
                            for i in findMatches:
                                new_entries.append(sourceTier.entryList[i])

                            time_points = []

                            for j in range(len(new_entries)):
                                # new_entry = [(start, stop, label) for start, stop, label in keywordIntervals]
                                start = new_entries[j][0]
                                stop = new_entries[j][1]
                                time_points.append(start)
                                time_points.append(stop)
                                # time_points.append(stop)
                            # print("!!---------", time_points)
                            new_entry = time_points[0], time_points[3], new_text
                            targetTier.insertEntry(new_entry, collisionCode='replace')

                elif len(keyword) == 3:
                    print(index, keyword)

                    findMatches_1 = sourceTier.find(str(keyword[0]))
                    findMatches_2 = sourceTier.find(str(keyword[1]))
                    findMatches_3 = sourceTier.find(str(keyword[2]))

                    if any(item in [x + 1 for x in findMatches_1] for item in findMatches_2) & any(
                            item in [x + 2 for x in findMatches_1] for item in findMatches_3):
                        for ind in findMatches_1:
                            if (ind + 1 in findMatches_2) & (ind + 2 in findMatches_3):
                                findMatches = [ind, ind + 1, ind + 2]

                                # for i in findMatches:
                                #     keywordIntervals.append(sourceTier.entryList[i])
                                #
                                # for j in range(len(keywordIntervals)):
                                #     new_entry = [(start, stop, new_text) for start, stop, label in keywordIntervals]
                                #     targetTier.insertEntry(new_entry[j], collisionCode='replace')
                            new_entries = []
                            for i in findMatches:
                                new_entries.append(sourceTier.entryList[i])

                            time_points = []

                            for j in range(len(new_entries)):
                                # new_entry = [(start, stop, label) for start, stop, label in keywordIntervals]
                                start = new_entries[j][0]
                                stop = new_entries[j][1]
                                time_points.append(start)
                                time_points.append(stop)
                                # time_points.append(stop)
                            # print("!!---------", time_points)
                            new_entry = time_points[0], time_points[5], new_text
                            targetTier.insertEntry(new_entry, collisionCode='replace')
                    else:
                        print(index, "!!!!!!!! Skipped! Check log!!!!!!!!")
                        # print(index, pragmatics)
                        outliers = index + '\t' + pragmatics + '\t' + str(datetime.now()) + '\n'
                        with open("%s/!log.txt" % out_tg, 'a') as f:
                            f.write(outliers)


                else:
                    print(index, "!!!!!!!! Skipped! Check log!!!!!!!!")
                    # print(index, pragmatics)
                    outliers = index + '\t' + pragmatics + '\t' + str(datetime.now()) + '\n'
                    with open("%s/!log.txt" % out_tg, 'a') as f:
                        f.write(outliers)

            tg.save("%s%s_%s_%s.TextGrid" % (out_tg, task, participant, index))

        else:
            print(index, 'No accent.')



if __name__ == '__main__':
    task = "TFLK"
    participants = ["LP01", "LP02", "LP03", "LP04", "LP05", "LP06", "LP08", "LP09"]
    # participants = ["LP01"] # for testing

    in_excel = "C:/Users/sprin/Desktop/test/mark/TEST.xlsx"
    in_tg = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TFLK/utterances/"
    out_tg = in_tg  # !!! Note: for now, the out_tg has to be the same as the in_tg if multiple tiers are modified at the same time.

    square_brackets = re.compile('\[\[(.*?)\]\]')
    angle_brackets = re.compile('\<\<(.*?)\>\>')
    curly_brackets = re.compile('\{\{(.*?)\}\}')
    round_brackets = re.compile('\(\((.*?)\)\)')
    all_brackets = re.compile('\[(.*?)\]|\<(.*?)\>|\{(.*?)\}|\((.*?)\)')

    for participant in participants:
        df = pd.read_excel(in_excel, "Sheet1")
        index_list = df.iloc[:, 0].to_list()  # the column containing all index numbers
        text_list = df.iloc[:, 1].to_list()  # the column containing all texts
        pragmatics_list = df.iloc[:, 2].to_list()  # the column containing all pragmatic analysis labels

        ##### ##### #####
        # label information tier
        sourceTier_name = "utterance"
        targetTier_name = "information"

        ## find square brackets: new information
        brackets = square_brackets
        new_text = "N"
        mark_accent(index_list, text_list, task, participant, pragmatics_list, brackets, sourceTier_name,
                    targetTier_name, new_text)

        ## find angle brackets: given information
        brackets = round_brackets
        new_text = "G"
        mark_accent(index_list, text_list, task, participant, pragmatics_list, brackets, sourceTier_name,
                    targetTier_name, new_text)

        ## find curly brackets: contrastive information
        brackets = curly_brackets
        new_text = "C"
        mark_accent(index_list, text_list, task, participant, pragmatics_list, brackets, sourceTier_name,
                    targetTier_name, new_text)

        ## find angle brackets: unsure what information
        brackets = angle_brackets
        new_text = "N G C*"  # need manual correction in textgrid
        mark_accent(index_list, text_list, task, participant, pragmatics_list, brackets, sourceTier_name,
                    targetTier_name, new_text)

        ##### ##### #####
        # label location tier
        sourceTier_name = "utterance"
        targetTier_name = "location"
        brackets = all_brackets
        new_text = "I M L"
        mark_accent(index_list, text_list, task, participant, pragmatics_list, brackets, sourceTier_name,
                    targetTier_name, new_text)


        ##### ##### #####
        # label stress tier
        sourceTier_name = "utterance"
        targetTier_name = "stress"
        brackets = all_brackets
        new_text = "S"
        mark_accent(index_list, text_list, task, participant, pragmatics_list, brackets, sourceTier_name,
                    targetTier_name, new_text)

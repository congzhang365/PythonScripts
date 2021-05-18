import re
import pandas as pd
import os
import shutil
from praatio import tgio

input_dir = "C:/Users/sprin/Desktop/test/mark/data/"
target_dir = "C:/Users/sprin/Desktop/test/mark/data/new/"



def tier_text(tg, tier_number):
    # What tiers are stored in this textgrid?
    # print(tg.tierNameList)

    # It's possible to access the tiers by their position in the TextGrid
    # (i.e. the order they were added in)
    text_in_tier = tg.tierDict[tg.tierNameList[tier_number-1]]

    # # Or by their names
    # wordTier = tg.tierDict['word']

    # I just want the labels from the entryList
    labelList = [entry[2] for entry in text_in_tier.entryList]

    # print(labelList)
    return labelList


def move_file(in_dir, tar_dir):
    files = os.listdir(in_dir)
    files.sort()
    for f in files:
        source = in_dir+f
        dest = tar_dir+f
        shutil.move(source,dest)


for f in os.listdir(input_dir):
    if f.endswith(".TextGrid"):
        tg = tgio.openTextgrid(os.path.join(input_dir, f))
        snd = str(f[:-8]) + 'wav'

        labelList = tier_text(tg, 4)
        if labelList == []:
            shutil.move(input_dir + f, target_dir + f)
            if os.path.exists(input_dir + snd):
                shutil.move(input_dir + snd, target_dir + snd)
                print('Moved', snd)
            else:
                print(snd, 'does not exist.')

            print('Moved:', f)
        else:
            print('Not moved:', f)


        # utterance = f.split('_')[2]
        # # print(utterance)
        #
        # tg = tgio.openTextgrid(os.path.join(input_dir, f))
        # # print(len(tg.tierNameList))
        #
        # # check whether the textgrid had the expected number of tiers
        # if len(tg.tierNameList) != expected_tier_number:
        #     print(f)
        #
        # # check if a certain tier has the expected number of intervals
        # selected_tier = tg.tierDict[tg.tierNameList[-1]]
        # labelList = [entry[2] for entry in selected_tier.entryList]
        # # print(f, ": ", len(labelList))
        #
        # if expected_intervals[utterance] != len(labelList):
        #     print(f, ":", len(labelList))


        # labelList = [entry[2] for entry in wordTier.entryList]
        # print(labelList)

        # moddedTG.save(os.path.join(output_dir, f))




# entryList = tg.tierDict["speaker_1_tier"].entryList # Get all intervals

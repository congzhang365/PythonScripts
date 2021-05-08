import re
import pandas as pd
import os
from praatio import tgio

input_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Related_Projects/Comparison_Study/Full/Processed_Data/cut/vowel-level/archive/H6"
# output_dir = "C:/Users/sprin/Desktop/test/t/new2"
expected_tier_number = 4
expected_intervals = {"U1": 7,
                      "U2": 6,
                      "U3": 4,
                      "U4": 6,
                      "U5": 6}

for f in os.listdir(input_dir):
    if f.endswith(".TextGrid"):
        # print(f)

        utterance = f.split('_')[2]
        # print(utterance)

        tg = tgio.openTextgrid(os.path.join(input_dir, f))
        # print(len(tg.tierNameList))

        # check whether the textgrid had the expected number of tiers
        if len(tg.tierNameList) != expected_tier_number:
            print(f)

        # check if a certain tier has the expected number of intervals
        selected_tier = tg.tierDict[tg.tierNameList[-1]]
        labelList = [entry[2] for entry in selected_tier.entryList]
        # print(f, ": ", len(labelList))

        if expected_intervals[utterance] != len(labelList):
            print(f, ":", len(labelList))


        # labelList = [entry[2] for entry in wordTier.entryList]
        # print(labelList)

        # moddedTG.save(os.path.join(output_dir, f))




# entryList = tg.tierDict["speaker_1_tier"].entryList # Get all intervals

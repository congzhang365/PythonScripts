import re
import pandas as pd


def extract_participant_line(md_text, md_index):
    '''
    md_text is the entire mini dialogue
    md_index is the index number of the current mini dialogue
    '''
    md_by_line = md_text.split('\n')
    text_b = md_by_line[1].lstrip().lower()  # participant line (leading spaces are removed 'lstrip')

    non_spoken = re.compile('(\[.*?\])') # content in square brackets
    text_b = non_spoken.sub("", text_b)  # delete contents in square brackets
    punctuation = re.compile("\.|\;|\*|\<|\>|\!")
    text_b = punctuation.sub("", text_b) # remove .;*<>!
    return text_b



if __name__ == '__main__':
    input = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Task_Materials/Dialogue_Task/GR/Rand_Formula.xlsx"
    output = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/Greek/Athens/DIAL/individual wavs/txt/"
    df = pd.read_excel(input, "May2020")
    index_list = df.iloc[:, 0].to_list()
    text_list = df.iloc[:, 1].to_list()


    for i in range(0, len(df)):
        md_index = "DIAL" + index_list[i][4:7]
        md_text = text_list[i]
        participant_line = extract_participant_line(md_text, md_index)
        participant_numbers = ["AP01", "AP02", "AP03", "AP04", "AP05", "AP06", "AP07", "AP08"]
        for participant_number in participant_numbers:
            with open(output + "DIAL_" + participant_number + "_" + md_index + '.txt', 'w', encoding='utf-8') as f:
                f.write(participant_line)
                print("Done!")

'''
This script extracts the participant lines from the SRPINT Greek data
The participant lines contain unspoken contents in [] and <>. These are removed from the participant lines.
    To run this file, you need to install
        regex
        pandas
    input file: an excel file containing the conversations. 
    output folder: where you would like to save your result txt files

Dr Cong Zhang 06/11/2020 @SPRINT
Last commit: 06/11/2020 
'''

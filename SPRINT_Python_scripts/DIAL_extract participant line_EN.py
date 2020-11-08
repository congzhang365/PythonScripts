import re
import pandas as pd


def find_bold(str):
    ## find text in angle brackets and return everything except for the angle brackets themselves

    bold = re.compile('(<.*?>)')
    str_word = str.split(" ")
    # print(str_word)
    for i in range(len(str_word)):
        if not bold.search(str_word[i]):
            text = " " + str_word[i]

        else:
            text = " " + str_word[i].replace('<', "").replace('>', "")
    return text


def find_bracket(str):
    ## find text in square brackets and return what's NOT in the brackets
    brackets = re.compile('(\(.*?\))')
    # print(str_word)
    if brackets.search(str):
        bracket_text = brackets.findall(str)[0]
        text_b_main = str.replace(bracket_text, '')
    else:
        text_b_main = str
    return text_b_main


def find_bold_bracket(str):
    ## find text in angle brackets and round bracket together, and return what's NOT in the round brackets and remove angle brackets

    bold = re.compile('(<.*?>)')
    brackets = re.compile('(\(.*?\))')
    both = re.compile('(<.*?>)|(\(.*?\))')
    run_text_list = list(filter(None, re.split(both, str)))
    # print(run_text_list)
    for i in range(len(run_text_list)):
        if bold.search(run_text_list[i]):
            text = run_text_list[i].replace('<', "").replace('>', "")
        elif brackets.search(run_text_list[i]):
            text = run_text_list[0]

        else:
            text = run_text_list[i]
    return text


def separate_lines(md_text, md_index):
    '''
    md_text is the entire mini dialogue
    md_index is the index number of the current mini dialogue
    '''

    md_by_line = md_text.split('\n')
    text_a = md_by_line[0]
    text_b = md_by_line[1]

    if len(md_by_line) == 2:
        confederate_line1 = text_a
        participant_line = find_bold_bracket(text_b)
        confederate_line2 = ''

    elif len(md_by_line) == 3:
        confederate_line1 = text_a
        participant_line = find_bold_bracket(text_b)
        confederate_line2 = md_by_line[2]

    dial_index = md_index  # mini_dialogue index
    return dial_index, confederate_line1, participant_line, confederate_line2


if __name__ == '__main__':
    input = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Task_Materials/Dialogue_Task/EN/dialogues_EN.xlsx"
    output = "C:/Users/sprin/Desktop/test/txt/"
    prefix = 'DIAL_LP01_mono_'
    version = 'RAND1'
    df = pd.read_excel(input, "pilot_order").sort_values(by=version) # sort df by Column 'RAND1'
    index_list = df.iloc[:, 0].to_list()
    text_list = df.iloc[:, 1].to_list()


    for i in range(0, len(df)):
        md_index = index_list[i]
        md_text = text_list[i]
        dial_index = separate_lines(md_text, md_index)[0]
        confederate_line1 = separate_lines(md_text, md_index)[1]
        participant_line = separate_lines(md_text, md_index)[2]
        confederate_line2 = separate_lines(md_text, md_index)[3]
        print(dial_index, participant_line)
        # with open(output + prefix + '%s.txt' % dial_index,  'w', encoding='UTF-8') as f:
        #     f.write(participant_line)


'''
This script is for extracting participants' lines in the dialogue task
    To run this file, you need to install
        regex
        pandas
    input file: tab-delimited txt file or excel file. Comment out the option that you don't need.


Dr Cong Zhang 26/06/2020 @SPRINT
Last commit: 26/06/2020 
'''

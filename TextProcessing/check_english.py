import re

def count_appearances(str):
    counts = dict()
    words = str.split()

    for token in words:
        if token in counts:
            counts[token] += 1
        else:
            counts[token] = 1
    return counts


def count_English_words(input_file, output_file):
    with open (input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        word_num = []
        for i in range(len(lines)):
            count = len(re.findall("[a-zA-Z_]+", lines[i]))
            word_num.append(count)
        total_num = sum(word_num)
        # print(sum(word_num))
        all_lines = 'total words in this document: %d\n' %total_num + 'number of words on each line: \n' + ''.join(str(word_num))
    with open('%s.txt'%output_file, 'w', encoding='utf-8') as file:
        file.write(str(all_lines))




#### unfinished code, probably useless
# def
#     with open('D:\Rokid\pycharm\English/new.txt','r', encoding='utf-8') as f:
#         lines = f.readlines()
#         new_nums = []
#         for i in range(len(lines)):
#             if i % 2 == 0:
#                 new_num = re.sub(r'[^\x00-\x7F]|(#2)|(#3)', '-', lines[i])
#                 new_nums.append(new_num)
#             else:
#                 new_num = re.sub(r'[a-z]+\d', '-', lines[i])
#                 new_nums.append(new_num)
#
#             # new_line = new_num + lines[i+1]
#             # new_nums.append(new_line)
#     with open('only_english2.txt', 'w', encoding='utf-8') as file:
#         file.write(''.join(new_nums))
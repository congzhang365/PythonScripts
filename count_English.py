import re

def count_English(input_file):
    with open('%s'%input_file,'r', encoding='utf-8') as f:
        lines = f.readlines()
        wrong_ones = []
        correct_ones = []
        for i in range(len(lines)):
            if i % 2 == 0:
                idx = lines[i].split('\t')[0]
                sentence = lines[i].split('\t')[1].strip('\n')
                subbed = re.sub(r'[^\x00-\x7F]', '-', sentence)
                text = re.sub(r"(-#1-)", '-', subbed)
                annotation = lines[i+1].strip('\n')
                sub_anno = re.sub(r'[a-z]+\d', '-', annotation)
                word = re.split('#1',text)
                word_annotation = sub_anno.split('/')
                # print(len(word), len(word_annotation))

                if len(word) != len(word_annotation):
                    linked = idx + '\t'+ text+ '\n'+ sub_anno+ '\n'
                    wrong_ones.append(linked)
                else:
                    linked = idx + '\t'+ text+ '\n'+ sub_anno+ '\n'
                    correct_ones.append(linked)
        # print('wrong ones:',''.join(wrong_ones))
        # print('right ones:',''.join(correct_ones))
        print('wrong ones:', len(wrong_ones))
        print('right ones:', len(correct_ones))

    with open('wrong.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(wrong_ones))

    with open('right.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(correct_ones))











            # print(''.join(new_lines))
        # else:
        #     new_num = re.sub(r'[a-z]+\d', '-', lines[i])
        #     new_nums.append(new_num)
#
#             # new_line = new_num + lines[i+1]
#             # new_nums.append(new_line)
# with open('only_english.txt', 'w', encoding='utf-8') as file:
#     file.write(''.join(new_nums))
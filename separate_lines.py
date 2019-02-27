import re

def separate_lines(file, odd, even):
    with open(file,'r', encoding='utf-8') as f:
        lines = f.readlines()
        odd_lines = []
        even_lines = []
        for i in range(len(lines)):
            if i % 2 == 0:
                odd_lines.append(lines[i])
            else:
                even_lines.append(lines[i])
    with open('%s.txt'%odd, 'w', encoding='utf-8') as file:
        file.write(''.join(odd_lines))
    with open('%s.txt'%even, 'w', encoding='utf-8') as file:
        file.write(''.join(even_lines))

def remove_labels(file, old_text, new_text, output_file):

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = []
        for i in range(len(lines)):
            new_line = re.sub(old_text, new_text, lines[i])
            new_lines.append(new_line)
    with open('%s.txt'%output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(new_lines))

text = 'D:\Rokid\pycharm\DataTest/000001-010000.txt'
separate_lines(text, 'text', 'pinyin')

# chinese = 'D:\Rokid\pycharm\DataTest\chinese.txt'
# old_text = re.compile(r'(#1)|(#2)|(#3)|(#4)')
# new_text = ''
# remove_labels(chinese, old_text, new_text, 'clean')

no_punc = 'D:\Rokid\pycharm\DataTest/no_punc.txt'
remove_labels(no_punc, '')
import re

'''
This file is to deal with files with a line of Chinese characters and a line of pinyin.
The character line is usually the odd line, and the pinyin line, even line.

'''

# separate text line from pinyin line
# write the results into different txt files
def separate_lines(file, odd, even):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        odd_lines = []
        even_lines = []
        for i in range(len(lines)):
            if i % 2 == 0:
                odd_lines.append(lines[i])
            else:
                even_lines.append(lines[i])
    with open('%s.txt' % odd, 'w', encoding='utf-8') as file:
        file.write(''.join(odd_lines))
    with open('%s.txt' % even, 'w', encoding='utf-8') as file:
        file.write(''.join(even_lines))


# replace old_text with new_text
def remove_labels(file, old_text, new_text, output_file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = []
        for i in range(len(lines)):
            new_line = re.sub(old_text, new_text, lines[i])
            new_lines.append(new_line)
    with open('%s.txt' % output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(new_lines))


if __name__ == '__main__':
    text = "D:\Rokid\data\儿童005501-006000.txt"
    separate_lines(text, 'song1000_text', 0)

    # chinese = 'D:\Rokid\pycharm\DataTest\chinese.txt'
    # old_text = re.compile(r'(#1)|(#2)|(#3)|(#4)')
    # new_text = ''
    # remove_labels(chinese, old_text, new_text, 'clean')
    #
    # no_punc = 'D:\Rokid\pycharm\DataTest/no_punc.txt'
    # remove_labels(no_punc, '')

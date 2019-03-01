import re
with open('D:\Rokid\pycharm\English/new.txt','r', encoding='utf-8') as f:
    lines = f.readlines()
    new_nums = []
    for i in range(len(lines)):
        if i % 2 == 0:
            new_num = re.sub(r'[^\x00-\x7F]|(#2)|(#3)', '-', lines[i])
            new_nums.append(new_num)
        else:
            new_num = re.sub(r'[a-z]+\d', '-', lines[i])
            new_nums.append(new_num)

            # new_line = new_num + lines[i+1]
            # new_nums.append(new_line)
with open('only_english2.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(new_nums))
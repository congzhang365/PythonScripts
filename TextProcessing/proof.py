import re
with open('D:\Rokid\pycharm\English\mix/text.txt','r', encoding='utf-8') as f:
    lines = f.readlines()
    new_nums = []
    for i in range(len(lines)):
        if i % 2 == 0:
            # print(lines[i])
            new_num = re.sub(r'\d', r'3', lines[i], count=1)
            new_line = new_num + lines[i+1]
            new_nums.append(new_line)
with open('new.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(new_nums))
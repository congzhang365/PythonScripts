import re
def change_names(input_file, old_tag, new_tag, output_file):
    with open(input_file,'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_nums = []
        for i in range(len(lines)):
            new_num = re.sub(old_tag, new_tag, lines[i], count=1)
            new_nums.append(new_num)
    with open('%s.txt'%output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(new_nums))

## This is for changing the line numbers on odd lines
## add 'not' on 'if' line when the line numbers are on even lines
def change_names_skipline(input_file, old_tag, new_tag, output_file):
    with open(input_file,'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_nums = []
        for i in range(len(lines)):
            if i % 2 == 0:
                # print(lines[i])
                new_num = re.sub(old_tag, new_tag, lines[i+1], count=1)
                new_line = new_num + lines[i]
                new_nums.append(new_line)
    with open('%s.txt'%output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(new_nums))

if __name__ == '__main__':
    file = "D:\Rokid\Projects\Songs\实验\ex1\song1000_text.txt"
    old = re.compile(r'\d')
    new = '4'
    change_names(file, old, new, "D:\Rokid\Projects\Songs\实验\ex1\song1000.txt")

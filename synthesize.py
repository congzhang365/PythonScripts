with open('D:\Rokid\pycharm\English/output_dict','r', encoding='utf-8') as f:
    lines = f.readlines()
    new_lines = []
    for i in range(len(lines)):
        pron = lines[i].split('\t')[1]
        new_lines.append(pron)
with open('synth.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(new_lines))
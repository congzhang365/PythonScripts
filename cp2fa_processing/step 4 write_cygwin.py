import sys
sys.path.append('D:\Rokid\pycharm\_PythonScripts')
import os


input_dir ="C:/Users\Cong\Desktop\ViaX\Xinrong Wang\S4\cut"

lines = []
for root, dirs, files in os.walk(input_dir):
    break
for file in files:
    filename = file[:-4]
    line = 'python align.py mirex/%s.wav mirex/%s.txt mirex/%s.TextGrid' % (filename, filename, filename)
    lines.append(line)
with open('C:/Users\Cong\Desktop\ViaX\Xinrong Wang\S4\cut/align.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))


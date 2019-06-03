import parselmouth
from parselmouth.praat import call
import os
import pandas as pd



def extract_pitch(input_dir,output_dir):

    if os.path.isdir(input_dir):
        # print(input_dir)
        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith('.wav'):
                snd = parselmouth.Sound(input_dir+file)
                dur = snd.get_total_duration()
                manipulation = call(snd, "To Manipulation", 0.01, 75, 600)
                pitch_tier = call(manipulation, "Extract pitch tier")
                # print(pitch_tier)

                # # create a file with two columns:
                # first col is time (0.01s step by default), second col is pitch (hz)
                resultfile_padding = 'result'
                output_name = '%s%s_%s.txt' % (output_dir, file[:-4],resultfile_padding)
                call(pitch_tier, "Write to headerless spreadsheet file", output_name)
                print(output_name)
                # rounding time info to 2 digits
                with open('%s'%output_name, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    # rounded_time = []
                    # all_pitch = []
                    new_lines = []
                    for line in lines:
                        time = line.split('\t')[0]
                        rounded = round(float(time),2)
                        # rounded_time.append(rounded)
                        pitch = line.split('\t')[1]
                        # all_pitch.append(pitch)
                        new_line = str(rounded) + '\t' + pitch
                        new_lines.append(new_line)

                    final = ''.join(new_lines)
                    # print(final)

                with open('%s'%output_name, 'w', encoding='utf-8') as f:
                    f.write(final)


if __name__ == '__main__':
    dir = ("D:\Rokid\pycharm\music/align_lyrics/")
    out = dir
    extract_pitch(dir, out)
import parselmouth
from parselmouth.praat import call
import os
import pandas as pd
import numpy as np
import praatio


def extract_pitch_separate_txt(input_dir, output_dir, time_step, min_f0, max_f0):
    if os.path.isdir(input_dir):
        # print(input_dir)
        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith('.wav'):
                snd = parselmouth.Sound(input_dir + file)
                dur = snd.get_total_duration()
                manipulation = call(snd, "To Manipulation", time_step, min_f0, max_f0)
                pitch_tier = call(manipulation, "Extract pitch tier")
                print(pitch_tier)

                # # create a file with two columns:
                # first col is time (0.01s step by default), second col is pitch (hz)
                resultfile_padding = 'result'
                output_name = '%s%s_%s.txt' % (output_dir, file[:-4], resultfile_padding)
                call(pitch_tier, "Write to headerless spreadsheet file", output_name)
                print(output_name)
                # rounding time info to 2 digits
                with open('%s' % output_name, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    # rounded_time = []
                    # all_pitch = []
                    new_lines = []
                    for line in lines:
                        time = line.split('\t')[0]
                        rounded = round(float(time), 2)
                        # rounded_time.append(rounded)
                        pitch = line.split('\t')[1]
                        # all_pitch.append(pitch)
                        new_line = str(rounded) + '\t' + pitch
                        new_lines.append(new_line)

                    final = ''.join(new_lines)
                    # print(final)

                with open('%s' % output_name, 'w', encoding='utf-8') as f:
                    f.write(final)


def extract_pitch_one_txt(input_dir, output_dir, time_step, min_f0, max_f0):
    if os.path.isdir(input_dir):
        # print(input_dir)
        for root, dirs, files in os.walk(input_dir):
            break
        results = []
        for file in files:
            if file.endswith('.wav'):
                # results.append()

                snd = parselmouth.Sound(input_dir + file)
                dur = snd.get_total_duration()
                tmin = 0
                tmax = dur
                pitch = snd.to_pitch(time_step, min_f0, max_f0)
                for time in np.arange(tmin, tmax-tmin, time_step):
                    pitch_value = pitch.get_value_at_time(time)

                    pitch_listing_line = str(file[:-4]) + \
                                   "\t" + \
                                   str(round(time, str(time_step)[::-1].find('.'))) + \
                                   "\t" + \
                                   str(pitch_value)+ \
                                   "\n"
                    results.append(pitch_listing_line)

        output_name = "results.txt"
        title_line = "filename\ttime\tf0\n"


        with open('%s%s' % (output_dir, output_name), 'w+', encoding='utf-8') as f:
            f.write(title_line)
            f.write(''.join(results))
            print("Mission accomplished.")


if __name__ == '__main__':
    input_dir = "C:/Users/sprin/Dropbox (Personal)/Journal_Article/TJ_YNQ/data/production/audio/"
    output_dir = "C:/Users/sprin/Desktop/test/ynq/"
    time_step = 0.01
    min_f0 = 50
    max_f0 = 500
    extract_pitch_one_txt(input_dir, output_dir, time_step, min_f0, max_f0)

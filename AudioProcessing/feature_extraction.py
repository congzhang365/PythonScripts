import parselmouth
from parselmouth.praat import call
import os
import pandas as pd
import numpy as np
from praatio import tgio
import re

def extract_pitch_separate_txt(input_dir, output_dir, time_step, min_f0, max_f0):
    if os.path.isdir(input_dir):
        # print(input_dir)
        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith('.wav') and not ("D" in file or "E" in file or "F" in file):
                snd = parselmouth.Sound(input_dir + file)
                dur = snd.get_total_duration()
                manipulation = call(snd, "To Manipulation", time_step, min_f0, max_f0)
                pitch_tier = call(manipulation, "Extract pitch tier")
                # print(pitch_tier)

                # # create a file with two columns:
                # first col is time (0.01s step by default), second col is pitch (hz)
                resultfile_padding = 'result'
                output_name = '%s%s_%s.txt' % (output_dir, file[:-4], resultfile_padding)
                call(pitch_tier, "Write to headerless spreadsheet file", output_name)
                # print(output_name)
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


def extract_pitch_one_txt(input_dir, tg_dir, analysis_tier, output_file, time_step, min_f0, max_f0):
    if os.path.isdir(input_dir):
        for root, dirs, files in os.walk(input_dir):
            break

        results = []

        for file in files:
            if file.endswith('.wav'):
                base_name = file[:-4]
                snd = parselmouth.Sound(input_dir + file)
                pitch = snd.to_pitch(time_step, min_f0, max_f0)

                dur = snd.get_total_duration()

                textgrid = str("%s.Textgrid" % base_name)

                tg = tgio.openTextgrid(os.path.join(tg_dir, textgrid))
                labels = tg.tierDict[tg.tierNameList[analysis_tier-1]].entryList
                for label in labels:
                    min_t, max_t, text = label


                    for time in np.arange(min_t, max_t, time_step):
                        # print(time)
                        pitch_value = pitch.get_value_at_time(time)
                        rounded_time = round(time, str(time_step)[::-1].find('.'))
                        pitch_listing_line = str(file[:-4]) + \
                                       "\t" + \
                                        str(text) + \
                                        "\t" + \
                                       str(time) + \
                                       "\t" + \
                                        str(min_t) + \
                                        "\t" + \
                                        str(max_t) + \
                                        "\t" + \
                                        str(max_t-min_t) + \
                                        "\t" + \
                                       str(rounded_time) + \
                                       "\t" + \
                                       str(pitch_value)+ \
                                       "\n"
                        results.append(pitch_listing_line)
                        # print(pitch_listing_line)

            title_line = "filename\ttext\ttime\tmin_t\tmax_t\tdur\trounded_time\tf0\n"


            with open('%s' % (output_file), 'w+', encoding='utf-8') as f:
                f.write(title_line)
                f.write(''.join(results))
    print("Mission accomplished.")


def extract_pitch_by_gender(input_dir, tg_dir, analysis_tier, output_file, time_step, min_f0, max_f0):
    if os.path.isdir(input_dir):
        for root, dirs, files in os.walk(input_dir):
            break

        results = []

        for file in files:
            if file.endswith('.wav') and ("D" in file or "E" in file or "F" in file):
                base_name = file[:-4]
                snd = parselmouth.Sound(input_dir + file)
                pitch = snd.to_pitch(time_step, min_f0, max_f0)

                dur = snd.get_total_duration()

                textgrid = str("%s.Textgrid" % base_name)

                tg = tgio.openTextgrid(os.path.join(tg_dir, textgrid))
                labels = tg.tierDict[tg.tierNameList[analysis_tier-1]].entryList
                for label in labels:
                    min_t, max_t, text = label


                    for time in np.arange(min_t, max_t, time_step):
                        # print(time)
                        pitch_value = pitch.get_value_at_time(time)
                        rounded_time = round(time, str(time_step)[::-1].find('.'))
                        pitch_listing_line = str(file[:-4]) + \
                                       "\t" + \
                                        str(text) + \
                                        "\t" + \
                                       str(time) + \
                                       "\t" + \
                                        str(min_t) + \
                                        "\t" + \
                                        str(max_t) + \
                                        "\t" + \
                                        str(max_t-min_t) + \
                                        "\t" + \
                                       str(rounded_time) + \
                                       "\t" + \
                                       str(pitch_value)+ \
                                       "\n"
                        results.append(pitch_listing_line)
                        # print(pitch_listing_line)

            title_line = "filename\ttext\ttime\tmin_t\tmax_t\tdur\trounded_time\tf0\n"


            with open('%s' % (output_file), 'w+', encoding='utf-8') as f:
                f.write(title_line)
                f.write(''.join(results))
    print("Mission accomplished.")



if __name__ == '__main__':
    input_dir = "C:/Users/sprin/Dropbox (Personal)/Journal_Article/TJ_YNQ/data/production/audio/"
    tg_dir = input_dir
    analysis_tier = 2


    # output_file = "C:/Users/sprin/Desktop/test/ynq/f.txt"
    output_dir = "C:/Users/sprin/Desktop/test/ynq/m/"
    time_step = 0.01
    min_f0 = 130
    max_f0 = 370
    extract_pitch_by_gender(input_dir, tg_dir, analysis_tier, output_file, time_step, min_f0, max_f0)

    # output_file = "C:/Users/sprin/Desktop/test/ynq/m.txt"
    # output_dir = "C:/Users/sprin/Desktop/test/ynq/m/"
    # time_step = 0.01
    # min_f0 = 55
    # max_f0 = 265
    # extract_pitch_separate_txt(input_dir, output_dir, time_step, min_f0, max_f0)

import parselmouth
from parselmouth.praat import call
import os
import numpy as np
from praatio import tgio


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
                labels = tg.tierDict[tg.tierNameList[analysis_tier - 1]].entryList
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
                                             str(max_t - min_t) + \
                                             "\t" + \
                                             str(rounded_time) + \
                                             "\t" + \
                                             str(pitch_value) + \
                                             "\n"
                        results.append(pitch_listing_line)
                        # print(pitch_listing_line)

            title_line = "filename\ttext\ttime\tmin_t\tmax_t\tdur\trounded_time\tf0\n"

            with open('%s' % output_file, 'w+', encoding='utf-8') as f:
                f.write(title_line)
                f.write(''.join(results))
    print("Mission accomplished.")


def extract_pitch_by_gender(input_dir, tg_dir, analysis_tier, output_file, time_step, min_f0, max_f0):
    if os.path.isdir(input_dir):
        for root, dirs, files in os.walk(input_dir):
            break

        results = []

        for file in files:
            if file.endswith('.wav') and ("SJ101" in file or "SJ106" in file or "SJ110" in file):
                base_name = file[:-4]
                snd = parselmouth.Sound(input_dir + file)
                pitch = snd.to_pitch(time_step, min_f0, max_f0)

                dur = snd.get_total_duration()

                textgrid = str("%s.Textgrid" % base_name)

                tg = tgio.openTextgrid(os.path.join(tg_dir, textgrid))
                labels = tg.tierDict[tg.tierNameList[analysis_tier - 1]].entryList
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
                                             str(max_t - min_t) + \
                                             "\t" + \
                                             str(rounded_time) + \
                                             "\t" + \
                                             str(pitch_value) + \
                                             "\n"
                        results.append(pitch_listing_line)
                        # print(pitch_listing_line)

            title_line = "filename\ttext\ttime\tmin_t\tmax_t\tdur\trounded_time\tf0\n"

            with open('%s' % output_file, 'w+', encoding='utf-8') as f:
                f.write(title_line)
                f.write(''.join(results))
    print("Mission accomplished.")


def extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword):
    if os.path.isdir(input_dir):
        for root, dirs, files in os.walk(input_dir):
            break

        results = []

        for file in files:
            if file.endswith('.wav') and (keyword in file):
                print(file)
                snd = parselmouth.Sound(input_dir + file)
                pitch = snd.to_pitch_ac(time_step, pitch_floor=min_f0, pitch_ceiling=max_f0, octave_cost=octave_cost)
                # pitch = snd.to_pitch(time_step, min_f0, max_f0)

                dur = snd.get_total_duration()
                # manipulation = call(snd, "To Manipulation", time_step, min_f0, max_f0)
                # pitch_tier = call(manipulation, "Extract pitch tier")

                for time in np.arange(0, dur, time_step):
                    # print(time)
                    pitch_value = pitch.get_value_at_time(time)
                    rounded_time = round(time, str(time_step)[::-1].find('.'))
                    pitch_listing_line = str(file[:-4]) + \
                                         "\t" + \
                                         str(rounded_time) + \
                                         "\t" + \
                                         str(pitch_value) + \
                                         "\n"
                    results.append(pitch_listing_line)

            title_line = "filename\ttime\tf0\n"

            with open('%s' % output_file, 'w+', encoding='utf-8') as f:
                f.write(title_line)
                f.write(''.join(results))
    print("Mission accomplished.")


if __name__ == '__main__':
    # tasks = ["SCUB"]
    tasks = ["DIAL", "OBJE", "TFLK", "TNEW", "SCUB", "MAPS"]
    for task in tasks:
        try:
            keyword = "LP01"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (task, keyword)

            time_step = 0.01
            min_f0 = 75
            max_f0 = 235
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

            keyword = "LP02"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (
            task, keyword)

            time_step = 0.01
            min_f0 = 95
            max_f0 = 290
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

            keyword = "LP03"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (
            task, keyword)

            time_step = 0.01
            min_f0 = 75
            max_f0 = 200
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

            keyword = "LP04"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (
            task, keyword)

            time_step = 0.01
            min_f0 = 120
            max_f0 = 345
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

            keyword = "LP05"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (
            task, keyword)

            time_step = 0.01
            min_f0 = 95
            max_f0 = 390
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

            keyword = "LP06"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (
            task, keyword)

            time_step = 0.01
            min_f0 = 75
            max_f0 = 320
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

            keyword = "LP08"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (
            task, keyword)

            time_step = 0.01
            min_f0 = 125
            max_f0 = 290
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

            keyword = "LP09"

            input_dir = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/" % task
            output_file = r"C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/%s_%s.txt" % (
            task, keyword)

            time_step = 0.01
            min_f0 = 75
            max_f0 = 230
            octave_cost = 0.1
            extract_all_with_octave(input_dir, output_file, time_step, min_f0, max_f0, octave_cost, keyword)

        except:
            print("Something is wrong with %s-%s" % (task, keyword))
            error = "%s-%s" % (task, keyword)

            with open(
                    "C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/Data/Praat_Data/refined_KM/!error_log.txt",
                    'a') as f:
                f.write("\n")
                f.write(error)
            pass

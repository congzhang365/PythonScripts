import parselmouth
import glob
import os.path


def wav_duration(in_path, out_path):
    filenames = []
    for wav in glob.glob(in_path + "*.wav"):
        f_wav = wav.split("/")[-1]
        f_wav = f_wav.split("\\")[-1]
        f_wav = f_wav.split(".")[0]
        filenames.append(f_wav)

    files = glob.glob(in_path + "*.wav")
    for file_count in range(len(files)):
        snd = parselmouth.Sound(files[file_count])
        dur = snd.get_total_duration()
        log_name = out_path + '%s.log' % filenames[file_count]
        if os.path.isfile(log_name):
            with open(log_name, 'a', encoding='utf-8') as f:
                f.write('实际音频时长为(秒): \n%s\n' % dur)
        else:
            print("Log does not exist.")


def dur_diff(in_path, out_path, log_style='merged_log'):
    filenames = []
    for log in glob.glob(in_path + "*.log"):
        f_log = log.split("/")[-1]
        f_log = f_log.split("\\")[-1]
        f_log = f_log.split(".")[0]
        filenames.append(f_log)

    if log_style == 'merged_log':
        files = glob.glob(out_path + "*.log")
        log_lines = []
        log_header = 'filename, ssml计算时间(s), wav真实时间(s), wav-ssml时间差(s)' + '\n'
        log_lines.append(log_header)

        for file_count in range(len(files)):
            log_name = out_path + '%s.log' % filenames[file_count]
            line_set = []
            if not os.path.isfile(log_name):
                print('Cannot find log file.')
            else:
                with open(log_name, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    # print(lines)
                    ssml_dur = lines[1].strip('\n')
                    # print(ssml_dur)
                    wav_dur = lines[3].strip('\n')
                    # print(wav_dur)
                    diff = float(ssml_dur) - float(wav_dur)
                    line = str(filenames[file_count]) + ',' + str(ssml_dur) + ',' + str(wav_dur) + ',' + str(
                        diff) + '\n'
                    line_set.append(line)
                    log_body = ','.join(line_set)
                    log_lines.append(log_body)
            with open('%s/diff_log.csv' % out_path, 'w', encoding='utf-8') as f:
                f.write(''.join(log_lines))

    elif log_style == 'separate_logs':
        files = glob.glob(out_path + "*.log")
        for file_count in range(len(files)):
            log_name = out_path + '%s.log' % filenames[file_count]
            if os.path.isfile(log_name):
                with open(log_name, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    # print(lines)
                    ssml_dur = lines[1].strip('\n')
                    # print(ssml_dur)
                    wav_dur = lines[3].strip('\n')
                    # print(wav_dur)
                    diff = float(ssml_dur) - float(wav_dur)
                with open(log_name, 'a', encoding='utf-8') as f:
                    f.write('The difference is (seconds):\n%s' % diff)
            else:
                print('Cannot find log file.')
    else:
        print('What style do you want your log to be? Start again.')


if __name__ == '__main__':
    in_path = "D:\Rokid\Projects\Songs/tool\Tool Testing\midi2ssml_scripts/"
    out_path = "D:\Rokid\Projects\Songs/tool\Tool Testing\midi2ssml_scripts/"

    wav_duration(in_path, out_path)
    dur_diff(in_path, out_path, 'merged_log')

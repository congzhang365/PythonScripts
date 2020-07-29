import os
import parselmouth



def wav_duration(in_path):
    for filename in os.listdir(in_path):
        print(filename)
        if filename.endswith('.wav'):
            file = in_path + '\\' + filename
            snd = parselmouth.Sound(file)
            dur = snd.get_total_duration()
        print('The length of the %s is: %s seconds\n' % (filename, dur))
    return dur


def wav_duration_subdir(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
            for dirname in dirs:
                # print(dirs)
                folder = os.path.join(root, dirname)
                dir = folder + '/'
                # print(dir)

                if os.path.isdir(dir):
                    for rs, ds, fs in os.walk(dir):
                        break

                    for file in fs:
                        # print(fs)
                        files_durs = []
                        if file.endswith('.wav'):
                            full_path = dir + file
                            snd = parselmouth.Sound(full_path)
                            dur_sec = snd.get_total_duration()
                            dur_min = dur_sec/60
                            file_dur = file + '\t' + str(dur_sec) + '\n'
                            files_durs.append(file_dur)
                            # print('The length of the %s is: %s minutes' % (file, dur_min))
                        # print(files_durs)
                        log_name = output_dir + 'duration.txt'
                        with open(log_name, 'a', encoding='utf-8') as f:
                            f.write('%s' % ''.join(files_durs))



if __name__=='__main__':
    in_path = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/"
    out_path = "C:/Users/sprin/Desktop/test/"
    wav_duration_subdir(in_path, out_path)
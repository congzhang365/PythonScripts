import parselmouth
from parselmouth.praat import call
import os


def check_channel_num(input_dir):
    if os.path.isdir(input_dir):
        for root, dirs, files in os.walk(input_dir):
            break

        for file in files:
            if file.endswith('.wav'):
                snd = parselmouth.Sound(input_dir + file)
                channel_num = call(snd, "Get number of channels")
                print('%s\'s channel_num is %s!'%(file, channel_num))


def reduce_channel(input_dir, output_dir, channel='mono'):
    if os.path.isdir(input_dir):

        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith('.wav'):
                snd = parselmouth.Sound(input_dir + file)
                if channel is 'mono':
                    channel_num = call(snd, "Get number of channels")
                    if not channel_num == 1:
                        new = call(snd, "Convert to mono")
                        print('%s has been converted!'%file)
                        if os.path.isdir(output_dir):
                            new.save("%s%s"%(output_dir,file), "WAV")
                        else:
                            os.makedirs(os.path.dirname(output_dir))
                            new.save("%s%s" % (output_dir, file), "WAV")
                    else:
                        print('%s has 1 channel!'%file)
                else:
                    print("Do you want to convert your sound to mono?")



def resample(input_dir, output_dir, out_rate=8000):
    if os.path.isdir(input_dir):
        # print(input_dir)

        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith('.wav'):
                snd = parselmouth.Sound(input_dir + file)
                # dur = snd.get_total_duration()
                resampled = call(snd, "Resample...", out_rate, 50)
                # print(pitch_tier)
                if os.path.isdir(output_dir):
                    resampled.save("%s%s"%(output_dir,file), "WAV")
                else:
                    os.makedirs(os.path.dirname(output_dir))
                    resampled.save("%s%s" % (output_dir, file), "WAV")


if __name__ == "__main__":
    path_in = "C:/Users/audio/" #  add an asterisk for looping through subdir
    path_out = "C:/Users/audio/"

    # check the number of channels
    check_channel_num(path_in)
    # reduce to mono
    reduce_channel(path_in, path_out)
    # resample audio
    resample(path_in, path_out, out_rate=8000)

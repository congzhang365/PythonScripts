import parselmouth
from parselmouth.praat import call
import os


def reduce_channel(input_dir, output_dir, channel='mono'):
    if os.path.isdir(input_dir):
        # print(input_dir)

        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith('.wav'):
                snd = parselmouth.Sound(input_dir + file)
                if channel is 'mono':
                    new = call(snd, "Convert to mono")
                else:
                    print("Do you want to convert your sound to mono?")
                if os.path.isdir(output_dir):
                    new.save("%s%s"%(output_dir,file), "WAV")
                else:
                    os.makedirs(os.path.dirname(output_dir))
                    new.save("%s%s" % (output_dir, file), "WAV")


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
    path_in = "C:\cygwinfolders\cppfa\wav8k/" #  add asterisks is for looping through subdir
    path_out = "D:\Rokid\Projects\Songs/annotation\LH\wav8k/"
    reduce_channel(path_in,path_in)
    # resample(path_in, path_out, out_rate=8000)



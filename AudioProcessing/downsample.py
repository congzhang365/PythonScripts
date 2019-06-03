import parselmouth
from parselmouth.praat import call
import os


def resampling(input_dir, output_dir, out_rate=8000):
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
    path_in = "D:\Rokid\Projects\Songs/annotation\LH\wav24k/" #  add asterisks is for looping through subdir
    path_out = "D:\Rokid\Projects\Songs/annotation\LH\wav8k/"
    resampling(path_in, path_out, out_rate=8000)

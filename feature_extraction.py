import parselmouth
from parselmouth.praat import call
import glob
import pandas as pd

dir = ("./training_data/")

filenames = []
for wav in glob.glob(dir + "*.wav"):
    f_wav = wav.split("/")[-1]
    f_wav = f_wav.split("\\")[-1]
    f_wav = f_wav.split(".")[0]
    filenames.append(f_wav)
print(filenames)

files = glob.glob(dir + "*.wav")
for file_count in range(len(files)):
    snd = parselmouth.Sound(files[file_count])
    dur = snd.get_total_duration()
    manipulation = call(snd, "To Manipulation", 0.01, 75, 600)
    pitch_tier = call(manipulation, "Extract pitch tier")
    call(pitch_tier, "Write to headerless spreadsheet file", "raw.txt")

df = pd.read_csv('raw.txt', sep='\t', header=None)
a = round(df.iloc[:, 0], 2)
df.update(a)
# print(df)

df.to_csv('raw123.txt', index=False, header=False, sep='\t')
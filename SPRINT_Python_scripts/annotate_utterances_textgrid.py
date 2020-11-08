import parselmouth
import glob
import os.path


def textgrid_header(audio_duration, total_interval = 3, total_tier = 1):
    file_type = 'File type = \"ooTextFile\"'
    object_class = 'Object class = \"TextGrid\"'
    audio_begin = str(0)
    audio_end = str(audio_duration)
    exist = '<exists>'
    total_tiers = str(total_tier)
    tier_type = '\"IntervalTier\"'
    tier_num = '\"1\"'
    interval_num = str(total_interval)

    header_text = '\n'.join([file_type, object_class,audio_begin, audio_end,
                   exist,total_tiers,tier_type,tier_num,audio_begin,audio_end,
                   interval_num])
    # print(header_text)
    return header_text


def textgrid_body(dur, transcription):
    # create 3 intervals. The second interval contains the transcription text.
    interval_1 = '0' + '\n' + '0.1'+ '\n' + '""' + '\n'
    interval_2 = '0.1' + '\n' + '%s' % (dur - 0.1) + '\n' + '\"%s\"' % (transcription) + '\n'
    interval_3 = '%s' % (dur - 0.1) + '\n' + '%s' % (dur)+ '\n' + '""' + '\n'

    textgrid_body = [interval_1, interval_2, interval_3]

    body_text = ''.join(textgrid_body)
    # print(body_text)
    return body_text


def create_textgrid(wav_dir, txt_dir, tg_dir):
    files = glob.glob(wav_dir + "*.wav")

    for file_count in range(len(files)):
        filename = os.path.basename(files[file_count])
        snd = parselmouth.Sound(files[file_count])
        dur = snd.get_total_duration()

        with open(txt_dir + filename[:-3] + 'txt', "r", encoding='utf-8') as f:
            transcription = f.read()
        tg = textgrid_header(dur) + '\n' + textgrid_body(dur,transcription)
        with open(tg_dir + filename[:-3] + 'TextGrid', 'w', encoding='utf-8') as f:
            f.write(tg)



if __name__=='__main__':
    wav_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/Greek/Athens/DIAL/individual wavs/wav/"
    txt_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/Greek/Athens/DIAL/individual wavs/txt/"
    tg_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/Greek/Athens/DIAL/individual wavs/textgrid/"
    create_textgrid(wav_dir, txt_dir, tg_dir)


'''
This script creates textgrids for the SRPINT Greek data on the utterance level
Only 1 tier consisting 3 intervals is created. The boundaries are 0.1s and total wav duration - 0.1s.
The participant lines are put down in the 2nd interval.
    To run this file, you need to install
        praat-parselmouth  
Three directories need to be provided:
    - wav dir: where your wav files are
    - txt dir: where your txt transcription files are
    - tg dir: where you would like to save your textgrids

Dr Cong Zhang 06/11/2020 @SPRINT
Last commit: 06/11/2020 
'''

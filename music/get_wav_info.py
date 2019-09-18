import os
import soundfile as sf

# for a single wave file
def wav_info(input_wav):
    ob = sf.SoundFile(input_wav)
    sample_rate = ob.samplerate
    print('Sample rate: %s'% sample_rate)
    channel_num = ob.channels
    print('Channels: %s'% channel_num)
    bit_rate = ob.subtype[4:]
    print('Bit rate: %s'% bit_rate)
    return sample_rate, channel_num, bit_rate


# loop through a folder
def get_info(input_dir, output_dir):
    if os.path.isdir(input_dir):
        # print(input_dir)
        results = []
        header = 'filename\tsample_rate\tchannel_num\tbit_rate\n'
        results.append(header)
        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith('.wav'):
                print(file)
                ob = sf.SoundFile('%s%s' % (input_dir,file))
                sample_rate = ob.samplerate
                print('Sample rate: %s' % sample_rate)
                channel_num = ob.channels
                print('Channels: %s' % channel_num)
                bit_rate = ob.subtype[4:]
                print('Bit rate: %s' % bit_rate)
                result_line = '%s\t%s\t%s\t%s\n'%(file, sample_rate, channel_num, bit_rate)
                results.append(result_line)
            else:
                print('!!!!!!!!!! Attention! %s is not a wav file!!!!!!!!'%file)
        info = ''.join(results)

        with open('%swav_info.txt'%output_dir, 'w', encoding='utf-8') as f:
            f.write(info)

    else:
        print('path does not exist!')

if __name__ == "__main__":
    input_dir = "C:\Rokid\Projects\Songs\luo_data\Bopop Studio 人声50首（第二批）/voc50/" #  add asterisks is for looping through subdir
    output_dir = "C:\Rokid\Projects\Songs\luo_data\Bopop Studio 人声50首（第二批）/voc50/"

    get_info(input_dir,output_dir)
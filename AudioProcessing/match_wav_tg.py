import os


# check whether every wave file has a corresponding textgrid file

def wav_tg(wav_dir, tg_dir):
    wav_names = []
    for root, dirs, files in os.walk(wav_dir):
        # print(files)
        for file in files:
            if file.endswith('.wav'):
                wav_names.append(file[:-4])
    # print(wav_names)

    tgfile_list = []
    for wav in wav_names:
        tg_name = wav + ".TextGrid"
        # print(tg_name)
        tgfile_list.append(tg_name)
    # print('the textgrid file list is: ', tgfile_list)

    existing_tgs = []
    for root, dirs, files in os.walk(tg_dir):
        # print(files)
        for file in files:
            if file.endswith('.TextGrid'):
                existing_tgs.append(file)
    # print('the textgrid files are: ', existing_tgs)


    no_file = [item for item in tgfile_list if item not in existing_tgs]
    if not no_file == []:
        print("These %i files do not exist: " %len(no_file), no_file)

if __name__ == '__main__':
    wav_dir = "D:\Rokid\pycharm\music/"
    tgdir = "D:\Rokid\pycharm\music/"
    result = wav_tg(wav_dir, tgdir)
    # with open('result.txt', 'w', encoding='utf-8') as f:
    #     f.write(result)
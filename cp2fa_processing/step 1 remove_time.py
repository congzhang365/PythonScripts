import os


def get_lyrics(lyrics_file,output_dir, output_prefix, output_suffix):
    with open(lyrics_file,'r', encoding='utf-8') as f:
        lyrics_lines = f.read().split('\n')
        for i in range(len(lyrics_lines)):
            if len(str(i)) == 1:
                with open('%s%s0000%d%s.txt'%(output_dir, output_prefix,i+1,output_suffix), 'w', encoding='utf-8') as f:
                    f.write(lyrics_lines[i])
            elif len(str(i)) == 2:
                with open('%s%s000%d%s.txt'%(output_dir, output_prefix,i+1,output_suffix), 'w', encoding='utf-8') as f:
                    f.write(lyrics_lines[i])
            elif len(str(i)) == 3:
                with open('%s%s00%d%s.txt'%(output_dir, output_prefix,i+1,output_suffix), 'w', encoding='utf-8') as f:
                    f.write(lyrics_lines[i])
            else:
                print('how many lines do you have?')


def is_chinese(uni_ch):
    """判断一个 unicode 是否是汉字。"""
    if uni_ch >= u'\u4e00' and uni_ch <= u'\u9fa5':
        return True
    else:
        return False


def isdigit(uni_ch):
    """判断一个 unicode 是否是十进制数字。"""
    if uni_ch >= u'\u0030' and uni_ch <= u'\u0039':
        return True
    else:
        return False


def remove_time_single_line(input_dir, output_dir, sub_dir = True):
    if sub_dir:
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
                        if file.endswith('.txt'):
                            txt = dir + file
                            # print(txt)
                            with open(txt, 'r', encoding='utf-8') as f:
                                text = f.read()
                                segs = text.split('\t')
                                print(segs)
                                no_time = segs[2:]
                                print(no_time)
                                new_text = ''.join(no_time)

                            with open('%s%s' % (output_dir, file), 'w', encoding='utf-8') as f:
                                f.write(new_text)
                                print(' all done for %s' % file)
    elif sub_dir is False:
        dir = input_dir
        if os.path.isdir(dir):
            print(dir)
            for root, dirs, files in os.walk(dir):
                break

            for file in files:
                if file.endswith('.txt'):
                    txt = dir + file
                    # print(txt)
                    with open(txt, 'r', encoding='utf-8') as f:
                        text = f.read()
                        segs = text.split('\t')
                        print(segs)
                        no_time = segs[2:]
                        print(no_time)
                        new_text = ''.join(no_time)

                    with open('%s%s' % (output_dir, file), 'w', encoding='utf-8') as f:
                        f.write(new_text)
                        print(' all done for %s' % file)
    else:
        print('something is wrong')



def remove_time_file(input_dir, output_dir):
    dir = input_dir
    if os.path.isdir(dir):
        print(dir)
        for root, dirs, files in os.walk(dir):
            break

        for file in files:
            if file.endswith('.txt'):
                txt = dir + file
                # print(txt)
                with open(txt, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    no_time = []
                    for line in lines:
                        segs = line.split('\t')
                        all_seg = ''.join(segs[2:])
                        no_time.append(all_seg)
                    print(no_time)
                    new_text = ''.join(no_time)

                with open('%s%s' % (output_dir, file), 'w', encoding='utf-8') as f:
                    f.write(new_text)
                    print(' all done for %s' % file)



if __name__ == '__main__':
    # step 1:
    # save as different lyrics files

    # input = 'C:\Rokid\pycharm\music/align_lyrics/abc/'
    output = 'C:\Rokid\pycharm\music/align_lyrics/abc/removed/'

    if not os.path.exists(output):
        os.makedirs(output)
    #
    #     remove_time_single_line(input,output)
    #

    input= "C:/Users\Cong\Documents\BaiduYunDownload\Textgrid/"
    remove_time_file(input,output)
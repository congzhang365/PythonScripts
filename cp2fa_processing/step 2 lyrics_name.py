import os


def get_lyrics(lyrics_file,output_dir, output_prefix, output_suffix):
    with open(lyrics_file,'r', encoding='utf-8') as f:
        lyrics_lines = f.read().split('\n')
        for i in range(len(lyrics_lines)):
            if len(str(i+1)) == 1:
                with open('%s%s0000%d%s.txt'%(output_dir, output_prefix,i+1,output_suffix), 'w', encoding='utf-8') as f:
                    f.write(lyrics_lines[i])
            elif len(str(i+1)) == 2:
                with open('%s%s000%d%s.txt'%(output_dir, output_prefix,i+1,output_suffix), 'w', encoding='utf-8') as f:
                    f.write(lyrics_lines[i])
            elif len(str(i+1)) == 3:
                with open('%s%s00%d%s.txt'%(output_dir, output_prefix,i+1,output_suffix), 'w', encoding='utf-8') as f:
                    f.write(lyrics_lines[i])
            else:
                print('how many lines do you have?')


if __name__ == '__main__':
    # step 1:
    # save as different lyrics files
    set = ['BJ','DN','FQ','GB','GG','JZ','LB','LL','PM','PY','SN','TH','WD','WM','WW','XH','YC','YH','YL','YZ']
    for item in set:
        dir = 'C:/Users\Cong\Desktop\ViaX\Xinrong Wang\S4\lyrics/'
        if not os.path.exists(dir):
            os.makedirs(dir)
        get_lyrics('C:/Users\Cong\Desktop\ViaX\Xinrong Wang\S4\lyrics/%s.txt'%item, dir, '%s_'%item,'')














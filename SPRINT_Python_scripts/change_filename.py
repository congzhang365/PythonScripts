'''
This script is for replacing part of the file name (replace_filename) or add prefix and/or suffix (add_suffix_prefix)
    input_dir: input folder. It is also the output folder
    file_ext: the file extension you'd like to process. For instance, '.txt', '.wav', '.TextGrid'
    old_name: this is the part you'd like to replace
    new_name: this is the part you'd like to replace the old part with
    
    prefix: a string added to the start of the filenames. Leave as '' if not needed.
    suffix: a string added to the end of the filenames. Leave as '' if not needed. 

Dr Cong Zhang 17/07/2020 @SPRINT 
'''



import glob
import os

def replace_filename(input_dir, file_ext, old_name, new_name):
    for f in glob.glob('%s/*%s' % (input_dir, file_ext)):
        new_filename = f.replace("%s" % old_name, "%s" % new_name)
        os.rename(f, new_filename)


def add_suffix_prefix(input_dir, file_ext, prefix, suffix):
    for f in glob.glob('%s/*%s' % (input_dir, file_ext)):
        base_name = os.path.basename(f)
        base_name = "%s/%s" % (input_dir, prefix) + base_name + "%s" % suffix
        os.rename(f, base_name)




if __name__ == '__main__':
    input_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/DIAL/LP09/"
    file_ext = '.wav'
    old_name = 'DIAL_LP09_'
    new_name = ''
    prefix = 'DIAL_LP09_'
    suffix = ''
    # replace_filename(input_dir, file_ext, old_name, new_name)
    add_suffix_prefix(input_dir, file_ext, prefix, suffix)

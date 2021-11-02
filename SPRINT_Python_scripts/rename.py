import os

def remove_string_at_index(filename, index):
   print('*** Remove character at specific index ***')
   # Slice string to remove character at index
   if len(filename) > index:
       filename = filename[0 : index : ] + filename[index + 1 : :]
   print('Modified String : ', filename)
   print('*** Remove first character ***')


def remove_string_between(filename, start, stop):
    print('*** Remove multiple characters at index range***')
    # Remove charactes from index start to stop
    if len(filename) > stop :
       filename = filename[0: start:] + filename[stop + 1::]
    print('Modified String : ', filename)
    return filename

def remove_first_n_characters(filename, n):
   print('*** Remove first n character(s) ***')
   # Slice string to remove first n character
   filename = filename[n : : ]
   print('Modified String : ' , filename)


def remove_last_n_characters(filename, n):
   print('*** Remove Last n character(s) ***')
   # Slice string to remove last character
   filename = filename[:-n:]
   print('Modified String : ', filename)


def get_filename_extension(input_dir):
    for f in os.listdir(input_dir):
        filename = f.split('.')[0]
        extension = f.split('.')[1]
        return filename, extension


def replace_file_extension(input_dir, output_dir, old_extension, new_extension):
    for f in os.listdir(input_dir):
        old = os.path.join(input_dir, f)
        new = old.replace(old_extension, new_extension)
        os.rename(os.path.join(input_dir, old), os.path.join(output_dir, new))


def add_suffix(input_dir, output_dir, suffix, extension):
    for f in os.listdir(input_dir):
        if f.endswith(extension):
            filename = f.split('.')[0]
            os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s%s%s' % (filename, suffix, extension)))


def add_prefix(input_dir, output_dir, prefix):
    for f in os.listdir(input_dir):
        os.rename(os.path.join(input_dir, f), os.path.join(output_dir, "{}{}".format(prefix, f)))


if __name__ == '__main__':

    input_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/DIAL/annotations/maus/ipa/renamed"
    output_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/DIAL/annotations/maus/ipa/renamed"

    for f in os.listdir(input_dir):
        if f.endswith((".TextGrid", ".wav")): # put all the file extensions you'd like to change in the tuple
            filename = f.split('.')[0]
            extension = f.split('.')[1]
            # 1-word utterance, broad focus: W1_FB0
            W1_FB0 = ["004", "008", "020", "024", # names
                      "012", "016", "028", "032"] # places
            if any(x in filename for x in W1_FB0):
                new_name = filename + "_W1_FB0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + "." + extension
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 2-word utterance, broad focus: W2_FB0
            W2_FB0 = ["001", "002", "003", "005", "006", "007", # names
                      "017", "018", "019", "021", "022", "023", # names
                      "009", "010", "011", "013", "014", "015", # places
                      "025", "026", "027", "029", "030", "031"] # places
            if any(x in filename for x in W2_FB0):
                new_name = filename + "_W2_FB0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + "." + extension
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 1-word utterance, narrow focus: W1_FN0
            W1_FN0 = ["033", "035", "036", "037", # names
                      "040", "042", "043", "044"] # places
            if any(x in filename for x in W1_FN0):
                new_name = filename + "_W1_FN0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + "." + extension
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 2-word utterance, narrow focus: W2_FN1
            W2_FN1 = ["038", # name
                      "045"] # place
            if any(x in filename for x in W2_FN1):
                new_name = filename + "_W2_FN1"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + "." + extension
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))

            # 2-word utterance, narrow focus: W2_FB2
            W2_FN2 = ["034", "039", # names
                      "041", "046"] # places
            if any(x in filename for x in W2_FN2):
                new_name = filename + "_W2_FN2"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + "." + extension
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))



'''
This script has functions for renaming files.

Dr Cong Zhang 30/11/2020 @SPRINT
Last commit: 09/12/2020 
'''

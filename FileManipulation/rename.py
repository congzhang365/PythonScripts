import os


def remove_string_at_index(filename, index):
    print('*** Remove character at specific index ***')
    # Slice string to remove character at index
    if len(filename) > index:
        filename = filename[0: index:] + filename[index + 1::]
    print('Modified String : ', filename)
    print('*** Remove first character ***')


def remove_string_between(filename, start, stop):
    print('*** Remove multiple characters at index range***')
    # Remove charactes from index start to stop
    if len(filename) > stop:
        filename = filename[0: start:] + filename[stop + 1::]
    print('Modified String : ', filename)
    return filename


def remove_first_n_characters(filename, n):
    print('*** Remove first n character(s) ***')
    # Slice string to remove first n character
    filename = filename[n::]
    print('Modified String : ', filename)


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


def copy_files(input_dir, output_dir, file_type):
    import shutil

    if os.path.isdir(input_dir):

        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith(file_type):
                shutil.copy2(input_dir + file, output_dir)  # complete target filename given


def move_files(input_dir, output_dir, file_type):

    if os.path.isdir(input_dir):

        for root, dirs, files in os.walk(input_dir):
            break
        for file in files:
            if file.endswith(file_type):
                os.rename(os.path.join(input_dir, file), os.path.join(output_dir, file))


if __name__ == '__main__':

    input_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/DIAL/PaPE/W2_FB0 W2_FN2/miss or uptalk/"
    output_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/DIAL/PaPE/W2_FB0 W2_FN2/miss or uptalk/"

    for f in os.listdir(input_dir):
        if f.endswith(".TextGrid"):
            filename = f.split('.')[0]
            extension = f.split('.')[1]
            # 1-word utterance, broad focus: W1_FB0
            W1_FB0 = ["005", "008", "020", "024"]
            if any(x in filename for x in W1_FB0):
                new_name = filename[:-3] + "_W1_FB0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".TextGrid"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 2-word utterance, broad focus: W2_FB0
            W2_FB0 = ["001", "002", "003", "004", "006", "007", "017", "018", "019", "021", "022", "023"]
            if any(x in filename for x in W2_FB0):
                new_name = filename[:-3] + "_W2_FB0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".TextGrid"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 1-word utterance, narrow focus: W1_FN0
            W1_FN0 = ["033", "035", "036", "037"]
            if any(x in filename for x in W1_FN0):
                new_name = filename[:-3] + "_W1_FN0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".TextGrid"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 2-word utterance, narrow focus: W2_FN1
            W2_FN1 = ["038"]
            if any(x in filename for x in W2_FN1):
                new_name = filename[:-3] + "_W2_FN1"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".TextGrid"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))

            # 2-word utterance, narrow focus: W2_FB2
            W2_FN2 = ["034", "039"]
            if any(x in filename for x in W2_FN2):
                new_name = filename[:-3] + "_W2_FN2"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".TextGrid"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))

    for f in os.listdir(input_dir):
        if f.endswith(".wav"):
            filename = f.split('.')[0]
            extension = f.split('.')[1]
            # 1-word utterance, broad focus: W1_FB0
            W1_FB0 = ["005", "008", "020", "024"]
            if any(x in filename for x in W1_FB0):
                new_name = filename[:-3] + "_W1_FB0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".wav"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 2-word utterance, broad focus: W2_FB0
            W2_FB0 = ["001", "002", "003", "004", "006", "007", "017", "018", "019", "021", "022", "023"]
            if any(x in filename for x in W2_FB0):
                new_name = filename[:-3] + "_W2_FB0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".wav"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 1-word utterance, narrow focus: W1_FN0
            W1_FN0 = ["033", "035", "036", "037"]
            if any(x in filename for x in W1_FN0):
                new_name = filename[:-3] + "_W1_FN0"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".wav"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))
            # 2-word utterance, narrow focus: W2_FN1
            W2_FN1 = ["038"]
            if any(x in filename for x in W2_FN1):
                new_name = filename[:-3] + "_W2_FN1"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".wav"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))

            # 2-word utterance, narrow focus: W2_FB2
            W2_FN2 = ["034", "039"]
            if any(x in filename for x in W2_FN2):
                new_name = filename[:-3] + "_W2_FN2"
                # remove the characters between 11 and 13 (count from 0): DIAL_LP02_DIAL006_W2_FB0 -> DIAL_LP02_D006_W2_FB0
                output_name = remove_string_between(new_name, 11, 13) + ".wav"
                os.rename(os.path.join(input_dir, f), os.path.join(output_dir, '%s' % (output_name)))

'''
This script has functions for renaming files.

Dr Cong Zhang 30/11/2020 @SPRINT
Last commit: 30/11/2020 
'''

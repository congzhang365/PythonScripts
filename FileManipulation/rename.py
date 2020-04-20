import os


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


    input_dir = "C:/Users/test/"
    output_dir = "C:/Users/test/"


    # example of replacing file extension: e.g. abc.txt -> abc.TextGrid
    old_extension = '.txt'
    new_extension = '.TextGrid'
    replace_file_extension(input_dir, output_dir, old_extension, new_extension)


    # example of adding prefix: e.g. abc.txt -> new_abc.txt
    prefix = 'new_'
    add_prefix(input_dir, output_dir, prefix)


    # example of replacing adding suffix to filename e.g. abc.txt -> abc_new.txt
    suffix = '_new'
    extension = '.txt'
    add_suffix(input_dir, output_dir, suffix, extension)

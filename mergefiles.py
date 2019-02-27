import os


def merge_files(input_folder, output_file, print_info, remove_file=1):
    for a, b, files in os.walk(input_folder):
        all_lines = []
        if remove_file:
            files.remove(file_to_remove)    # remove the first file. delete line if not needed.
        for file in files:
            with open(input_folder + file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if print_info:
                    lines.insert(0, '>>>from the file\'%s\'<<<\n' % file[:-4])
                print('This file %s has' % file, len(lines), 'lines.')
                all_lines.append(''.join(lines))
        print('The final file contains', len(all_lines), 'files.')
    with open('%s.txt' % output_file, 'w', encoding='utf-8') as final_file:
        final_file.write(''.join(all_lines))


if __name__ == "__main__":
    file_to_remove = 'mixed_out.txt'
    folder = 'D:\Rokid\pycharm/test_set/12/'
    merge_files(folder, 'polyphone_merged', 1)

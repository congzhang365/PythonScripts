import os
import re


def merge_files(input_folder, output_file, print_info, remove_file=0):
    for a, b, files in os.walk(input_folder):
        all_lines = []
        if remove_file:
            files.remove(file_to_remove)  # remove the first file. delete line if not needed.
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


def find_all(input_file, target, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        output_lines = []
        for line in lines:
            if target in line:
                output_lines.append(line)
    with open('%s.txt' % output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(output_lines))


def delete_lines(input_file, target_file, output_file):
    with open(target_file, 'r', encoding='utf-8') as t:
        target_list = t.readlines()
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            if not line in target_list:
                new_lines.append(line)
    with open('%s.txt' % output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(new_lines))


if __name__ == "__main__":
    # # file_to_remove = 'mixed_out.txt'
    # # folder = 'D:\Rokid\pycharm/test_set/12/'
    # # merge_files(folder, 'polyphone_merged', 1)
    #
    # folder = 'D:\Rokid\Projects\Test\多音字测试集合/'
    # merge_files(folder, 'polyphone_merged', 0)
    target1 = '【'
    find_all('D:\Rokid\pycharm/test_set\polyphone_merged.txt', target1, 'left_quote')
    delete_lines('D:\Rokid\pycharm/test_set\polyphone_merged.txt', 'D:\Rokid\pycharm/test_set\left_quote.txt', 'sans_left')

    # target2 = '】'
    # find_all('D:\Rokid\pycharm/test_set/sans_left.txt', target2, 'right_quote')
    # delete_lines('D:\Rokid\pycharm/test_set/sans_left.txt', 'D:\Rokid\pycharm/test_set/right_quote.txt', 'sans_lr')
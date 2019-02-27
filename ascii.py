import os
import zipfile


def extract_lines(file, start_num, end_num, output_file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = []
        for i in range(start_num - 1, end_num):
            new_line = lines[i].split('\t')
            if not all(ord(c) < 255 for c in new_line[1]):
                print(new_line[1])
            new_line = '\t'.join(new_line)
            new_lines.append(new_line)
        # new_lines.
    with open('D:\Rokid\Projects\Test\Microsoft\标贝公开数据集\%s.txt' % output_file, 'w', encoding='utf-8-sig') as file:
        file.write(''.join(new_lines)[:-1])


def compress_files(input_folder, output_folder, start_num, end_num, output_file):
    files_to_compress = []
    for num in range(start_num, end_num+1):
        file_to_compress = '00' + str(num) + '.wav'
        files_to_compress.append(file_to_compress)

    final_zip = zipfile.ZipFile(output_folder + output_file, "w", zipfile.ZIP_DEFLATED)
    for folder, subfolders, files in os.walk(input_folder):
        for file in files_to_compress:
            final_zip.write(os.path.join(folder, file), file)
    final_zip.close()


## extract lines
# no_punc = 'D:\Rokid\Projects\Test\Microsoft\标贝公开数据集/new.txt'
# extract_lines(no_punc, 2501, 3000, '3000')
# extract_lines(no_punc, 3001, 3500, '3500')
# extract_lines(no_punc, 3501, 4000, '4000')
# extract_lines(no_punc, 4001, 4500, '4500')
# extract_lines(no_punc, 4501, 5000, '5000')
# extract_lines(no_punc, 5001, 5500, '5500')
# extract_lines(no_punc, 5501, 6000, '6000')
# extract_lines(no_punc, 6001, 6500, '6500')
# extract_lines(no_punc, 6501, 7000, '7000')
# extract_lines(no_punc, 7001, 7500, '7500')
# extract_lines(no_punc, 7501, 8000, '8000')
# extract_lines(no_punc, 8001, 8500, '8500')
# extract_lines(no_punc, 8501, 9000, '9000')
# extract_lines(no_punc, 9001, 9500, '9500')
# extract_lines(no_punc, 9501, 10000, '10000')

## compress files
save_to = 'D:\Rokid\Projects\Test\Microsoft\标贝公开数据集/'
files_from = 'D:\Rokid\Projects\Test\Microsoft\标贝公开数据集/Wave/'
# compress_files(files_from, save_to, 4001, 4500, '4500.zip')
# compress_files(files_from, save_to, 4501, 5000, '5000.zip')
# compress_files(files_from, save_to, 5001, 5500, '5500.zip')
# compress_files(files_from, save_to, 5501, 6000, '6000.zip')
# compress_files(files_from, save_to, 6001, 6500, '6500.zip')
# compress_files(files_from, save_to, 6501, 7000, '7000.zip')
# compress_files(files_from, save_to, 7001, 7500, '7500.zip')
# compress_files(files_from, save_to, 7501, 8000, '8000.zip')
compress_files(files_from, save_to, 8001, 8500, '8500.zip')
compress_files(files_from, save_to, 8501, 9000, '9000.zip')
compress_files(files_from, save_to, 9001, 9500, '9500.zip')
compress_files(files_from, save_to, 9501, 10000, '10000.zip')
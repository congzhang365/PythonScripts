#! /usr/bin/python
# -*- coding: UTF-8 -*-
# author: robot527
# created at 2016-05-30
# https://github.com/robot527/add-spaces/blob/master/add_spaces.py

"""
自动给中文英文之间加入合理的空格
"""
import os

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

def isalpha(uni_ch):
    """判断一个 unicode 是否是字母。"""
    if (uni_ch >= u'\u0041' and uni_ch <= u'\u005a') \
        or (uni_ch >= u'\u0061' and uni_ch <= u'\u007a'):
        return True
    else:
        return False


def is_en_symbol(uni_ch):
    """判断一个 unicode 是否是英文符号。"""
    if uni_ch in [u':', u';', u'%', u'!', u'?', u'`', u'°', u'*', u'_',\
            u'<', u'=', u'>', u'"', u'$', u'&', u'\'', u',', u'.', u'~',\
            u'/', u'@', u'\\', u'^', u'|']:
        return True
    else:
        return False


def is_en_l_bracket(uni_ch):
    """判断一个 unicode 是否是英文左括号。"""
    if uni_ch == u'(' or uni_ch == u'[':
        return True
    else:
        return False


def is_en_r_bracket(uni_ch):
    """判断一个 unicode 是否是英文右括号。"""
    if uni_ch == u')' or uni_ch == u']':
        return True
    else:
        return False


def is_zh_l_bracket(uni_ch):
    """判断一个 unicode 是否是中文左括号。"""
    if uni_ch == u'\uff08':
        return True
    else:
        return False


def is_zh_r_bracket(uni_ch):
    """判断一个 unicode 是否是中文右括号。"""
    if uni_ch == u'\uff09':
        return True
    else:
        return False


def add_spaces_to_string(string, code):
    """给字符串添加合理的空格。"""
    from re import sub
    newustr = ""
    flag = 0
    ustr = string.decode(code)
    ch_lst = list(ustr)
    length = len(ch_lst)
    for i in range(0, length):
        if i < length - 1:
            #中文(括号)与英文(括号)之间需要增加空格
            if (is_chinese(ch_lst[i]) and isalpha(ch_lst[i + 1])) \
                or (isalpha(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
            elif (isalpha(ch_lst[i]) and is_zh_l_bracket(ch_lst[i + 1])) \
                or (is_zh_r_bracket(ch_lst[i]) and isalpha(ch_lst[i + 1])):
                ch_lst[i] += u" "
            elif (is_chinese(ch_lst[i]) and is_en_l_bracket(ch_lst[i + 1])) \
                or (is_en_r_bracket(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
            #中文与英文符号之间需要增加空格
            elif (is_chinese(ch_lst[i]) and is_en_symbol(ch_lst[i + 1])) \
                or (is_en_symbol(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
                flag = 1
            #中文(括号)与数字之间需要增加空格
            elif (is_chinese(ch_lst[i]) and isdigit(ch_lst[i + 1]))\
                or (isdigit(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
            elif (isdigit(ch_lst[i]) and is_zh_l_bracket(ch_lst[i + 1]))\
                or (is_zh_r_bracket(ch_lst[i]) and isdigit(ch_lst[i + 1])):
                ch_lst[i] += u" "

        newustr += ch_lst[i]
    newstring = newustr.encode(code)
    if flag == 1:
        #处理中文里的粗体字和斜体字
        newstring = sub(r' \* ', '*', newstring)
        newstring = sub(r' \*\* ', '**', newstring)
        newstring = sub(' _ ', '_', newstring)
        newstring = sub(' __ ', '__', newstring)

    return add_space_betw_digit_and_unit(newstring)


def add_space_betw_digit_and_unit(string):
    """给数字与单位之间增加空格。"""
    from re import sub
    # 常用单位，不齐全
    units = ['bps', 'Kbps', 'Mbps', 'Gbps',
            'B', 'KB', 'MB', 'GB', 'TB', 'PB',
            'g', 'Kg', 't',
            'h', 'm', 's']
    for unit in units:
        pattern = r'(?<=\d)' + unit #positive lookbehind assertion,
                                    #如果前面是括号中 '=' 后面的字符串，则匹配成功
        repl = ' ' + unit
        string = sub(pattern, repl, string)
    return string


def add_spaces_betw_ch(string):
    """给中文字之间添加合理的空格。"""
    from re import sub
    newustr = ""
    flag = 0
    ustr = string
    ch_lst = list(ustr)
    length = len(ch_lst)
    for i in range(0, length):
        if i < length - 1:
            #中文(括号)与英文(括号)之间需要增加空格
            if (is_chinese(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
            elif (is_chinese(ch_lst[i]) and isalpha(ch_lst[i + 1])) or (isalpha(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
        newustr += ch_lst[i]
    newstring = newustr#.encode(code)
    # if flag == 1:
    #     #处理中文里的粗体字和斜体字
    #     newstring = sub(r' \* ', '*', newstring)
    #     newstring = sub(r' \*\* ', '**', newstring)
    #     newstring = sub(' _ ', '_', newstring)
    #     newstring = sub(' __ ', '__', newstring)

    return newstring

def add_sp(string):
    new_string = 'sp' + string + 'sp'
    return new_string

def sp_spaces(input_dir, sub_dir = True):
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
                                string = f.read()
                                wrap_sp = add_sp(string)
                                print('sp is added at both ends!')
                                add_space = add_spaces_betw_ch(wrap_sp)
                                print('spaces are added!')
                            with open('%s%s' % (dir, file), 'w', encoding='utf-8') as f:
                                f.write(add_space)
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
                        string = f.read()
                        wrap_sp = add_sp(string)
                        add_space = add_spaces_betw_ch(wrap_sp)
                        print(add_space)
                    with open('%s%s' % (dir, file), 'w', encoding='utf-8') as f:
                        f.write(add_space)
    else:
        print('something is not right')


# def add_spaces_to_file(file_name, code="gbk"):
#     """给文本文件的内容添加合理的空格, 生成处理过的新文件。"""
#     import os.path
#     dir_name = os.path.dirname(file_name)
#     base_name = os.path.basename(file_name)
#     if dir_name == '':
#         new_file = code + "-" + base_name
#     else:
#         new_file = dir_name + "/" + code + "-" + base_name
#     try:
#         with open(file_name) as text:
#             line_list = [add_spaces_to_string(line, code) \
#                             for line in text]
#     except UnicodeDecodeError as err:
#         return str(err)
#     except IOError as err:
#         return str(err)
#     try:
#         with open(new_file, "w") as nfile:
#             nfile.writelines(line_list)
#             print 'Finished adding spaces, generated new file: %s' % new_file
#             return 'Success.'
#     except IOError as err:
#         return str(err)


if __name__ == '__main__':
    # print(add_spaces_betw_ch('sp 啊啊啊 sp 啊啦啦啦sp','utf-8'))

    input_dir = 'C:/Users\Cong\Desktop\ViaX\Xinrong Wang\S4\cut/'
    # 只处理subfolders里面的txt
    # sp_spaces(input_dir, sub_dir=1)

    # 处理dir里面的文件
    sp_spaces(input_dir, sub_dir=False)

##### code from original document
    # import sys
    # argc = len(sys.argv)
    # codeset = ['gb2312', 'gbk', 'utf8', 'gb18030', 'hz',\
    #             'iso2022_jp_2', 'big5', 'big5hkscs']
    # if argc == 1:
    #     print 'Usage: python add_spaces.py /path/to/file code(e.g. gbk, utf8)'
    #     print '    or python add_spaces.py /path/to/file'
    # elif argc == 2:
    #     for item in codeset:
    #         if add_spaces_to_file(sys.argv[1], item) == 'Success.':
    #             print 'Processing completed.'
    #             break
    # elif argc == 3:
    #     if sys.argv[2] in codeset:
    #         print add_spaces_to_file(sys.argv[1], sys.argv[2])
    #     else:
    #         print 'Parameter code (%s) error!' % sys.argv[2]
    #         print 'Supported codes are ' + ', '.join(codeset)
    # else:
    #     print 'Usage: python add_spaces.py /path/to/file code'


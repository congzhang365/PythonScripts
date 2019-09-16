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


def add_commas_to_string(string, code):
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
                ch_lst[i] += u","
            elif (isalpha(ch_lst[i]) and is_zh_l_bracket(ch_lst[i + 1])) \
                or (is_zh_r_bracket(ch_lst[i]) and isalpha(ch_lst[i + 1])):
                ch_lst[i] += u","
            elif (is_chinese(ch_lst[i]) and is_en_l_bracket(ch_lst[i + 1])) \
                or (is_en_r_bracket(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u","
            #中文与英文符号之间需要增加空格
            elif (is_chinese(ch_lst[i]) and is_en_symbol(ch_lst[i + 1])) \
                or (is_en_symbol(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u","
                flag = 1
            #中文(括号)与数字之间需要增加空格
            elif (is_chinese(ch_lst[i]) and isdigit(ch_lst[i + 1]))\
                or (isdigit(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u","
            elif (isdigit(ch_lst[i]) and is_zh_l_bracket(ch_lst[i + 1]))\
                or (is_zh_r_bracket(ch_lst[i]) and isdigit(ch_lst[i + 1])):
                ch_lst[i] += u","

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



def lyrics2csv(input_dir, sub_dir = True):
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
                        string_comma = add_commas_to_string(string)
                        print(string_comma)
                    with open('%s%s' % (dir, file), 'w', encoding='utf-8') as f:
                        f.write(string_comma)
    else:
        print('something is not right')




if __name__ == '__main__':
    input_dir = 'D:\Rokid\Projects\Songs/annotation\LH\AsrSsmlFinal/lyrics/'
    lyrics2csv(input_dir, sub_dir=False)



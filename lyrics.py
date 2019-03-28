import re


def remove_empty_string(text):
    while '' in text:
        text.remove('')


def remove_empty_list(list):
    while [] in list:
        list.remove([])


def split_characters(str):
    regex = r"[\u4e00-\ufaff]|[0-9]+|[a-zA-Z]+\'*[a-z]*"
    matches = re.findall(regex, str, re.UNICODE)
    return matches


def lyrics2block(input_file, output_file, replace_pattern=re.compile(r'\n|\u3000'), connector='\n\n\n\n'):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = []
        for i in range(len(lines)):
            if replace_pattern != 0:
                new = replace_pattern.split(lines[i])
                remove_empty_string(new)
                new_lines.append(connector.join(new))
            else:
                new = lines[i]
                new_lines.append(connector.join(new))
        remove_empty_string(new_lines)
        new_lyrics = connector.join(new_lines)
        if output_file != 0:
            with open('%s'%output_file, 'w', encoding='utf-8') as f:
                f.write(new_lyrics)
        else:
            print(new_lyrics)


def lyrics2csv(input_file, output_csv, delimiter=','):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        separated = []
        for line in lines:
            separated.append(delimiter.join(split_characters(line)))
        remove_empty_string(separated)
        new_lyrics = '\n\n\n\n'.join(separated)
        print(new_lyrics)
        if output_csv != 0:
            with open('%s.csv'%output_csv, 'w', encoding='utf-8') as file:
                file.write(new_lyrics)
        else:
            print(new_lyrics)





if __name__ == '__main__':
    input_file = 'a.txt'
    lyrics2csv(input_file,'newtest')
    pattern = re.compile(r'\n|\u3000')
    lyrics2block(input_file, 0, pattern, '\n')






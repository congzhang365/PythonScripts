import pandas as pd


def read_dict(dict_file):
    if dict_file.startswith('en'):
        en_map_full = pd.read_csv(dict_file)
        en_map_s1 = en_map_full.iloc[:, [0, 1]]
        en_map_s2 = en_map_full.iloc[:, [0, 2]]
        en_map_rs = en_map_full.iloc[:, [0, 3]]
        en_map_r = en_map_full.iloc[:, [0, 4]]
        en_map_min = en_map_full.iloc[:, [0, 5]]
        return make_dict(en_map_s1), make_dict(en_map_s2), make_dict(en_map_rs), make_dict(en_map_r), make_dict(
            en_map_min)
    else:
        return None


def make_dict(category):
    new_dict = dict(category.values)
    return new_dict


def process_replace_by_tag(source_data, map_dict, file_name, split='_'):
    write_lines = []
    for line in source_data:
        one_line = line.split(' ')
        splitted = []
        for e in one_line:
            if len(e) > 0:
                tag = e.split(split)[-1]
                _tag = '/' + str(map_dict.get(tag.strip(' '), '-----'))
                if _tag == '/nan':
                    _tag = ""
                word = e.split(split)[0]
            if _tag != '-----':
                _e = e.replace(tag, _tag)
                splitted.append(word + _tag)
            else:
                splitted.append(word + tag)
        _line = ' '.join(splitted)
        write_lines.append(_line)


    with open('%s.txt' % file_name, 'w', encoding='UTF-8') as f:
        f.write('\n'.join(write_lines))


if __name__ == '__main__':
    with open('brown.txt', 'r', encoding='UTF-8') as source_file:
        en_data = source_file.read().splitlines()
        dict_s1, dict_s2, dict_rs, dict_r, dict_min = read_dict('en_map.csv')

    _f = {

        'en_s1': dict_s1,
        'en_s2': dict_s2,
        'en_rs': dict_rs,
        'en_r': dict_r,
        'en_min': dict_min,
    }
    for k in _f.keys():
        map_dict = _f[k]
        process_replace_by_tag(source_data=en_data, map_dict=map_dict, file_name=k, split='_')


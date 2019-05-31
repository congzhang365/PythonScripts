import pandas as pd


def make_dict(categ):
    new_dict = dict(categ.values)
    return new_dict


def process_replace_by_tag(source_data, map_dict, file_name, split='/'):
    write_lines = []
    for line in source_data:
        one_line = line.split(' ')
        splitted = []
        for e in one_line:
            if len(e) > 0:
                tag = e.split(split)[-1]
                _tag = str(map_dict.get(tag.strip(' '), '-----'))
                if _tag != '-----':
                    _e = e.replace(tag, str(_tag))
                    splitted.append(_e)
                else:
                    splitted.append(e)
        _line = ' '.join(splitted)
        if "/nan" in _line:
            _line = _line.replace("/nan", "")
        write_lines.append(_line)
    with open('%s.txt' % file_name, 'w', encoding='UTF-8') as f:
        f.write('\n'.join(write_lines))
		
if __name__=='__main__':
    # get dictionary info
    ch_map_full = pd.read_csv('ch_map.csv')
    ch_map_s1 = ch_map_full.iloc[:, [0, 1]]
    ch_map_s2 = ch_map_full.iloc[:, [0, 2]]
    ch_map_rs = ch_map_full.iloc[:, [0, 3]]
    ch_map_r = ch_map_full.iloc[:, [0, 4]]
    ch_map_min = ch_map_full.iloc[:, [0, 5]]

    # make dictionaries
    dict_s1 = make_dict(ch_map_s1)
    dict_s2 = make_dict(ch_map_s2)
    dict_rs = make_dict(ch_map_rs)
    dict_r = make_dict(ch_map_r)
    dict_min = make_dict(ch_map_min)

    with open('people2014_clean.txt',  'r', encoding='UTF-8') as source_file:
        ch_data = source_file.read().splitlines()
        process_replace_by_tag(source_data=ch_data,map_dict=dict_s1,file_name='ch_s1',split='/')
        process_replace_by_tag(source_data=ch_data,map_dict=dict_s2,file_name='ch_s2',split='/')
        process_replace_by_tag(source_data=ch_data,map_dict=dict_rs,file_name='ch_rs',split='/')
        process_replace_by_tag(source_data=ch_data,map_dict=dict_r,file_name='ch_r',split='/')
        process_replace_by_tag(source_data=ch_data,map_dict=dict_min,file_name='ch_min',split='/')
import re

def scale_to_notes(original_scale, output_csv):
    new_scale = re.sub('; ',';',original_scale)
    split_by_semicolon = new_scale.split(';')
    full_set = []
    all_notes = []
    all_durs = []
    for i in range(len(split_by_semicolon)):
        split_by_space = split_by_semicolon[i].split(' ')
        all_notes.append(split_by_space[0])
        all_durs.append(split_by_space[1])
        string_element = ','.join(split_by_space)
        full_set.append(string_element+ '\n')
    final_set = ''.join(full_set)
    # print(all_notes)

    with open('%s'%output_csv, 'w', encoding='utf-8') as f:
        f.write(final_set)
    return all_notes, list(map(float, all_durs))


def interval_times(intercept,tempo):
    interval_begin = []
    interval_end = []

    for num in range(len(durs)):
        if num == 0:
            segment_begin = intercept
            segment_end = segment_begin + 60 / tempo * durs[num]
            interval_begin.append(round(segment_begin,3))
            interval_end.append(round(segment_end,3))
        else:
            segment_begin = interval_end[num-1]
            segment_end = segment_begin + 60 / tempo * durs[num]
            interval_begin.append(round(segment_begin,3))
            interval_end.append(round(segment_end, 3))

    return interval_begin, interval_end


def textgrid_body():
    body = []
    for i in range(len(interval_begintimes)):
        one_interval = '\n'.join([str(interval_begintimes[i]), str(interval_endtimes[i]), '\"\"'])
        body.append(one_interval)
    body_text = '\n'.join(body)
    audio_dur = max(interval_endtimes)

    return body_text, audio_dur


def textgrid_header(audio_duration, total_interval, total_tier = 1):
    file_type = 'File type = \"ooTextFile\"'
    object_class = 'Object class = \"TextGrid\"'
    audio_begin = str(0)
    audio_end = str(audio_duration)
    exist = '<exists>'
    total_tiers = str(total_tier)
    tier_type = '\"IntervalTier\"'
    tier_num = '\"1\"'
    interval_num = str(total_interval)

    header_text = '\n'.join([file_type, object_class,audio_begin, audio_end,
                   exist,total_tiers,tier_type,tier_num,audio_begin,audio_end,
                   interval_num])
    return header_text



if __name__=='__main__':
    scale = "G4 0.5;E4 0.5;NL 2;D4 0.5;C4 0.5;G4 0.5;E4 0.5;NL 3;G4 0.5;E4 0.5;" \
            "NL 2;D4 0.5;C4 0.5;E4 0.5;D4 0.5;NL 3;G4 0.5;E4 0.5;NL 2;D4 0.5;C4 0.5;" \
            "G4 0.5;E4 0.5;NL 3;G4 0.5;E4 0.5;NL 2.5;C4 0.5;E4 0.75;E4 0.75;F4 0.5;" \
            "E4 0.75;D4 0.75;C4 3.5;G4 0.5;E4 3.5;D4 0.5;C4 3.5;E4 0.5;G4 2.5;NL 2;" \
            "E4 1;G4 0.5;G4 0.5;E4 1;G4 0.5;G4 0.5;B4 0.5;C5 0.5;B4 0.5;C5 0.5;B4 1;" \
            "G4 1;F4 0.5;E4 0.5;F4 0.5;E4 0.5;F4 1;E4 1;F4 0.5;E4 0.5;C4 0.5;D4 1.5;" \
            "NL 1;E4 1;G4 0.5;G4 0.5;E4 1;G4 0.5;G4 0.5;B4 0.5;C5 0.5;B4 0.5;C5 0.5;" \
            "B4 1;G4 1;F4 0.5;E4 0.5;F4 0.5;E4 0.5;F4 1;E4 1;F4 0.5;E4 0.5;F4 0.5;" \
            "G4 1.5;NL 1;E4 1;G4 0.5;G4 0.5;E4 1;G4 0.5;G4 0.5;B4 0.5;C5 0.5;B4 0.5;" \
            "C5 0.5;B4 1;G4 1;F4 0.5;E4 0.5;F4 0.5;E4 0.5;F4 1;E4 1;F4 0.5;E4 0.5;" \
            "C4 0.5;D4 1.5;NL 1;E4 1;G4 0.5;G4 0.5;E4 1;G4 0.5;G4 0.5;B4 0.5;C5 0.5;B4 0.5;" \
            "C5 0.5;B4 1;G4 1;F4 0.5;E4 0.5;F4 0.5;E4 0.5;F4 1;E4 1;E4 0.5;E4 0.5;E4 0.5;F4 0.5;" \
            "E4 0.75;D4 0.75;C4 2.5; NL 1;G4 0.5;E4 3.5;D4 0.5;C4 3.5;NL 1;E4 0.75;E4 0.75;F4 0.5;" \
            "E4 0.75;D4 0.75;C4 2.5"

    notes, durs = scale_to_notes(scale,'test.csv')
    interval_begintimes, interval_endtimes = interval_times(intercept=0,tempo=120)
    body_text, audio_dur = textgrid_body()
    header_text = textgrid_header(audio_dur, len(notes))

    with open('piggy_whole.TextGrid', 'w', encoding='utf-8') as f:
        f.write(header_text + '\n' + body_text)
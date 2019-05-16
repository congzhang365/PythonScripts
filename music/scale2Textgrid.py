import re
import os

def find_tempo(xml_doc):
    with open(xml_doc, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            find_tempo = re.findall(r'\<sing tempo=\"(.*?)\"',line)
            if not find_tempo == []:
                tempo_string = ''.join(find_tempo)
                tempo = int(tempo_string)
    return tempo


def scale_to_notes(xml_doc, output_csv=None):
    with open(xml_doc, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        note_set = []
        for line in lines:
            notes = re.findall(r'\<s pd=\"(.*?)\"\>',line)
            if not notes == []:
                note_set.append(notes)
    original_scale = [number for sublist in note_set for number in sublist + [';']][:-1]
    new_scale = ''.join(original_scale)

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
    if not output_csv == 'None':
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


def textgrid_body(interval_begintimes, interval_endtimes):
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
    xml_doc = "D:\Rokid\pycharm\generic\houlai.xml"
    notes, durs = scale_to_notes(xml_doc)
    interval_begintimes, interval_endtimes = interval_times(intercept=0.02, tempo=find_tempo(xml_doc))
    body_text, audio_dur = textgrid_body(interval_begintimes, interval_endtimes)
    header_text = textgrid_header(audio_dur, len(notes))
    filename = os.path.splitext(xml_doc)[0]
    with open(filename + '.TextGrid', 'w', encoding='utf-8') as f:
        f.write(header_text + '\n' + body_text)
## you need three documents:
## 1. mapping.csv
## 2. notes.txt
## 3. lyrics.txt


import csv


def make_dict(input_csv):
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        mydict = {rows[0]: rows[1] for rows in reader}
    return mydict


def convert_notes(mapping_dict, input_notes, by_line = 1):
    with open(input_notes, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        notes_by_line = []
        for line in lines:
            notes = line.strip('\n').split(';')
            new_line_notes = []
            for note_seg in notes:
                note_list = note_seg.split(' ')
                new_note_seg = []
                for note in note_list:
                    new_note = mapping_dict.get(note)
                    new_note_seg.append(new_note)
                new_line_notes.append(' '.join(new_note_seg))
            # print(new_line_notes)
            converted_line_notes = '; '.join(new_line_notes)
            notes_by_line.append(converted_line_notes)
        # print(notes_by_line)
        all_notes = '; '.join(notes_by_line)

        # print(notes_by_line, all_notes)
        if by_line:
            return notes_by_line
        else:
            return all_notes


def get_lyrics(lyrics_file):
    with open(lyrics_file,'r', encoding='utf-8') as f:
        lyrics_lines = f.read().split('\n')
        return lyrics_lines

def write_xml(note_by_line, lyrics_lines):
    header = '<speak>\n<voice name="CHILD.MOOD.ADD1K4.MIX1K">\n<sing tempo="???" tone="0">\n'
    footer = '</sing>\n</voice>\n</speak>'

    line_start = '<s pd="'
    note_end = '">'
    line_end = '</s>'


    notes_list = note_by_line
    lyrics_list = lyrics_lines

    all_lines = []
    for i, j in zip(range(len(notes_list)), range(len(lyrics_list))):
        note_line = note_by_line[i]
        lyrics_line = lyrics_lines[j]

        line = line_start + note_line + note_end + lyrics_line + line_end
        all_lines.append(line)

    # print(all_lines)


    doc = header + '\n'.join(all_lines) + footer
    print(doc)

    return doc

if __name__=='__main__':
    note_by_line = convert_notes(make_dict('mapping.csv'), 'notes.txt')
    lyrics_lines = get_lyrics('ly.txt')

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(write_xml(note_by_line,lyrics_lines))
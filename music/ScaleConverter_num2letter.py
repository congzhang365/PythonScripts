import re
import os
from fractions import Fraction


def add_NL(input_csv):
    with open(input_csv, 'r', encoding='utf-8') as f:
        file = f.readlines()[4:]
        for i in range(len(file)):
            if i % 2 == 0:  # odd number: note line
                note_beat = [x for x in file[i].strip('\n').split(',') if x]
                # note_beat = [x for x in note_beat if x]
                print(note_beat)
                lyric_line = [x for x in file[i + 1].strip('\n').split(',') if x]
                # print(lyric_line)

                # Add NL to match the numbers of note line and lyrics line
                if len(note_beat) - len(lyric_line) == 1 and note_beat[-1].find('0') is 1:
                    lyric_line.append('NL')
                    print(lyric_line)
                elif len(note_beat) != len(lyric_line):
                    print("Note number and lyrics don't match!")
                else:
                    print(lyric_line)


def extract_number_note(string):
    try:
        start = string.index('[') + len('[')
        end = string.index(']', start)
        return string[start:end]
    except ValueError:
        return print("extract_number_note ERROR!")


def remove_number_note(string):
    number_note = re.compile(r"[^[]*\[([^]]*)\]")
    beat = re.sub(number_note, '', string)
    return beat


def number_letter_conversion(map_key):
    note_map = {'0': 'NL', '1': 'C4', '2': 'D4', '3': 'E4', '4': 'F4', '5': 'G4', '6': 'A4', '7': 'B4', \
                '1-': 'C3', '2-': 'D3', '3-': 'E3', '4-': 'F3', '5-': 'G3', '6-': 'A3', '7-': 'B3', \
                '1+': 'C5', '2+': 'D5', '3+': 'E5', '4+': 'F5', '5+': 'G5', '6+': 'A5', '7+': 'B5', \
                '1#': 'c4', '2#': 'd4', '3#': 'ERR', '4#': 'f4', '5#': 'g4', '6#': 'a4', '7#': 'ERR', \
                '1-#': 'c3', '2-#': 'd3', '3-#': 'ERR', '4-#': 'f3', '5-#': 'g3', '6-#': 'a3', '7-#': 'ERR', \
                '1+#': 'c5', '2+#': 'd5', '3+#': 'ERR', '4+#': 'f5', '5+#': 'g5', '6+#': 'a5', '7+#': 'ERR', \
                '1b': 'ERR', '2b': 'c4', '3b': 'd4', '4b': 'ERR', '5b': 'f4', '6b': 'g4', '7b': 'a4', \
                '1-b': 'ERR', '2-b': 'c3', '3-b': 'd3', '4-b': 'ERR', '5-b': 'f3', '6-b': 'g3', '7-b': 'a3', \
                '1+b': 'ERR', '2+b': 'c5', '3+b': 'd5', '4+b': 'ERR', '5+b': 'f5', '6+b': 'g5', '7+b': 'a5'}

    map_value = note_map.get(map_key)
    return map_value


def beat_conversion(input_string):
    # whole_beat = 1
    beat_map = {'': 1, '/': 1/2, '//': 1/4, '///': 1/8, '.': 3/2, '/.': 3/4, '//.': 3/8, '///.': 3/16,
                't': round(1/3,4), '/t': round(1/6,4), '//t': round(1/12,4), '///t': round(1/24,4)}
    # beat_map = {'': Fraction(1, 1), '/': Fraction(1, 2), '//': Fraction(1, 4), '///': Fraction(1, 8),
    #             '.': Fraction(3, 2), '/.': Fraction(3, 4), '//.': Fraction(3, 8), '///.': Fraction(3, 16),
    #             '[1/3]': Fraction(1, 3), '/[1/3]': Fraction(1, 6), '//[1/3]': Fraction(1, 12),
    #             '///[1/3]': Fraction(1, 24)}
    beats = remove_number_note(input_string)
    # print(beats)
    beat_number = beat_map.get(beats)
    # print(beat_number)
    return beat_number


# def merge_same_notes(string):


def notescale_converter(input_csv, output_txt):
    with open(input_csv, 'r', encoding='utf-8') as f:
        whole_file = f.readlines()
        header = '\n'.join(whole_file[0:4])
        print(header)
        file = whole_file[4:]
        final_notes = []
        for i in range(len(file)):
            if i % 2 == 0:  # odd number: note line
                note_beat = [x for x in file[i].strip('\n').split(',') if x]
                print(note_beat)

                line_notes = []
                for item in note_beat:
                    notes = item.split('&')
                    # print(notes)

                    if len(notes) > 1:
                        letter_notes = []
                        for j in range(len(notes)-1):

                            if extract_number_note(notes[j]) == extract_number_note(notes[j+1]):
                                letter_note = number_letter_conversion(extract_number_note(notes[j]))
                                # print('letter note1: %s' % letter_note)
                                beat_number = beat_conversion(notes[j]) + beat_conversion(notes[j+1])
                                # print('beat number1: %s' % beat_number)
                                letter_notes.append(str(letter_note) + ' ' + str(beat_number))
                            else:
                                letter_note1 = number_letter_conversion(extract_number_note(notes[j]))
                                letter_note2 = number_letter_conversion(extract_number_note(notes[j+1]))

                                # print('letter note2: %s' % letter_note)
                                beat_number1 = beat_conversion(notes[j])
                                beat_number2 = beat_conversion(notes[j+1])

                                # print('beat number2: %s' % beat_number)
                                letter_notes.append(str(letter_note1) + ' ' + str(beat_number1) + ' ' + str(letter_note2) + ' ' + str(beat_number2))

                        line_notes.append(' '.join(letter_notes))
                    else:
                        letter_notes = []
                        for j in range(len(notes)):
                            numeric_note = extract_number_note(notes[j])
                            letter_note = number_letter_conversion(numeric_note)
                            # print('letter note3: %s'%letter_note)
                            beat_number = beat_conversion(notes[j])
                            # print('beat number3: %s'%beat_number)
                            letter_notes.append(str(letter_note) + ' ' + str(beat_number))
                            # letter_notes_dict[letter_note] = beat_number
                        line_notes.append(' '.join(letter_notes))

                final_notes.append(';'.join(line_notes))
                final_notes.append(file[i+1])

        notes = '\n'.join(final_notes)
        print(header + notes)
        with open('%s'%output_txt, 'w', encoding='utf-8') as f:
            f.write(header + notes)
    return '%s'%output_txt


def simple_converter(input_csv, output_txt):
    with open(input_csv, 'r', encoding='utf-8') as f:
        whole_file = f.readlines()
        header = '\n'.join(whole_file[0:4])
        print(header)
        file = whole_file[4:]
        final_notes = []
        for i in range(len(file)):
            if i % 2 == 0:  # odd number: note line
                note_beat = [x for x in file[i].strip('\n').split(',') if x]
                print(note_beat)

                line_notes = []
                for item in note_beat:
                    notes = item.split('&')
                    # print(notes)

                    letter_notes = []
                    for note in notes:
                        letter_note = number_letter_conversion(extract_number_note(note))
                        # print('letter note: %s' % letter_note)
                        beat_number = beat_conversion(note)
                        # print('beat number: %s' % beat_number)
                        letter_note = str(letter_note) + ' ' + str(beat_number)
                        letter_notes.append(letter_note)
                    #     print(note)
                    #     print(letter_note)
                    # print(letter_notes)
                    line_notes.append(' '.join(letter_notes))

                final_notes.append(';'.join(line_notes))
                final_notes.append(file[i+1])

        notes = '\n'.join(final_notes)
        print(header + notes)
        with open('%s'%output_txt, 'w', encoding='utf-8') as f:
            f.write(header + notes)
    return '%s'%output_txt

def batch_convert(input_dir, output_dir):
    dir = input_dir
    if os.path.isdir(dir):
        print(dir)
        for root, dirs, files in os.walk(dir):
            break

        for file in files:
            if file.endswith('.csv'):
                input_csv = '%s%s' % (input_dir, file)
                output_txt = '%s%s_data.txt' % (output_dir, file[:-4])
                simple_converter(input_csv, output_txt)


if __name__ == '__main__':
    input_dir = 'C:\Rokid\Projects\Songs\EXP2_Singing\标注规则与样例\标注需求\eg\in/'
    output_dir = 'C:\Rokid\Projects\Songs\EXP2_Singing\标注规则与样例\标注需求\eg\out/'
    batch_convert(input_dir, output_dir)

    input_csv = 'C:\Rokid\Projects\Songs\EXP2_Singing\标注规则与样例\标注需求\eg\in/abc.csv'
    output_txt = 'C:\Rokid\Projects\Songs\EXP2_Singing\标注规则与样例\标注需求\eg\out/abc.txt'
    # simple_converter(input_csv, output_txt)
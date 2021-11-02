import docx
from docx.enum.text import WD_COLOR_INDEX
import pandas as pd


def highlight2brackets(input_file):
    document = docx.Document(input_file)
    new_doc = []
    for paragraph in document.paragraphs:
        # print('para', paragraph.text)

        new_paragraph = []
        for run in paragraph.runs:
            # print(run.text)
            if run.font.highlight_color==WD_COLOR_INDEX.YELLOW:
                highlight_yellow = '[[' + run.text + ']]'
                # print('yellow:', highlight_yellow)
                new_paragraph.append(highlight_yellow)
            elif run.font.highlight_color==WD_COLOR_INDEX.PINK:
                highlight_pink = '{{' + run.text + '}}'
                # print('pink:', highlight_pink)
                new_paragraph.append(highlight_pink)
            elif run.font.highlight_color==WD_COLOR_INDEX.GRAY_25:
                highlight_gray = '((' + run.text + '))'
                # print('gray:', highlight_gray)
                new_paragraph.append(highlight_gray)
            elif run.font.highlight_color==WD_COLOR_INDEX.TURQUOISE:
                highlight_turquoise = '<<' + run.text + '>>'
                # print('turquoise:', highlight_turquoise)
                new_paragraph.append(highlight_turquoise)
            else:
                # print('not highlight', run.text)
                new_paragraph.append(run.text)
        # new_paragraph = ''.join(new_paragraph)

        new_doc.append(''.join(new_paragraph))

    new_text = '\n'.join(new_doc)
    # print(new_text)
    return new_text


def split2excel(text):
    text_line = text.split('\n')
    df = pd.DataFrame(columns=['time', 'speaker', 'text'])
    new_line = []
    for line in text_line:
        col_text = line.split('\t')
        if len(col_text) == 1:
            df = df.append(pd.Series(col_text, index=['text']), ignore_index=True)
        elif len(col_text) == 2:
            df = df.append(pd.Series(col_text, index=['time', 'text']), ignore_index=True)
        elif len(col_text) == 3:
            df = df.append(pd.Series(col_text, index=['time', 'speaker', 'text']), ignore_index=True)
    print(df)
    return df


    # return new_text


if __name__ == '__main__':
    input_file = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Training/Pragmatic_annotation/TNEW/TNEW.docx"
    output_file = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Training/Pragmatic_annotation/TNEW/TNEW.xlsx"
    #
    # with open(output_file, 'w', encoding='utf-8') as f:
    #     f.write(split2excel(highlight2brackets(input_file)))

    df = split2excel(highlight2brackets(input_file))
    df.to_excel(output_file, index=False)

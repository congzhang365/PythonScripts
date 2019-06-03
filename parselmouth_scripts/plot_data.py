"""
Listing 2 shows how this kind of plotting function can be combined with the Python
data manipulation library pandas and the FacetGrid functionality of seaborn to compose
a structured array of spectrograms with overlaid pitch contours. This example
visualises a small dataset consisting of the numbers 1 to 5 being spoken in English by the
first two authors. The example assumes we have stored these audio files in a directory
named audio, and that each audio file has been named in accordance with the convention
{digit} {speaker-id}.wav. It also assumes a csv data frame whose rows contain variables
that uniquely identify a speaker-id / digit combination that we wish to plot in the
grid. The next example (see Section 2.2) goes into more detail on file system integration
for structured data frames. The resulting array of spectrograms, with the number being
spoken along the columns, and a row for each speaker, is shown in Figure 2.

https://ai.vub.ac.be/~yajadoul/jadoul_introducing-parselmouth_a-python-interface-to-praat.pdf
"""

import pandas as pd


def facet_util(data, **kwargs):
    digit, speaker_id = data[['digit', 'speaker_id']].iloc[0]
    sound = parselmouth.Sound("audio/{0}_{1}.wav".format(digit, speaker_id))
    pitch = sound.to_pitch()
    sound.pre_emphasize()
    draw_spectrogram(sound.to_spectrogram())
    plt.twinx()
    draw_pitch(pitch)
    # If not the rightmost column, then clear the right side axis
    if speaker_id != 'y':
        plt.ylabel("")
        plt.yticks([])

if __name__ == '__main__':

    results = pd.read_csv("audio/digit_list.csv")

    grid = sns.FacetGrid(results, row='digit', col='speaker_id')
    grid.map_dataframe(facet_util)
    grid.set_titles(col_template="{col_name}", row_template="{row_name}")
    grid.set_axis_labels("time [s]", "frequency [Hz]")
    grid.set(xlim=(0, None))
    # Optionally: grid.set(facecolor='white')
    plt.show()

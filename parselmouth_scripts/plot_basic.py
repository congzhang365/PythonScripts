"""
https://ai.vub.ac.be/~yajadoul/jadoul_introducing-parselmouth_a-python-interface-to-praat.pdf

plt documentation: https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
plt.pcolormesh documentation: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolormesh.html
"""

import parselmouth
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()  # Use seaborn's default style to make attractive graphs


def draw_spectrogram(spect, dynamic_range=70):
    X, Y = spect.x_grid(), spect.y_grid()
    sg_db = 10 * np.log10(spect.values)
    min_db = sg_db.max() - dynamic_range
    plt.pcolormesh(X, Y, sg_db, vmin=min_db, cmap='afmhot')
    plt.ylim([spect.ymin, spect.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")


def draw_pitch(pitch):
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN to not plot
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values == 0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='b')
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("fundamental frequency [Hz]")


def draw_intensity(intensity):
    plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='y')
    plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("intensity [dB]")


if __name__ == '__main__':

    snd = parselmouth.Sound("D:\Rokid\Files\Wechat files接收\wav\cmp-12.wav")
    pitch = snd.to_pitch()
    intensity = snd.to_intensity()
    # Optionally pre-emphasize the sound before calculating the spectrogram
    snd.pre_emphasize()
    spectrogram = snd.to_spectrogram(maximum_frequency=8000.0)

    plt.figure()
    draw_spectrogram(spectrogram)
    plt.twinx()
    draw_pitch(pitch)
    draw_intensity(intensity)
    plt.xlim([snd.xmin, snd.xmax])
    plt.show()  # or plt.savefig("spectrogram.pdf")

    # Another plot
    # Plot nice figures using Python's "standard" matplotlib library
    snd = parselmouth.Sound("D:\Rokid\Files\Wechat files接收\wav\cmp-12.wav")
    plt.figure()
    plt.plot(snd.xs(), snd.values.T)
    plt.xlim([snd.xmin, snd.xmax])
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.show() # or plt.savefig("sound.png"), or plt.savefig("sound.pdf")
"""
Listing 7: Code snippets accessing Parselmouth functionality inserted into a PsychoPy experiment
through a Code Component, respectively in the Before Experiment, Begin Routine, and
End Routine section. Usage of Parselmouth functionality is highlighted in red; a version with
detailed comments can be found in the supplementary material

https://ai.vub.ac.be/~yajadoul/jadoul_introducing-parselmouth_a-python-interface-to-praat.pdf
"""

# -- Begin experiment --
import parselmouth
import numpy as np
import random
if __name__ == '__main__':


    conditions = ['a', 'e']
    stimulus_files = {'a': 'audio/bat.wav', 'e': 'audio/bet.wav'}

    STANDARD_INTENSITY = 70.
    stimuli = {}
    for condition in conditions:
        stimulus = parselmouth.Sound(stimulus_files[condition])
        stimulus.scale_intensity(STANDARD_INTENSITY)
        stimuli[condition] = stimulus

    # -- Begin Routine --
    random_condition = random.choice(conditions)
    random_stimulus = stimuli[random_condition]

    noise_samples = np.random.normal(size=random_stimulus.n_samples)
    noisy_stimulus = parselmouth.Sound(noise_samples, sampling_frequency=random_stimulus.sampling_frequency)
    noisy_stimulus.scale_intensity(STANDARD_INTENSITY - level)
    noisy_stimulus.values += random_stimulus.values
    noisy_stimulus.scale_intensity(STANDARD_INTENSITY)

    # 'filename' variable is set by PsychoPy and contains base file name
    # of saved log/output files, so we'll use that to save our custom stimuli
    stimulus_file_name = filename + '_stimulus_' + str(trials.thisTrialN) + '.wav'
    noisy_stimulus.resample(44100).save(stimulus_file_name, "WAV")
    sound_1.setSound(stimulus_file_name)
    # -- End routine --


    trials.addResponse(key_resp_2.keys == random_condition)

import sys

sys.path.append('D:\Rokid\pycharm\_PythonScripts')
from inspect import getmembers, isfunction


if __name__ == '__main__':
    import import_modules
    import list_all_modules
    import list_functions
    import __init__
    # import AudioProcessing.downsampling
    # import AudioProcessing.feature_extraction
    # import AudioProcessing.match_wav_tg
    import AudioProcessing.__init__
    # import FileManipulation.change_line_numbers
    # import FileManipulation.mergefiles
    # import FileManipulation.rename
    import FileManipulation.__init__
    # import Music.get_wav_duration
    # import Music.lyrics
    # import Music.scale2Textgrid
    import Music.__init__
    # import Parselmouth_scripts.analysis
    # import Parselmouth_scripts.audio_manipulation
    # import Parselmouth_scripts.batch
    # import Parselmouth_scripts.experiment
    # import Parselmouth_scripts.file_manipulation
    # import Parselmouth_scripts.integrate_script
    # import Parselmouth_scripts.plot_basic
    # import Parselmouth_scripts.plot_data
    import Parselmouth_scripts.__init__
    # import TextProcessing.ascii
    # import TextProcessing.check_english
    # import TextProcessing.ch_replace
    # import TextProcessing.combine_lists
    # import TextProcessing.count_English
    # import TextProcessing.en_replace
    # import TextProcessing.regex_practical
    # import TextProcessing.separate_lines
    import TextProcessing.__init__

    # This script is to list all the functions
    # It can get all the functions in one module at a time
    # The target module name needs to be changed every time
    # The target module needs to be imported
    # The modules in the parent directory need to be imported separately
    # The modules in the sub directories can be imported through their init files


    functions_list = [o for o in getmembers(AudioProcessing.downsampling, isfunction)]   # change the module name
    for i in range(len(functions_list)):
        function_names = functions_list[i][0]
        print(function_names)
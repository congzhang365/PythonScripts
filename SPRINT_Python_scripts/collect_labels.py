from praatio import tgio
import pandas as pd
import os


in_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/TFLK/utterances/"
out_file = "C:/Users/sprin/Desktop/test/mark/data/result.txt"


'''
tier1 = "ORT-MAU"       # orthographic information, i.e. analysis unit information
tier2 = "MAU"           # segments
tier3 = "MAS"   
tier4 = "stress"
tier5 = "distance"
tier6 = "initial"
tier7 = "final"
tier8 = "AM"
tier9 = "type"
tier10 = "utterance"
'''


results = []

for f in os.listdir(in_dir):
    if f.endswith(".TextGrid"):
        tg = tgio.openTextgrid(os.path.join(in_dir, f))


        seg_labels = tg.tierDict["MAU"].entryList
        if not len(seg_labels) == 0:
            for seg_label in seg_labels:

                seg_start, seg_stop, seg_text = seg_label
                # print(f, ":", stress_label)

                stress_labels = tg.tierDict["stress"].entryList
                for stress_label in stress_labels:
                    stress_start, stress_stop, stress_text = stress_label


                    if seg_start >= stress_start and seg_stop <= stress_stop and not stress_text == "":
                        result_line = []
                        result_line.append(f)

                        result_line.append(seg_text)
                        result_line.append(str(seg_start))
                        result_line.append(str(seg_stop))
                        result_line.append(str(seg_stop - seg_start))

                        result_line.append(stress_text)
                        result_line.append(str(stress_start))
                        result_line.append(str(stress_stop))
                        result_line.append(str(stress_stop - stress_start))
                    # else:
                    #     result_line.append(str("\t\t\t"))

                        type_labels = tg.tierDict["type"].entryList
                        for type_label in type_labels:
                            type_start, type_stop, type_text = type_label
                            if stress_start >= type_start and stress_stop <= type_stop:
                                result_line.append(type_text)
                                result_line.append(str(type_start))
                                result_line.append(str(type_stop))

                                word_labels = tg.tierDict["ORT-MAU"].entryList
                                analysis_window_label = []
                                for word_label in word_labels:
                                    word_start, word_stop, word_text = word_label

                                    if word_start >= type_start and word_stop <= type_stop:
                                        analysis_window_label.append(word_text)
                                result_line.append(' '.join(analysis_window_label))

                        am_labels = tg.tierDict["AM"].entryList
                        for am_label in am_labels:
                            am_start, am_stop, am_text = am_label
                            if stress_start >= am_start and stress_stop <= am_stop:
                                result_line.append(am_text)

                        initial_labels = tg.tierDict["initial"].entryList
                        for initial_label in initial_labels:
                            initial_start, initial_stop, initial_text = initial_label
                            if stress_start >= initial_start and stress_stop <= initial_stop:
                                result_line.append(initial_text)


                        final_labels = tg.tierDict["final"].entryList
                        for final_label in final_labels:
                            final_start, final_stop, final_text = final_label
                            if stress_start >= final_start and stress_stop <= final_stop:
                                result_line.append(final_text)


                        results.append('\t'.join(result_line))
            # print('\n'.join(results))


title_line = "file_name\tseg_label\tseg_start\tseg_end\tseg_duration\tstress_label\tstress_start\tstress_end\tstress_duration\ttype_label\tanalysis_start\tanalysis_end\tanalysis_label\tam_label\tinitial_label\tfinal_label\n"


with open(out_file, 'w+', encoding="UTF-8") as f:
    if not os.path.exists(out_file):
        f.write(title_line)
        f.write('\n'.join(results))
        print('Result file is saved.')
    else:
        override = input('File exists. Do you want to override? \n Press 1 in Python Console to override. \n Press 0 in Python Console to abort.')
        if override == "1":
            f.write(title_line)
            f.write('\n'.join(results))
            print('Result file is saved.')
        elif override == "0":
            print('Mission aborted.')
        else:
            print('What did you say? Run again.')

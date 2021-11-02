from praatio import tgio
import pandas as pd
import os

tasks = ["DIAL", "MAPS", "OBJE", "TFLK", "TNEW", "SCUB"]

for task in tasks:

    in_dir = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/ToBI/KM/" % task
    out_file = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/AM_ToBI/ToBI_labels/KM_%s_Tobi.txt" % task


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


            seg_labels = tg.tierDict["stress"].entryList
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


                            result_line.append(stress_text)
                            # result_line.append(str(stress_start))
                            # result_line.append(str(stress_stop))
                            # result_line.append(str(stress_stop - stress_start))
                        # else:
                        #     result_line.append(str("\t\t\t"))

                            type_labels = tg.tierDict["AM"].entryList
                            for type_label in type_labels:
                                type_start, type_stop, type_text = type_label
                                if stress_start >= type_start and stress_stop <= type_stop:
                                    result_line.append(type_text)
                                    # result_line.append(str(type_start))
                                    # result_line.append(str(type_stop))

                                    word_labels = tg.tierDict[tg.tierNameList[0]].entryList
                                    analysis_window_label = []
                                    for word_label in word_labels:
                                        word_start, word_stop, word_text = word_label

                                        if word_start >= type_start and word_stop <= type_stop:
                                            analysis_window_label.append(word_text)
                                    result_line.append(' '.join(analysis_window_label))




                            results.append('\t'.join(result_line))
                # print('\n'.join(results))


    title_line = "file_name\tstress_label\ttype_label\tanalysis_label\n"


    with open(out_file, 'w+', encoding="UTF-8") as f:
        f.write(title_line)
        f.write('\n'.join(results))


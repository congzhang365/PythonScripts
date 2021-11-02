from praatio import tgio
import pandas as pd
import os


# all you need to change is the in_dir and out_file
# this script will loop through all tasks
# make sure the path keeps the %s and the % task part since it represents the task name


tasks = ["DIAL", "MAPS", "OBJE", "TFLK", "TNEW", "SCUB"]

for task in tasks:
    in_dir = "C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Audio/%s/utterances/"% task
    out_file = "C:/Users/kmarcoux/SPRINT Dropbox/Academic Research/Production_Pilots/Analysis/EN_full_pilot/ToBI/TextGrid_Info_final/%s_result.txt" % task



    '''
    tier1 = "ORT-MAU"       # orthographic information, i.e. analysis unit information #It's not always called ORT-MAUS ex DIAL_LP04_D034_W2_FN2
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
            print(f)

            # seg_labels = tg.tierDict[tg.tierNameList[2-1]].entryList
            # if not len(seg_labels) == 0:
            #     for seg_label in seg_labels:

            #         seg_start, seg_stop, seg_text = seg_label
                    # print(f, ":", stress_label)

            stress_labels = tg.tierDict["stress"].entryList
            if not len(stress_labels) == 0:
                for stress_label in stress_labels:
                    stress_start, stress_stop, stress_text = stress_label


                #if seg_start >= stress_start and seg_stop <= stress_stop and not stress_text == "":
                    result_line = []
                    result_line.append(f)

                    # result_line.append(seg_text)
                    # result_line.append(str(seg_start))
                    # result_line.append(str(seg_stop))
                    # result_line.append(str(seg_stop - seg_start))

                    result_line.append(stress_text)
                    # result_line.append(str(stress_start))
                    # result_line.append(str(stress_stop))
                    # result_line.append(str(stress_stop - stress_start))
                # else:
                #     result_line.append(str("\t\t\t"))

                    # type_labels = tg.tierDict["type"].entryList
                    # for type_label in type_labels:
                    #     type_start, type_stop, type_text = type_label
                    #     if stress_start >= type_start and stress_stop <= type_stop:
                    #         result_line.append(type_text)
                    #         result_line.append(str(type_start))
                    #         result_line.append(str(type_stop))

                    

                    # am_labels = tg.tierDict["AM"].entryList
                    # for am_label in am_labels:
                    #     am_start, am_stop, am_text = am_label
                    #     if stress_start >= am_start and stress_stop <= am_stop:
                    #         result_line.append(am_text)
                            # result_line.append(str(am_start))
                            # result_line.append(str(am_stop))
                            # result_line.append(str(am_stop - am_start))
                            
                    # word_labels = tg.tierDict[tg.tierNameList[1-1]].entryList
                    # analysis_window_label = []
                    # for word_label in word_labels:
                    #     word_start, word_stop, word_text = word_label

                    #     if word_start >= am_start and word_stop <= am_stop:
                    #         analysis_window_label.append(word_text)
                    #         result_line.append(' '.join(analysis_window_label))

                    # initial_labels = tg.tierDict["initial"].entryList
                    # for initial_label in initial_labels:
                    #     initial_start, initial_stop, initial_text = initial_label
                    #     if stress_start >= initial_start and stress_stop <= initial_stop:
                    #         result_line.append(initial_text)


                    final_labels = tg.tierDict["final"].entryList
                    for final_label in final_labels:
                        final_start, final_stop, final_text = final_label
                        if stress_start >= final_start and stress_stop <= final_stop:
                            result_line.append(final_text)


                    results.append('\t'.join(result_line))
        # print('\n'.join(results))

    title_line = "file_name\tstress_label\tfinal\n"
    #title_line = "file_name\tseg_label\tseg_start\tseg_end\tseg_duration\tstress_label\tstress_start\tstress_end\tstress_duration\ttype_label\tanalysis_start\tanalysis_end\tanalysis_label\tam_label\tinitial_label\tfinal_label\n"


    with open(out_file, 'w+', encoding="UTF-8") as f:
        f.write(title_line)
        f.write('\n'.join(results))
        print('Result file is saved.')

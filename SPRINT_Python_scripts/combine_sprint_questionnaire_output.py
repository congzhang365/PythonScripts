# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:51:54 2020

@author: sprin
"""

import os, csv


# please change the two paths accordingly
individual_questionnaires = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Questionnaires/QDEM"
complete_questionnaires = "C:/Users/sprin/SPRINT Dropbox/Academic Research/Production_Pilots/Data_Processed/English/London/Questionnaires" # output will be saved here






##################################

filenames = os.listdir(individual_questionnaires)
filename_dict = {filename.split("_")[0]:[] for filename in filenames}
filename_dict["QDEM_email"] = [] 
for filename in filenames:
    if "email" in filename:
        filename_dict["QDEM_email"].append(filename)
    else:
        filename_dict[filename.split("_")[0]].append(filename)



for questionnaire_type in filename_dict.keys():         #each iteration deals with a different questionnaire type (demographic, exit, autism etc.)
    filenames = filename_dict[questionnaire_type]

    combined_questionnaires = os.path.join(complete_questionnaires,questionnaire_type+"_complete.txt")
    
    if os.path.isfile(combined_questionnaires):         # if there's a pre-existing combined table, its content will be incorporated
        with open(combined_questionnaires) as infile:        
            all_headers,*all_rows = [r for r in csv.reader(infile, delimiter = '\t')]
    else:      
        all_headers, all_rows, nr_of_rows = [],[],0   
    
    complete_dict = dict()   # maps header to column values
    
    for n, header in enumerate(all_headers):           # mapping for pre-existing table
        complete_dict[header] = [row[n] for row in all_rows]
    
    
    for filename in filenames:
    
        with open(os.path.join(individual_questionnaires,filename)) as infile:        
            headers,row = [r for r in csv.reader(infile, delimiter = '\t')][:2]
            
        individual_dict = dict(zip(headers,row))      # maps header to column values for individual files 
        
        all_headers = list(complete_dict.keys())    # headers of the final combined table
        if all_headers:
            nr_of_rows = len(complete_dict[all_headers[0]]) 
     
        for header in headers:              # headers of the individual file
            if header not in all_headers:   # if file introduces a new header which so far cannot be found in the combined table, it's added to the latter
                complete_dict[header] = ["NA"] * nr_of_rows + [individual_dict[header]]
            else:
                complete_dict[header].append(individual_dict[header])
                
        for header in all_headers:         # if combined table has a header which is not included in the individual file, the corresponding value is set to NA
            if header not in individual_dict.keys():
                complete_dict[header].append("NA")
        
    # prepare to save combined table
        
    all_headers = list(complete_dict.keys())
    nr_of_rows = len(complete_dict[all_headers[0]])
    rows = [all_headers]
    for n in range(nr_of_rows):
        row = []
        for header in all_headers:
            row.append(complete_dict[header][n])
        if row not in rows:   # avoids accidental duplicates
            rows.append(row)
        
    with open(combined_questionnaires, 'w',newline='') as outfile:
        writer = csv.writer(outfile,delimiter = "\t")
        writer.writerows(rows) 

     

    
    

import pandas
import numpy as np

'''
This script is to create randomised orders for the dialogues (or other stimuli), without having the same category consecutively.
- input is the your input excel
- 'RAND_criteria' is the column name of the categories (e.g. names, places, and you don't want to have two names consecutively)
- the output is a csv file that contains four randomised orders


Dr. Cong Zhang @SPRINT, University of Kent
'''

input = pandas.read_excel("C:/Users/sprin/Desktop/test/test.xlsx", 'Sheet1')
output = "C:/Users/sprin/Desktop/test/result.csv"

def randomise(input):
    randomized = False
    while not randomized:
        xlist = input.sample(frac=1).reset_index(drop=True) # where df is the original file read in
        # print(xlist)
        # check for repeats
        for i in range(0, len(xlist)):
            # print('Iteration number: %s'%i)
            try:
                if i == len(xlist) - 1:
                    randomized = True
                elif xlist['RAND_criteria'][i] != xlist['RAND_criteria'][i+1]:
                    continue
                elif xlist['RAND_criteria'][i] == xlist['RAND_criteria'][i+1]:
                    break
            except IndexError:
                pass
    return xlist

# create the 1st randomised order
rand1 = randomise(input)
rand1_index = []
for i in range(len(rand1.index)):
    rand1_index.append(i)
rand1.insert(3, 'rand1', rand1_index)

# create the 2nd randomised order
rand2 = randomise(rand1)
rand2_index = []
for i in range(len(rand1.index)):
    rand2_index.append(i)
rand2.insert(4, 'rand2', rand2_index)

# create the 3rd randomised order
rand3 = randomise(rand2)
rand3_index = []
for i in range(len(rand1.index)):
    rand3_index.append(i)
rand3.insert(5, 'rand3', rand3_index)

# create the 4th randomised order
rand4 = randomise(rand3)
rand4_index = []
for i in range(len(rand1.index)):
    rand4_index.append(i)
rand4.insert(6, 'rand4', rand4_index)

# view the first few lines of the dataframe
print(rand4.head())
## print(input.sort_values(by='index')) # sort values by the column 'index'

# write all results to the output file
rand4.to_csv("%s"%output)

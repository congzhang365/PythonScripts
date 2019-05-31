import itertools
import string


def combine_lists(iterables, sep, output_file):
    combinations = []
    for t in itertools.product(*iterables):
        combinations.append(sep.join(t))
    result = '\n'.join(combinations)
    print('There are', len(combinations), 'combinations in total.')
    with open('%s.txt'%output_file, 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == "__main__":
    tar_loc = ['start', 'mid', 'end']
    tar_len = ['l1', 'l2', 'l3']
    tar_char = ['A1', 'B4', 'C4', 'C1', 'D4', 'E4', 'F2', 'G4', 'H2', 'I4', 'I1', 'J4', 'J0', 'K4', 'K1', 'L2', 'M2',
               'N1', 'O1', 'P4', 'Q4', 'Q1', 'R4', 'S2', 'T4', 'U1', 'V1', 'W2', 'X2', 'Y4', 'Z4', 'P1', 'W1', 'J1']
    all_char = list(string.ascii_uppercase)
    all_num = list(string.digits)
    all_num.append('10')

	bi_list=[all_char,all_char]
	bi_char = combine_lists(bi_list, '', 'bi_char')

	# tri_list = [all_char,all_char,all_char]
	# tri_char = combine_lists(tri_list, '', 'tri_char')

	num_char_list = [all_char, all_num,all_char]
	num_char = combine_lists(num_char_list,'','num_char')
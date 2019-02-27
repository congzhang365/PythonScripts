import re
with open('D:\Rokid\pycharm\English/new.txt','r', encoding='utf-8') as f:
    lines = f.readlines()

    hash_fours = []
    for i in range(len(lines)):
        if i % 2 == 0:
            tag_split = re.compile("(#4)").split(lines[i])
            a = [x for x in lines[i] if lines[i]]

### 没写完

            if len(re.search(r"(#4)"),lines[i]) >= 2:
                print(lines[i])

            # print(tags)
#             for j in range(len(tag_split)):
#                 if tag_split[j] == '#4':
#                     result = 'In sentence "'+ lines[i].strip('\n') + '", "' + tag_split[j-1] + '" was labelled as #4.\n'
#                     hash_fours.append(result)
#
#
#
# with open('hash4hash.txt', 'w', encoding='utf-8') as file:
#     file.write(''.join(hash_fours))
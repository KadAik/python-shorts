"""
Count letters occurences in an input file.
Letters are treated case insensitivly
"""

from os import strerror

chars_map = {}

def letters_freq(file):
    try:
        with open(file, mode='rt', encoding='ascii') as file_stream:
            char = file_stream.read(1)
            while char != '':
                if char.isspace():
                    char = file_stream.read(1)
                    continue
                if not char in chars_map:
                    chars_map[char] = 1
                else:
                    chars_map[char] +=1
                char = file_stream.read(1)
        return chars_map

    except IOError as e:
        print("An error occured :", strerror(e.errno))
            
result = letters_freq('c:/users/rodol/desktop/text.txt')

def output_sorter(data_dict):
    data_list = []
    for key, val in data_dict.items():
        data_list.append((key, val))
    # sorting
    sorted_list = sorted(data_list, key=lambda x: x[1], reverse=True)
    
    return sorted_list

sorted_result = output_sorter(result)

for elmt in sorted_result:
    print(elmt[0], '->', elmt[1])

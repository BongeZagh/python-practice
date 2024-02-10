#coding:utf8
import sys
import pandas as pd

# create a new dict
dict_data = {}

# delete adjacent duplicates
def del_adjacent(alist):
    for i in range(len(alist) - 1, 0, -1):
        if alist[i] == alist[i-1]:
            del alist[i]

# syntax
symb1 = '-'
symb2 = '::'

# open an md file
with open(sys.argv[1], 'r') as file:
    current_data = {}
    for line in file:
        if symb1 in line.strip()[:2]:
            if current_data.get('title'):
                dict_data.setdefault('title', []).append(current_data['title'])
                for key, value in current_data.items():
                    if key != 'title':
                        dict_data.setdefault(key, []).append(value)
            current_data = {}
            if 'query' in line or '.csv' in line:
                continue
            elif line.strip()[2:].count('\n') == len(line.strip()[2:]):
                continue
            else:
                current_data['title'] = line.strip()[2:].strip(" #]\n").replace('[', '')
        elif symb2 in line:
            if 'query' in line or '.csv' in line:
                continue
            else:
                for kv in [line.strip().split('::')]:
                    if len(kv) != 1:
                        current_data.setdefault(kv[0], kv[1].strip())
                    else:
                        current_data.setdefault(kv[0], '')
        else:
            continue

    # Add the last set of data
    if current_data.get('title'):
        dict_data.setdefault('title', []).append(current_data['title'])
        for key, value in current_data.items():
            if key != 'title':
                dict_data.setdefault(key, []).append(value)

# Get the keys as a list
columnsname = list(dict_data.keys())

# Create DataFrame object
frame = pd.DataFrame(dict_data, columns=columnsname)

# Output DataFrame to CSV without index
frame.to_csv('./' + sys.argv[2], index=False)


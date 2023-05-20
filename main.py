# This is a sample Python script.
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from os import walk
import csv
import pandas as pd


# def get_data_path(data_path = './train_dataset_Росатом/Anonimized', save_path = './train_dataset_Росатом/Anonimized/final_'):
f = []
for (dirpath, dirnames, filenames) in walk('./train_dataset_Росатом/Anonimized'):
    f.extend(filenames)
    break
# for i in f:
#
#     with open(f'./train_dataset_Росатом/Anonimized/{i}', 'r', encoding='utf-8', errors='ignore') as infile, open(f'./train_dataset_Росатом/Anonimized/final_{i}', 'w', errors='ignore', newline='', encoding='utf-8') as outfile:
#         inputs = csv.reader(infile)
#         output = csv.writer(outfile)
#
#         for row in inputs:
#             output.writerow(row)

# def trash_delete(path = './train_dataset_Росатом/Anonimized/', prefix = 'final'):
#     for i in f:
#         # if 'final' in i:
#         #     os.remove(f'./train_dataset_Росатом/Anonimized/{i}')

competitors_dict = {}

with open('train_dataset_Росатом/Участники_final.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    inputs = csv.reader(infile)
    for index, row in enumerate(inputs):
        # Create file with no header
        if index == 0:
            continue

        competitors_dict.setdefault(row[0], [])


for champ_file in f:
    if 'final_' in champ_file:
        with open(f'./train_dataset_Росатом/Anonimized/{champ_file}', 'r', encoding='utf-8', errors='ignore') as infile:
            inputs = csv.reader(infile)

            for index, row in enumerate(inputs):
                # Create file with no header

                if index > 0:
                    # print(cntr)
                    p = row[fio_in].split('; ')
                    # print(len(p))
                    # print(p)
                    if len(p) == 1 and row[fio_in] != 'XXX':
                        # print(competitors_dict[row[fio_in]])
                        competitors_dict[row[fio_in]].append(row[marks_in].replace('%', '').replace(',', '.'))
                        competitors_dict[row[fio_in]].append('s')
                    elif len(p) > 1:
                        # print(p)
                        for i in p:
                            competitors_dict[i].append((row[marks_in].replace('%', '') if row[marks_in] != '' else row[ed_in]).replace(',', '.'))
                            competitors_dict[i].append('t')
                            competitors_dict[i].append(row[1])
                            competitors_dict[i].append(len(p))
                            # competitors_dict[row[fio_in][i]].append(row[marks_in])
                    # 334, 342

                else:
                    fio_in = row.index('ФИО') if 'ФИО' in row else row.index('ФИО участников')
                    ed_in = row.index('Баллы, ед.')

                    marks_in = row.index(
                        'Баллы, %')

competitors_dict_filt = {k: v for k, v in competitors_dict.items() if v is not None}
# competitors_dict_filt = {k: ''.join(v).replace(',', '.') for k, v in competitors_dict.items() if v is not None}
for key, value in competitors_dict_filt.items():
    print(key, ' : ', value)


a = result = [[key] + value for key, value in competitors_dict_filt.items()]
print(a)
df = pd.DataFrame(a)


df.to_csv('out.csv')







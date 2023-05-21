# This is a sample Python script.
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from os import walk
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import warnings
import numpy as np
warnings.filterwarnings('ignore')

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
                        competitors_dict[row[fio_in]].append(None)
                        competitors_dict[row[fio_in]].append(None)
                        competitors_dict[row[fio_in]].append(rez_exist)
                        if rez_exist:
                            competitors_dict[row[fio_in]].append(row[rez_ind])
                            for i in rez_lst:
                                competitors_dict[row[fio_in]].append(row[i])

                    elif len(p) > 1:
                        # print(p)
                        for i in p:
                            competitors_dict[i].append(float((row[marks_in].replace('%', '') if row[marks_in] != '' else row[ed_in]).replace(',', '.'))/len(p))
                            competitors_dict[i].append('t')
                            competitors_dict[i].append(row[1])
                            competitors_dict[i].append(len(p))
                            competitors_dict[i].append(rez_exist)
                            if rez_exist:
                                competitors_dict[i].append(row[rez_ind])
                                for j in rez_lst:
                                    competitors_dict[i].append(row[j])
                            # competitors_dict[row[fio_in][i]].append(row[marks_in])


                else:
                    fio_in = row.index('ФИО') if 'ФИО' in row else row.index('ФИО участников')
                    ed_in = row.index('Баллы, ед.')
                    marks_in = row.index('Баллы, %')
                    rez_cnt = 1
                    rez_exist = False
                    # print(champ_file)
                    if 'Результат' in row:
                        rez_ind = row.index("Результат")
                        rez_exist = True
                        rez_lst = []
                        for i in range(rez_cnt, 19): #TODO: Заменить 19 на чиселку n - функция
                            if (rez_str := f'Результат.{i}') in row:
                                rez_lst.append(row.index(rez_str))


competitors_dict_filt = {k: v for k, v in competitors_dict.items() if v is not None}
# competitors_dict_filt = {k: ''.join(v).replace(',', '.') for k, v in competitors_dict.items() if v is not None}
# for key, value in competitors_dict_filt.items():
#     print(key, ' : ', value)


a = result = [[key] + value for key, value in competitors_dict_filt.items()]
# print(a)
df = pd.DataFrame(a)
df.columns = ['name', 'summary_rez', 'comp_stat', 'team_name', 'team_memb', 'rez_exist', 'rezult', *[f'rezult_{i}' for i in range(1, 18)]]
# print(df.columns)

# df.to_csv('out.csv')

import pandas as pd
import numpy as np
from pathlib import Path
import math

df2 = pd.read_csv("train_dataset_Росатом/Участники.csv")
#меняем значение в перемнной образование по словарю
# print(df2['Образование'].unique().tolist())
prof_dict = {np.nan: "Информация об образовании не указана", 'Высшее': "Высшее образование без указания уровня", 'бакалавр': "Бакалавриат",
             'высшее': "Высшее образование без указания уровня", 'Основное общее образование': "Основное общее образование",
             'Высшее ': "Высшее образование без указания уровня", 'Среднее профессиональное': "Среднее профессиональное образование",
             'высшее, специалитет': "Специалитет", 'Неоконченное высшее': "Неоконченное высшее образование",
             'Среднее специальное ': "Среднее профессиональное образование", '14.05.02': "Специалитет",
             'Всшее;Среднее специальное': "Среднее профессиональное образование и высшее образование без указания уровня",
             'Студент ': "Получает высшее образование", 'Среднее-специальное': "Среднее профессиональное образование",
             'Высшее;Высшее': "Высшее образование без указания уровня", 'Высшее;Среднее техническое': "Среднее профессиональное образование и высшее образование без указания уровня",
             'Среднее профессиональное;Начальное профессиональное': "Среднее профессиональное образование",
             'ВЫСШЕЕ ТЕХНИЧЕСКОЕ': "Высшее образование без указания уровня", 'Среднее общее': "Среднее общее образование",
             'высшее;высшее': "Высшее образование без указания уровня", 'неоконченное СПО': "Неоконченное среднее профессиональное образование",
             'Полное высшее': "Высшее образование без указания уровня", 'Среднее': "Среднее профессиональное образование",
             'ВЫСШЕЕ': "Высшее образование без указания уровня", 'высшее профессиональное': "Высшее образование без указания уровня",
             'Специальное профессиональное': "Среднее профессиональное образование",
             'Высшее ;Высшее;Среднее специальное ': "Среднее профессиональное образование и высшее образование без указания уровня",
             'Высшее (Бакалавриат)': "Бакалавриат", 'Среднее специальное': "Среднее профессиональное образование",
             'профессиональное': "Среднее профессиональное образование", 'Среднеспециальное ': "Среднее профессиональное образование",
             'Высшее ;Высшее': "Высшее образование", 'Средне-специальное;Высшее': "Среднее профессиональное образование и высшее образование без указания уровня",
             'Высшее (магистр);Высшее (специалист)': "Магистратура и специалитет", 'среднее профессиональное': "Среднее профессиональное образование"}
df2['Образование'] = df2['Образование'].replace(prof_dict)
#конвертируем дату рождения в нужный формат
df2['Дата рождения'] = pd.to_datetime(df2['Дата рождения'][df2['Дата рождения'].notnull()], errors='coerce')
#считаем текущий возраст
df2['Текущий возраст'] = (pd.Timestamp.now() - df2['Дата рождения'][df2['Дата рождения'].notnull()])/np.timedelta64(1, 'Y')
#избавляемся от некорректных данных по возрасту
df2["Текущий возраст"] = df2["Текущий возраст"][df2["Текущий возраст"]>14]
# df_out = pd.read_csv("out.csv", sep=",")
result1 = pd.concat([df2, df], axis=1)
#конвертируем возраст в инт, чтобы округлить его
result1["Текущий возраст"] = result1["Текущий возраст"][result1["Текущий возраст"].notnull()].astype('int')
#рассчитываем количество интервалов для разбиения на интервалы
n = 1 + 3.322*np.log10(result1["Текущий возраст"].count())
n = int(n)
h = (result1["Текущий возраст"].max() - result1["Текущий возраст"].min())/n
x = result1["Текущий возраст"].min()
#создаем интервалы и обозначения для них
bins = []
for i in range(n):
    first = x
    second = x + h
    bins.append(math.ceil(x))
    x = second
bins.append(int(result1["Текущий возраст"].max())+1)
labels = np.arange(1, len(bins))
#добавляем метки интервалов возрастов в датасет
result1["Интервал по возрасту"] = pd.cut(result1["Текущий возраст"], bins=bins,
                        labels=labels, right=False)
#удаляем лишние переменные
#result1.drop(columns=['Unnamed: 0', 'name'], axis=1, inplace=True)
#сохраняем файл
filepath = Path('final2_data2.xlsx')
filepath.parent.mkdir(parents=True, exist_ok=True)
result1.to_excel(filepath)


import re
# df2 = pd.read_excel('final_data.xlsx', index_col=0)
# # print(df2['Начало трудовой деятельности в РОСАТОМ'])
# df2 = df2[pd.to_datetime(df2['Начало трудового стажа'], errors='coerce').notnull()]
# # print(df2)
# # df[(df == 'banana').any(axis=1)]

from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score

# df2 = df2[df2['summary_rez'].notna()]
X = result1[['Текущий возраст', 'summary_rez']]
X = X.dropna()
k = 6  # Number of clusters
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(X_scaled)
print(clusters)
plt.figure(figsize=(10, 5))
scatter = plt.scatter(X['Текущий возраст'], X['summary_rez'], c=clusters, cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Received Points')
plt.title('Clustering based on KMeans')
legend_handles = []
unique_clusters = np.unique(clusters)
# print(unique_clusters)
for cluster_label in unique_clusters:
    if cluster_label == -1:
        legend_label = 'Noise'
        color = scatter.cmap(scatter.norm(cluster_label))
    else:
        legend_label = f'Cluster {cluster_label}'
        color = scatter.cmap(scatter.norm(cluster_label))
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', label=legend_label, markerfacecolor=color, markersize=8))
#
plt.legend(handles=legend_handles, title='Clusters')
plt.colorbar(scatter, label='Cluster')
plt.show()
silhouette = silhouette_score(X_scaled, clusters)
calinski_harabasz = calinski_harabasz_score(X_scaled, clusters)
print(f'KMean sil: {silhouette}')
print(f'KMean cal_h: {calinski_harabasz}')

result1['Cluster'] = pd.Series(clusters)
filepath = Path('cluster_data.xlsx')
filepath.parent.mkdir(parents=True, exist_ok=True)
result1.to_excel(filepath)

X_e = result1[['Текущий возраст', 'summary_rez', 'Образование']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#
# Perform clustering using DBSCAN
eps = 0.5  # Maximum distance between two samples to be considered in the same neighborhood
min_samples = 4  # Minimum number of samples in a neighborhood for a data point to be considered as a core point
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
clusters = dbscan.fit_predict(X)

# Visualize initial and received values
plt.figure(figsize=(10, 5))
scatter = plt.scatter(X['Текущий возраст'], X['summary_rez'], c=clusters, cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Received Points')
plt.title('Clustering based on Age and Received Points (DBSCAN)')
clusters = dbscan.fit_predict(X_scaled)
# num_clusters = len(np.unique(clusters))
legend_handles = []
unique_clusters = np.unique(clusters)
# print(unique_clusters)
for cluster_label in unique_clusters:
    if cluster_label == -1:
        legend_label = 'Noise'
        color = scatter.cmap(scatter.norm(cluster_label))
    else:
        legend_label = f'Cluster {cluster_label}'
        color = scatter.cmap(scatter.norm(cluster_label))
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', label=legend_label, markerfacecolor=color, markersize=8))

plt.legend(handles=legend_handles, title='Clusters')
plt.colorbar(scatter, label='Cluster')
plt.show()

silhouette = silhouette_score(X_scaled, clusters)
calinski_harabasz = calinski_harabasz_score(X_scaled, clusters)
print(f'DBSCAN sil: {silhouette}')
print(f'DBSCAN cal_h: {calinski_harabasz}')


from sklearn.cluster import SpectralClustering
# print(X_scaled)
n_clusters = 6  # Number of clusters
spectral_clustering = SpectralClustering(n_clusters=4, affinity='rbf', gamma=120, random_state=42)
clusters = spectral_clustering.fit_predict(X)

silhouette = silhouette_score(X_scaled, clusters)
calinski_harabasz = calinski_harabasz_score(X_scaled, clusters)
print(f'Stectral sil: {silhouette}')
print(f'Spectral cal_h: {calinski_harabasz}')
plt.figure(figsize=(10, 5))
scatter = plt.scatter(X['Текущий возраст'], X['summary_rez'], c=clusters, cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Received Points')
plt.title('Clustering based on Spectral clustering')
legend_handles = []
unique_clusters = np.unique(clusters)
# print(unique_clusters)
for cluster_label in unique_clusters:
    if cluster_label == -1:
        legend_label = 'Noise'
        color = scatter.cmap(scatter.norm(cluster_label))
    else:
        legend_label = f'Cluster {cluster_label}'
        color = scatter.cmap(scatter.norm(cluster_label))
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', label=legend_label, markerfacecolor=color, markersize=8))
plt.legend(handles=legend_handles, title='Clusters')
plt.colorbar(scatter, label='Cluster')
plt.show()

from sklearn.cluster import OPTICS
plt.figure(figsize=(10, 5))
scatter = plt.scatter(X['Текущий возраст'], X['summary_rez'], c=clusters, cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Received Points')
plt.title('Clustering based on Age and Received Points (DBSCAN)')
clusters = OPTICS(min_samples=2).fit_predict(X)
legend_handles = []
unique_clusters = np.unique(clusters)
# print(unique_clusters)
for cluster_label in unique_clusters:
    if cluster_label == -1:
        legend_label = 'Noise'
        color = scatter.cmap(scatter.norm(cluster_label))
    else:
        legend_label = f'Cluster {cluster_label}'
        color = scatter.cmap(scatter.norm(cluster_label))
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', label=legend_label, markerfacecolor=color, markersize=8))

plt.legend(handles=legend_handles, title='Clusters')
plt.colorbar(scatter, label='Cluster')
plt.show()

silhouette = silhouette_score(X, clusters)
calinski_harabasz = calinski_harabasz_score(X, clusters)
print(f'OPTICS sil: {silhouette}')
print(f'OPTICS cal_h {calinski_harabasz}')

from sklearn.model_selection import GridSearchCV
# param_grid = {
#     'n_clusters': [4, 5, 6, 7],
#     'affinity': ['nearest_neighbors', 'rbf'],
#     'gamma': [5, 100, 0.01, 110, 120, 130]
# }
# best_score = -1
# best_params = {}
# for n_clusters in param_grid['n_clusters']:
#     for affinity in param_grid['affinity']:
#         for gamma in param_grid['gamma']:
#             clustering = SpectralClustering(n_clusters=n_clusters, affinity=affinity, gamma=gamma, random_state=42)
#             labels = clustering.fit_predict(X_scaled)
#             score = silhouette_score(X_scaled, labels)
#
#             if score > best_score:
#                 best_score = score
#                 best_params = {'n_clusters': n_clusters, 'affinity': affinity, 'gamma': gamma}
#
# # Print the best parameters and score
# print("Best Parameters:")
# for key, value in best_params.items():
#     print(f"{key}: {value}")
#
# print(f"Best Silhouette Score: {best_score}")

# Best Parameters:
# n_clusters: 4
# affinity: rbf
# gamma: 120
# Best Silhouette Score: 0.48953773862258354



# param_grid = {
#     'n_clusters': [3, 4, 5, 6],
#     'init': ['k-means++', 'random'],
#     'n_init': [5, 10, 15, 20, 25, 30],
#     'max_iter': [5, 20, 25, 30, 50, 100]
# }
#
# # Perform grid search using Silhouette score
#
#
# best_score = -1
# best_params = {}
#
# # Perform grid search using silhouette score
# for n_clusters in param_grid['n_clusters']:
#     for init in param_grid['init']:
#         for n_init in param_grid['n_init']:
#             for max_iter in param_grid['max_iter']:
#                 kmeans = KMeans(n_clusters=n_clusters, init=init, n_init=n_init, max_iter=max_iter, random_state=0)
#                 labels = kmeans.fit_predict(X_scaled)
#                 score = silhouette_score(X_scaled, labels)
#
#                 if score > best_score:
#                     best_score = score
#                     best_params = {'n_clusters': n_clusters, 'init': init, 'n_init': n_init, 'max_iter': max_iter}
#
# # Print the best parameters and score
# print("Best Parameters:")
# for key, value in best_params.items():
#     print(f"{key}: {value}")
#
# print(f"Best Silhouette Score: {best_score}")

# Best Parameters:
# n_clusters: 3
# init: random
# n_init: 20
# max_iter: 5
# Best Silhouette Score: 0.41777840388158494


result1['Cluster'] = pd.Series(clusters)
filepath = Path('cluster_data.xlsx')
filepath.parent.mkdir(parents=True, exist_ok=True)
result1.to_excel(filepath)



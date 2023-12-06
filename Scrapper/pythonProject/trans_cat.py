import csv
import pandas as pd
import os

hed_str='ID;Aktywny (0 lub 1);Nazwa*;Kategoria nadrzędna;Główna kategoria (0/1);Opis;Meta-tytuł;Słowa kluczowe meta;Opis meta;Przepisany URL;URL zdjęcia;ID / Nazwa sklepu'
headers = hed_str.split(';')
product_id = 1

# if os.path.isfile('categories_1.csv'):
#     os.remove('categories_1.csv')
#     df = pd.DataFrame(columns=headers)
#     df.to_csv('categories_1.csv', index=False, sep=';', encoding='utf-8')
# else:
#     df = pd.DataFrame(columns=headers)
#     df.to_csv('categories_1.csv', index=False, sep=';', encoding='utf-8')
out_csv = 'categories.csv'
out_csv1 = 'produkts_categories_comma.csv'
level1 =[]
level2 =[]
level3 =[]

with open('/home/kist/EB/electronic_business/pythonProject/transformed_PL_ski.csv', 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    out = out_csv1
    for row in reader:
        if row[0] == 'Aktywny (0 lub 1)':
            continue
        if row[2].__contains__('ALL, '):
            continue
        splitted = row[2].split(', ')
        # for item in splitted:
        #     if item == 'Ski':
        #         image = row[46].split(',')
        #         image = image[0]
        #         root = 0
        #         if len(splitted)>1:
        #             for i in range (0, len(splitted)-1, 1):
        #                 splitted[i+1]=splitted[i+1]+f'({splitted[i]})'
        #         row[2] = splitted[len(splitted)-1]
        #         if len(splitted) == 1:
        #             level1.append(splitted[0])
        #         elif len(splitted) == 2:
        #             level1.append(splitted[0])
        #             level2.append(splitted[1])
        #         elif len(splitted) == 3:
        #             level1.append(splitted[0])
        #             level2.append(splitted[1])
        #             level3.append(splitted[2])
        #         level1 = set(level1)
        #         level2 = set(level2)
        #         level3 = set(level3)
        #         level1 = list(level1)
        #         level2 = list(level2)
        #         level3 = list(level3)
        #         continue
        image = row[46].split(',')
        image = image[0]
        root = 0
        if len(splitted)>1:
            for i in range (0, len(splitted)-1, 1):
                splitted[i+1]=splitted[i+1]+f'({splitted[i]})'
        row[2] = splitted[len(splitted)-1]
        if len(splitted) == 1:
            level1.append(splitted[0])
        elif len(splitted) == 2:
            level1.append(splitted[0])
            level2.append(splitted[1])
        elif len(splitted) == 3:
            level1.append(splitted[0])
            level2.append(splitted[1])
            level3.append(splitted[2])
        level1.append('Ski')
        level1 = set(level1)
        level2 = set(level2)
        level3 = set(level3)
        level1 = list(level1)
        level2 = list(level2)
        level3 = list(level3)
levels= [level1, level2, level3]
for level in levels:
    for category in level:
        if category == '':
            continue
        if level == level1:
            parent = ''

        elif level == level2:
            parent = category.split('(')
            parent = parent[len(parent)-1].split(')')
            parent = parent[0]
            category = category.split('(')
            category[1] = category[1].split(')')[0]
            category = category[1]+'-'+category[0]
        elif level == level3:
            parent = category.split('(')
            parent = parent[1]+f'({parent[2]}'
            parent = parent.split(')')
            parent = parent[0]+')'
            parent = parent.split('(')
            parent = parent[len(parent)-1].split(')')[0]+'-'+parent[0]
            category = category.split('(')
            category[2] = category[2].split('))')[0]
            category = category[2]+'-'+category[1]+'-'+category[0]
        category = category.replace('(', '-')
        category = category.replace('))', '-')
        category = category.replace(')','-')
        if category[len(category) - 1] == '-':
            category = category[:len(category)-1]
        parent = parent.replace('(', '-')
        parent = parent.replace('))', '-')
        parent = parent.replace(')','-')
        if len(parent) > 1 and parent[len(parent) - 1] == '-':
            parent = parent[:len(parent)-1]
        category_data = {
            'ID': '',
            'Aktywny (0 lub 1)': 1,
            'Nazwa*': category,
            'Kategoria nadrzędna': parent,
            'Główna kategoria (0/1)': 0,
            'Opis': '',
            'Meta-tutył': '',
            'Słowa kluczowe meta': '',
            'Opis meta': '',
            'Przepisany URL': 'category-url',
            'URL zdjęcia': '',
            'ID / Nazwa sklepu': ''
        }

        with open(out, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=category_data.keys(), delimiter=';')

            # Check if the file is empty and write the headers if needed
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(category_data)

# usuwanie duplikatów
df = pd.read_csv('categories_1.csv', sep=';')
df.drop_duplicates(subset=['Nazwa*'], keep='first', inplace=True)
df.to_csv('categories_1.csv', index=False, sep=';', encoding='utf-8')
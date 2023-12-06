import csv
import pandas as pd
import os

hed_str = 'ID;Aktywny (0 lub 1);Nazwa*;Kategoria nadrzędna;Główna kategoria (0/1);Opis;Meta-tytuł;Słowa kluczowe meta;Opis meta;Przepisany URL;URL zdjęcia;ID / Nazwa sklepu'
headers = hed_str.split(';')
product_id = 1

# if os.path.isfile('trans+cat.csv'):
#     os.remove('trans+cat.csv')
#     df = pd.DataFrame(columns=headers)
#     df.to_csv('trans+cat.csv', index=False, sep=';', encoding='utf-8')
# else:
#     df = pd.DataFrame(columns=headers)
#     df.to_csv('trans+cat.csv', index=False, sep=';', encoding='utf-8')
out_csv = 'produkty.csv'
out_csv1 = 'categories_1.csv'
level1 =[]
level2 =[]
level3 =[]
count=0

with open('/home/kist/EB/electronic_business/pythonProject/transformed_PL_ski.csv', 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    out = out_csv
    with open(out, 'w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=';')
        for row in reader:
            count+=1
            if row[0] == 'Aktywny (0 lub 1)':
                continue
            if row[2].__contains__('ALL, '):
                continue
            if row[1].__contains__('<') or row[1].__contains__('>'):
                continue
            splitted = row[2].split(', ')
            splitted[len(splitted)-1] = splitted[len(splitted)-1].split(')')[0]
            image = row[46].split(',')
            image = image[0]
            root = 0
            if len(splitted) == 2:
                row[2]=splitted[0]+'-'+splitted[len(splitted)-1]
            elif len(splitted) == 3:
                row[2]=splitted[0]+'-'+splitted[1]+'-'+splitted[2]
            elif len(splitted)==1:
                row[2]=splitted[0]
            else:
                continue
            # if len(splitted) > 1:
            #     for i in range(0, len(splitted) - 1, 1):
            #         splitted[i + 1] = splitted[i + 1] + f'-{splitted[i]}'
            # else :
            #     row[2]=row[2]
            # if splitted[len(splitted)-1] != '':
            #     row[2]=splitted[len(splitted)-1]
            if count %3 ==0:
                row[22]= 60
            else:
                row[22]= 5
            
            # Write the modified row back to the output file
            writer.writerow(row)

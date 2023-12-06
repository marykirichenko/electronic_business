import csv
import pandas as pd
import os

hed_str = 'Aktywny (0 lub 1);Nazwa*;Kategorie (x,y,z...);Cena bez podatku. (netto);ID reguły podatku;Cena zawiera podatek. (brutto);W sprzedaży (0 lub 1);Wartość rabatu;Procent rabatu;Rabat od dnia (rrrr-mm-dd);Rabat do dnia (rrrr-mm-dd);Indeks #;Kod dostawcy;Dostawca;Marka;kod EAN13;Kod kreskowy UPC;MPN;Podatek ekologiczny;Szerokość;Wysokość;Głębokość;Waga;Czas dostawy produktów dostępnych w magazynie:;Czas dostawy wyprzedanych produktów z możliwością rezerwacji:;Ilość;Minimalna ilość;Niski poziom produktów w magazynie;Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu;Widoczność;Dodatkowe koszty przesyłki;Jednostka dla ceny za jednostkę;Cena za jednostkę;Podsumowanie;Opis;Tagi (x,y,z...);Meta-tytuł;Słowa kluczowe meta;Opis meta;Przepisany URL;Etykieta, gdy w magazynie;Etykieta kiedy dozwolone ponowne zamówienie;Dostępne do zamówienia (0 = Nie, 1 = Tak);Data dostępności produktu;Data wytworzenia produktu;Pokaż cenę (0 = Nie, 1 = Tak);Adresy URL zdjęcia (x,y,z...);Tekst alternatywny dla zdjęć (x,y,z...);Usuń istniejące zdjęcia (0 = Nie, 1 = Tak);Cecha(Nazwa:Wartość:Pozycja:Indywidualne);Dostępne tylko online (0 = Nie, 1 = Tak);Stan:;Konfigurowalny (0 = Nie, 1 = Tak);Można wgrywać pliki (0 = Nie, 1 = Tak);Pola tekstowe (0 = Nie, 1 = Tak);Akcja kiedy brak na stanie;Wirtualny produkt (0 = No, 1 = Yes);Adres URL pliku;Ilość dozwolonych pobrań;Data wygaśnięcia (rrrr-mm-dd);Liczba dni;ID / Nazwa sklepu;Zaawansowane zarządzanie magazynem;Zależny od stanu magazynowego;Magazyn;Akcesoria (x,y,z...)'
headers = hed_str.split(';')
product_id = 1

if os.path.isfile('transformed_PL_ski.csv'):
    os.remove('transformed_PL_ski.csv')
    df = pd.DataFrame(columns=headers)
    df.to_csv('transformed_PL_ski.csv', index=False, sep=';', encoding='utf-8')
else:
    df = pd.DataFrame(columns=headers)
    df.to_csv('transformed_PL_ski.csv', index=False, sep=';', encoding='utf-8')
out_csv = 'transformed_PL_ski.csv'
out_csv1 = 'transformed_PL_1_ski.csv'
out_csv2 = 'transformedPL_PL_2_ski.csv'

with open('/home/kist/EB/electronic_business/pythonProject/balenciaga.csv', 'r', encoding='latin-1') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    out = out_csv
    for row in reader:
        if row[0] == 'Enabled':
            continue
        # if row[2] != 'Skiwear Collection':
        #     continue
        if row[2]. __contains__('ALL, '):
            continue
        if row[2].__contains__('Ski'):
            row[2]='Ski'
        category = row[2].split(', ')
        product_data = {
            'Aktywny (0/1)': 1,
            'Nazwa *': row[1],
            'Kategorie (x,y,z...)': row[2],
            'Cena bez podatku. (netto)': str(float(row[3].replace(' ',''))*4.46*0.77),
            'ID reguły podatku': 1,
            'Cena zawiera podatek. (brutto)': str(float(row[3].replace(' ',''))*4.46),
            #'Koszt własny': '',
            'W sprzedaży (0 lub 1)': 1,
            'Wartość rabatu': '',
            'Procent rabatu': '',
            'Rabat od dnia (yyyy-mm-dd)': '',
            'Rabat do dnia (yyyy-mm-dd)': '',
            'Indeks #': str(row[13]),
            'Kod dostawcy': 'RP-demo_'+str(product_id),
            'Dostawca': 'Balenciaga store',
            'Marka': 'Balenciaga',
            'kod EAN13': 1234567890123,
            'Kod kreskowy UPC': '',
            'MPN': '',
            'Podatek ekologiczny': '',
            'Szerokość': '',
            'Wysokość': '',
            'Głębokość': '',
            'Waga': '',
            'Czas dostawy produktów dostępnych w magazynie': '',
            'Czas dostawy wyprzedanych produktów z możliwością rezerwacji': '',
            'Ilość': 20,
            'Minimalna ilość': 1,
            'Niski poziom produktów w magazynie': '',
            'Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu': 0,
            'Widoczność': 'both',
            'Dodatkowe koszty przesyłki': '',
            'Jednostka dla ceny za jednostkę': '',
            'Cena za jednostkę': '',
            'Podsumowanie': '<p>'+row[10]+'<p>',
            'Opis': '<p>'+row[11]+'<p>',
            'Tagi (x,y,z...)': row[2],
            'Meta-tytuł': '',#'Meta title-'+row[1],
            'Słowa kluczowe meta': '',#'Meta keywords-'+row[1],
            'Opis meta': '',
            'Przepisany URL': row[1].replace(" ","-").lower(),
            'Etykieta, gdy w magazynie': 'W magazynie',
            'Etykieta kiedy dozwolone ponowne zamówienie': '',
            'Dostępne do zamówienia (0 = Nie, 1 = Tak)': 1,
            'Data dostępności produktu': '',
            'Data wytworzenia produktu': '',
            'Pokaż cenę (0 = Nie, 1 = Tak)': 1,
            'Adresy URL zdjęcia (x,y,z...)': row[12],
            'Tekst alternatywny dla zdjęć (x,y,z...)': 'image',
            'Usuń istniejące zdjęcia (0 = Nie, 1 = Tak)': 0,
            'Cecha(Nazwa:Wartość:Pozycja:Indywidualne)': '',
            'Dostępne tylko online (0 = Nie, 1 = Tak)': 1,
            'Stan:': 'new',
            'Konfigurowalny (0 = Nie, 1 = Tak)': 0,
            'Można wgrywać pliki (0 = Nie, 1 = Tak)': 0,
            'Pola tekstowe (0 = Nie, 1 = Tak)': 0,
            'Akcja kiedy brak na stanie': 0,
            'Produkt wirtualny (0 = Nie, 1 = Tak)': 0,
            'Adres URL pliku': '',
            'Liczba dozwolonych pobrań': '',
            'Data wygaśnięcia (rrrr-mm-dd)': '',
            'Liczba dni': '',
            'ID / Nazwa sklepu': 0,
            'Zaawansowane zarządzanie magazynem': 0,
            'Zależny od stanu magazynowego': 0,
            'Magazyn': 0,
            'Akcesoria (x,y,z...)': '',
        }

        with open(out, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=product_data.keys(), delimiter=';')

            # Check if the file is empty and write the headers if needed
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(product_data)
        product_id += 1
        # if product_id == 2244 and out == out_csv:
        #     product_id = 1
        #     out = out_csv1
        # if product_id == 2244 and out == out_csv1:
        #     product_id = 1
        #     out = out_csv2

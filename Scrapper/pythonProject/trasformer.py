#Product ID;Active (0/1);Name *; Categories (x,y,z...);Price tax excluded;Tax rules ID;Wholesale price;On sale (0/1);Discount amount;Discount percent;Discount from (yyyy-mm-dd);Discount to (yyyy-mm-dd);Reference #;Supplier reference #;Supplier;Manufacturer;EAN13;    UPC;Ecotax;  Width;Height;Depth;Weight;Delivery time of in-stock products;Delivery time of out-of-stock products with allowed orders;Quantity;Minimal quantity;Low stock level;Send me an email when the quantity is under this level;Visibility;Additional shipping cost;Unity;Unit price;Summary;Description;Tags (x,y,z...);Meta title;Meta keywords;Meta description;URL rewritten;Text when in stock;Text when backorder allowed;Available for order (0 = No, 1 = Yes);Product available date;Product creation date;Show price (0 = No, 1 = Yes);Image URLs (x,y,z...);Image alt texts (x,y,z...);Delete existing images (0 = No, 1 = Yes);Feature(Name:Value:Position);Available online only (0 = No, 1 = Yes);Condition;Customizable (0 = No, 1 = Yes);Uploadable files (0 = No, 1 = Yes);Text fields (0 = No, 1 = Yes);Out of stock action;Virtual product;File URL;Number of allowed downloads;Expiration date;Number of days;ID / Name of shop;Advanced stock management;Depends On Stock;Warehouse;Acessories  (x,y,z...)
#   1;           1;   iPod Nano;       iPods;                 100;             1;            80;           1;                 ;            5.5;             2013-06-01;           2018-12-31;              RP-demo_1;      RF-demo_1;     Applestore; Apple; 1234567890123;    ;1;0.6;0.2;0.4;0.068357;;;160;1;0;0;;;;;<p>New design.</p>;<p>New design.</p>;apple, ipod, nano;Meta title-Nano;Meta keywords-Nano;Meta description-Nano;iPod-Nano;In Stock;Current supply. Ordering availlable;1;2013-03-01;2013-01-01;1;http://localhost/prestashop/img/p/1/5/15.jpg,http://localhost/prestashop/img/p/2/3/23.jpg;First alt text,Second alt text;0;;0;new;0;0;0;0;0;;;;;0;0;0;0;
import csv
import pandas as pd
import os


hed_str = 'Product ID;Active (0/1);Name *;Categories (x,y,z...);Price tax excluded;Tax rules ID;Wholesale price;On sale (0/1);Discount amount;Discount percent;Discount from (yyyy-mm-dd);Discount to (yyyy-mm-dd);Reference #;Supplier reference #;Supplier;Manufacturer;EAN13;UPC;Ecotax;Width;Height;Depth;Weight;Delivery time of in-stock products;Delivery time of out-of-stock products with allowed orders;Quantity;Minimal quantity;Low stock level;Send me an email when the quantity is under this level;Visibility;Additional shipping cost;Unity;Unit price;Summary;Description;Tags (x,y,z...);Meta title;Meta keywords;Meta description;URL rewritten;Text when in stock;Text when backorder allowed;Available for order (0 = No, 1 = Yes);Product available date;Product creation date;Show price (0 = No, 1 = Yes);Image URLs (x,y,z...);Image alt texts (x,y,z...);Delete existing images (0 = No, 1 = Yes);Feature(Name:Value:Position);Available online only (0 = No, 1 = Yes);Condition;Customizable (0 = No, 1 = Yes);Uploadable files (0 = No, 1 = Yes);Text fields (0 = No, 1 = Yes);Out of stock action;Virtual product;File URL;Number of allowed downloads;Expiration date;Number of days;ID / Name of shop;Advanced stock management;Depends On Stock;Warehouse;Acessories  (x,y,z...)'
headers = hed_str.split(';')
product_id = 1

if os.path.isfile('transformed.csv'):
    os.remove('transformed.csv')
    df = pd.DataFrame(columns=headers)
    df.to_csv('transformed.csv', index=False, sep=';', encoding='utf-8')
else:
    df = pd.DataFrame(columns=headers)
    df.to_csv('transformed.csv', index=False, sep=';', encoding='utf-8')
out_csv = 'transformed.csv'

with open('balenciaga.csv', 'r') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    for row in reader:
        if row[0] == 'Enabled':
            continue
        product_data = {
            'Product ID': product_id,
            'Active (0/1)': 1,
            'Name *': row[1],
            'Categories (x,y,z...)': row[2],
            'Price tax excluded': str(float(row[3].replace(' ',''))*4.46),
            'Tax rules ID': 1,
            'Wholesale price': str(float(row[3].replace(' ',''))*4.46),
            'On sale (0/1)': 1,
            'Discount amount': '',
            'Discount percent': '',
            'Discount from (yyyy-mm-dd)': '',
            'Discount to (yyyy-mm-dd)': '',
            'Reference #': '',
            'Supplier reference #': '',
            'Supplier': 'Balenciaga store',
            'Manufacturer': 'Balenciaga',
            'EAN13': '',
            'UPC': '',
            'Ecotax': '',
            'Width': '',
            'Height': '',
            'Depth': '',
            'Weight': '',
            'Delivery time of in-stock products': '',
            'Delivery time of out-of-stock products with allowed orders': '',
            'Quantity': '',
            'Minimal quantity': '',
            'Low stock level': '',
            'Send me an email when the quantity is under this level': '',
            'Visibility': '',
            'Additional shipping cost': '',
            'Unity': '',
            'Unit price': '',
            'Summary': row[10],
            'Description': row[11],
            'Tags (x,y,z...)': '',
            'Meta title': '',
            'Meta keywords': '',
            'Meta description': '',
            'URL rewritten': '',
            'Text when in stock': '',
            'Text when backorder allowed': '',
            'Available for order (0 = No, 1 = Yes)': 1,
            'Product available date': '',
            'Product creation date': '',
            'Show price (0 = No, 1 = Yes)': 1,
            'Image URLs (x,y,z...)': row[12],
            'Image alt texts (x,y,z...)': '',
            'Delete existing images (0 = No, 1 = Yes)': 0,
            'Feature(Name:Value:Position)': '',
            'Available online only (0 = No, 1 = Yes)': 1,
            'Condition': '',
            'Customizable (0 = No, 1 = Yes)': 0,
            'Uploadable files (0 = No, 1 = Yes)': 0,
            'Text fields (0 = No, 1 = Yes)': 0,
            'Out of stock action': '',
            'Virtual product': '',
            'File URL': '',
            'Number of allowed downloads': '',
            'Expiration date': '',
            'Number of days': '',
            'ID / Name of shop': 'Balenciaga',
            'Advanced stock management': '',
            'Depends On Stock': '',
            'Warehouse': '',
            'Acessories  (x,y,z...)': '',
        }
        with open(out_csv, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=product_data.keys(), delimiter=';')

            # Check if the file is empty and write the headers if needed
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(product_data)
        product_id += 1

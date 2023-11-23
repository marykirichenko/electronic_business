from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import time
import re
import csv
import os.path

url = 'https://www.balenciaga.com/en-pl'

data = []
errors=0
headers = ["Enabled", "Name", "Categories", "Price", "Tax rule ID", "Buying price", "On sale", "Reference", "Weight", "Quantity", "Short desc.", "Long desc", "Images URL", "ID", "Properties"]
if os.path.isfile('balenciaga.csv'):
    os.remove('balenciaga.csv')
    df = pd.DataFrame(columns=headers)
    df.to_csv('balenciaga.csv', index=False, sep=';', encoding='utf-8')
else:
    df = pd.DataFrame(columns=headers)
    df.to_csv('balenciaga.csv', index=False, sep=';', encoding='utf-8')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = []

other_links = []

for i in range(4):
    if i == 0:
        sex = 'women'
    elif i == 1:
        sex = 'men'
    elif i == 2:
        sex = 'gifts'
    else:
        sex = 'new-arrivals'
    tmp = (soup.find('div', class_='l-site page').find('header').find('div').find('div', class_='l-header')
                   .find('div', class_='l-header__mainnav').find('div').find('nav').find('div').find('div',
                    class_='c-nav__scroller').find('ul').find('li', attrs={"data-cgid": f"{sex}"}).find('div').find('ul')
                   .find_all('li', attrs={"data-level2": "true"}))
    for link in tmp:
        other_links.append(link)

for other_link in other_links:
    link = 'https://www.balenciaga.com' + other_link.find('a').get('href')
    if link.__contains__('/view-all'):
        continue
    links.append(link)

for link in links:
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        products_categories = (soup.find('div', class_='l-plp').find('div').find('ul', class_='c-tabsnavcarousel__wrapper')
                               .find_all('li', class_='c-tabsnavcarousel__item'))
    except AttributeError:
        continue
    except requests.exceptions.ConnectionError:
        continue
    except Exception as e:
        print(e)
        continue
    for category_link in products_categories:
        if str(category_link.find('a').get('href')).__contains__('https://www.balenciaga.com'):
            link = category_link.find('a').get('href')
        else:
            link = 'https://www.balenciaga.com' + category_link.find('a').get('href')
        link_previous = ''
        if link == link_previous:
            continue
        link_previous = link
        if ('https://www.balenciaga.com/en-pl/searchcontent?fdid=evenings-dresses' == category_link.find('a').get('href') or
                'https://couture.balenciaga.com/en/' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/explore' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/women/ready-to-wear/view-all' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/women/shoes/view-all-2' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/women/bags/view-all' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/women/small-leather-goods/view-all' == category_link.find('a').get('href')or
                'https://www.balenciaga.com/en-pl/women/accessories/view-all' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/men/ready-to-wear/view-all' == category_link.find('a').get(
                    'href') or
                'https://www.balenciaga.com/en-pl/men/shoes/view-all-2' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/men/bags/view-all' == category_link.find('a').get('href') or
                'https://www.balenciaga.com/en-pl/men/small-leather-goods/view-all' == category_link.find('a').get(
                    'href') or
                'https://www.balenciaga.com/en-pl/men/accessories/view-all' == category_link.find('a').get('href')):
            continue
        if link.__contains__('/view-all'):
            continue
        else:
            print("MAin link - entry:  " + link)
            try:
                driver = webdriver.Chrome()
                driver.get(link)
                    # time.sleep(3)
                pr_height = driver.execute_script('return document.body.scrollHeight')
                while True:
                    driver.execute_script('window.scrollTo(0  , document.body.scrollHeight);')
                    time.sleep(3)
                    new_height = driver.execute_script('return document.body.scrollHeight')
                    if new_height == pr_height:
                        break
                    pr_height = new_height
                    response = driver.page_source
                    soup = BeautifulSoup(response, 'html.parser')
                    elements = (soup.find('div', class_='c-toggleview').find('div').find('div', class_='l-productgrid')
                            .find('div', class_='l-productgrid__wrapper').find('ul').find_all('li',
                                                                                              class_='l-productgrid__item'))
            except AttributeError:
                continue
            except Exception as e:
                print(e)
                continue
        elements_links = []
        for element in elements:
            try:
                elements_links.append(element.find('div', class_='c-product__item').find('a').get('href'))
            except AttributeError:
                continue
            except Exception as e:
                print(e)
                continue
        for product_url in elements_links:
            try:
                response = requests.get('https://www.balenciaga.com' + product_url)
                print('SUBlink entry :  https://www.balenciaga.com' + product_url)
                # https://www.balenciaga.com/en-pl/trompe-l-%C5%93il-shirt-oversized-red-699371TNM256167.html
                # TEST : IF LINK ==  https://www.balenciaga.com/en-pl/trompe-l-%C5%93il-shirt-oversized-red-699371TNM256167.html
                # THEN DEBUG
                if 'https://www.balenciaga.com' + product_url == 'https://www.balenciaga.com/en-pl/trompe-l-%C5%93il-shirt-oversized-red-699371TNM256167.html':
                    print('DEBUG')
                productSoup = BeautifulSoup(response.text, 'html.parser')
                #get product images
            except AttributeError:
                continue
            except Exception as e:
                print(e)
                continue
            try:
                images_ul = (
                    productSoup.find('div', class_='l-pdp__content').find('div').find('div', class_='l-pdp__images')
                    .find('div').find('div').find('div').find('ul').find_all('li'))
                #get product categories
                categories = productSoup.find('ol', class_='c-breadcrumbs').find_all('li')
                categories_list = []
                for i in range (0, len(categories)-1):
                    categories_list.append(re.sub(r'\s+', ' ', categories[i].text).strip())
                #get product name
                name = re.sub(r'\s+', ' ', productSoup.find('h1', class_='c-product__name').text).strip()
                #get product price (without currency)
                price = re.sub(r'\s+', ' ', productSoup.find('p', class_='c-price__value--current').text).strip()
                #get short description
                short_description = re.sub(r'\s+', ' ', productSoup.find('p', class_='c-product__longdesc').text).strip()
                #get characteristics
                properties = re.sub(r'\s+', ' ', productSoup.find('div', class_='c-product__detailinfo').text).strip()
                properties += ' ' + re.sub(r'\s+', ' ', productSoup.find('ul', class_='c-product__detailinfo').find('li').text).strip()
                #get id
                product_id = re.sub(r'\s+', ' ', productSoup.find('span', attrs={"data-bind": "styleMaterialColor"}).text).strip()
                #get long description
                long_description = re.sub(r'\s+', ' ', productSoup.find('div', class_='c-accordion__sustainability').text).strip()
                product_data = {
                    "Enabled": 1,
                    "Name": name,
                    "Categories": ", ".join(categories_list),
                    "Price": price[:-2],
                    "Tax rule ID": " ",
                    #price without last 2 characters
                    "Buying price": price[:-2],
                    "On sale": 0,
                    "Reference": " ",
                    "Weight": " ",
                    "Quantity": 0,
                    #short description without dots !!!!!!!!!!!!!!!!!!!!!!!must be changed
                    "Short desc.": short_description,
                    "Long desc": long_description,
                    "Images URL": ", ".join([image.find('button', class_='c-productcarousel__button').find('img').get('data-src') for image in images_ul]),
                    "ID": product_id,
                    "Properties": properties,
                }
                csv_file = "balenciaga.csv"
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=product_data.keys(), delimiter=';')

                    # Check if the file is empty and write the headers if needed
                    if file.tell() == 0:
                        writer.writeheader()

                    writer.writerow(product_data)
                print(product_data)
                print('SubLInk end :   https://www.balenciaga.com' + product_url)
            except AttributeError:
                continue
            except Exception as e:
                print(e)
                continue
            finally:
                errors += 1
                print('ERROR - HANDLED')
                print('SubLInk end :   https://www.balenciaga.com' + product_url)
                time.sleep(3)
                continue

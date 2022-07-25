from uuid import uuid4
from bs4 import BeautifulSoup
from django.utils.text import slugify
import requests

#webscrapping for jumia

#use + instead of - for the search query
def query_slugify(value, seperator='-'):
    return slugify(value).replace('-', seperator)


def jumia_get_product(product):
    """
    argument - a dictionary with a name and brand parameter
    returns a dictionary with name, price , link and img_src parameter
    """

    return {
        'name': 'mockphone',
        'brand': 'generic',
        'price': 'N 9000',
        'link': 'jumia.com/generics+mockphone',
        'img_src': 'generics/jpg',
        'platform_name': 'jumia'
    }
    phones = []
    page = 1
    while page <= 1:
        URL = f"https://www.jumia.com.ng/smartphones/?q={query_slugify(product['name'])}&sort=lowest-price&page={page}"
        response = requests.get(URL)
        parsed_response = BeautifulSoup(response.text,'html.parser')
        for tag in parsed_response.find_all(class_="prd"):
            phones.append(
                {
                    'name': tag.a.find(class_='name').get_text(),
                    'brand': tag.a.get('data-brand'),
                    'price': tag.a.find(class_='prc').get_text(),
                    'link': tag.a.get('href'),
                    'img_src': tag.a.find('img')['data-src'],
                    'platform_name': 'jumia'
                }
            )
        page += 1
    for phone in phones:
        if product['name'].lower() in phone['name'].lower() and product['brand'].lower() in phone['brand'].lower():
            return phone


def jumia_product(product):
    products = []
    product_list = [
        {
            'name': 'infinix hot 11',
            'brand': 'infinix'
        },
        {
            'name': 'infinix hot 12',
            'brand': 'infinix'
        },
        {
            'name': 'samsung galaxy a73',
            'brand': 'samsung'
        },
        {
            'name': 'samsung galaxy s22',
            'brand': 'samsung'
        }
    ]

    for prod in product_list:
       products.append(jumia_get_product(prod))
   


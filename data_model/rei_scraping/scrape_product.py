import requests
from bs4 import BeautifulSoup
import json

def get_product_detail(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    product_selection = soup.find("div", {"class": "product-color-and-size-selection"})

    script = product_selection.find('script')

    script_text = script.text

    products_json = json.loads(script_text)

    size_list = products_json['sizeList'][0]
    size_colors = size_list['colors']

    colors = {item['label'] for item in size_colors}

    product_soup = soup.find("div", {"id": "product-container"})

    vendor = product_soup.find('input', {'name': 'vendor'})['value']

    product_name = product_soup.find('input', {'name': 'product_desc'})['value']
    parsed_name = product_name.split(' - ')[0]
    parsed_name = parsed_name.replace(vendor, '').lstrip()

    product = {'name': parsed_name, 'vendor': vendor, 'colors': colors}
    return product


# url = 'https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
# product_soup = soup.find("div", {"id": "product-container"})
#
# vendor = product_soup.find('input',{'name':'vendor'})['value']
#
# product_name = product_soup.find('input',{'name':'product_desc'})['value']
# parsed_name = product_name.split(' - ')[0]
# parsed_name = parsed_name.replace(vendor, '').lstrip()
#
#
#
# product_selection = soup.find("div", {"class": "product-color-and-size-selection"})


#product-container > div:nth-child(2) > div > div.col-xs-12.col-md-8.product-media-wrapper.apparel-media-wrapper > div.product-title > h1


url = 'https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens'

product = get_product_detail(url)
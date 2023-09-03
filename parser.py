import requests as r
from bs4 import BeautifulSoup as bs
from dict_elements import headers,page_products
import math
import re
import json


def max_page(url,headers):
    req=r.get(url,headers)
    soup = bs(req.content, 'html.parser').select_one("span[class='product-facet__meta-bar-item product-facet__meta-bar-item--count']").text
    product_amount = int(''.join(filter(str.isdigit, soup)))
    max_page = math.ceil(product_amount / page_products)
    return max_page,product_amount

def items_info(url,headers):
    req = r.get(url, headers).text
    soup = bs(req, 'lxml')
    scripts = soup.findAll('script')
    for s in scripts:
        if 'var meta' in s.text:
            script = s.text
            script = script.split('var meta = ')[1]
            script = script.split(';\nfor (var attr in meta)')[0]
            jsonStr = script
            jsonObj = json.loads(jsonStr)
    return jsonObj

def item_parse(url,headers):
    req = r.get(url+'.json', headers).text
    return req


def remove_patterns(input_string):
    patterns = [r'\s*-\s*XS',r'\s*-\s*S',r'\s*-\s*M', r'\s*-\s*O/S', r'\s*-\s*3XL',r'\s*-\s*L',r'\s*-\s*XL',r'\s*-\s*L',r'\s*-\s*XXL']
    for pattern in patterns:
        output_string = re.sub(pattern, '', input_string)
    return output_string
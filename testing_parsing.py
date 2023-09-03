from parser import max_page,items_info,item_parse
from dict_elements import headers
import time
import numpy as np
import json
import datetime
import re


i = 1
info=[]
products_len=1
while products_len > 0:
    print(f'{i}')
    time.sleep(np.random.choice([x / 10 for x in range(7, 22)]))
    buffer=items_info(f"https://www.npeal.com/collections/all?page={i}",headers=headers)
    products_len=len(buffer['products'])
    if products_len==0:
        break
    else:
        info.append(items_info(f"https://www.npeal.com/collections/all?page={i}",headers=headers))
        i += 1

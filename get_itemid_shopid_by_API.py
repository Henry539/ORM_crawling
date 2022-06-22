import time

import requests
import csv
t1=time.time()

from func import *

def extract_use_proxy1(proxy: str,shopid: str):
    try:
        r = requests.get(f"https://shopee.vn/api/v4/recommend/recommend?bundle=shop_page_category_tab_main&item_card=2&limit=30&offset=0&section=shop_page_category_tab_main_sec&shopid={shopid}&sort_type=1&tab_name=popular&upstream=pdp", proxies={'http' : proxy,'https': proxy}, timeout=2)
        return r.json()
    except:
        return False

def extract_use_proxy2(proxy: str,shopid: str,offset: str):
    try:
        r = requests.get(f"https://shopee.vn/api/v4/recommend/recommend?bundle=shop_page_category_tab_main&item_card=2&limit=30&offset={offset}&section=shop_page_category_tab_main_sec&shopid={shopid}&sort_type=1&tab_name=popular&upstream=pdp", proxies={'http' : proxy,'https': proxy}, timeout=2)
        return r.json()
    except:
        return False

def get_item_shop_id1(proxy: str,shopid: str):
    data_itemid_shopid = []

    data = extract_use_proxy1(proxy,shopid)
    if data == False:
        return False
    list_data1 = data["data"]["sections"][0]["index"]
    for item1 in list_data1:
        data_itemid_shopid.append(item1["key"].split(":"))
    return data_itemid_shopid

def get_item_shop_id2(proxy,shopid,offset,count):
    data_itemid_shopid = []

    data = extract_use_proxy2(proxy, shopid, str(offset))
    if count == 3:
        return ["END"]
    if data == False:
        return False
    try:
        list_data2 = data["data"]["sections"][0]["index"]
        for item2 in list_data2:
            da = item2["key"].split(":")
            data_itemid_shopid.append(da)
    except:
        print("RETRY:", count+1)
        return get_item_shop_id2(proxy,shopid,offset,count+1)
    return data_itemid_shopid

def check_proxy1(proxy:str,shopid:str):
    itemid_shopid = get_item_shop_id1(proxy,shopid)
    if itemid_shopid == False:
        return False
    return itemid_shopid

def check_proxy2(proxy:str,shopid:str,offset:int):
    itemid_shopid = get_item_shop_id2(proxy,shopid,offset,0)
    if itemid_shopid == False:
        return False
    return itemid_shopid

def replace_proxy1(list_proxy,shopid, i):
    if i == len(list_proxy):
        return ["CANT CONNECT BY PROXY IN EXTRAC1"]
    result = check_proxy1(list_proxy[i],shopid)
    if result != False:
        print("-----SUCCESS AT REP_PROX_1-----")
        return result
    i+=1
    print(f"FALSE CHECK_1_{i}")
    return replace_proxy1(list_proxy,shopid,i)

def replace_proxy2(list_proxy,shopid, i,offset):
    if i == len(list_proxy):
        return ["CANT CONNECT BY PROXY IN EXTRAC1"]
    result = check_proxy2(list_proxy[i],shopid,offset)
    if result != False:
        print(f"-----SUCCESS AT REP_PROX_2-OFFSET_{offset}-----")
        return result
    i+=1
    print(f"FALSE CHECK_2_{i}")
    return replace_proxy2(list_proxy,shopid,i,offset)


def read_data_txt_1():
    proxy_list = []
    with open('data_proxy.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            proxy_list.append(row[0])
    return proxy_list

def run_2(list_proxy,shopid,shop_name):
    data_list1 = replace_proxy1(list_proxy,shopid,0)
    offset = 0
    data_list2 = []
    while True:
        data_list2_check = replace_proxy2(list_proxy,shopid,0,offset)
        if data_list2_check == ["END"]:
            break
        if data_list2_check != ["CANT CONNECT BY PROXY IN EXTRAC1"]:
            data_list2 += data_list2_check
        offset+=30
    data_list = data_list1 + data_list2

    if data_list != []:
        if check_shopid(shopid=int(shopid)):
            update_shop(shopid=int(shopid),shopname=shop_name)
        for i in data_list:
            if check_itemid(int(i[0])):
                update_shop_item(shopid=int(i[1]),itemid=int(i[0]))

    print("PROCESSING 3 - CRAWLING-SHOPID&ITEMID: DONE!")
    print("---------------------------------")
    return data_list

if __name__ == "__main__":
    result = run_2(read_data_txt_1(),"85729003","one_shop108")
    print("TOTAL:",len(result),"---FINISHED IN:", time.time()-t1)



from get_data_from_database import *
from func import *

import csv
import requests
import random
import time
import concurrent.futures

def re_check_none_data():
    value_database = re_check_data()
    none_list = []
    for value in value_database:
        if value["historical_sold"] == None:
            none = []
            none.append(value["dataid"])
            none.append(value["itemid"])
            none_list.append(none)
    return none_list

def re_update_data():
    list_item_shop_dataid = []
    for dataid in re_check_none_data():
        result = get_all_shop_itemid2(dataid[1])
        result.append(dataid[0])
        list_item_shop_dataid.append(result)
    return list_item_shop_dataid


def read_data_txt_2():
    proxy_list = []
    with open('data_proxy.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            proxy_list.append(row[0])
    return proxy_list

def read_shopee(itemid,shopid,proxy):
    try:
        response = requests.get(f"https://shopee.vn/api/v4/item/get?itemid={itemid}&shopid={shopid}", proxies={'http' : proxy,'https': proxy}, timeout=5)
        data = response.json()
        return data["data"]["historical_sold"]
    except:
        return -1000



def check(itemid,shopid,num,dataid):

    result = read_shopee(itemid, shopid, list_proxy[num])
    if num == (a-1):
        return False
    if result == -1000 and num < (a-1):
        return check(itemid, shopid, num + 1,dataid)
    if result != -1000:
        his_sold = result
        re_update_item_data(dataid, his_sold)
        return True


def main_recheck():
    item_shop_dataid = re_update_data()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(run, item_shop_dataid)


def run(i):
    if check(i[0], i[1], 0,i[2]):
        raise print(f"[RE-UPDATE] --- {i[0]}---{i[1]}")
    update_item_data(i[0], None)
    raise print("NON-PROXY_IP CAN USE!")


if __name__ == "__main__":
    list_proxy = read_data_txt_2()
    a = len(list_proxy)
    main_recheck()
    session.commit()
    # print(re_update_data())
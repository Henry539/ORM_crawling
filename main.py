print("-----------BEGIN-----------")
import random
import time
import concurrent.futures

t = time.time()
from func import *
from get_itemid_shopid_by_SELENIUM import *
from get_itemid_shopid_by_API import *
from get_data_from_database import *
from check_proxy import *
from models import *
from re_check_crawling import main_recheck


Base.metadata.create_all(engine)
import requests
import csv


def read_data_txt_2():
    proxy_list = []
    with open('data.txt', 'r') as f:
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



def check(itemid,shopid,num):

    result = read_shopee(itemid, shopid, list_proxy[num])
    if num == (a-1):
        return False
    if result == -1000 and num < (a-1):
        return check(itemid, shopid, num + 1)
    if result != -1000:
        his_sold = result
        update_item_data(itemid, his_sold)
        return True


def main():
    for shopid in get_all_shops():
        list_shope = get_all_shop_itemid(shopid)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(run, list_shope)


def run(i):
    if check(i[0], i[1], 0):
        raise print(f"UPDATE! --- {i[0]}")
    update_item_data(i[0], None)
    raise print("NON-PROXY_IP CAN USE!")

if __name__ == "__main__":
    list_proxy = read_data_txt_2()
    a = len(list_proxy)

    main_2()

    # result = run_2(read_data_txt_1(),"85729003","one_shop108")
    # print("TOTAL:",len(result),"---FINISHED IN:", time.time()-t1)

    main()

    for i in range(0,4):
        print(f"-----RECHECK_{i}-----")
        main_recheck()

    session.commit()
    print("PROCESSING ALL-DONE IN:", time.time() - t)
    print("-----------END-----------")



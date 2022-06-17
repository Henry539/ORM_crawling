from func import *

Base.metadata.create_all(engine)
import requests
import csv


def read_data_txt():
    proxy_list = []
    with open('data.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            proxy_list.append(row[0])
    return proxy_list

def read_shopee(itemid,shopid,proxy):
    try:
        response = requests.get(f"https://shopee.vn/api/v4/item/get?itemid={itemid}&shopid={shopid}", proxies={'http' : proxy,'https': proxy}, timeout=2)
        data = response.json()
        return data["data"]["historical_sold"]
    except:
        return -1


def update_data(itemid, shopid, historical_sold):
    if check_shopid(shopid):
        update_shop(shopid)
    else:
        print("{messange: shopid exist}")
    if check_itemid(itemid):
        update_shop_item(shopid,itemid)
    else:
        print("{messange: shopid-itemid exist}")
    update_item_data(itemid, int(historical_sold))
    print("update!")

list_shope=[[9805929978,120324880],[16474833352,18796445],[18701518960,120324880],[9256605454,317428602],[10412346716,210089851]]

def check(itemid,shopid,num):
    print(f"{num+1}")
    if num == 9:
        return False
    if read_shopee(itemid, shopid, list_proxy[num]) != -1:
        his_sold = read_shopee(itemid, shopid, list_proxy[num])
        update_data(itemid, shopid, his_sold)
        return True
    return check(itemid,shopid,num+1)

if __name__ == "__main__":
    list_proxy = read_data_txt()
    for i in list_shope:
        if check(i[0],i[1],0):
            continue
        print("NON-PROXY_IP CAN USE!")
        break

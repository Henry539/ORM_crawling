import time

from func import *

import requests

Base.metadata.create_all(engine)

def read_shopee(itemid,shopid):

    proxies = {"http": "36.94.40.123:9812"}

    response = requests.get(f"https://shopee.vn/api/v4/item/get?itemid={itemid}&shopid={shopid}", proxies=proxies)
    data = response.json()
    return data["data"]["historical_sold"]


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

if __name__ == "__main__":
    count = 0
    while True:
        for i in list_shope:
            his_sold = read_shopee(i[0],i[1])
            update_data(i[0],i[1],his_sold)
        count+=1
        if count == 2:
            break
        time.sleep(20)

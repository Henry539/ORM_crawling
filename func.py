import random

from models import *
from database import session, engine
import time
from typing import Optional



def update_shop(shopid: int,shopname: Optional[str] = None):
    shop = Shops(SHOP_ID=shopid,SHOP_NAME=shopname,STATUS=True)
    session.add(shop)
    # session.commit()
    # session.refresh(shop)

def update_shop_item(shopid,itemid):
    shop_item = Items(SHOP_ID=shopid,ITEM_ID=itemid)
    session.add(shop_item)



# time_wait=[0.12,0.012,0.23,0.34,0.45,0.56,0.67,0.7,0.9,1.33,1.1,1.3,0.124,0.02,0.213,0.314,0.415,0.516,0.617,0.718,0.819,1.1,1.11,1.12,0.112,0.12,0.123]
def update_item_data(itemid,historical_sold):
    # time.sleep(random.choice(time_wait))
    seconds = time.time()
    local_time = time.ctime(seconds)
    item_data = Data_Items(TIME=local_time,ITEM_ID=itemid,HISTORICAL_SOLD=historical_sold)
    session.add(item_data)


def re_update_item_data(dataid,historical_sold):
    seconds = time.time()
    local_time = time.ctime(seconds)
    data = session.query(Data_Items).filter(Data_Items.ID__ == dataid).first()
    data.TIME = local_time
    data.HISTORICAL_SOLD = historical_sold
    session.add(data)



def check_shopid(shopid: int):
    data = session.query(Shops).filter(Shops.SHOP_ID == shopid).first()
    if data:
        return False
    return True

def check_itemid(itemid: int):
    data1 = session.query(Items).filter(Items.ITEM_ID == itemid).first()
    if data1:
        return False
    return True

def get_all_shops():
    list_all_shops = []
    data_shops = session.query(Shops).all()
    for shopid in data_shops:
        list_all_shops.append(shopid.SHOP_ID)
    return list_all_shops

def get_all_shop_itemid(shopid):
    list_all_shop_item_id = []
    data_shops = session.query(Items).filter(Items.SHOP_ID == shopid).all()
    for shopid in data_shops:
        li = []
        li.append(shopid.ITEM_ID)
        li.append(shopid.SHOP_ID)
        list_all_shop_item_id.append(li)
    return list_all_shop_item_id

def get_all_shop_itemid2(itemid):
    item_shops = []
    data_shop = session.query(Items).filter(Items.ITEM_ID == itemid).first()
    item_shops.append(data_shop.ITEM_ID)
    item_shops.append(data_shop.SHOP_ID)
    return item_shops



if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    # print(get_all_shop_itemid(193863118))
    # print(get_all_shops())
    print(get_all_shop_itemid2(7660585681))
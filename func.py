from models import *
from database import session, engine
import time
from typing import Optional



def update_shop(shopid: int,shopname: Optional[str] = None):
    shop = Shops(SHOP_ID=shopid,SHOP_NAME=shopname)
    session.add(shop)
    session.commit()
    session.refresh(shop)

def update_shop_item(shopid,itemid):
    shop_item = Items(SHOP_ID=shopid,ITEM_ID=itemid)
    session.add(shop_item)
    session.commit()
    session.refresh(shop_item)

def update_item_data(itemid,historical_sold):
    seconds = time.time()
    local_time = time.ctime(seconds)
    item_data = Data_Items(TIME=local_time,ITEM_ID=itemid,HISTORICAL_SOLD=historical_sold)
    session.add(item_data)
    session.commit()
    session.refresh(item_data)

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

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # update_shop(12,"thanhson")
    # update_shop_item(12,12222)
    update_item_data(12222,1233)
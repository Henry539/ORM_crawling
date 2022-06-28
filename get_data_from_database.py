from database import engine


connection = engine.connect()


def get_data_by_itemid(itemid: int):
    query = f"SELECT ITEM_ID, TIME, HISTORICAL_SOLD FROM DATA_ITEMS WHERE ITEM_ID = {itemid}"
    result = connection.execute(query)
    values = result.fetchall()
    list_data = []
    for i in values:
        dict = {}
        dict["itemid"]= i[0]
        dict["time"]=i[1]
        dict["historical_sold"]=i[2]
        list_data.append(dict)
    return list_data

def get_itemid_shopid(itemid: int):
    query = f"SELECT ITEM_ID, SHOP_ID FROM ITEMS WHERE ITEM_ID = {itemid}"
    result = connection.execute(query)
    values = result.fetchall()
    list_data = []
    for i in values:
        lis = []
        lis.append(i[0])
        lis.append(i[1])
        list_data.append(lis)
    return list_data

def re_check_data():
    query = f"SELECT ID__, TIME, ITEM_ID, HISTORICAL_SOLD FROM DATA_ITEMS"
    result = connection.execute(query)
    values = result.fetchall()
    list_data = []
    for i in values:
        dict = {}
        dict["dataid"]= i[0]
        dict["time"]=i[1]
        dict["itemid"]=i[2]
        dict["historical_sold"]=i[3]
        list_data.append(dict)
    return list_data



# list_data = []
# for i in get_data_by_itemid(9805929978):
#     list_data.append(i["historical_sold"])
#
# print(re_check_data())
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


print(get_data_by_itemid(9805929978))
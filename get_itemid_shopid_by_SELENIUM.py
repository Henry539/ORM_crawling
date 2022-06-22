from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

from func import *

t = time.time()



def slipt_id(url):
    sli = url.split("?")
    sl = sli[0].split(".")
    return sl[-1], sl[-2]



def main_3_1(shop_name):
    cookie = "shopee.pkl"

    s = Service('/usr/bin/chromedriver2')

    # Step 1) Open Chrome
    browser = webdriver.Chrome(service=s)

    # Step 2) Navigate to Facebook
    browser.get("https://shopee.vn/buyer/login")

    cookies = pickle.load(open(f"{cookie}", 'rb'))
    for cookie in cookies:
        browser.add_cookie(cookie)
    list_item_url = []
    for i in range(0, 10):
        try:
            browser.get(f"https://shopee.vn/{shop_name}?page={i}&sortBy=pop")
            element = WebDriverWait(browser, 8).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='shopee-page-controller']"))
            )
            rows = browser.find_elements(By.XPATH, "//a[@data-sqe='link']")

            for row in rows:
                item_url = row.get_attribute("href")
                list_item_url.append(item_url)
        except:
            break
    browser.close()

    list_shop = []
    for url in list_item_url:
        list_id = []
        itemid, shopid = slipt_id(url)
        list_id.append(itemid)
        list_id.append(shopid)
        list_shop.append(list_id)

    # "https://shopee.vn/product/8509024/1160760420"
    print("PRODUCTS:", len(list_shop), " ---", " TIME_RUN_OUT:", time.time() - t)

    if check_shopid(list_shop[0][1]):
        update_shop(list_shop[0][1],shop_name)
    for i in list_shop:
        if check_itemid(i[0]):
            update_shop_item(i[1],i[0])
        continue
    print("PROCESSING 3 - CRAWLING-SHOPID&ITEMID: DONE!")
    print("---------------------------------")

if __name__ == "__main__":

    main_3_1("a.k.s_design")
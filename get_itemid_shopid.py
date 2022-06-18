from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

t = time.time()

s = Service('/usr/bin/chromedriver2')

list_item_url = []
for i in range(0, 10):
    browser = webdriver.Chrome(service=s)
    try:
        browser.get(f"https://shopee.vn/day_nit_doc?page={i}&sortBy=pop")
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='shopee-page-controller']"))
        )
        rows = browser.find_elements(By.XPATH, "//a[@data-sqe='link']")

        for row in rows:
            item_url = row.get_attribute("href")
            list_item_url.append(item_url)
    except:
        break
    finally:
        browser.close()


def slipt_id(url):
    sli = url.split("?")
    sl = sli[0].split(".")
    return sl[-2], sl[-1]


list_shop = []
for url in list_item_url:
    dict_id = {}
    itemid, shopid = slipt_id(url)
    dict_id["itemid"] = itemid
    dict_id["shopid"] = shopid
    list_shop.append(dict_id)

print(list_shop)
print("PRODUCTS:", len(list_shop), " ---", " TIME_RUN_OUT:", time.time() - t)

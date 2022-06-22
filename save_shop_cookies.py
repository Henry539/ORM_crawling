from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import Path
import time
import pickle


base_path = Path(__file__).parent
print(base_path)

s = Service('/usr/bin/chromedriver2')

# Step 1) Open Chrome
browser = webdriver.Chrome(service=s)
#
# Step 2) Navigate to Facebook
browser.get("https://shopee.vn/buyer/login")


time.sleep(30)

pickle.dump(browser.get_cookies(), open("shopee.pkl",'wb'))
browser.close()


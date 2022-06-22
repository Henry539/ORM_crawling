import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path


cookie = "shopee.pkl"

s = Service('/usr/bin/chromedriver2')

# Step 1) Open Chrome
browser = webdriver.Chrome(service=s)

# Step 2) Navigate to Facebook
browser.get("https://shopee.vn/buyer/login")

cookies = pickle.load(open(f"{cookie}",'rb'))
for cookie in cookies:
    browser.add_cookie(cookie)

browser.get("https://shopee.vn/a.k.s_design?page=0&sortBy=pop")
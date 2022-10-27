from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import time
# import Email

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument("--disable-gpu")


def nhce_news():
    url = 'https://newhorizoncollegeofengineering.in/events/'
    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(url)
    print("refreshing webpage...")
    # Wait for webpage to load
    time.sleep(3)

    # new_titles = driver.find_elements(By.CLASS_NAME, "LastUpdatedTitle-module_allTitle_20kmL")

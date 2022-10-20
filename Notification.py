from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import time


def fun():
    comic_list = ["Moebana", "Naruto"]
    history = ["Chapter 16: THE DEWA-NO-KUNI SCHOOL"]

    option = webdriver.ChromeOptions()

    option.add_argument('--headless')
    option.add_argument("--disable-gpu")

    url = 'https://mangaplus.shueisha.co.jp/manga_list/updated'

    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver1.get(url)

    time.sleep(3)

    all_titles = driver1.find_elements(By.CLASS_NAME, "LastUpdatedTitle-module_allTitle_20kmL")

    for titles in all_titles[0:10]:
        title = titles.find_element(By.CLASS_NAME, "LastUpdatedTitle-module_title_3HJEY")
        # print(title.text)
        for comic in comic_list:
            if title.text == comic:
                link = titles.get_attribute("href")
                print(link)
                driver2.get(link)

                time.sleep(3)

                infolist = driver2.find_elements(By.CLASS_NAME, "ChapterListItem-module_title_3Id89")
                info = infolist[-1]
                if info.text == history[0]:
                    print("already read")
                else:
                    print(info.text)
                    history[0] = info.text


fun()

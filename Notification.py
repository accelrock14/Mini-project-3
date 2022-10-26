from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import mysql.connector
import time
import Email

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1@nc310t",
    database="notification"
)

option = webdriver.ChromeOptions()

option.add_argument('--headless')
option.add_argument("--disable-gpu")

my_cursor = mydb.cursor()


def main():
    my_cursor.execute("SELECT * FROM comics")

    comic_list = my_cursor.fetchall()

    url = 'https://mangaplus.shueisha.co.jp/manga_list/updated'

    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    driver.get(url)

    time.sleep(3)

    new_titles = driver.find_elements(By.CLASS_NAME, "LastUpdatedTitle-module_allTitle_20kmL")

    for titles in new_titles[0:5]:
        title = titles.find_element(By.CLASS_NAME, "LastUpdatedTitle-module_title_3HJEY")
        # print(title.text)
        for comic in comic_list:
            if title.text == comic[1]:
                link = titles.get_attribute("href")
                print(link)
                last_read(link, comic)


def last_read(link, comic):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(link)

    time.sleep(3)

    new_chapters = driver.find_elements(By.CLASS_NAME, "ChapterListItem-module_title_3Id89")
    recent_chapter = new_chapters[-1]

    if recent_chapter.text != comic[2]:
        my_cursor.execute("SELECT email_id FROM emails JOIN users ON emails.user_id = users.user_id WHERE "
                          "comic_id = " + str(comic[0]))
        emails = my_cursor.fetchall()

        my_cursor.execute("UPDATE comics SET last_chapter = '" + recent_chapter.text +
                          "' WHERE comic_id = " + str(comic[0]))
        mydb.commit()

        for email in emails:
            print("sending mail to " + email[0])
            print(recent_chapter.text)
            Email.mail(comic[1], recent_chapter.text, link, email[0])
    else:
        print("already read")


main()

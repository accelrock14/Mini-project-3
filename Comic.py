from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import mysql.connector
import time
import Email

# Establish connection with mySQL database
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


def manga_plus():
    # get list of comic titles
    my_cursor.execute("SELECT * FROM comics")
    comic_list = my_cursor.fetchall()

    url = 'https://mangaplus.shueisha.co.jp/manga_list/updated'
    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(url)
    print("refreshing webpage...")
    # Wait for webpage to load
    time.sleep(3)

    # Get titles of comics with new chapters from the website
    new_titles = driver.find_elements(By.CLASS_NAME, "LastUpdatedTitle-module_allTitle_20kmL")

    for titles in new_titles[0:10]:
        title = titles.find_element(By.CLASS_NAME, "LastUpdatedTitle-module_title_3HJEY")
        for comic in comic_list:
            if title.text == comic[1]:
                print("found title match!")
                # getting image and link of the comic
                link = titles.get_attribute("href")
                img = titles.find_element(By.CLASS_NAME, "LastUpdatedTitle-module_image_33lsO")
                src = img.get_attribute("src")
                last_read(link, comic, src)


def last_read(link, comic, src):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(link)

    print("loading the comic page...")
    time.sleep(3)
    # get list of new chapters in comic
    new_chapters = driver.find_elements(By.CLASS_NAME, "ChapterListItem-module_title_3Id89")
    recent_chapter = new_chapters[-1]

    # check if the notification for the new chapter has already been sent
    if recent_chapter.text != comic[2]:
        print("sending mail...")
        my_cursor.execute("SELECT email_id FROM emails JOIN users ON emails.user_id = users.user_id WHERE "
                          "comic_id = " + str(comic[0]))
        emails = my_cursor.fetchall()

        my_cursor.execute("UPDATE comics SET last_chapter = '" + recent_chapter.text +
                          "' WHERE comic_id = " + str(comic[0]))
        mydb.commit()

        print(recent_chapter.text)
        Email.mail(comic[1], recent_chapter.text, link, emails, src)
    else:
        print("already read")


manga_plus()
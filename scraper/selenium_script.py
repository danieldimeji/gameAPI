from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from google_play_scraper import app
import os
import time 
import re
from api.models import *


def getGames(categories):

    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--window-size=1920x1080")
    chromeDriver = os.getcwd() +"\\chromedriver.exe"
    driver1 = webdriver.Chrome(options=chromeOptions, executable_path=chromeDriver)
    driver2 = webdriver.Chrome(options=chromeOptions, executable_path=chromeDriver)

    for category in categories:
        print(category)
        driver1.get(category.category_link)
        print(driver1)
        collectionLinks = driver1.find_elements_by_class_name('U8Ww7d')
        time.sleep(5)
        # Getting games by collections in categories
        for i in collectionLinks:
            print(i)
            collectionLink = str(i.get_attribute("href"))
            driver2.get(collectionLink)
            gameDetailsLinks = driver2.find_elements_by_class_name('poRVub')
            # Getting and saving game details in database
            for i in gameDetailsLinks:
                appId = i.get_attribute("href")[46:]
                gameData = app(appId, lang = 'en', country = 'us')
                # Removing html tags in description
                clean = re.compile('<.*?>')
                description = re.sub(clean, '', gameData['description'])
                # description = gameData['description'].replace("<b>", "")
                # description = description.replace("</b>", "")
                
                Games.objects.get_or_create(
                    title = gameData['title'],
                    category = category,
                    details_link = gameData['url'],
                    app_id = gameData['appId'],
                    image_link = gameData['icon'],
                    description = description,
                    ratings = gameData['ratings'],
                    score = gameData['score'],
                )
                print(f'Saved {gameData["title"]} to db')
                time.sleep(5)

    driver1.close()
    driver2.close()

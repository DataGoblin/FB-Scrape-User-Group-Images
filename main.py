from requests import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
import time
import pandas as pd
import requests

class FacebookGS():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='tools/chromedriver.exe')
        self.driver.set_window_rect(width=100, height=1000)
        self.cookies = json.load(open('cookies.json'))
        self.driver.get('https://www.facebook.com/')

        for cookie in self.cookies:
            self.driver.add_cookie(cookie)

    def harvest(self):
        # replace with your link. 
        self.driver.get('https://www.facebook.com/groups/{snipped}/user/{snipped}')
        time.sleep(3)

        self.images = []
        image_limit = 560
        while image_limit > len(self.images):
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
            
            image_objects = self.driver.find_elements(By.CSS_SELECTOR, '.x1ey2m1c.xds687c.x5yr21d.x10l6tqk.x17qophe.x13vifvy.xh8yej3.xl1xv1r')

            image_urls = []
            for image in image_objects:
                url = image.get_attribute('src')
                image_urls.append(url)
            
            self.images = image_urls
            
    def downloadImages(self):
        df = pd.DataFrame(self.images, columns=['image_url']).drop_duplicates()

        for count, image in enumerate(df['image_url']):
            download = requests.get(image)

            with open(f'export/{count+1}.jpg', 'wb') as out:
                out.write(download.content)

        
        

def main():
    FG = FacebookGS()
    FG.harvest()
    FG.downloadImages()


main()
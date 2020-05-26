import requests # needed to access a URL
from bs4 import BeautifulSoup
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = './chromedriver'
base_url = 'https://www.eventbrite.com/d/online/free--music--events--this-month/?lang=en&page=1'


driver = webdriver.Chrome(PATH)
driver.get(base_url)
driver.implicitly_wait(100)

html = driver.page_source
# Activates beautiful soup: 1st parameter is page to scrape, 2nd parameter is parser used to traverse html document
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all(class_='eds-event-card-content__image')

driver.quit()

print(images)
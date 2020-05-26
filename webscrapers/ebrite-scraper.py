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
soup = BeautifulSoup(html, 'lxml')

# Grab Images
images = soup.find_all(class_='eds-event-card-content__image')

# Grab Event Names (grab all '.eds-event-card__formatted-name--is-clamped' inside of 'search-event-card-square-image')
event_names = soup.select('.search-event-card-square-image .eds-event-card__formatted-name--is-clamped')
for tag in event_names:
  print(tag.text)

# Grab event date and time (grab all '.eds-l-pad-bot-1' inside of 'search-event-card-square-image')
event_date_times = soup.select('.search-event-card-square-image .eds-l-pad-bot-1')
for date_time in event_date_times:
  print(date_time.text)

# Grab event link (Grab all 'eds-event-card-content__action-link' inside the aside elements when aside is in '.search-event-card-square-image')
event_links = soup.select('.search-event-card-square-image aside .eds-event-card-content__action-link')
for link in event_links:
  print(link.get('href'))


driver.quit()

# print(images)


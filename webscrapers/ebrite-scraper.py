import requests # needed to access a URL
from bs4 import BeautifulSoup
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import time

PATH = './chromedriver'
base_url = 'https://www.eventbrite.com/d/online/free--music--events--this-month/?lang=en&page=1'


driver = webdriver.Chrome(PATH)
driver.get(base_url)
time.sleep(1)

html_doc = driver.find_element_by_tag_name('html')

with open('covents_data.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['id', 'event_name', 'event_image', 'event_date_time', 'event_link']
  csv_writer.writerow(headers)

  id_counter = 0

  while True:
    html_doc = driver.find_element_by_tag_name('html')

    html_doc.send_keys(Keys.COMMAND + 'r')
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)


    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')

    images = soup.select('.eds-event-card-content__image')
    event_names = soup.select('.search-event-card-square-image .eds-event-card__formatted-name--is-clamped')
    event_date_times = soup.select('.search-event-card-square-image .eds-l-pad-bot-1')
    event_links = soup.select('.search-event-card-square-image aside .eds-event-card-content__action-link')

    counter = -1

    for img in images:
      counter += 1
      id_counter += 1
      img_src = img.get('src').replace(',', '')
      name = event_names[counter].get_text()
      date_time = event_date_times[counter].get_text()
      link = event_links[counter].get('href')
      event_id = id_counter
      csv_writer.writerow([event_id, name, img_src, date_time, link])

    try:
      next_button = driver.find_element_by_xpath("//button[@data-spec='page-next']")
      next_button.click()
    except ElementNotInteractableException:
      break

driver.quit()


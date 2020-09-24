def scrape_it():
  import requests
  import os
  from bs4 import BeautifulSoup
  from csv import writer
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  from selenium.common.exceptions import ElementNotInteractableException
  import time

  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

  current_month_url = 'https://www.eventbrite.com/d/online/free--music--events--this-month/?lang=en&page=1'
  next_month_url = 'https://www.eventbrite.com/d/online/free--music--events--next-month/?lang=en&page=1'

  driver.get(current_month_url)
  time.sleep(1)

  html_doc = driver.find_element_by_tag_name('html')

  id_counter = 0
  data = []

  while True:
    html_doc = driver.find_element_by_tag_name('html')

    html_doc.send_keys(Keys.COMMAND + 'r')
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')

    images = soup.select('.eds-max-img')
    print(len(images))
    event_names = soup.select('.search-event-card-square-image .eds-event-card__formatted-name--is-clamped')
    event_date_times = soup.select('.search-event-card-square-image .eds-l-pad-bot-1')
    print(len(event_date_times))
    event_links = soup.select('.search-event-card-square-image aside .eds-event-card-content__action-link')

    counter = -1

    for img in images:
      json_data = {}
      counter += 1
      id_counter += 1
      event_date_time = event_date_times[counter].get_text()
      event_date_split = event_date_time.split()
      print(img)

      if len(event_date_split) == 0:
        pass
      else:
        try:
          event_date = event_date_split[0] + ' ' + event_date_split[1] + ' ' + event_date_split[2] + ' ' + event_date_split[3]
          event_time = event_date_split[4] + ' ' + event_date_split[5] + ' ' + event_date_split[6]
        except IndexError:
          break

      json_data['image'] = img.get('data-src')
      json_data['event_name'] = event_names[counter].get_text()
      json_data['date'] = event_date
      json_data['time'] = event_time
      json_data['link'] = event_links[counter].get('href')
      json_data['id'] = id_counter

      data.append(json_data)

    try:
      next_button = driver.find_element_by_xpath("//button[@data-spec='page-next']")
      next_button.click()
    except ElementNotInteractableException:
      break

  driver.quit()

  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
  driver.get(next_month_url)
  time.sleep(1)

  while True:
    html_doc = driver.find_element_by_tag_name('html')

    html_doc.send_keys(Keys.COMMAND + 'r')
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html_doc.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')

    images = soup.select('.eds-max-img')
    event_names = soup.select('.search-event-card-square-image .eds-event-card__formatted-name--is-clamped')
    event_date_times = soup.select('.search-event-card-square-image .eds-l-pad-bot-1')
    event_links = soup.select('.search-event-card-square-image aside .eds-event-card-content__action-link')

    counter = -1

    for img in images:
      json_data = {}
      counter += 1
      id_counter += 1
      event_date_time = event_date_times[counter].get_text()
      print(counter)
      event_date_split = event_date_time.split()

      if len(event_date_split) == 0:
        pass
      else:
        try:
          event_date = event_date_split[0] + ' ' + event_date_split[1] + ' ' + event_date_split[2] + ' ' + event_date_split[3]
          event_time = event_date_split[4] + ' ' + event_date_split[5] + ' ' + event_date_split[6]
        except IndexError:
          break

      json_data['image'] = img.get('data-src')
      json_data['event_name'] = event_names[counter].get_text()
      json_data['date'] = event_date
      json_data['time'] = event_time
      json_data['link'] = event_links[counter].get('href')
      json_data['id'] = id_counter

      data.append(json_data)

    try:
      next_button = driver.find_element_by_xpath("//button[@data-spec='page-next']")
      next_button.click()
    except ElementNotInteractableException:
      break

  driver.quit()
  return data

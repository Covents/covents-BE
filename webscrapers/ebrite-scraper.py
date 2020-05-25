import requests # needed to access a URL
from bs4 import BeautifulSoup
from csv import writer

# get request for a website URL, used to access the web and stores it into variable
page_to_scrape = requests.get('https://www.eventbrite.com/d/online/free--music--events--this-month/?lang=en&page=1')
# grabs the content from the request and stores it in variable
page_content = page_to_scrape.content

# prints 200 status code stating the page is indeed accessible uncomment below line to see status code
# print(page_to_scrape.status_code)

# Activates beautiful soup: 1st parameter is page to scrape, 2nd parameter is parser used to traverse html document
# store this as soup for easier access
soup = BeautifulSoup(page_content, 'lxml')

#prints the html body of the provided URL, uncomment print below to see the soup body
# print(soup.body)

images = soup.find_all(class_='eds-event-card-content__image')

print(images)

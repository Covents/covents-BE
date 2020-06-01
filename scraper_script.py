import json
from api import Event
from api import db
from webscrapers import ebrite_scraper
from webscrapers import csv_to_json

ebrite_scraper.scrape_it()
csv_to_json.convert()

with open('webscrapers/covents_json.json') as json_data:
    file_data = json_data.read()
    scraped_data = json.loads(file_data)


    for i in scraped_data:
        r = Event(name=i['event_name'], link=i['link'], date=i['date'], time=i['time'], image=i['image'])
        events_by_name_and_date = Event.query.filter_by(name=i['event_name']).filter_by(date=i['date']).all()
        if len(events_by_name_and_date) == 0:
            db.session.add(r)
            db.session.commit()


json_data.close()
# ebrite_scraper.scrape_it()


from application.__init__ import Event
from application.__init__ import db
from webscrapers import ebrite_scraper

scraped_data = ebrite_scraper.scrape_it()

for i in scraped_data:
    r = Event(name=i['event_name'], link=i['link'], date=i['date'], time=i['time'], image=i['image'])
    events_by_name_and_date = Event.query.filter_by(name=i['event_name']).filter_by(date=i['date']).all()
    if len(events_by_name_and_date) == 0:
        db.session.add(r)
        db.session.commit()






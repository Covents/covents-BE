### Contributors
[Megan Venetianer - Front End](https://github.com/megan-venetianer)

[Cristina Peña - Front End](https://github.com/CLPena)

[Dan Reardon - Back End](https://github.com/dreardon1021)

[Kelly Bard - Back End](https://github.com/KellyIB)



## Deployed App
[c o v e n t s](https://covents.netlify.app/#/)

   
### BE API deployed on Heroku
  
  - Covent-BE Production is at: https://fierce-earth-48309.herokuapp.com
  
### Capstone Presentation

  [Capstone Presentation](https://docs.google.com/presentation/d/1FwUGeC-TW4hBnwJTv6_vczn0SngD5CpbFQ5CY2KzNMI/edit?ts=5ed955f0#slide=id.g897d938f84_0_5)
  
  
## Endpoint Goals

  - MVP Endpoints: All Events, Event by date, keyword search functionality - MET
  
  - Extension Endpoints: Events by ID, Name - MET
  
  - Future Extensions: Multi-Keyword search
  

## Current API Endpoints:


** All Events

  - '/api/v1/resources/events/all', methods=['GET']
    - no params, returns all events objects
    - example request: http://localhost:5000/api/v1/resources/events/all
    - example response: 
  ```
  [
      {
        "date": "Sun, May 31, 2020",
        "id": 1,
        "image": "https://www.metallica.com/on/demandware.static/-/Sites-Metallica-Library/default/dwbb154b9c/images/homepage/home-hero-stadium.jpg",
        "link": "https://www.metallica.com/",
        "name": "Metallica",
        "time": "7:00 PM CDT"
      },
      {
        "date": "Sat, May 30, 2020",
        "id": 2,
        "image": "https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F99457776%2F119015619107%2F1%2Foriginal.20200424-194945?w=512&auto=format%2Ccompress&q=75&sharp=10&rect=382%2C0%2C1068%2C534&s=825de94e15775c953040327b94efe728",
        "link": "https://www.eventbrite.com/e/dcjazzfest-from-home-series-tickets-103369585212?aff=ebdssbonlinesearch",
        "name": "DCJazzFest From Home Series",
        "time": "7:00 PM EDT"
      }
     ]
  ```   

** Event by ID
    
  - '/api/v1/resources/event_by_id', methods=['GET']
    - params:  id=id, returns  events object by id
    - example_request: http://localhost:5000/api/v1/resources/event_by_id?id=1
    - example_response:
  ```
        {
          "date": "Sun, May 31, 2020",
          "id": 1,
          "image": "https://www.metallica.com/on/demandware.static/-/Sites-Metallica-Library/default/dwbb154b9c/images/homepage/home-hero-stadium.jpg",
          "link": "https://www.metallica.com/",
          "name": "Metallica",
          "time": "7:00 PM CDT"
        }
  ```

** Event by Name

  - '/api/v1/resources/event_by_name', methods=['GET']
    - params:  id=id, returns  events object by event name
    - example_request: http://localhost:5000/api/v1/resources/event_by_name?id=Metallica
    - example_response: 
 ```    
        {
          "date": "Sun, May 31, 2020",
          "id": 1,
          "image": "https://www.metallica.com/on/demandware.static/-/Sites-Metallica-Library/default/dwbb154b9c/images/homepage/home-hero-stadium.jpg",
          "link": "https://www.metallica.com/",
          "name": "Metallica",
          "time": "7:00 PM CDT"
        } 
  ```
    
** Keyword Search

  - '/api/v1/resources/events/keyword', methods=['GET']
    - params: (1) keyword=keyword, (but trying for multiple keywords) meant to search event name
       (case insensitive, can search with partial words)
    - example request: http://localhost:5000/api/v1/resources/event_keyword?keyword=e
    - example_response: 
 ```    
        [
          {
            "date": "Sun, May 31, 2020",
            "id": 1,
            "image": "https://www.metallica.com/on/demandware.static/-/Sites-Metallica-Library/default/dwbb154b9c/images/homepage/home-hero-stadium.jpg",
            "link": "https://www.metallica.com/",
            "name": "Metallica",
            "time": "7:00 PM CDT"
          },
          {
            "date": "Sat, May 30, 2020",
            "id": 2,
            "image": "https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F99457776%2F119015619107%2F1%2Foriginal.20200424-194945?w=512&auto=format%2Ccompress&q=75&sharp=10&rect=382%2C0%2C1068%2C534&s=825de94e15775c953040327b94efe728",
            "link": "https://www.eventbrite.com/e/dcjazzfest-from-home-series-tickets-103369585212?aff=ebdssbonlinesearch",
            "name": "DCJazzFest From Home Series",
            "time": "7:00 PM EDT"
          }
        ]
  ```

** Search by Date

  - '/api/v1/resources/events/when', methods=['GET']
    - params:  date=date, returns events for a date
    - example_request: http://localhost:5000/api/v1/resources/events/when?date=May 30
    - example_response: 
  ```   
          {
            "date": "Sat, May 30, 2020",
            "id": 2,
            "image": "https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F99457776%2F119015619107%2F1%2Foriginal.20200424-194945?w=512&auto=format%2Ccompress&q=75&sharp=10&rect=382%2C0%2C1068%2C534&s=825de94e15775c953040327b94efe728",
            "link": "https://www.eventbrite.com/e/dcjazzfest-from-home-series-tickets-103369585212?aff=ebdssbonlinesearch",
            "name": "DCJazzFest From Home Series",
            "time": "7:00 PM EDT"
          }
  ```

API Endpoints
  - '/api/v1/resources/events/all', methods=['GET']
    - no params, returns all events objects
    
  - '/api/v1/resources/events/when', methods=['GET']
    - params:  date=date, returns events for a date
    
  - '/api/v1/resources/events/keyword', methods=['GET']
    - params: (1) keyword=keyword, (but trying for multiple keywords) meant to search event name

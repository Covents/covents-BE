# This file is no longer needed but will be kept for legacy purposes
def convert():
    import csv, json

    csv_file_path = './covents_data.csv'
    json_file_path = './covents_json.json'

    data = []
    with open(csv_file_path) as csvFile:
      csvReader = csv.DictReader(csvFile)
      for csvRow in csvReader:
          row_to_split = csvRow['event_date_time']
          event_date_split = row_to_split.split()
          if len(event_date_split) == 0:
              pass
          else:
              try:
                  event_date = event_date_split[0] + ' ' + event_date_split[1] + ' ' + event_date_split[2] + ' ' + event_date_split[3]
                  event_time = event_date_split[4] + ' ' + event_date_split[5] + ' ' + event_date_split[6]
              except IndexError:
                    break
          data_row = {
                    'id': csvRow['id'],
                    'event_name': csvRow['event_name'],
                    'image': csvRow['event_image'],
                    'date': event_date,
                    'time': event_time,
                    'link': csvRow['event_link']
                    }
          data.append(data_row)

    with open(json_file_path, 'w') as jsonFile:
      jsonFile.write(json.dumps(data, indent=2))


    # open csv file and grab the rows and create keys in the data obj as the id
    # open up the json file and write into it as jsonFile
    # dump converts the data dictionary into a json string
    # write into the json file the data which is the first argument
    # indent=2 allows the json file to be readable and not just one long line object
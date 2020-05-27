import csv, json

csv_file_path = './covents_data.csv'
json_file_path = './covents_json.json'

data = {}
with open(csv_file_path) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for csvRow in csvReader:
    id = csvRow['id']
    data[id] = csvRow

with open(json_file_path, 'w') as jsonFile:
  jsonFile.write(json.dumps(data, indent=2))


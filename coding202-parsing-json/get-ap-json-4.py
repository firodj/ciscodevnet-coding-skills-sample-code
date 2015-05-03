import json
import requests
url = 'https://64.103.26.61/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone'
headers = {'Authorization': 'Basic bGVhcm5pbmc6bGVhcm5pbmc==', 'Accept': 'application/json'}
response = requests.get(url, headers=headers, verify=False)
responseString = response.text

jsonObject = json.loads(responseString)
print(json.dumps(jsonObject, sort_keys=True, indent=4))
accessPoints = jsonObject['Floor']['AccessPoint']
for ap in accessPoints:
  print('Access Point: ' + ap['name'] + '\t eth: ' + ap['ethMacAddress'] + '\t ip: ' + ap['ipAddress'])

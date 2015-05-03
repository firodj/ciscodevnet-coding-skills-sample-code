import requests
url = 'https://64.103.26.61/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone'
headers = {'Authorization': 'Basic bGVhcm5pbmc6bGVhcm5pbmc==', 'Accept': 'application/json'}
response = requests.get(url, headers=headers, verify=False)
responseString = response.text
print(responseString)

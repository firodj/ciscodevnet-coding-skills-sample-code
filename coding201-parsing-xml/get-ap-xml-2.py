import requests
import xml.dom.minidom as minidom
url = 'https://64.103.26.61/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone'
headers = {'Authorization': 'Basic bGVhcm5pbmc6bGVhcm5pbmc=='}
response = requests.get(url, headers=headers, verify=False)
responseString = response.text
dom = minidom.parseString(responseString)
xml = dom.toprettyxml()
print(xml)

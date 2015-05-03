import requests
import xml.dom.minidom as minidom
url = 'https://64.103.26.61/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone'
headers = {'Authorization': 'Basic bGVhcm5pbmc6bGVhcm5pbmc=='}
response = requests.get(url, headers=headers, verify=False)
responseString = response.text
dom = minidom.parseString(responseString)
xml = dom.toprettyxml()
print(xml)

access_points = dom.getElementsByTagName('AccessPoint')
for access_point in access_points:
  ap_name = access_point.getAttribute('name')
  ap_eth_addr = access_point.getAttribute('ethMacAddress')
  ap_ip_addr = access_point.getAttribute('ipAddress')
  print(access_point.tagName + ": " + ap_name + '\t eth: ' + ap_eth_addr + '\t ip: ' + ap_ip_addr)

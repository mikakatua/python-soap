
#import zeep
#import xml.etree.ElementTree as ET
from zeep.plugins import HistoryPlugin
from zeep import Client
from lxml import etree

#wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
wsdl_url = 'CountryInfoService.wsdl'

history = HistoryPlugin()
client = Client(wsdl_url, plugins=[history])
client.service.ListOfCountryNamesByCode()
# Print the SOAP response
print(etree.tostring(history.last_received["envelope"], encoding="unicode", pretty_print=True))

tree = etree.parse('countries.xml')
root = tree.getroot()
for index, item in enumerate(root.findall('tCountryCodeAndName')):
  code = item.find('sISOCode').text
  country = item.find('sName').text
  request = client.create_message(client.service, 'CapitalCity', sCountryISOCode=code)
  # Print the SOAP request
  print(etree.tostring(request, encoding="unicode", pretty_print=True))
  capital = client.service.CapitalCity(sCountryISOCode=code)
  print(f"Capital of {country} is {capital}")
  if index == 1:
    break

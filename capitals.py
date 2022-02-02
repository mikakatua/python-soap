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
your_pretty_xml = etree.tostring(history.last_received["envelope"], encoding="unicode", pretty_print=True)
#print(your_pretty_xml)

tree = etree.parse('countries.xml')
root = tree.getroot()
for item in root.findall('tCountryCodeAndName'):
  code = item.find('sISOCode').text
  country = item.find('sName').text
  capital = client.service.CapitalCity(sCountryISOCode=code)
  print(f"Capital of {country} is {capital}")

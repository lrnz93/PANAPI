import requests
import xml.etree.ElementTree as ET
import json
import xmltodict

#Static values
APIKEY = "LUFRPT15OC9NSjRobndlMmsvT3dBazRweU9HaHNnczQ9VkhLS3oyLzFiaDdGMm9LTHU3eW0rRW9FTEh2bDhHbUpsQzg4QUlIQkdpRExUYjlTb2RDZHdoY1R6eGs5cmY0Tg=="
VSYS = "vsys1"
URL = "https://fwpan01.biseswar.tech/api/?type=config&action="
ACTION = "get"

def list_security_rules(url, vsys, apikey,action):

    xpath = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name="+"'"+vsys+"'"+"]/rulebase/security"
    r_seclist = requests.get(url+action+"&xpath="+xpath+"&key="+apikey)
    list = []

    if r_seclist.status_code != 200:
        return r_seclist.status_code

    else:
        output = []
        root_seclist = ET.fromstring(r_seclist.content)
        for child in root_seclist.iter('entry'):
            output.append(child.attrib['name'])

        klaar = json.dumps(output)
        return klaar

def edit_security_rules():
    response_code = ''
    return response_code

def commit_config():
    curl_response = ''
    return curl_response

newlist = list_security_rules(URL, VSYS, APIKEY, ACTION)
print(newlist)
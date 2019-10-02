import requests
import xml.etree.ElementTree as ET
import sys


#Static values
APIKEY = "LUFRPT15OC9NSjRobndlMmsvT3dBazRweU9HaHNnczQ9VkhLS3oyLzFiaDdGMm9LTHU3eW0rRW9FTEh2bDhHbUpsQzg4QUlIQkdpRExUYjlTb2RDZHdoY1R6eGs5cmY0Tg=="
VSYS = "\"vsys1\""
URL = "https://fwpan01.biseswar.tech/api/?type=config&action="

def list_security_rules(url, vsys, apikey):
    ACTION = "get"
    xpath = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name="+vsys+"]/rulebase/security"

    try:
        r_seclist = requests.get(url+ACTION+"&xpath="+xpath+"&key="+apikey)
    except requests.ConnectionError as e:
        print e
        sys.exit()

    output = []
    root_seclist = ET.fromstring(r_seclist.content)
    for child in root_seclist.iter('entry'):
        output.append(child.attrib['name'])

    #klaar = json.dumps(output)
    return output

def edit_security_rules(url, vsys, apikey,secrules):

    ACTION = "set"
    for i in secrules:
        xpath = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name="+vsys+"]/rulebase/security/rules/entry[@name=\""+i+"\"]&element=<log-setting>test_Ubuntu</log-setting>"
        print xpath


        try:
            r_editrule = requests.get(url + ACTION + "&xpath=" + xpath + "&key=" + apikey)
        except Exception:
            print "error"

    return r_editrule




def commit_config():
    curl_response = ''
    return curl_response

# Call functions
newlist = list_security_rules(URL, VSYS, APIKEY)
print newlist

r_code = edit_security_rules(URL,VSYS,APIKEY,newlist)
print r_code



import requests
import xml.etree.ElementTree as ET
import sys
import time

#Static values
APIKEY = "LUFRPT15OC9NSjRobndlMmsvT3dBazRweU9HaHNnczQ9VkhLS3oyLzFiaDdGMm9LTHU3eW0rRW9FTEh2bDhHbUpsQzg4QUlIQkdpRExUYjlTb2RDZHdoY1R6eGs5cmY0Tg=="
VSYS = "\"vsys1\""
URL = "https://fwpan01.biseswar.tech/api/?type=config&action="

# function create firwall list
def list_security_rules(url, vsys, apikey):
    ACTION = "get"
    xpath = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name="+vsys+"]/rulebase/security"

    try:
        r_seclist = requests.get(url+ACTION+"&xpath="+xpath+"&key="+apikey)
        time.sleep(1)
    except requests.ConnectionError as e:
        print e
        sys.exit()

    r_output = []
    root_seclist = ET.fromstring(r_seclist.content)
    for child in root_seclist.iter('entry'):
        r_output.append(child.attrib['name'])

    return r_output

# function edit security rules
def edit_security_rules(url, vsys, apikey,secrules):

    ACTION = "set"
    for count in secrules:
        xpath = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name="+vsys+"]/rulebase/security/rules/entry[@name=\""+count+"\"]&element=<log-setting>testing</log-setting>"

        try:
            r_editrule = requests.get(url + ACTION + "&xpath=" + xpath + "&key=" + apikey)
            print "rule: "+count+"---"+ "statuscode: "+str(r_editrule.status_code)
            time.sleep(1)
        except requests.ConnectionError as e:
            print e + "rule: "+count+"---"+ "statuscode: "+str(r_editrule.status_code)
            sys.exit()

    return ("end edit function ")

#function commit to firewall
def commit_config(apikey):
    URL = "https://fwpan01.biseswar.tech/api/?type=commit&cmd=<commit></commit>"

    try:
        r_commit = requests.get(URL + "&key=" + apikey)
        print "Commit succesfull"

    except requests.ConnectionError as e:
        print e
        sys.exit()

    return ("end commit function ")

# Call functions
newlist = list_security_rules(URL, VSYS, APIKEY)
print newlist

r_code = edit_security_rules(URL,VSYS,APIKEY,newlist)
print r_code

r_commit = commit_config(APIKEY)
print r_commit
#!/usr/bin/env python

import requests
import json
import os
import sys
from bs4 import BeautifulSoup

es = requests.Session()

sis = es.get("https://sis.rit.edu/portalServices/portal.do")
        #fill in with own username and password
payload = {'j_username': '', 'j_password': '', '_eventId_proceed': ''}

login = es.post(sis.url, data = payload)

sis = es.get("https://sis.rit.edu/portalServices/portal.do")

soup = BeautifulSoup(login.text, 'html.parser')

input_list = soup.find_all('input')

payload2 = {input_list[0]['name']:input_list[0]['value'], input_list[1]['name']:input_list[1]['value']}

fin = es.post(soup.find_all('form')[0]['action'], data = payload2)

home = es.get("https://sis.rit.edu/portalServices/diningBalance.do")

script = home.text.split("   var obj = ")[1]

script = script.split(";")[0].strip()

final = json.loads(script)

debitBalance = str(final['customer']['balances'][1]['food'])

f = open('debit', 'w')
f.write('$' + debitBalance)

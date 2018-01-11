#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import requests
import sys

# args
args = sys.argv
output_folder = args[1]
now = datetime.now().strftime("%Y%m%d_%H%M")
output_file = output_folder + "/" + now + ".json"

# Request
url = "https://fx.click-sec.com/neo/rfl/calendarList"
response = requests.get(url)
print(response.status_code) 

# Write Response
f = open(output_file, 'w')
f.write(response.text.encode('utf_8'))
f.close()

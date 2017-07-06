#!/usr/bin/env python

"""
Script is used to check the chef service status page
"""
import urllib,json

url = "http://status.chef.io/?format=json"
response = urllib.urlopen(url)
data = json.loads(response.read())
if data['components'][2]["status"] == "operational":
    print(0)
else:
    print(1)

#!/usr/bin/env python

"""
Script is used to check the chef status page
"""
import urllib,json

url = "http://status.chef.io/?format=json"
response = urllib.urlopen(url)
data = json.loads(response.read())
if data['components'][2]["status"] != "operational":
    print("Hosted Chef issues")

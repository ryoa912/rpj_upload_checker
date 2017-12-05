#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import httplib

storage_api_url = '/service/storage/files/usb1'
directory_name  = 'rpj_upload_checker'
file_name       = 'image01.jpg'

connection = httplib.HTTPConnection('localhost:80')
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
connection.request('PUT', storage_api_url+'/'+directory_name+'/'+file_name, params, headers)
response = connection.getresponse()
data = response.read()
print response.status, response.reason
print data

print '-'*50

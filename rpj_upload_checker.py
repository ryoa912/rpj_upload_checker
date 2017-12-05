#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import httplib

server_url      = 'localhost:80'
storage_api_url = '/service/storage/files/usb1'
directory_name  = 'rpj_upload_checker'
file_name       = 'image01.jpg'

f = open('contents/image01.jpg')
str = f.read()
print str

connection = httplib.HTTPConnection(server_url)

headers = { 'Content-type':'application/octet-stream', 'Overwrite': 'T'}
connection.request('PUT', storage_api_url+'/'+directory_name+'/'+file_name, str, headers)
response = connection.getresponse()
data = response.read()
print response.status, response.reason
print data

print '-'*50

f.close()

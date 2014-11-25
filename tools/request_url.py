__author__ = 'linw'


import urllib2

def request_url(url_):
    response = urllib2.urlopen(url_)
    return response.read()

def request_url_no_read(url_):
    response = urllib2.urlopen(url_)

print request_url('http://127.0.0.1:5000/get/MapEditor/0/')
__author__ = 'linw'

import urllib2
import urllib
import re
import os
import urlparse
from flask import flash

from BeautifulSoup import BeautifulSoup

def download(url_, dst_):
    urllib.urlretrieve(url_, dst_)

def parser(url_):
    page = urllib2.urlopen(url_).read()
    rs = []
    if page is not None:
        html = BeautifulSoup(page)
        all = html.findAll('a')
        for item in all:
            if item.has_key('href'):
                cur_uri = item.attrMap['href']
                cur_url = urlparse.urljoin(url_, cur_uri)
                rs.append(cur_url)
    return rs

def test(url_):
    list = parser(url_)#'http://docs.jinkan.org/docs/flask/genindex.html')
    for item in list:
        try:
            file_url = 'C:\OUTPUT\%s'% re.match('http:\/\/docs.jinkan.org\/(.*)', item).group(1)
            file_url = file_url.replace('/', '\\').encode(encoding='ascii').decode(encoding='ascii')
            file_dir = file_url[0:file_url.rindex("\\")]
            if not os.path.isdir(file_dir):
                os.makedirs(file_dir)
            download(item, file_url)
            flash('downloaded %s '% item)
        except:
            flash('download error: %s '% item)
    return list
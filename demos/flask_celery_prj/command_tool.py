__author__ = 'linw'

import urllib2
import urllib
import re
import os
import urlparse
from flask import flash

from BeautifulSoup import BeautifulSoup

def download(url_, dst_):
    if dst_ is not None:
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
            download(item, None)
            flash('downloaded %s '% item)
        except:
            flash('download error: %s '% item)
    return list


import subprocess

def exe_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if p is not None:
        return p.stdout
    return None

def print_cmd(cmd_out):
    if cmd_out is None:
        print None
        return
    rs = cmd_out.readlines()
    for line in rs:
        print line

def parser_cmd(cmd_out):
    if cmd_out is None:
        return []
    rs = []
    rs_line = cmd_out.readlines()
    for line in rs_line:
        rs.append(line)
    return rs

def test_cmd():
    out = exe_cmd("svn help")
    return ''.join(parser_cmd(out))


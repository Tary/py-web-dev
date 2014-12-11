__author__ = 'linw'
import urllib2
import urllib
import re
import os
import time

from BeautifulSoup import BeautifulSoup

def download(url_, dst_):
    urllib.urlretrieve(url_, dst_)

def parser(url_, dir_):
    page = urllib2.urlopen(url_).read()
    if page is not None:
        html = BeautifulSoup(page)
        all = html.findAll(attrs={'id':'J_UlThumb'})
        if all.source.attrs is None:
            return

        down_load_list = []
        all_img = all[0].findAll('img')
        for img in all_img:
            if img.has_key('src'):
                img_url = img.attrMap['src']
            elif img.has_key('data-src'):
                img_url = img.attrMap['data-src']
            else:
                continue
            big_url = re.match('(.*)_(.*).jpg', img_url).group(1)
            down_load_list.append(big_url)

        localtime = time.localtime(time.time())
        forder = time.asctime(localtime)
        forder = forder.replace(':', '-')
        if not os.path.isdir(dir_):
            os.mkdir(dir_)
        dst_ = os.path.join(dir_, forder)
        if not os.path.isdir(dst_):
            os.mkdir(dst_)

        re_file_name = '(.*)!!(.*)'
        for url_ in down_load_list:
            name = re.match(re_file_name, url_).group(2)
            download(url_, os.path.join(dst_, name))

print u'q退出, 输出到C:\\OUT_PUT'
website = raw_input("Enter URL:")
while website != 'q':
    parser(website, 'c:/OUT_PUT')
    website = raw_input("Enter URL:")
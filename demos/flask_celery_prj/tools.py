import chardet

__author__ = 'linw'
def str_unicode(str):
    encoding = chardet.detect(str)['encoding']
    if encoding == 'ascii':
        encoding = 'utf-8'
    return unicode(str, encoding)
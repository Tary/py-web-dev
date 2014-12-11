__author__ = 'linw'

import sys
sys.path.insert(0, '..')
from flask import Flask, Response, _app_ctx_stack, render_template, flash
import os
from command_test import *

app = Flask(__name__)
app.config.from_object('SETTINGS')

@app.route('/')
def index():
    list = parser('http://docs.jinkan.org/docs/flask/genindex.html')
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
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:25:00 2014

@author: linw
"""
from bottle import route, run, template, static_file, Bottle, get, post, request
import os
import sys



SER_PORT = 8080
SER_HOST = 'localhost'
SER_RELOAD = False


#port
#reload
#host
def check_args():
  global SER_PORT
  global SER_HOST
  global SER_RELOAD
  if(len(sys.argv) > 1):
    SER_PORT = sys.argv[1]
    if(len(sys.argv) > 2):
      if sys.argv[2] == 'True' or sys.argv[2] == 'true':
        SER_RELOAD = True
      else:
        SER_RELOAD = False
#end of check_args

app = Bottle()

@app.get('/')
def index():
  return template('index', title = 'Tary')


@app.post('/upload')
def do_login():
  data = request.files.data
  if data and data.file:
    filePath = os.path.join(os.getcwd(), 'upload', data.filename)
    fi = open(filePath, 'wb+')
    fi.write(data.file.read())
    fi.close()
    return "文件已经上传"
  else:
    return 'empty'




if __name__ == "__main__":
  check_args()
  run(app, host=SER_HOST, port=SER_PORT, debug=True, reload=SER_RELOAD)

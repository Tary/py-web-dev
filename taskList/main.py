# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:25:00 2014

@author: linw
本服务专门干活,干完了POST结果给调用指定的URL


"""
from bottle import route, run, template, Bottle, get, post, request
import os
import sys


SER_PORT = 8081
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


BUILD_LOG = ""
SVN_LOG = ""

def exeCMD(cmd):
    log = os.popen(cmd)
    log_text = log.read()
    log.close()
    return log_text

def build():


@app.get('/')
def index():
  return template('暂时没活~~')


@app.post('/start/<param>/<url>')
def do_task(param, url = ''):
  cmd = "cd ../../workspace/ && git pull"
  SVN_LOG = exeCMD(cmd)
  cmd = "/var/www/html/web/toolWeb/trdpart/build%s.sh" % param
  BUILD_LOG = exeCMD(cmd)

  if url and len(url) > 0:





if __name__ == "__main__":
  check_args()
  run(app, host=SER_HOST, port=SER_PORT, debug=True, reload=SER_RELOAD)

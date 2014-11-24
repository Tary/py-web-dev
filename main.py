# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:25:00 2014

@author: linw
"""
from bottle import route, run, template, static_file

state = ""

currentProject = ""

import os

def exeCMD(cmd):
    log = os.popen(cmd)
    log_text = log.read()
    log.close()
    print log
    return log_text

def svnUpdate(path):
    cmd = "svn up \"%s\" --non-interactive -q"
    return exeCMD(cmd % path)


def svnCommit(path):
    cmd = "svn add \"%s\" --force"
    logtext = exeCMD(cmd % path)
    print logtext
    cmd = "svn commit \"%s\" -m 'Auto Commit'"
    return logtext + '\n' + exeCMD(cmd % path)

TRD_PATH = "E:/Python/dev/toolWeb/trdpart/"
def build():
    cmd = "start " + TRD_PATH + "build.bat"
    return " build start " + exeCMD(cmd)

def copy(path):
    return " copy to path:%s" % path

def publishProject(path):
    log = svnUpdate(path)
    #log += build(path)
    log += svnCommit(path)
    return log + copy(path)

class projectInfo(object):
    def __init__(self, _name, _uri):
        self.name = _name;
        self.uri = _uri

@route('/')
def index():
    lis = []
    lis.append(projectInfo("粒子编辑器", "Particle"))
    lis.append(projectInfo("技能编辑器", "SkillEditor"))
    lis.append(projectInfo("场景编辑器", "SceneEditor"))
    return template("templates/index.html", projects=lis, title="tEEE")


@route('/publish/<proj>')
def publish(proj):
    global state
    global currentProject

    if(state == "BUILDING"):
        return "已经正在发布%s  稍后刷新" % currentProject
    currentProject = proj
    state = "BUILDING"
    return "正在发布%s  稍后刷新" % proj


@route('/download/<filename>')
def download(filename):
    return static_file(filename=filename, root='E:/Python/dev/toolWeb/staticfiles/', download=filename)


run(host='localhost', port=8080, debug=True, reload=True)

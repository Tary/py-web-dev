from distutils.core import setup
import py2exe

includes = ["encodings", "encodings.*"]

setup(
windows=[{"script":"checkbox.py", "icon_resources":[(1, "myicon.ico")]}],
version='1.0',
description='For Beibei',
name='Hello Beibei',
options = {"py2exe": {"compressed": 1,"optimize": 2, "bundle_files": 1}},
zipfile=None)

from distutils.core import setup
import py2exe

setup(console=['taobao_image_parser.py'],
version='1.0',
description='For Beibei',
name='Hello Beibei',
options = {"py2exe": {"compressed": 1,"optimize": 2, "bundle_files": 1}},
zipfile=None)
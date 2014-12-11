from distutils.core import setup
import py2exe

setup(windows=['aa.py'],
version='1.0',
description='For Beibei',
name=u'大家好,我是病毒^_^',
options = {"py2exe": {"compressed": 1,"optimize": 2, "bundle_files": 1}},
zipfile=None)
__author__ = 'linw'

import sys
sys.path.insert(0, '..')
from tools import LogDatabaseTool
from tools import SimpleXML
from SETTINGS import *




#print(xml_tool.toxml())

from flask import Flask, Response

app = Flask(__name__)
app.config.from_object('SETTINGS')

import mimetypes
@app.route('/<version>')
def index(version):
    db_tool = LogDatabaseTool(DATABASE)
    db_tool.init_db(open(DATABASE_SCHEMA, 'r'))

    xml_tool = SimpleXML('cdata')
    xml_tool.initialize_from_file(XML_TEMPLATE)
    xml_tool.set_cdata_val('\n'.join(db_tool.get_log('T', int(version))))
    return Response(xml_tool.toxml(), mimetype='application/xml')

app.run()
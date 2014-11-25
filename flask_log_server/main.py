__author__ = 'linw'

import sys
sys.path.insert(0, '..')
from tools import LogDatabaseTool
from tools import SimpleXML
from SETTINGS import *
from flask import Flask, Response, _app_ctx_stack

db_tool = LogDatabaseTool(DATABASE)

app = Flask(__name__)
app.config.from_object('SETTINGS')

log_xml_tool = SimpleXML(UPDATER_DESC_TAG)
log_xml_tool.initialize_from_file(LOG_XML_TEMPLATE)

version_xml_tool = SimpleXML(VERSION_TAG)

@app.route('/')
def index():
    print 23/0

@app.route('/get/<project>/<int:version>/')
def get_log(project, version):
    version_xml_tool.initialize_from_file(PRJ_ROUTE[project])
    log_xml_tool.set_value(DOWNLOAD_URL_TEMPLATE % project, UPDATER_URL_TAG)
    app_version, rs = version_xml_tool.get_value()
    if rs:
        log_xml_tool.set_value(app_version, UPDATER_VERSION_TAG)
    log_xml_tool.set_cdata_val('\n'.join(db_tool.get_log(project, version)))
    return Response(log_xml_tool.toxml(), mimetype='application/xml')

@app.route('/add/<project>/<int:version>/<path:log>/')
def add_log(project, version, log):
    db_tool.add_log(project, version, log)
    return log

@app.route('/clear/<project>/')
def clear_log(project):
    db_tool.clear(project)
    return project

def init_db():
    """Creates the database tables."""
    with app.app_context():
        with app.open_resource(DATABASE_SCHEMA, mode='r') as schema_file:
            db_tool.init_db(schema_file)

if __name__ == '__main__':
    init_db()
    app.run()
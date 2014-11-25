__author__ = 'linw'

#database
DATABASE = 'inner_static/log.db'
DATABASE_SCHEMA = 'inner_static/schema.sql'



LOG_XML_TEMPLATE = 'inner_static/updater_template.xml'


DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

VERSION_TAG = 'versionNumber'

PRJ_CFG_PATH_TEMPLATE = 'inner_static/test_proj/%s-app.xml'
PRJ_ROUTE = {
    'MapEditor': PRJ_CFG_PATH_TEMPLATE % 'EditorUI',
    'ModelEditor': PRJ_CFG_PATH_TEMPLATE % 'Main',
    'ModelView': PRJ_CFG_PATH_TEMPLATE % 'ModelExplorerMain',
    'ParticleEditor': PRJ_CFG_PATH_TEMPLATE % 'ParticleEditor',
    'SkillEditor': PRJ_CFG_PATH_TEMPLATE % 'SkillEditor',
}

PRJ_ROUTE2 = {
    'MapEditor': PRJ_CFG_PATH_TEMPLATE % 'EditorUI',
    'ModelEditor': PRJ_CFG_PATH_TEMPLATE % 'Main',
    'ModelView': PRJ_CFG_PATH_TEMPLATE % 'ModelExplorerMain',
    'ParticleEditor': PRJ_CFG_PATH_TEMPLATE % 'ParticleEditor',
    'SkillEditor': PRJ_CFG_PATH_TEMPLATE % 'SkillEditor',
}
#update
DOWNLOAD_URL_TEMPLATE = 'http://192.168.88.200/download/%s.exe'
UPDATER_VERSION_TAG = 'version'
UPDATER_DESC_TAG = 'description'
UPDATER_URL_TAG = 'url'
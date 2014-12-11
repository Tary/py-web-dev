from tools import str_unicode

__author__ = 'linw'

import ConfigParser
import os
import re
import chardet

CONFIG_DIR = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'configs')
RE_CONFIG_NAME = '(.*).ini'
IGNORE_FLAG = 'ignore'
GLOBAL_CFG_SECTION = '_global_'
GLOBAL_ROOT_DIR_FLAG = 'root_dir'

OS_PATH_ENCODING = "gbk"

configs = {}



class cfg_info(object):
    def __init__(self, config, section_name):
        self.cmd = None
        self.desc = None
        self.set_data(config, section_name)

    def set_data(self, config, section_name):
        if config.has_option(section_name, 'cmd'):
            self.cmd = config.get(section_name, 'cmd')
            self.cmd = str_unicode(self.cmd)
        if config.has_option(section_name, 'cmd'):
            self.desc = config.get(section_name, 'desc')
            self.desc = str_unicode(self.desc)

    def to_str(self):
        return "cmd:%s  desc:%s" % (self.cmd, self.desc)


def load_cfg():
    file_list = os.listdir(CONFIG_DIR)
    _configs = {}
    for file_name in file_list:
        file_name = unicode(file_name, OS_PATH_ENCODING)
        path = os.path.join(CONFIG_DIR, file_name)
        if re.match(RE_CONFIG_NAME, file_name) is None:
            continue
        if os.path.isdir(path):
            continue
        _ROOT_DIR = None
        config = ConfigParser.RawConfigParser()
        config.read(path)
        sections = config.sections()
        if config.has_option(GLOBAL_CFG_SECTION, GLOBAL_ROOT_DIR_FLAG):
            _ROOT_DIR = config.get(GLOBAL_CFG_SECTION, GLOBAL_ROOT_DIR_FLAG)
            sections.remove(GLOBAL_CFG_SECTION)
            _ROOT_DIR = str_unicode(_ROOT_DIR)

        for section_name in sections:
            if GLOBAL_CFG_SECTION == section_name:
                continue
            if config.has_option(section_name, IGNORE_FLAG) and \
                    config.getboolean(section_name, IGNORE_FLAG):
                continue
            _configs[str_unicode(section_name)] = cfg_info(config, section_name)
    return _configs, _ROOT_DIR


from tools import str_unicode

__author__ = 'linw'

import ConfigParser
import os
import re

CONFIG_DIR = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'configs')
SUB_CONFIG_DIR = os.path.join(CONFIG_DIR, 'sub_config')
RE_CONFIG_NAME = '(.*).ini'
IGNORE_FLAG = 'ignore'
GLOBAL_CFG_SECTION = '_global_'
GLOBAL_ROOT_DIR_FLAG = 'root_dir'
DESC_OPTION_FLAG = 'desc'
OS_PATH_ENCODING = "gbk"

sub_configs = {}
configs = {}


class cfg_info(object):
    def __init__(self, config, section_name):
        self.cmd = None
        self.desc = None
        self.id = None
        self.set_data(config, section_name)

    def set_data(self, config, section_name):
        self.id = str_unicode(section_name)
        if config.has_option(section_name, 'cmd'):
            self.cmd = config.get(section_name, 'cmd')
            self.cmd = str_unicode(self.cmd)
        if config.has_option(section_name, DESC_OPTION_FLAG):
            self.desc = config.get(section_name, DESC_OPTION_FLAG)
            self.desc = str_unicode(self.desc)

    def to_str(self):
        return "cmd:%s  desc:%s" % (self.cmd, self.desc)


class cfg_group(object):
    def __init__(self, config, section_name):
        self.cmds = []
        self.desc = None
        self.id = str_unicode(section_name)
        self.set_data(config, section_name)

    def set_data(self, config, section_name):
        self.id = str_unicode(section_name)
        items = config.options(section_name)
        items.remove(DESC_OPTION_FLAG)
        if config.has_option(section_name, DESC_OPTION_FLAG):
            self.desc = config.get(section_name, DESC_OPTION_FLAG)
            self.desc = str_unicode(self.desc)
        for item in items:
            task = config.get(section_name, item)
            task = str_unicode(task)
            self.cmds.append(task)

    def to_str(self):
        return "desc:%s cmds:%s  " % (self.desc, ','.join(self.cmds))


def load_cfg_imp(dir, cls_config):
    file_list = os.listdir(dir)
    _configs = {}
    for file_name in file_list:
        file_name = unicode(file_name, OS_PATH_ENCODING)
        path = os.path.join(dir, file_name)
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
            _configs[str_unicode(section_name)] = cls_config(config, section_name)
    return _configs, _ROOT_DIR


def load_sub_cfg():
    return load_cfg_imp(SUB_CONFIG_DIR, cfg_info)


def load_group_cfg():
    return load_cfg_imp(CONFIG_DIR, cfg_group)
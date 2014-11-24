__author__ = 'linw'

from xml.dom.minidom import parse
from os import path
import codecs


class SimpleXML(object):
    u"""简单的XML配置修改工具,
        目的是用来修改打包的项目的版本号更新说明
        Tag为默认的标签.如:
        <root>
            <tag1>value</tag1>
            <version>value</version>
            <url>value</url>
        </root>
        所示的tag1, version, url 等, 如有多个仅修改第一个
        """

    def __init__(self, default_tag=None):
        u"""
        :type default_tag: str
        default_tag为默认的标签
        """
        self.tree = None
        self.file_path = None
        self.defaultTag = default_tag

    def initialize_from_file(self, xml_path):
        u"""
        从xml文件初始化，成功返回True
        如果文件是上次打开的则根据上次成功与否返回，不重新初始化
        :type xml_path: str
        """
        assert isinstance(xml_path, str)
        if xml_path == self.file_path:
            return None != self.tree
        if path.isfile(xml_path):
            self.file_path = xml_path
            self.tree = parse(xml_path)
        else:
            self.file_path = None
            self.tree = None
        return None != self.tree

    def set_value(self, value, tag=None):
        u"""
        设置值 如果存在多个，仅仅设置第一个
        :param value: 新的值
        :param tag: 标签等于None时 使用默认Tag
        :return:
        """
        if tag is None:
            tag = self.defaultTag
        if tag is None or self.tree is None:
            return False
        tag_values = self.tree.getElementsByTagName(tag)
        if len(tag_values) == 0:
            return False
        tag_values[0].firstChild.data = value
        return True

    def get_value(self, tag=None):
        u"""
        获取值 如果存在多个，仅仅返回第一个
        :param tag: 标签等于None时 使用默认Tag
        :return: 标签内的值和True/False
        """
        if tag is None:
            tag = self.defaultTag
        if tag is None or self.tree is None:
            return None, False

        tag_values = self.tree.getElementsByTagName(tag)
        if len(tag_values) == 0:
            return None, False
        return tag_values[0].firstChild.data.strip(), True

    def set_cdata_val(self, value, tag=None):
        u"""
        设置注释类节点值
        :rtype : bool
        :param value:
        :param tag:
        :return: 成功返回True else False
        """
        if tag is None:
            tag = self.defaultTag
        if self.tree is None or tag is None:
            return False
        tag_values = self.tree.getElementsByTagName(tag)
        if len(tag_values) == 0:
            return False
        cdata_node = self.tree.createCDATASection(value)
        tag_values[0].replaceChild(cdata_node, tag_values[0].firstChild)
        return True

    def get_cdata_val(self, tag=None):
        u"""
        查找注释类节点值
        :param tag:可选标签
        :return: 成功返回属性值和True/False
        """
        if tag is None:
            tag = self.defaultTag
        if self.tree is None or tag is None:
            return None, False
        tag_values = self.tree.getElementsByTagName(tag)
        if len(tag_values) == 0:
            return None, False
        return tag_values[0].firstChild.wholeText.strip(), True

    def save(self, file_path=None):
        u"""
        保存文件
        :param file_path: 可选路径， None时使用初始化的文件覆盖保存
        """
        if file_path is None:
            file_path = self.file_path

        if self.tree is None or file_path is None:
            return False
        try:
            save_to_file = open(file_path, 'w')
            xml_writer = codecs.lookup('utf-8').streamwriter(save_to_file)
            self.tree.writexml(xml_writer, encoding='utf-8')
        except IOError:
            print('输出文件时出错', file_path)
            print(self.toxml())
            return False
        return True

    def toxml(self):
        u"""
        转换为xml字符串
        :rtype : str
        """
        if self.tree is None:
            return None
        return self.tree.toxml()

__author__ = 'linw'

import unittest
from simple_xml import *
import os
import random


class SimpleXMLTestCase(unittest.TestCase):
    def setUp(self):
        self.xml_file = os.path.join(os.getcwd(), 'test_data', 'test_xml.xml')
        self.xml_tool = SimpleXML('prop1')
        self.xml_tool.initialize_from_file(self.xml_file)
    def tearDown(self):
        self.xml_file = None
        self.xml_tool = None
    def test_cdata(self):
        assert self.xml_tool.get_cdata_val('sds'), 'get_cdata_val failed'
        assert self.xml_tool.get_cdata_val('cdata')[1], 'get_cdata_val rs failed'
        assert self.xml_tool.set_cdata_val('newvalue%d'% random.random(), 'cdata'), 'set_cdata_val failed'

    def test_value(self):
        assert self.xml_tool.get_value('cdata'), 'test not exist value'
        assert self.xml_tool.get_value('cdata')[1], 'test exist value'
        assert self.xml_tool.set_value('newvalue%d'% random.random()), 'set_value'

    def test_to_xml(self):
        assert self.xml_tool.toxml() is not None, 'to xml failed'

    def test_save(self):
        assert self.xml_tool.save(), 'save failed'
        assert self.xml_tool.save(os.path.join(os.getcwd(), 'test_data', 'test_save_as_xml.xml')), 'save as failed'

    #def suite(self):
        #suite = unittest.TestSuite()
        #suite.addTest(SimpleXMLTestCase("test_cdata"))
        #suite.addTest(SimpleXMLTestCase("test_value"))
        #suite.addTest(SimpleXMLTestCase("test_to_xml"))
        #suite.addTest(SimpleXMLTestCase("test_save"))
        #return suite

if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:25:00 2014

@author: linw
"""
from tools import XMLTool, test
vt = XMLTool()


from tools import SimpleXML

#help(SimpleXML)

import os
xml_file = os.path.join(os.getcwd(), 'tools', 'test_xml.xml')
xml_tool = SimpleXML('prop1')
xml_tool.initialize_from_file(xml_file)

print xml_tool.get_cdata_val('cdata')
xml_tool.set_cdata_val('newvalue', 'cdata')

print xml_tool.get_value()
xml_tool.set_value('newvalue')

print(xml_tool.toxml())
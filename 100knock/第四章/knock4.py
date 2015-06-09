#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import StringIO
from function_common import *
import pprint

def knock30():
	m_lines=[]
	m_lines=read_line("neko.txt.mecab")
	pp(m_lines)
	return 0

if __name__=="__main__":
	print "python"
	print "あいうえお　愛"
	print sys.getdefaultencoding()
	m_map_neko=knock30()


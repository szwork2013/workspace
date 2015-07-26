#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
knock6.py
"""
from function_common import *

def knock50():
	m_text=open_file("nlp.txt")
	list_text=get_list_re(m_text,r"(?P<text_main>[A-Z].+?)(\.|\;|\:|\?|\!)\s","text_main")
	for line in list_text:
		print line
	#get_list_re(read_line("nlp.txt"),".*?¥.")
		#".*?(¥.|¥;|¥:|¥?|¥!)¥s")
	#print list_text


def main():
	knock50()
	# knock51()
	# knock52()
	# knock53()
	# knock54()
	# knock55()
	# knock56()
	# knock57()
	# knock58()
	# knock59()

if __name__=='__main__':
	main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
aaa
"""
import sys
import StringIO
from function_common import *


g_article_england=[]

#title:イギリスのtext項目を読み取りg_textに入れる
def knock20():
	m_filename="jawiki-country.json"
	m_data_json=read_json(m_filename)
	count=0
	for m_line in m_data_json:
		if "イギリス" in m_line["title"]:
			m_text=m_line["text"]
			#print g_text
			break
	return m_text

def knock21(m_text):
	m_buffer=StringIO.StringIO(m_text)
	m_lines=m_buffer.readlines()
	#print m_lines
	#print m_text
	for m_line in m_lines:
		if "Category" in m_line:
			print m_line
	

def knock22():
	pass
def knock23():
	pass
def knock24():
	pass
def knock25():
	pass
def knock26():
	pass
def knock27():
	pass
def knock28():
	pass
def knock29():
	pass

if __name__=="__main__":
	print "python"
	print "あいうえお　愛"
	print sys.getdefaultencoding()
	m_text=knock20()
	knock21(m_text)
	knock22()
	knock23()
	knock24()
	knock25()
	knock26()
	knock27()
	knock28()
	knock29()


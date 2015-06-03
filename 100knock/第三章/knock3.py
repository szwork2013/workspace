#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
aaa
"""
import sys
import StringIO
from function_common import *
import pprint


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

#カテゴリー名を含む行を抽出する
def knock21(m_text):
	m_buffer=StringIO.StringIO(m_text)
	m_lines=m_buffer.readlines()
	#print m_lines
	#print m_text
	for m_line in m_lines:
		if "Category" in m_line:
			print m_line
	
#カテゴリー名を抽出する
def knock22(m_text):
	m_list_categoryname=get_list_re(m_text,r"\A\[\[Category:(?P<name_category>.+?)\]\]","name_category")
	pp(m_list_categoryname)

#セクション名とそのレベルを表示する
def knock23(m_text):
	m_list_level_section=get_list_re(m_text,r"\A(?P<level_section>=+)(?P<name_section>.+?)=+","level_section")
	m_list_name_section=get_list_re(m_text,r"\A(?P<level_section>=+)(?P<name_section>.+?)=+","name_section")
	# for m_line in m_list_level_section:
	# 	m_line=len(m_line)
	# m_dict_section=dict(zip(m_list_name_section,m_list_level_section))
	for m_level_section,m_name_section in zip(m_list_level_section,m_list_name_section):
		print m_name_section," is level ",len(m_level_section)
	#pp(m_dict_section)

#文中のメディアファイルを抽出する
def knock24(m_text):
	m_list_media=get_list_re(m_text,u"ファイル:(?P<name_file>.+?)\|",u"name_file")
	pp(m_list_media)

#基本情報テンプレートのフィールドと値を抜き出す(ちょっとうまくいってない。抜き出したあとの文章の抜き出し)
def knock25(m_text):
	m_list_baseinfo=get_list_re(m_text,u"^\{\{基礎情報 国(?P<baseinfo>.+?)\}\}$",1,1)
	#for line in m_list_baseinfo:
	#	print line.decode("utf-8")
	m_list_field_baseinfo=get_list_re(m_text,u"^\|(?P<name_field>.+?)=(?P<name_value>.+?)$","name_field")
	m_list_value_baseinfo=get_list_re(m_text,u"^\|(?P<name_field>.+?)=(?P<name_value>.+?)$","name_value")
	print m_list_field_baseinfo
	m_dict_baseinfo=dict(zip(m_list_field_baseinfo,m_list_value_baseinfo))
	m_keys_baseinfo=m_dict_baseinfo.keys()
	for m_key in m_keys_baseinfo:
		print m_key,":",m_dict_baseinfo[m_key]

	
def knock26(m_text):
	pass
def knock27(m_text):
	pass
def knock28(m_text):
	pass
def knock29(m_text):
	pass

if __name__=="__main__":
	print "python"
	print "あいうえお　愛"
	print sys.getdefaultencoding()
	m_text=knock20()
	#knock21(m_text)
	#knock22(m_text)
	#knock23(m_text)
	#knock24(m_text)
	knock25(m_text)
	knock26(m_text)
	knock27(m_text)
	knock28(m_text)
	knock29(m_text)


#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
aaa
"""
import sys
import StringIO
from function_common import *
import pprint
import urllib,urllib2
from xml.dom.minidom import parse as parseXML


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

#基本情報テンプレートのフィールドと値を抜き出す
def knock25(m_text):
	m_list_baseinfo=get_list_re(m_text,u"^\{\{基礎情報 国(?P<baseinfo>.+?)\}\}$",1,1)
	#m_list_baseinfoをテキストに変換
	m_text_baseinfo=''.join(m_list_baseinfo)
	m_list_field_baseinfo=get_list_re(m_text_baseinfo,u"^\|(?P<name_field>.+?)=(?P<name_value>.+?)$","name_field")
	m_list_value_baseinfo=get_list_re(m_text_baseinfo,u"^\|(?P<name_field>.+?)=(?P<name_value>.+?)$","name_value")
	m_dict_baseinfo=dict(zip(m_list_field_baseinfo,m_list_value_baseinfo))
	m_keys_baseinfo=m_dict_baseinfo.keys()
	#次回以降処理しやすいよう、辞書型をリストにする
	m_list_template=[]
	for m_key in m_keys_baseinfo:
		#print m_key,":",m_dict_baseinfo[m_key]
		m_field_template=str(str(m_key)+":"+str(m_dict_baseinfo[m_key]))
		m_list_template.append(m_field_template)
	return m_list_template

	"""
#def knock26(m_list_template):
	m_list_erased_markup=erase_list_re(m_list_template,)
	pplist(m_list_erased)
	#pplist(m_list_template,r"\'+?")
	
	# m_text=''.join(m_list_template)
	# m_text.replace('\'','')
	# m_list=list(m_text)
	# pplist(m_list)
	
	#print m_text.decode("utf-8")
	pass
	
#def knock27(m_list_template):
	m_list_erased_markup=erase_list_re(m_list_template)
	pass
"""
#どうせ26,27と同じ作業をしなければならないので、ここでまとめてやってしまう
#テンプレート内のマークアップを可能な限り削除する
def knock28(m_list_template):
	#knock26
	m_list_erased_markup_emphasis=erase_list_re(m_list_template,r"\'+?")
	#pplist(m_list_erased_markup_emphasis)
	#knock27
	m_list_erased_markup_link=erase_list_re(m_list_erased_markup_emphasis,r"\[\[|\]\]")
	#pplist(m_list_erased_markup_link)
	#knock28
	m_list_erased_markup_all=erase_list_re(m_list_erased_markup_emphasis,r"(\[+)|(\]+)|(\{+)|(\}+)|(\<.*?\>)|(.+?\=.+?\&)|(\(\&.+?\;\))")
	#m_list_erased_markup_link=erase_list_re(m_list_erased_markup_emphasis)
	pplist(m_list_erased_markup_all)
	pass

#イギリスの国旗画像のURLを取得する
#一応形だけはできたが納得がいかない……ちゃんと先生に聞いて解決しよう
def knock29(m_text):
	#最初から辞書型で渡せばよかったが…国旗のタイトルを取得するためにテンプレートリスト化
	m_list_baseinfo=get_list_re(m_text,u"^\{\{基礎情報 国(?P<baseinfo>.+?)\}\}$",1,1)
	m_text_baseinfo=''.join(m_list_baseinfo)
	m_list_field_baseinfo=get_list_re(m_text_baseinfo,u"^\|(?P<name_field>.+?) = (?P<name_value>.+?)$","name_field")
	m_list_value_baseinfo=get_list_re(m_text_baseinfo,u"^\|(?P<name_field>.+?) = (?P<name_value>.+?)$","name_value")
	m_dict_baseinfo=dict(zip(m_list_field_baseinfo,m_list_value_baseinfo))
	m_keys_baseinfo=m_dict_baseinfo.keys()
	
	m_flag_title=m_dict_baseinfo[u"国旗画像"]
	print m_flag_title
	#pplist(m_keys_baseinfo)
	m_url_UK=urllib2.urlopen("http://ja.wikipedia.org/w/api.php?action=query&format=json&titles=File:Flag%20of%20the%20United%20Kingdom.svg&prop=imageinfo&iiprop=url")
	for temp in m_url_UK:
		print temp

	#print m_url_UK
if __name__=="__main__":
	print "python"
	print "あいうえお　愛"
	print sys.getdefaultencoding()
	m_text=knock20()
	#knock21(m_text)
	#knock22(m_text)
	#knock23(m_text)
	#knock24(m_text)
	m_list_template=knock25(m_text)
	#knock28(m_list_template)
	knock29(m_text)


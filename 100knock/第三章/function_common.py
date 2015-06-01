#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,json,codecs,re

#デフォルトのエンコーディングをutf-8にする		
reload(sys)
sys.setdefaultencoding('utf-8')
#標準入出力で日本語を扱う設定にする
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

if __name__=="__main__":
	print "function_common"
	pass


#ファイルを行単位で読み込んでリストとして返す
def read_line(m_filename):
	m_file_open=codecs.open(m_filename,"r","utf-8")
	m_lines=m_file_open.readlines()
	m_file_open.close()
	return m_lines

#与えた正規表現に該当する文字列をリストにして返す
def get_list_re(m_expression):
	m_list=[]

 #日本語を含んだリストや辞書をプリティプリントする	
def pp(obj):
  if isinstance(obj, list) or isinstance(obj, dict):
    orig = json.dumps(obj, indent=4)
    print eval("u'''%s'''" % orig).encode('utf-8')
  else:
    print obj

#JSONファイルを辞書のリストにして返す
def read_json(m_filename):
	m_data_json=[]
	with codecs.open(m_filename,"r","utf-8") as m_stream:
		for m_line in m_stream:
			#m_json=json.loads(m_line)
			#m_text=json.dumps(m_line,sort_keys=True,ensure_ascii=False,indent=2)
			#m_data_json.append(m_text)
			m_data_json.append(json.loads(m_line))
	m_stream.close()
	return m_data_json

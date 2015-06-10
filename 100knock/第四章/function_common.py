#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,json,codecs,re,StringIO,urllib,urllib2
from xml.dom.minidom import parse as parseXML

#デフォルトのエンコーディングをutf-8にする		
reload(sys)
sys.setdefaultencoding('utf-8')
#標準入出力で日本語を扱う設定にする
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

if __name__=="__main__":
	print "function_common"
	pass


#ファイルを行単位で読み込んでリストとして返す()
def read_line(m_filename):
	m_file_open=codecs.open(m_filename,"r","utf-8")
	m_lines=m_file_open.readlines()
	m_file_open.close()
	return m_lines

#与えた正規表現に該当する文字列をリストにして返す
#m_text:検索する文字列
#m_expression:与える正規表現
#m_num_group:抽出するグループ番号
#m_flag_multi:0で行検索。1で複数行検索
def get_list_re(m_text,m_expression,m_num_group=0,m_flag_multi=0):
	m_buffer=StringIO.StringIO(m_text)
	m_lines=m_buffer.readlines()
	m_list_hit=[]

	if m_flag_multi>0:
		# for m_line in m_lines:
		# 	m_text_hit=re.search(m_expression,m_line,re.MULTILINE)
		m_text_hit=re.search(m_expression,m_text.decode("utf-8"),re.MULTILINE|re.DOTALL)
		if m_text_hit:
			m_list_hit.append(m_text_hit.group(m_num_group))
	else:
		for m_line in m_lines:
			m_text_hit=re.search(m_expression,m_line)
			if m_text_hit:
				m_list_hit.append(m_text_hit.group(m_num_group))
	return m_list_hit

#よく考えると、抜き出す最小単位はこっちなんだよな
#上はこれをリスト型に使う、ってだけで。よし、今度からもっと分解して作るようにしよう
#あと、拡張しやすいように正規表現はcompileでやるように
def get_text_re(m_text,m_expression,m_num_group=0):
	m_pattern=re.compile(m_expression)
	m_text_hit=m_pattern.search(m_text)
	return m_text_hit.group(m_num_group)

#名前は一時的、上のをバージョンアップし、複数の型と、グループに対応させた
def get_list_re2(m_object,m_expression,m_num_group):
	m_list_return=[]
	if isinstance(m_object, list):
		m_pattern=re.compile(m_expression)
		m_lines=m_object
		for m_line in m_lines:
			m_text_hit=m_pattern.search(m_line)
			if isinstance(m_num_group, list):
				if m_text_hit:
					m_text_extraction=map(str,m_text_hit.group(m_num_group))
				else:
					m_text_extraction=str(m_line)
				m_list_return.append(m_text_extraction)
		return m_list_return


#正規表現にヒットした文字列を削除して返す(テキスト型、リスト型、どちらでも対応できるようにした)
def erase_list_re(m_object,m_expression):
	m_list_erased=[]
	if isinstance(m_object, str):
		pass
	if isinstance(m_object, list):
		m_pattern=re.compile(m_expression)
		for m_line in m_object:
			m_list_erased.append(m_pattern.sub('',m_line))
		return m_list_erased
	#m_pattern=re.compile(m_expression)
	#for m_line in m_list:
	#	pass

"""
バッファで統一したほうが良かったかも。オープンはまた別の関数で。text_to_buffとかfile_to_buffとかでバッファに変換
いやいあ、バッファにするのはreadlineが使いたいから
そんな一時的な理由でするのも
でも、read_lineはバッファに対しての処理なんだし、どういう形にすればよかったんだろう？
ただ、あんまり効率的にし過ぎるとわかりにくいコードになりそうだし、時間もかかるし
あと、渡すファイルは統一しなくていいんじゃないか？そこにこだわりだすと大変そう
"""
#日本語を含んだリストや辞書をプリティプリントする
def pp(obj):
  if isinstance(obj, list) or isinstance(obj, dict):
    orig = json.dumps(obj, indent=4)
    print eval("u'''%s'''" % orig).encode('utf-8')
  else:
    print obj

#↑がエラー吐くこと増えたのでリスト表示用関数をもう一個
def pplist(m_list):
	if isinstance((m_list), list):
		for m_line in m_list:
			print m_line.decode("utf-8")

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

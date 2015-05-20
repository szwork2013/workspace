#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json as json
 
#各地域の最高気温入れるオブジェクト
class HighTemp:
	def __init__(self,name_prefecture,name_region,temp_high,date):
		self.name_prefecture=name_prefecture
		self.name_region=name_region
		self.temp_high=temp_high
		self.date=date

#utf-8でエンコードして出力
def print_encode8(string):
	print string.encode("utf-8")


 #リストや辞書の中身を表示する
def pp(obj):
  if isinstance(obj, list) or isinstance(obj, dict):
    orig = json.dumps(obj, indent=4)
    print eval("u'''%s'''" % orig).encode('utf-8')
  else:
    print obj

#ファイルを行単位d読み込んでリストとして返す
def linereader_knock2(m_filename):
	m_file_open=codecs.open(m_filename,"r","utf-8")
	m_lines=m_file_open.readlines()
	return m_lines

#渡したファイルの行数を数えて表示
def knock10(m_filename):
	print sum(1 for line in open(m_filename))

#タブをスペースに変換して表示する
def knock11(m_filename):
	for line in open(m_filename):
		print line.replace('\t',' ')

#各行の1列目をcol1.txtに、2列目をcol2.tx5に保存
def knock12(m_filename):
	col1=open("col1.txt","w")
	col2=open("col2.txt","w")
	m_lines=codecs.open(m_filename,"r","utf-8")
	for line in m_lines:
		col1.write(line[0:1].encode("utf-8")+"\n")
		col2.write(line[1:2].encode("utf-8")+"\n")
	col1.close()
	col2.close()

#col1とcol2をマージしてタブ区切りで表示
def knock13(m_filename):
	m_col1=codecs.open("col1.txt","r","utf-8")
	m_col2=codecs.open("col2.txt","r","utf-8")
	m_col3=open("col3.txt","w")
	count=0
	while True:
		m_line_col1=m_col1.readline()
		m_line_col2=m_col2.readline()
		print m_line_col1.encode("utf-8")
		print m_line_col2.encode("utf-8")
		count = count+1
		print count
		m_col3.write(m_line_col1.replace("\n","").encode("utf-8")+"\t"+m_line_col2.encode("utf-8"))
		if not(m_line_col1 and m_line_col2):
			break
	m_col1.close()
	m_col2.close()
	m_col3.close()

#受け取ったファイルの先頭からN行を出力
def knock14(m_filename,m_show_line_head):
	m_count=0
	for line in open(m_filename):
		print line
		m_count=m_count+1
		if m_count >= m_show_line_head:
			break
#受け取ったファイルの末尾のN行を出力
def knock15(m_filename,m_show_line_tail):
	m_count=0
	m_file_open=open(m_filename)
	#関数作ればよかった……開いたファイルをリストにしてループで扱いやすくしている
	m_lines=m_file_open.readlines()
	m_lines.reverse()
	for line in m_lines:
		print line
		m_count=m_count+1
		if m_count >= m_show_line_tail:
			break

#受け取ったファイルをN分割する
def knock16(m_filename,m_num_split):
	m_count=0
	m_num_file=1
	m_file_knock16=open("file_knock16_1.txt","w")
	m_lines=linereader_knock2(m_filename)
	for line in m_lines:
		m_file_knock16.write(line.encode("utf-8"))
		#print line.encode("utf-8")
		m_count=m_count+1
		if m_count >= m_num_split:
			m_count=0
			m_file_knock16.close()
			m_num_file=m_num_file+1
			m_file_knock16=open("file_knock16_"+str(m_num_file),"w")

#http://d.hatena.ne.jp/t-fridge/20080323/1206217930
#各業の1列目の異なる文字列の集合を求めて表示
def knock17(m_filename):
	m_lines=linereader_knock2(m_filename)
	m_list_initial=[]
	for line in m_lines:
		m_list_initial.append(line[0:1].encode("utf-8"))
	pp(list(set(m_list_initial)))

def knock18(m_filename):
	m_lines=linereader_knock2(m_filename)#m_linesに行ずつ読み込み
	m_list_hightemp=[]#HighTempオブジェクトのリスト
	for line in m_lines:
		m_temp_high=line.encode("utf-8").split()
		m_list_hightemp.append(HighTemp(m_temp_high[0].decode("utf-8"),m_temp_high[1].decode("utf-8"),m_temp_high[2].decode("utf-8"),m_temp_high[3].decode("utf-8")))

	m_list_hightemp_sorted=sorted(m_list_hightemp, key=lambda hightemp: hightemp.temp_high,reverse=False)
	for temp_high in m_list_hightemp_sorted:
		print temp_high.name_prefecture.encode("utf-8")+" "+temp_high.name_region.encode("utf-8")+" "+temp_high.temp_high.encode("utf-8")+" "+temp_high.date.encode("utf-8")



g_filename="hightemp.txt"
print "10"
#knock10(filename)
print "11"
#knock11(filename)
print "12"
#knock12(g_filename)
print "13"
#knock13(filename)
print "14"
#knock14(filename,5)
print "15"
#knock15(g_filename,5)
print "16"
#knock16(g_filename,10)
print "17"
knock17(g_filename)
print "18"
knock18(g_filename)
print "19"

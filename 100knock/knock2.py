#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json as json
 
def pp(obj):
  if isinstance(obj, list) or isinstance(obj, dict):
    orig = json.dumps(obj, indent=4)
    print eval("u'''%s'''" % orig).encode('utf-8')
  else:
    print obj

def linereader_knock2(m_filename):
	m_file_open=codecs.open(m_filename,"r","utf-8")
	m_lines=m_file_open.readlines()
	return m_lines

def knock10(m_filename):
	print sum(1 for line in open(m_filename))

def knock11(m_filename):
	for line in open(m_filename):
		print line.replace('\t',' ')

def knock12(m_filename):
	col1=open("col1.txt","w")
	col2=open("col2.txt","w")
	m_lines=codecs.open(m_filename,"r","utf-8")
	for line in m_lines:
		col1.write(line[0:1].encode("utf-8")+"\n")
		col2.write(line[1:2].encode("utf-8")+"\n")
	col1.close()
	col2.close()

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

	#m_lines=codecs.open(m_filename,"r","utf-8")
def knock14(m_filename,m_show_line_head):
	m_count=0
	for line in open(m_filename):
		print line
		m_count=m_count+1
		if m_count >= m_show_line_head:
			break

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
def knock17(m_filename):
	m_lines=linereader_knock2(m_filename)
	m_list_initial=[]
	for line in m_lines:
		m_list_initial.append(line[0:1].encode("utf-8"))
	pp(list(set(m_list_initial)))


g_filename="hightemp.txt"
print "10"
#knock10(filename)
print "11"
#knock11(filename)
print "12"
knock12(g_filename)
print "13"
#knock13(filename)
print "14"
#knock14(filename,5)
print "15"
#knock15(g_filename,5)
print "16"
#knock16(g_filename,10)
print "17"
#knock17(g_filename)
print "18"
print "19"

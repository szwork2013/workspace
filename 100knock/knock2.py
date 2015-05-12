#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

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
		col1.writelines(line[0:1].encode("utf-8")+"\n")
		col2.writelines(line[1:2].encode("utf-8")+"\n")
	col1.close()
	col2.close()

def knock13(m_filename):
	m_col1=codecs.open("col1.txt","r","utf-8")
	m_col2=codecs.open("col2.txt","r","utf-8")
	m_col3=open("col3.txt","w")
	count=0
	while m_col1 and m_col2:
		print count+1
		m_line_col1=m_col1.readline()
		m_line_col2=m_col2.readline()
		m_col3.write(m_line_col1.encode("utf-8")+m_line_col2.encode("utf-8")+"\n")
	m_col1.close()
	m_col2.close()
	m_col3.close()

	#m_lines=codecs.open(m_filename,"r","utf-8")


filename="hightemp.txt"
print "10"
#knock10(filename)
print "11"
#knock11(filename)
print "12"
knock12(filename)
print "13"
knock13(filename)
print "14"
print "15"
print "16"
print "17"
print "18"
print "19"

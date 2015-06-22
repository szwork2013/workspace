#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import StringIO
from function_common import *
import pprint
import MeCab

#def make_list_morph(m_list_mprph):

	# for m_line in m_list_mprph:
	# 	m_morph_split=m_line.strip(',').split(',')
	# 	m_suface=m_morph_split[0]


def knock30():
	m_lines=[]
	m_lines=read_line("neko.txt.mecab")
	m_list_morph=[]
	#
	for m_line in m_lines:
		if m_line is "EOS":
			continue
		surface=get_text_re(m_line,r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)","surface")
		pos=get_text_re(m_line,r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)","pos")
		pos1=get_text_re(m_line,r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)","pos1")
		base=get_text_re(m_line,r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)","base")
		if surface and base and pos and pos1:
			m_dict_morph={
				"surface":surface,
				"pos":pos,
				"pos1":pos1,
				"base":base
			}
			m_list_morph.append(m_dict_morph)
	return m_list_morph
def knock31(m_map_neko):
	m_list_surface_verb=[]
	for m_word in m_map_neko:
		if m_word["pos"] == u"動詞":
			m_list_surface_verb.append(m_word["surface"])
	print pp(m_list_surface_verb)

def knock32(m_map_neko):
	m_list_base_verb=[]
	for m_word in m_map_neko:
		if m_word["pos"] == u"動詞":
			m_list_base_verb.append(m_word["base"])
	print pp(m_list_base_verb)

def knock33(m_map_neko):
	m_list_noun_sahen=[]
	for m_word in m_map_neko:
		if m_word["pos"] == u"名詞" and m_word["pos1"].find(u"サ変")!=-1:
			m_list_noun_sahen.append(m_word["surface"])
	print pp(m_list_noun_sahen)
	
def knock34(m_map_neko):
	m_list_phrase_noun=[]
	for m_count in range(0,len(m_map_neko)):
		if m_map_neko[m_count]["surface"]==u"の":
			if m_map_neko[m_count-1]["pos"]==u"名詞" and m_map_neko[m_count+1]["pos"]==u"名詞":
				m_list_phrase_noun.append(m_map_neko[m_count-1]["surface"]+u"の"+m_map_neko[m_count+1]["surface"])
				#m_phrase_noun=""
				#m_phrase_noun.join(m_map_neko[m_count+1]["surface"])
				#m_list_phrase_noun.append(m_phrase_noun)
			print m_map_neko[m_count]["surface"]

	pp(m_list_phrase_noun)
	
def knock35(m_map_neko):
	pass

"""
zenbun=inlines
inline=[我輩：（(surface:名詞),(base:)）,は:(形態素),]
名前(形態素),は:(形態素),
31
for line in zenbun_neko:一文
	for inline in line:一語
		if inline[surface]　 is 名詞:

dict[surface]&verb
32
dict[base]
33
dict[pos=サ変接続]
34
一文=形態素のリスト
for itibun in zenbun:
	count=0
	for count < len(itibun) count+=1:
		if itibun[count][pos1]=連接 and itibun[count][surface]=の:
			meisiku.append(itibun[count-1][surface]+"の"+itibun[count+1][surface])
35
?名詞句も名詞とするってことかな？ここは飛ばして先生に聞く

36
http://qiita.com/raydive/items/80a36a7f40f526441456
charset={x for x in goku[surface] for goku in itibun for itibun in zenbun}
↓
cnt = Counter
for itibun in zenbun:
	for goku in itibun:
		cnt[goku[surface]]+=1

37
words=re.findall('\w+',open('neko.txt').read().lower())
Counter(words).most_common(10)
もしくはcharsetを使うとか
終わったらmatplotibかGnuplotで表示
http://www.freia.jp/taka/blog/356/

38?
1種類のワードが1000回使われてて、5種類のワードが500回みたいな
出現頻度1が一番左でそれが何種類あるかを棒グラフでGnuplotとかで表示
Counter(sords)のキーでループさせて、list[1]=valueが1の見つかる度+=1
か、dict.valuesで値のリスト取ってきて、list[value]+1とか

39
両対数グラフの意味が分からん
けど、上ので使ったリストを使ってなんかやるんだろう




"""

if __name__=="__main__":
	print "python"
	print "あいうえお　愛"
	print sys.getdefaultencoding()
	m_map_neko=knock30()
	#knock31(m_map_neko)
	#knock32(m_map_neko)
	#knock32(m_map_neko)
	#knock33(m_map_neko)
	#knock34(m_map_neko)
	knock35(m_map_neko)
	#print m_map_neko


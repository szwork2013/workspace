#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import StringIO
from function_common import *
import pprint
import MeCab
# 単語数え上げよう
from collections import Counter
import numpy as np
import matplotlib
#これがないと図が出力できない
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# def make_list_morph(m_list_mprph):

# for m_line in m_list_mprph:
# 	m_morph_split=m_line.strip(',').split(',')
# 	m_suface=m_morph_split[0]


def knock30():
    m_lines = []
    m_lines = read_line("neko.txt.mecab")
    m_list_morph = []
    #
    for m_line in m_lines:
        if m_line is "EOS":
            continue
        surface = get_text_re(m_line,
                              r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)",
                              "surface")
        pos = get_text_re(m_line,
                          r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)",
                          "pos")
        pos1 = get_text_re(m_line,
                           r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)",
                           "pos1")
        base = get_text_re(m_line,
                           r"\A(?P<surface>[^\t]+?)\t(?P<pos>.+?)\,(?P<pos1>.+?)\,(?P<pos2>.+?)\,(?P<pos3>.+?)\,(?P<conjForm>.+?)\,(?P<conjType>.+?)\,(?P<base>.+?)\,(?P<read>.+?)\,(?P<pron>.+?)",
                           "base")
        if surface and base and pos and pos1:
            m_dict_morph = {
                "surface": surface,
                "pos": pos,
                "pos1": pos1,
                "base": base
            }
            m_list_morph.append(m_dict_morph)
    return m_list_morph


def knock31(m_map_neko):
    m_list_surface_verb = []
    for m_word in m_map_neko:
        if m_word["pos"] == u"動詞":
            m_list_surface_verb.append(m_word["surface"])
    print pp(m_list_surface_verb)


def knock32(m_map_neko):
    m_list_base_verb = []
    for m_word in m_map_neko:
        if m_word["pos"] == u"動詞":
            m_list_base_verb.append(m_word["base"])
    print pp(m_list_base_verb)


def knock33(m_map_neko):
    m_list_noun_sahen = []
    for m_word in m_map_neko:
        if m_word["pos"] == u"名詞" and m_word["pos1"].find(u"サ変") != -1:
            m_list_noun_sahen.append(m_word["surface"])
    print pp(m_list_noun_sahen)


def knock34(m_map_neko):
    m_list_phrase_noun = []
    for m_count in range(0, len(m_map_neko)):
        if m_map_neko[m_count]["surface"] == u"の":
            if m_map_neko[m_count - 1]["pos"] == u"名詞" and m_map_neko[m_count + 1]["pos"] == u"名詞":
                m_list_phrase_noun.append(
                    m_map_neko[m_count - 1]["surface"] + u"の" + m_map_neko[m_count + 1]["surface"])
            # m_phrase_noun=""
            # m_phrase_noun.join(m_map_neko[m_count+1]["surface"])
            # m_list_phrase_noun.append(m_phrase_noun)
            print m_map_neko[m_count]["surface"]

    pp(m_list_phrase_noun)


# ここまで分解すればよかった
def get_list_words(m_map_word):
    m_list_words = []
    for m_word in m_map_word:
        m_list_words.append(m_word["surface"].decode("utf-8"))
    return m_list_words


def get_counter_word_from_map(m_map_word):
    m_list_words = []
    for m_word in m_map_word:
        m_list_words.append(m_word["surface"].decode("utf-8"))
    # if m_dict_word_counted.has_key(m_word["surface"]):
    # 	m_dict_word_counted[m_word["surface"]]+=1
    # elif m_word != u"":
    # 	m_dict_word_counted[m_word["surface"]]=1
    # そのまま数え上げるより、カウンターオブジェクト作ったほうが後で使いやすい
    m_counter_word = Counter(m_list_words)
    return m_counter_word


# print m_counter_word.most_common(10)

def knock35(m_map_neko):
    pass


def knock36(m_map_neko):
    # 単語とその数をvalueとした辞書をもらう
    m_counter = get_counter_word_from_map(m_map_neko)
    for m_word, m_count in m_counter.most_common():
        print m_count, m_word.decode("utf-8")

    # plt.hist(m_count.most_common(10))


def knock37(m_map_neko):
    m_groups=10
    m_words_most_common_10=[]
    m_counts_most_common_10=[]
    m_counter=get_counter_word_from_map(m_map_neko)
    m_counter_most_common = m_counter.most_common(10)
    m_list_words_most_common_10=list(m_counter_most_common)
    #print m_list_words_most_common_10
    for m_word,m_count in m_list_words_most_common_10:
        m_words_most_common_10.append(m_word)
        m_counts_most_common_10.append(m_count)
  	    #for i in range(0,m_count):
        #        m_words_most_common_10.append(m_word)

    #print m_words_most_common_10
    #print m_counts_most_common_10
    #ここからグラフテスト
    m_groups=10
    m_index=np.arange(m_groups)
    m_bar_width=0.35
    m_opacity=0.4
    error_config={'ecolor':'0.3'}
    m_rects=plt.bar(m_index,m_counts_most_common_10,m_bar_width,color='b',label='words')


    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title('Words of most common 10 in neko')
    plt.xticks(m_index+m_bar_width,m_words_most_common_10)

    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.savefig('most_common_10_words.png')

    print u"ここまで"

# fontprop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")
# # m_dict_words_counter=
# for m_word,m_count in m_list_words_most_common_10:
#  	for i in range(0,m_count):
#  		m_words_most_common_10.append(m_word)
# plt.hist(m_words_most_common_10)
# plt.show()
# print m_words_most_common_10


def knock38(m_map_neko):
    pass


def knock39(m_map_neko):
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

if __name__ == "__main__":
    print "python"
    print "あいうえお　愛"
    print sys.getdefaultencoding()
    m_map_neko = knock30()
    # knock31(m_map_neko)
    # knock32(m_map_neko)
    # knock32(m_map_neko)
    # knock33(m_map_neko)
    # knock34(m_map_neko)
    # knock35(m_map_neko)
    # knock36(m_map_neko)
    knock37(m_map_neko)
    knock38(m_map_neko)
    knock39(m_map_neko)
# print m_map_neko

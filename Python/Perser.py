#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
#import logging
import sys
import urllib
#import string
import re
#import sys
import codecs
from collections import namedtuple
#Article = namedtuple(
#    'Article', 'title year city country month journal date volume number page authors language check')
#('Article', 'title name year month')
#sys.stdout = codecs.EncodedFile(sys.stdout, 'utf_8')


#alist = Article( -1, '', '', -1, '',-1, -1, -1, -1, ['', ''], "English", False)


#def init_data():
#    alist = Article(
#        '', -1, '', '', -1, '', -1, -1, -1, ['', ''], 'English', False)

#処理複雑になりすぎて失敗してる
#もっと関数に分割するとか、変数のルールを統一するとか
def make_pub_db():
    closed_author_list=[[]]
    author_list=[]
    closed_journal_list=[[]]
    journal_list=-1
    title = ''
    # namelist[[]]
    soup = BeautifulSoup(
        urllib.urlopen("http://pryo3.is.kochi-u.ac.jp/publication.html").read())

    tag = soup.li
    type(tag)
    count = 0
    # 書き込む用のファイルをオープンして初期設定
    f = open('makedb.txt', 'w')
    # http://lab.hde.co.jp/2008/08/pythonunicodeencodeerror.html
    # これないとエラー出る
    f = codecs.lookup('utf_8')[-1](f)
    f.write('from pub.models import Article,Author,Journal,Language\n')
    f.write('import datetime\n')
    f.write('from django.utils import timezone\n')
    
    f.write('english=Language(label=\"English\")\n')
    f.write('japanese=Language(label=\"Japanese\")\n')
    f.write('english.save()\n')
    f.write('japanese.save()\n')

    for mixsoup in [soup("li", "article"), soup("li", "article_p")]:
        for lisoup in mixsoup:
                # 変数を初期化しておく
                # title=
            title=""
            vol=-1
            number=-1
            page=""
            language=""
            date=-1
            day=-1
            month=""
            year=-1
            city=""
            country=""
            no=-1
            journal_list=-1
            del author_list[:]
            # リンク部分
            for linksoup in lisoup("a"):
                link = linksoup.get('href')
                linksoup.decompose()
            #(リンク消去後の()を削除)
           # タイトル部分
            tsoup = lisoup.find("span", "title")
            title = tsoup.get_text()
            #alist._replace(title=ttitle.encode('utf_8'))
            #print "ttitle="+ttitle.encode('utf_8'), "title="+alist.title
            tsoup.decompose()
            #print "publish\n"
            #"出版情報"
            for psoup in lisoup("span", "publisher"):
                #print psoup.get_text().encode('utf_8')
                temp_publish=psoup.get_text().encode('utf_8')
                re_publish=re.compile(r'(?P<editor>^.*?\(Eds\.\))?(?P<journal_name>.+)$')
                #re_publish=re.compile(r'(?P<editor>^.*?)(\(Eds\.\))?:?(?P<journal_name>.+)$')
                m=re_publish.search(temp_publish)
                if(m):
                    editors=m.group('editor')
                    if(editors is None):
                        editors=""
                    journals=m.group('journal_name')
                    if(([editors,journals] in closed_journal_list)==False):
                            #print "add!"
                            closed_journal_list.append([editors,journals])
                            f.write('j'+str(closed_journal_list.index([editors,journals])))
                            f.write("=Journal(publisher=\""+editors.decode("utf_8")+"\",name=\""+journals.decode("utf_8")+"\")\n")
                            f.write('j'+str(closed_journal_list.index([editors,journals]))+'.save()\n')

                    journal_list=closed_journal_list.index([editors,journals])
                    #print editors
                    #print '\n'
                    #print journals
                    #print '\n'
                psoup.decompose()
            # ここからは文字列を操作していく
            src = lisoup.get_text()
            ypattern = re.compile(
                r'(?P<author>^.+?):.*,\s(?P<time>(?P<day>\d{0,2}[-]?\d{0,2}?\s)?(?P<month>\w{0,10}\s)?(?P<year>\d*)?[^,]+)$')
            m = ypattern.search(src)
            if(m):
                #著者は処理が特殊
                authors = m.group('author')
                #print authors.encode("utf_8")
                temp=authors.encode('utf_8')
                t_list=temp.split(",")
                for x in t_list:
                    x=x.strip()
                    #文字列からlanguageを判断
                    re_lang=re.compile(r'^\W+$')
                    result=re_lang.search(x)
                    #print result
                    #日本語だった
                    if(result):
                        language="Japanese"
                        j_namelist=x.split(' ')
                        givenname=j_namelist[1]
                        surname=j_namelist[0]
                        #author_list.append([givenname,surname])
                        if(([givenname,surname] in closed_author_list)==False):
                            #print "add!"
                            closed_author_list.append([givenname,surname])
                            f.write('a'+str(closed_author_list.index([givenname,surname])))
                            f.write("=Author(j_givenname=\""+givenname.decode("utf_8")+"\",j_surname=\""+surname.decode("utf_8")+"\")\n")
                            f.write('a'+str(closed_author_list.index([givenname,surname]))+'.save()\n')

                            # print closed_author_list.index([givenname,surname]),givenname,surname
                        author_list.append(closed_author_list.index([givenname,surname]))
                        #print givenname
                    #英語だった
                    else:
                        language="English"
                        e_namelist1=x.split('and')
                        #andがあった
                        #if(len(e_namelist1)>1)
                        for temp_name in e_namelist1:
                            e_namelist2=temp_name.split('.')
                            if e_namelist2[0] and e_namelist2[1] :
                                givenname=e_namelist2[0].strip()
                                surname=e_namelist2[1].strip()
                                #author_list.append([givenname,surname])
                                if(([givenname,surname] in closed_author_list)==False):
                                    closed_author_list.append([givenname,surname])
                                    f.write('a'+str(closed_author_list.index([givenname,surname])))
                                    f.write("=Author(e_givenname=\""+givenname+"\",e_surname=\""+surname+"\")\n")
                                    f.write('a'+str(closed_author_list.index([givenname,surname]))+'.save()\n')

                                    #print closed_author_list.index([givenname,surname]),givenname,surname
                                author_list.append(closed_author_list.index([givenname,surname]))
                    #t_author="a"+str(closed_author_list.index([givenname,surname]))
                    #author_list.append(t_author)
                    #print closed_author_list.index([givenname,surname]),closed_author_list[closed_author_list.index([givenname,surname])]
                        #print x

                    #print x


                #for a in author_list:
                #    print a,
                day = m.group('day')
                month = m.group('month')
                year = m.group('year')
                src = src.replace(authors, "")
                # aushorは絶対に存在するので英語、日本語で場合分けして区切り、リストに含まれるか検索、含まれないなら追加

                if(day):
                    src = src.replace(day, "")
                if(month):
                    src = src.replace(month, "")
                if(year):
                    src = src.replace(year, "")
                else:
                    year=-1

            # ページ部分
            pagepat = re.compile(r'\s(p|pp)\.(?P<page>.*?),')
            m = pagepat.search(src)
            if(m):
                page = m.group('page')
                src = src.replace(page, "")

            # Vol部分
            volpat = re.compile(r'\svol\.(?P<vol>.*?),', re.I)
            m = volpat.search(src)

            if(m):
                vol = m.group('vol')
                src = src.replace(vol, "")

            # No部分
            nopat = re.compile(r'\sno\.(?P<no>.*?),', re.I)
            m = nopat.search(src)
            if(m):
                no = m.group('no')
                src = src.replace(no, "")

            # 地名部分
            coupat = re.compile(
                r'\s(?P<cou>(Japan|Spain|USA|Italy|Canada|Thailand|Indonesia|singapore)),', re.I)
            m = coupat.search(src)
            if(m):
                country = m.group('cou')
                src = src.replace(country, "")

            citpat = re.compile(
                r'\s(?P<city>(kochi|nara|kagoshima|vancourver|santandar|chiang mai|taipei|hong kong|kagawa|tokushima|ehime|iwate|kanazawa|kumamoto|hiroshima|salamanca|beijing|honolulu|vancouver|montreal|tokyo|washington, d.c.|nagoya|fukuoka|chang mai|heidelberg|rome|san antonio|orlando, florida|lugano|osaka|wakayama|yokohama|narashino|akita|okayama|sapporo|kusatsu|hyogo|wien)),', re.I)
            m = citpat.search(src)
            if(m):
                city = m.group('city')
                if(city is 'vancourver'):
                    city = 'vancouver'
                src = src.replace(city, "")

            # ファイルに書き込んでいく
            f.write(
                    "a=Article(title=\"" + title + "\",year=" + str(year) + ",city=\"" + city+\
                "\",country=\""+country+"\",month=\""+str(month)+"\",date="+str(day)+\
                ",volume=\""+str(vol)+"\",number=\""+str(no)+\
                "\",page=\""+str(page)+\
                "\")\n")
            f.write("a.save()\n")
            # ここからAuthorをプラスしていく
            #あとjournalとcheckと
            if(language=="Japanese"):
                temp_language='japanese'
                temp_check=False
            else:
                temp_language='english'
                temp_check=True
            f.write("a.language="+temp_language+"\n")
            f.write("a.check="+str(temp_check)+"\n")
            f.write("a.journal=j"+str(journal_list)+"\n")
            for x in author_list:
                f.write("a.authors.add(a"+str(x)+")\n")
            f.write("a.save()\n")


    f.close()
    print(src)
    print('aaaaaaa')


make_pub_db()

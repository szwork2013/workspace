# coding: utf-8
import sqlite3
from os import path
from simplemapper import BaseMapper
from model import UserMapper, PizzaMapper, OrderMapper, OrderPizzaMapper

#con = sqlite3.connect('/Users/xuzhongwei/Dropbox/pizza/cgi-bin/pizza.db')
con = sqlite3.connect('pizza.db')
UserMapper.setconnection(con)
PizzaMapper.setconnection(con)
OrderMapper.setconnection(con)
OrderPizzaMapper.setconnection(con)

# テーブルを作成
UserMapper.createtable()  
PizzaMapper.createtable()
OrderMapper.createtable()
OrderPizzaMapper.createtable()

# 初期データを登録
ins = UserMapper(
    username = 'syoui',
    password = 'syoui',
    session = None,
    session_expire = None,
    email = 'miyoshi@is.kochi-u.ac.jp',
)

ins = PizzaMapper(
    name = u'セキュアミックス',
    desc = u'どれにしようか迷ったらコレ！',
    ingredient = u'イタリアンソーセージ，ソーセージ，ペパロニ，コーン，ピーマン，オニオン，ブラックペッパー，マッシュルーム',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/arutomikkusu.png',
)

ins = PizzaMapper(
    name = u'4種チーズピザ',
    desc = u'濃厚なクリームチーズが絶妙！',
    ingredient = u'モッツァレラチーズ，ゴーダチーズ，クリームチーズ，パルメザンチーズ，ダイストマト，バジル，ガーリックパウダー',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/4syu.png',
)

ins = PizzaMapper(
    name = u'メキシカンヒート',
    desc = u'ピリ辛スパイシーがクセになる！',
    ingredient = u'チョリソーソーセージ，タコスミート，オニオン，ピーマン，ブラックペッパー，バジル，ガーリックパウダー',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/mekisikan.png',
)

ins = PizzaMapper(
    name = u'じゃがべー',
    desc = u'ほくほくアツアツじゃがいも！',
    ingredient = u'ベーコン，コーン，ポテト，オニオン，ツナ，ブラックペッパー，マヨネーズ，ガーリックパウダー',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/jagabe-.png',
)

ins = PizzaMapper(
    name = u'チキン南蛮ピザ',
    desc = u'甘酸ソースのチキン南蛮風ピザです！',
    ingredient = u'チキンナゲット，玉子サラダ，オニオン，ピーマン，マヨネーズ',
    sauce = u'南蛮ソース',
    price_m = 1155,
    price_l = 1785,
    pic_file = '/pizza_photos/tikin.png',
)

ins = PizzaMapper(
    name = u'ペパロニ',
    desc = u'シンプルだけどおいしい！',
    ingredient = u'ペパロニ，オニオン，パセリ',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/peparoni.png',
)

ins = PizzaMapper(
    name = u'ピリ辛ソーセージ',
    desc = u'ピリ辛が刺激的！',
    ingredient = u'チョリソーソーセージ，コーン，オニオン，マッシュルーム，ピーマン，ブラックペッパー，バジル，ガーリックパウダー',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/pirikara.png',
)

ins = PizzaMapper(
    name = u'カルボナーラ',
    desc = u'クリーミーな味わい！',
    ingredient = u'ベーコン，ツナ，マッシュルーム，オニオン，ゆで玉子，玉子サラダ，パセリ',
    sauce = u'ホワイトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/karubona-ra.png',
)

ins = PizzaMapper(
    name = u'コーンピザ',
    desc = u'コーンの甘さがほどよくグ〜！',
    ingredient = u'たっぷりコーン，ベーコン，オニオン，パセリ',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/ko-n.png',
)

ins = PizzaMapper(
    name = u'ミートデラックス',
    desc = u'たっぷりミートに大満足！',
    ingredient = u'ペパロニ，チョリソー，イタリアンソーセージ，タコスミート，ベーコン，オニオン，ピーマン，マッシュルーム',
    sauce = u'トマトソース',
    price_m = 1155,
    price_l = 1785,
    pic_file = '/pizza_photos/mi-toderakkusu.png',
)

ins = PizzaMapper(
    name = u'黒コショウソーセージ',
    desc = u'黒コショウとウインナーのコンビがGood!!',
    ingredient = u'ベーコン，ツナ，マッシュルーム，オニオン，ゆで玉子，玉子サラダ，パセリ',
    sauce = u'黒コショウマヨネーズソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/kurokoshou.png',
)

ins = PizzaMapper(
    name = u'トリプルガーリック',
    desc = u'3種類のガーリックがたまらない！',
    ingredient = u'オニオン，ペパロニ，ガーリックスライス，フライド粗挽ガーリック，チョリソー，ピーマン，ガーリックパウダー',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/toripuru.png',
)

ins = PizzaMapper(
    name = u'ポテトグラタン',
    desc = u'ほくほくポテトとクリームソースがグー！',
    ingredient = u'ポテト，チョリソーソーセージ，ベーコン，コーン，マッシュルーム，パセリ，マヨネーズ',
    sauce = u'ホワイトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/poteto.png',
)

ins = PizzaMapper(
    name = u'パイナップルベーコン',
    desc = u'南国のスウィート香りいっぱい',
    ingredient = u'パイナップル，オニオン，ベーコン，コーン，マヨネーズ，パセリ',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/painappuru.png',
)

ins = PizzaMapper(
    name = u'シーフードピザ',
    desc = u'海の幸たっぷり！',
    ingredient = u'エビ，イカ，アサリ，オニオン，ツナ，マヨネーズ，マッシュルーム，ガーリックパウダー，バジル',
    sauce = u'トマトソース',
    price_m = 1155,
    price_l = 1785,
    pic_file = '/pizza_photos/si-fu-do.png',
)

ins = PizzaMapper(
    name = u'バジルソースの3チーズピザ',
    desc = u'特製バジルソースの風味がたまりません！',
    ingredient = u'モッツァレラチーズ，ゴーダチーズ，パルメザンチーズ，ダイストマト，ガーリックパウダー',
    sauce = u'特製バジルソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/bajiruso-su.png',
)

ins = PizzaMapper(
    name = u'セキュアベジー',
    desc = u'野菜だっておいしく食べたい！',
    ingredient = u'オニオン，マッシュルーム，ピーマン，パルメザンチーズ，ダイストマト，コーン，ガーリックパウダー',
    sauce = u'トマトソース',
    price_m = 945,
    price_l = 1575,
    pic_file = '/pizza_photos/arutobeji-.png',
)



con.close()

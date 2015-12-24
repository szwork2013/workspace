# coding: utf-8
from simplemapper import BaseMapper

class UserMapper(BaseMapper):
    rows = (
        ('username', 'text'),
        ('password', 'text'),
        ('session', 'text'),
        ('session_expire', 'date'),
        ('email', 'text'),
    )

class PizzaMapper(BaseMapper):
    rows = (
        ('name', 'text'),   # ピザの名前
        ('desc', 'text'),   # ピザの説明
        ('ingredient', 'text'), # 使用している材料
        ('sauce', 'text'),  # ピザソースの種類
        ('price_m', 'int'),   # Mサイズの単価
        ('price_l', 'int'),   # Lサイズの単価
        ('pic_file', 'text'),   # ピザ画像ファイル名
    )

class OrderMapper(BaseMapper):
    rows = (
        ('user_id', 'int'),    # 注文したユーザのid
        ('order_date', 'date'), # 注文日時
    )

class OrderPizzaMapper(BaseMapper):
    rows = (
        ('order_id', 'int'),   # Orderのid
        ('pizza_id', 'int'),   # Pizzaのid
        ('size', 'text'),   # ピザのサイズ (m or l)
        ('count', 'int'),   # ピザの枚数
    )
